# Important: I used linux for this project, So you may have to edit 2-3 lines from this python code, No changes required in the ESP32 Firmware.


import cv2
import mediapipe as mp
import serial
import time



webcam_index = int(input("Enter WEBCAM INDEX (0, 1, 2, 3..): ")) 


# SERIAL
SERIAL_PORT = '/dev/ttyUSB0' # for Windows 'COMx'
BAUD = 115200
ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)
time.sleep(2)


# CAMERA
cap = cv2.VideoCapture(webcam_index, cv2.CAP_V4L2) # for Windows CAP_DSHOW
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cap.set(cv2.CAP_PROP_FPS,60)
cap.set(cv2.CAP_PROP_BUFFERSIZE,1)


# MEDIAPIPE
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    model_complexity=0,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)


# PID
Kp = 1.1
Kd = 0.30

prev_error_x = 0
prev_error_y = 0


# FILTER
filtered_x = 320
filtered_y = 240


# VELOCITY (for prediction)
prev_x = 320
prev_y = 240


# SERVO STATE
pan = 90
tilt = 90

SPEED_SCALE = 0.035

last_send = time.time()
prev_locked = False


while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame,1)

    h,w,_ = frame.shape
    cx = w//2
    cy = h//2

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    locked=False

    if results.pose_landmarks:

        lm = results.pose_landmarks.landmark

        ls = lm[mp_pose.PoseLandmark.LEFT_SHOULDER]
        rs = lm[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        lh = lm[mp_pose.PoseLandmark.LEFT_HIP]
        rh = lm[mp_pose.PoseLandmark.RIGHT_HIP]

        sx=(ls.x+rs.x)/2
        sy=(ls.y+rs.y)/2
        hx=(lh.x+rh.x)/2
        hy=(lh.y+rh.y)/2

        x=int(((sx+hx)/2)*w)
        y=int(((sy+hy)/2)*h)

        # SMOOTH FILTER
        filtered_x = filtered_x*0.7 + x*0.3
        filtered_y = filtered_y*0.7 + y*0.3

        # VELOCITY
        vx = filtered_x - prev_x
        vy = filtered_y - prev_y

        prev_x = filtered_x
        prev_y = filtered_y

        # PREDICTION
        predicted_x = filtered_x + vx*0.5
        predicted_y = filtered_y + vy*0.5

        dx = cx - predicted_x
        dy = cy - predicted_y

        derivative_x = dx - prev_error_x
        derivative_y = dy - prev_error_y

        control_x = Kp*dx + Kd*derivative_x
        control_y = Kp*dy + Kd*derivative_y

        prev_error_x = dx
        prev_error_y = dy

        pan += control_x*SPEED_SCALE
        tilt -= control_y*SPEED_SCALE

        pan=max(0,min(180,pan))
        tilt=max(10,min(170,tilt))

        if abs(dx)<60 and abs(dy)<60:
            locked=True

        cv2.circle(frame,(int(predicted_x),int(predicted_y)),8,(0,0,255),-1)

    else:
        pan=90
        tilt=80

    now=time.time()

    if now-last_send>0.02:

        ser.write(f"{int(pan)},{int(tilt)}\n".encode())

        if locked:
            if not prev_locked:
                ser.write(b"FIRE\n")
            prev_locked=True
        else:
            if prev_locked:
                ser.write(b"STOP\n")
            prev_locked=False

        last_send=now

    cv2.circle(frame,(cx,cy),6,(0,255,0),-1)

    cv2.imshow("MDL26 TRACKING SYSTEM",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()