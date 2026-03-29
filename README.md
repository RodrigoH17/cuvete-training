# Covete Training

This project is responsible for training computer vision models to automatically identify the type of meat contained in covetes.

## 📌 Objective

The goal of this project is to train image classification models capable of identifying different types of meat (e.g., chicken, pork, beef, turkey) based on images collected in a real industrial environment.

The trained model will later be deployed in the production system (`covete-classifier`), running on a Raspberry Pi for real-time classification and counting.

---

## 🧠 System Architecture

This project is part of a larger system composed of three components:

* **covete-capture** → image collection in the factory
* **covete-training** → model training (this project)
* **covete-classifier** → real-time classification and counting

---

## ⚙️ Environment Setup

Create a virtual environment:

python -m venv venv
```

Activate (Windows PowerShell):

venv\Scripts\Activate.ps1
```

Install dependencies:

pip install -r requirements.txt
```
---

## 👤 Author

Rodrigo Henriques
