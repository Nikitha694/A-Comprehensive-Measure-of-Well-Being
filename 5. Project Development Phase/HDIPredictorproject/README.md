# 🌍 A Comprehensive Measure of Well-Being: Intelligent HDI Prediction System

## 📌 Project Description

The Intelligent HDI Prediction System is a Machine Learning-based web application developed using Python and Flask. It predicts the Human Development Index (HDI) score of a country by analyzing important socio-economic indicators such as Life Expectancy, Mean Years of Schooling, Expected Years of Schooling, and Gross National Income (GNI) per Capita.

The application estimates the HDI score using a trained Linear Regression model and classifies the prediction into one of four development categories:
- Very High
- High
- Medium
- Low

---

## ✨ Project Highlights

- Machine Learning based HDI prediction
- Interactive Flask web application
- User-friendly input interface
- Real-time prediction results
- Automatic HDI category classification
- Input validation
- Responsive web pages

---

## 📂 Project Directory

```
HDIProject/
│
├── app.py
├── hdi_prediction.ipynb
├── requirements.txt
├── README.md
│
├── data/
│   └── hdi_dataset.csv
│
├── models/
│   ├── hdi_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    ├── style.css
    └── result.css
```

---

## 🛠 Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Linear Regression

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Backend

- Flask

### Frontend

- HTML
- CSS
- JavaScript

### Development Tools

- Jupyter Notebook
- Visual Studio Code

---

## 📊 Dataset Information

Dataset Source

- UNDP Human Development Report Dataset

Input Features

- Life Expectancy
- Mean Years of Schooling
- Expected Years of Schooling
- Gross National Income (GNI) per Capita

Target Variable

- Human Development Index (HDI)

---

## ⚙️ Installation

Clone the repository

```bash
git clone YOUR_GITHUB_URL
```

Move into the project folder

```bash
cd HDIProject
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Application

### Step 1

Run the Jupyter Notebook to train the model (only if model files are unavailable).

```bash
jupyter notebook
```

Run all notebook cells.

---

### Step 2

Start the Flask application.

```bash
python app.py
```

---

### Step 3

Open your browser.

```
http://127.0.0.1:5000
```

---

## 🔄 System Workflow

1. User enters development indicators.
2. Flask receives the input values.
3. Input data is normalized using the saved scaler.
4. Linear Regression predicts the HDI score.
5. The predicted score is converted into the corresponding HDI category.
6. The result page displays the HDI score, category, and interpretation.

---

## 📈 Model Information

| Item | Details |
|------|---------|
| Algorithm | Linear Regression |
| Features | 4 |
| Target | HDI Score |
| Train-Test Split | 80 : 20 |
| Saved Model | hdi_model.pkl |

---

## 📋 Sample Input Values

| Life Expectancy | Mean Schooling | Expected Schooling | GNI Per Capita |
|----------------|----------------|--------------------|---------------|
| 82.4 | 13.0 | 18.2 | 64660 |
| 76.2 | 10.5 | 14.8 | 18000 |
| 68.5 | 6.8 | 11.2 | 6500 |
| 54.3 | 3.2 | 7.5 | 1800 |

---

## 📦 Python Packages

- Flask
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

---

## 🚀 Future Enhancements

- Prediction history
- Country comparison
- Graphical analytics
- Updated HDI datasets
- Interactive dashboard

---

## 👩‍💻 Developer

**Grandhi Neha Nikitha**

---

## 📜 License

This project was developed for educational purposes as part of the SmartBridge internship program.