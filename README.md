# ♻️ Waste Detection Project

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.13.1-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![YOLOv5](https://img.shields.io/badge/YOLOv5-7.0-red?logo=opencv&logoColor=white)](https://github.com/ultralytics/yolov5/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/)
[![jQuery](https://img.shields.io/badge/jQuery-0769AD?logo=jquery&logoColor=white)](https://jquery.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Project Overview
**Waste Detection Project** is an end-to-end waste detection solution leveraging YOLOv5 to:
- 🔍 **Detect waste objects** from uploaded images
- 🎥 **Perform live object detection** via webcam
- 🌱 **Classify waste across 13 classes**:

> `banana`, `chilli`, `drinkcan`, `drinkpack`, `foodcan`, `lettuce`, `paperbag`, `plasticbag`, `plasticbottle`, `plasticcontainer`, `sweetpotato`, `teabag`, `tissueroll`

---

## 🔥 Project Workflow

The project is organized in a clean, modular fashion:

1️⃣ **constants** — Defines global constants, paths, and settings used across the project.  
2️⃣ **entity** — Defines the data models, configurations, and schema for inputs and outputs.  
3️⃣ **components** — Core processing units like data ingestion, data validation, and model training.  
4️⃣ **pipelines** — Orchestration of the end-to-end workflow by connecting components together.  
5️⃣ **app.py** — The main entry point that serves as the REST API and frontend handler.

---

---

## ⚡️ Features
✅ Upload an image and get detected waste results.  
✅ Real-time detection through webcam (`live detection`).  
✅ Integrated YOLOv5 ONNX model for high-performance inference.  
✅ REST API built with Flask for seamless integration.  

---

## 🗂️ Model Training Pipeline
This project implements a robust, modular pipeline:

```mermaid
graph TD
    A[Data Ingestion] --> B[Data Validation]
    B --> C[Model Trainer]
    C --> D[Results & Export]
````

### 1️⃣ Data Ingestion

* Collect waste images
* Split into train/test sets
* Store data for further processing

### 2️⃣ Data Validation

* Validate labels, images, and dataset structure
* Ensure model is trained on clean, organized data

### 3️⃣ Model Trainer

* Trains YOLOv5 ONNX model
* Export ONNX model for optimized inference

---

## ⚙️ Tech Stack

| Layer      | Tool              | Purpose                          |
| ---------- | ----------------- | -------------------------------- |
| Frontend   | HTML, CSS, jQuery | Responsive user interface        |
| Backend    | Flask             | REST APIs for detection          |
| Model      | YOLOv5 ONNX       | High-performance waste detection |
| Framework  | PyTorch           | Model Training and Export        |
| Deployment | ONNX Runtime      | Enables fast inference           |

---

## 🚀 Getting Started

### 🔥 Clone the Repository

```bash
git clone https://github.com/Phoenixarjun/Waste-Detection-Using-YOLOv5
cd Waste-Detection-Using-YOLOv5
```

### 🐍 Install Dependencies

```bash
pip install -r requirements.txt
```


## ⚡️ Usage

#### 🖥️ Run the App

```bash
python app.py
```

#### 🌐 Access the App

Visit 👉 [http://localhost:8080](http://localhost:8080)

#### 📷 Features

* **Upload Image** ➔ Get detection results
* **Live Detection** ➔ Real-time object detection using webcam
* **Stop Detection** ➔ Stops the live stream gracefully

---

## 🖼️ Demo

![Screenshot 2025-06-22 161441](https://github.com/user-attachments/assets/c78e6629-b1f1-4b37-a4ed-56d995f9eee8)

![Screenshot 2025-06-22 161458](https://github.com/user-attachments/assets/1edb1724-368c-4008-ae21-fc7f70c297cb)

![Screenshot 2025-06-22 161526](https://github.com/user-attachments/assets/91e58780-0b19-4918-b5ec-e7a7001b4aaf)

![Screenshot 2025-06-22 161549](https://github.com/user-attachments/assets/db64aad8-9c44-4f5a-a7ea-939d2e68767a)

---

## 🛠️ Future Improvements

* ✅ Export detection results as downloadable JSON
* 📊 Integrate analytics & dashboards
* ⚡️ Model optimization for mobile and edge deployments
* 🐳 Containerize app with Docker
* 📱 Build a mobile app for waste detection

---

## 📄 License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.

---

## 👋 Credits

Created by **Naresh B A**
💡 **Full Stack Developer | AI/ML Enthusiast**
[LinkedIn](https://www.linkedin.com/in/naresh-b-a-1b5331243)

> ⭐️ If you found this project helpful, give it a star!

---
