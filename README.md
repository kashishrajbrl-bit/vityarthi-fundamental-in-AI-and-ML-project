# 🏥 AI-Powered Doctor Recommendation System

> An intelligent symptom-based doctor recommendation system using Machine Learning and Graph Traversal algorithms to find the nearest suitable specialist.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange?logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-013243?logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Dataset](#-dataset)
- [Sample Output](#-sample-output)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

This project combines **Machine Learning** with **Graph Search Algorithms** to:

1. Predict the required medical specialist based on a patient's symptoms.
2. Find the **nearest clinic/hospital** offering that specialist using **BFS (Breadth-First Search)**.
3. List **all available paths** to the specialist using **DFS (Depth-First Search)**.

It simulates a real-world healthcare routing system where patients get directed to the right doctor through the shortest path.

---

## ✨ Features

- 🤖 **ML-based Symptom Classification** — Uses a Decision Tree Classifier to predict the appropriate specialist.
- 🗺️ **Shortest Path via BFS** — Finds the nearest healthcare facility with the required doctor.
- 🔁 **All Paths via DFS** — Lists every possible route to the required specialist.
- 🧠 **Graph-based Hospital Network** — Models real-world clinic/hospital connectivity as a graph.
- 💻 **Interactive CLI** — Simple terminal-based symptom input interface.

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.8+ |
| ML Model | `scikit-learn` — Decision Tree Classifier |
| Data Handling | `NumPy` |
| Graph Traversal | BFS & DFS (built-in `collections.deque`) |
| Interface | Command Line (CLI) |

---

## 🏗️ System Architecture

```
Patient Input (Symptoms)
        │
        ▼
┌───────────────────────┐
│  Decision Tree Model  │  ← Trained on symptom-specialist dataset
│  (Specialist Predict) │
└──────────┬────────────┘
           │ Recommended Specialist
           ▼
┌───────────────────────┐
│   Graph Search (BFS)  │  ← Finds shortest path to nearest doctor
│   Graph Search (DFS)  │  ← Finds all available doctor paths
└──────────┬────────────┘
           │
           ▼
  Output: Location + Path
```

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Steps

```bash

# 1. Navigate into the project directory
cd ai-doctor-recommendation

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install the required dependencies
pip install -r requirements.txt
```

### `requirements.txt`

```
numpy>=1.21.0
scikit-learn>=1.0.0
```

---

## 🚀 Usage

```bash
python doctor_recommendation.py
```

You will be prompted to enter symptoms interactively:

```
Enter symptoms (1 = Yes, 0 = No):
Fever: 
Cough: 
Chest Pain: 
Headache: 
```

Enter `1` for **Yes** or `0` for **No** for each symptom.

---

## 📁 Project Structure

```
ai-doctor-recommendation/
│
├── doctor_recommendation.py   # Main application script
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore rules
```

---

## ⚙️ How It Works

### 1. 🧪 Symptom-to-Specialist Prediction (Machine Learning)

A **Decision Tree Classifier** is trained on a small labeled dataset mapping symptom combinations to specialist types:

| Fever | Cough | Chest Pain | Headache | Specialist |
|:---:|:---:|:---:|:---:|---|
| ✅ | ✅ | ❌ | ❌ | General Physician |
| ❌ | ❌ | ✅ | ❌ | Cardiologist |
| ❌ | ❌ | ❌ | ✅ | Neurologist |
| ✅ | ❌ | ❌ | ✅ | General Physician |
| ❌ | ✅ | ❌ | ❌ | ENT |

The model predicts one of: `General Physician`, `Cardiologist`, `Neurologist`, `ENT`.

---

### 2. 🗺️ Hospital Network (Graph)

The healthcare facility network is represented as a **directed graph**:

```
         Home
        /    \
   Clinic_A  Clinic_B
      |           |
 Hospital_X   Hospital_Y
```

| Facility | Available Specialist |
|---|---|
| Clinic_A | General Physician |
| Clinic_B | ENT |
| Hospital_X | Cardiologist |
| Hospital_Y | Neurologist |

---

### 3. 🔍 BFS — Nearest Doctor

Breadth-First Search explores the graph **level by level**, guaranteeing the **shortest path** to the required specialist.

```python
bfs_find_doctor("Home", "Cardiologist")
# Returns: ("Hospital_X", ["Home", "Clinic_A", "Hospital_X"])
```

---

### 4. 🔁 DFS — All Available Paths

Depth-First Search explores **all possible routes** through the graph recursively.

```python
dfs_all_doctors("Home", "General Physician")
# Returns all paths leading to a General Physician
```

---

## 📊 Dataset

The model is trained on a small hardcoded dataset for demonstration purposes. The features are:

```python
X = np.array([
    [1, 1, 0, 0],  # Flu           → General Physician
    [0, 0, 1, 0],  # Chest issue   → Cardiologist
    [0, 0, 0, 1],  # Head issue    → Neurologist
    [1, 0, 0, 1],  # Mixed         → General Physician
    [0, 1, 0, 0],  # Cough only    → ENT
])
```

> **Note:** This dataset is minimal and intended for educational/demonstration use. A production system would use a larger, validated medical dataset.

---

## 🖥️ Sample Output

```
Enter symptoms (1 = Yes, 0 = No):
Fever: 0
Cough: 0
Chest Pain: 1
Headache: 0

Recommended Specialist: Cardiologist

Nearest Doctor at: Hospital_X
Path: Home → Clinic_A → Hospital_X

All available doctor paths (DFS):
Hospital_X: Home → Clinic_A → Hospital_X
```

---

## 🔮 Future Improvements

- [ ] Expand the symptom dataset with real medical data
- [ ] Add more symptom inputs (e.g., fatigue, nausea, shortness of breath)
- [ ] Integrate a weighted graph for distance-aware routing
- [ ] Build a web interface using Flask or Streamlit
- [ ] Add support for doctor availability and appointment booking
- [ ] Replace the Decision Tree with a more robust model (Random Forest, XGBoost)
- [ ] Include urgency-level detection for emergency routing

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes and commit (`git commit -m 'Add some feature'`)
4. Push to your branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

Please make sure your code follows clean coding practices and is well-commented.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Made with ❤️ for educational purposes.  
Feel free to ⭐ star this repository if you found it helpful!
