# 🚀 Python Security Camera

Welcome to the Python Security Camera project! This is a robust and efficient security camera system implemented in Python. It uses OpenCV for real-time video capture and Haar cascades for object detection, providing a comprehensive solution for home and office security needs.

## 🌟 Features

- **Real-time video capture**: The system captures video in real-time using the default camera, ensuring up-to-date surveillance.

- **Face and body detection**: Leveraging the power of Haar cascades, the system can detect faces and bodies in the video frames, making it a reliable tool for human presence detection.

- **Recording**: The system is smart! When it detects movement, it starts recording. It stops recording after a certain period of inactivity, saving storage space.

- **Timestamped video files**: Each video file is named with the date and time when recording started, making it easy to track and review footage.

## 📚 Modules Used

- `cv2`: OpenCV library for capturing video frames and image processing. It's a powerful library for computer vision tasks.

- `time` and `datetime`: These built-in Python modules are used for time-related functions, providing functionality for the system to react based on time events.

## 🚀 How to Run

1. Ensure you have Python installed on your machine.

2. Install the necessary libraries using pip:

```bash
pip install opencv-python

🕹️ How It Works
The script starts by initializing the video capture using the default camera and loading the Haar cascades for face and body detection.
It then enters an infinite loop where it continuously captures video frames and processes them.
Each frame is converted to grayscale and passed to the face and body detectors.
If any faces or bodies are detected, the system checks if it’s currently in detection mode. If it’s not, it enters detection mode, starts a new video recording, and prints “Started Recording!”.
If no faces or bodies are detected but the system is in detection mode, it checks if the timer has started. If it has, and enough time has passed since the last detection, it stops detection mode, stops the timer, stops the video recording, and prints “Stop Recording!”. If the timer hasn’t started, it starts the timer.

🤝 Contributions
Contributions to this project are welcome! Please fork the repository and open a pull request with your changes. Let’s make this project better together!

📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.

