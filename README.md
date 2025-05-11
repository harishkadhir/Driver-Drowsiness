# 🚗 Driver Drowsiness & Distraction Detection (YOLOv11)

This real-time AI system monitors drivers for signs of drowsiness, distraction, and unsafe behavior, enhancing road safety. Built with **YOLOv11**, **OpenCV**, and **Pygame**, it detects dangerous behaviors such as mobile phone usage, talking, head movement (left/right), and drowsiness, and triggers an audio alert when any of these are detected.

![GIF_20250511_102548](https://github.com/user-attachments/assets/2f248faf-7962-4339-bd48-fb5b1b7b7513)


## 🔍 Features

- **Real-time Detection:** Continuously processes webcam input.
- **Detects:**
  - Drowsiness
  - Mobile phone usage
  - Talking
  - Head movement (left/right)
  - Child presence
- **Audio Alerts:** Triggers an audio alarm via `pygame` when distraction is detected.
- **Custom YOLOv11 Model:** Trained on specific driver behavior data.
- **Works with Webcam:** Runs on any device with a webcam.

## 🧠 Tech Stack

- [YOLOv11](https://github.com/ultralytics/ultralytics) (Ultralytics for object detection)
- [OpenCV](https://opencv.org/) (Video frame processing)
- [Pygame](https://www.pygame.org/) (Audio alert handling)
- Python 3.8+

## 📁 Dataset

The dataset used for training includes several classes:

- **drowsy**
- **mobile**
- **talking**
- **child**
- **LeftRight**
- **person** (ensures that a driver is present)

You can easily modify or extend the dataset by adding more distraction classes.

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/harishkadhir/Driver-Drowsiness.git

   
   
