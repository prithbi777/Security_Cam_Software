# 🎥 Security Camera with Motion Detection  

**👨‍💻 Author:** Prithbiraj Mahanta  
**📅 Date:** 11 March, 2025  

## 📄 Overview  
The **Security Camera with Motion Detection** is a Python-based tool that uses a webcam to detect motion and plays a warning sound whenever movement is detected. This is ideal for home security, office surveillance, or monitoring specific areas.

## ⚙️ How It Works  
1️⃣ The webcam captures the initial frame as a reference.  
2️⃣ Each new frame is compared with the reference frame to detect motion.  
3️⃣ If motion is detected:  
   - 🟩 A **green rectangle** highlights the moving object.  
   - 🔊 A **warning sound** plays (with a cooldown period to prevent spamming).  
4️⃣ The reference frame is updated continuously to track ongoing motion effectively.  

## 🛠️ Technologies Used  
- **Python**  
- **OpenCV** (For video processing)  
- **Pygame** (For sound alerts)  
- **NumPy** (For efficient numerical operations)  

## 🚀 Features  
✅ Real-time motion detection.  
✅ Visual indication of detected motion.  
✅ Audio alert with cooldown to prevent repetitive sounds.  
✅ Simple and user-friendly interface.  

## 📦 Installation  
1. Install Python if not already installed.  
2. Install the required libraries using:  
   ```bash
   pip install opencv-python pygame numpy
