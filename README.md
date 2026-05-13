# MDL-26 — Autonomous Tracking Turret

## 🔹 Overview
**MDL-26** is an autonomous computer-vision tracking turret developed under **MantidelLabs**.

The system is designed to detect, track, and automatically aim at a human target using:
- Computer Vision
- Embedded Electronics
- Motion Control
- Mechanical Systems
- Real-Time Tracking Algorithms


---

## ✨ Features

✅ Human Body Detection using MediaPipe Pose  
✅ Real-Time Pan-Tilt Tracking  
✅ Python + OpenCV Vision Processing  
✅ ESP32-Based Servo & Hardware Control  
✅ PID-Based Motion Smoothing  
✅ Gear-Driven Mechanical System  
✅ Laser Alignment Testing  
✅ Limit Switch Safety Protection  
✅ Custom PCB Power Distribution  
✅ Real-Time Serial Communication  
✅ Autonomous Target Tracking & Firing

---

## 🧠 System Architecture

The MDL-26 uses two main processing layers:

### 💻 Laptop Side
- Webcam Video Processing
- Human Detection
- Pose Tracking
- PID Calculations
- Motion Prediction
- Serial Command Generation

### ⚡ ESP32 Side
- Servo Control
- Relay Control
- Limit Switch Monitoring
- Motion Smoothing
- Hardware Execution

The laptop sends target position data to the ESP32 through USB serial communication in real time.

---

## ⚙️ Software Stack

- Python
- OpenCV
- MediaPipe
- PySerial
- ESP32 Arduino Framework

---

## 🧩 Hardware Used

### 🔹 Mechanical Components
- MG996R Metal Gear Servos
- 38T & 56T Gear System
- Lazy Susan Bearing
- 22mm Ball Bearings
- Acrylic Structure
- Gel Blaster Platform
- Laser Module
- Webcam (1080p 30FPS)

### 🔹 Electronics
- ESP32 Dev Board
- Relay Module
- Limit Switch
- Custom Zero PCB
- Capacitors
- LEDs
- Fuse Protection
- Buck Converters
- 12V Power Supply

---

## 🎯 How It Works

1️⃣ The webcam captures live video.  
2️⃣ Python processes the frames using MediaPipe Pose Detection.  
3️⃣ The system calculates the target position.  
4️⃣ PID control smooths the movement.  
5️⃣ Position commands are sent to the ESP32.  
6️⃣ The ESP32 controls pan and tilt servos.  
7️⃣ When the target enters the lock zone, the firing system activates.

---

## ⚙️ Mechanical Design

The turret uses a custom acrylic pan-tilt mechanism with:
- Gear reduction system
- Servo-driven motion
- Load support bearings
- Counterweight balancing
- Lazy Susan rotational base

The design focuses on improving:
- Torque
- Stability
- Smoothness
- Structural balance

---

## 🔌 PCB & Electronics

The final system uses a custom soldered PCB design with:
- Thick common grounding
- Fuse protection
- Power filtering capacitors
- Relay control system
- Servo power distribution

The goal was to improve system stability compared to the temporary breadboard setup.

---

## 🎥 Tracking System

The turret tracks the human torso using:
- MediaPipe Pose Detection
- Motion Prediction
- PID Smoothing
- Real-Time Position Correction


---

## ⚠️ Current Limitations

- Low-light tracking performance is limited
- Webcam-based detection can fail in dark environments
- Servo-based motion still has physical limitations
- Tracking speed depends on camera FPS and processing speed

---

## ☘️ Planned Improvements For Next Version

- Better camera systems
- Night vision support
- Faster tracking hardware
- Industrial motors
- Dedicated control architecture
- Raspberry Pi-based processing
- Improved PCB systems
- Better stabilization and precision

---


## 🎥 Full Video Demo

📺 Full build video and testing:  
🔗 [YouTube Video Link]

---

## 💬 Author

👤 Created by: Apurv Singh  
🏢 Founder of MantidelLabs

📱 Socials:  
- Instagram: https://instagram.com/sciapurv  
- YouTube: https://youtube.com/@sciapurv
- LinkedIn: https://www.linkedin.com/in/sciapurv/

---

## 🧠 License

This project is open-source under the MIT License.

Feel free to learn from, modify, and improve the project, but please provide proper credit.

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository  
🔁 Share the project  
💬 Suggest improvements  
🛠️ Build your own version

---

> “MDL-26 is not just a turret project.. it is a learning platform for robotics, embedded systems, computer vision, and autonomous machine design.”
