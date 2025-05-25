# 🛡️ Network Security Threat Detection Pipeline

A complete machine learning pipeline to automate **ETL, model training, validation, deployment, and real-time predictions** for detecting network threats using structured data. Built using **FastAPI**, **MongoDB**, and **scikit-learn**, with modular components for each stage of the ML workflow.

---

## 🚀 Key Features

- ✅ Modular and reusable ETL pipeline (ingestion → validation → transformation)
- ✅ Model training and evaluation logic
- ✅ MongoDB for secure storage
- ✅ FastAPI app for real-time predictions via CSV upload
- ✅ HTML-based output visualization
- ✅ Docker-compatible

---

## 🧱 Project Structure

```

.
├── app.py                            # FastAPI web server for predictions
├── main.py                           # Script to trigger the full training pipeline
├── final\_models/                     # Trained model (.pkl files)
├── templates/                        # Jinja2 HTML templates for results display
├── prediction\_output/                # CSV files with prediction output
├── valid\_data/                       # Validated datasets
├── Network\_Data/                     # Raw input datasets
├── data\_schema/                      # Schema definition for validation
├── networksecurity/                 # Core ML components (ETL, config, exceptions)
├── requirements.txt                  # Dependencies
├── Dockerfile                        # Docker deployment setup
├── setup.py                          # Installable package config

````

---

## ⚙️ Tech Stack

- Python 3.x
- FastAPI
- Pandas, NumPy
- Scikit-learn
- Pymongo (MongoDB)
- Certifi, Uvicorn
- Docker
- HTML (Jinja2 templates)

---

## 💻 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/network-security-pipeline.git
cd network-security-pipeline
````

### 2. Create and Activate Environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file in the root with the following:

```env
MONGO_DB_URL=mongodb+srv://<username>:<password>@cluster.mongodb.net/dbname
```

### 5. Run the Full ML Pipeline

```bash
python main.py
```

### 6. Launch the Web Server (for predictions)

```bash
python app.py
```

Visit: `http://localhost:8000/docs` for Swagger UI.

---

## 🔎 FastAPI Endpoints

| Method | Endpoint   | Description                           |
| ------ | ---------- | ------------------------------------- |
| GET    | `/`        | Redirect to docs                      |
| GET    | `/train`   | Triggers full model training pipeline |
| POST   | `/predict` | Upload a CSV file for prediction      |

---

## 🧠 ML Pipeline Overview

1. **Data Ingestion**
   Pulls raw CSV data from `Network_Data/` and stores it in MongoDB.

2. **Data Validation**
   Ensures schema conformity based on rules in `data_schema/`.

3. **Data Transformation**
   Transforms features using scikit-learn preprocessing pipelines.

4. **Model Training**
   Trains a classification model and saves artifacts to `final_models/`.

5. **Prediction**
   CSV files can be uploaded via API; predictions are returned with HTML table view and saved to `prediction_output/`.

---

## 📦 Docker Usage

```bash
docker build -t network-security-app .
docker run -p 8000:8000 network-security-app
```

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Vaibhav** – Specializing in applied ML, automation pipelines, and cloud deployment.

---
