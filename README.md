# Real-Time Road Lane Detection using OpenCV

A real-time computer vision pipeline built with Python and OpenCV that detects yellow road lane markings from dashcam video footage using color thresholding, edge filtering, and probabilistic Hough transforms.

---

## 📌 Overview

This project implements an edge- and color-based lane detection algorithm designed to identify lane lines in driving videos. It isolates yellow lane markings using the HSV color space, filters noise, detects boundaries via Canny edge detection, and maps straight line segments onto the original video feed in real time[cite: 1].

---

## ⚙️ How It Works (Pipeline)

1. **Video Streaming & Looping.**
2. **Noise Reduction.**
3. **Color Space Conversion.**
4. **Yellow Masking.**
5. **Edge Detection.**
6. **Probabilistic Hough Transform.**
7. **Region Filtering & Overlay.**

---

## 🛠️ Tech Stack & Prerequisites

* **Language:** Python 3.x
* **Libraries:**
  * `opencv-python`[cite: 1]
  * `numpy`[cite: 1]
