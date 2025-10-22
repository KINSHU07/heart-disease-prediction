# 💓 Heart Disease Prediction Using Machine Learning

Heart disease is one of the leading causes of death in India, accounting for nearly **25% of all fatalities**. Factors such as sedentary lifestyle, unhealthy diet, stress, and lack of early diagnosis have made cardiovascular diseases increasingly common.

This project uses **Machine Learning** to predict the likelihood of heart disease in a patient based on clinical and demographic data. The model aims to assist in early detection and prevention, improving overall public health awareness.

---

## 🎯 Objective

To build a machine learning–based web application that predicts a person's heart disease risk using health parameters such as blood pressure, cholesterol, and heart rate.

---

## 📊 Dataset

- **Source:** UCI Heart Disease Dataset
- **Total Samples:** 303
- **Features:** 14 (13 independent + 1 target)

### Feature Description

| Feature | Description |
|---------|-------------|
| `age` | Age of the patient |
| `sex` | Sex (1 = male, 0 = female) |
| `cp` | Chest pain type (0–3) |
| `trestbps` | Resting blood pressure (mm Hg) |
| `chol` | Serum cholesterol (mg/dl) |
| `fbs` | Fasting blood sugar > 120 mg/dl (1 = true, 0 = false) |
| `restecg` | Resting electrocardiographic results (0–2) |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina (1 = yes, 0 = no) |
| `oldpeak` | ST depression induced by exercise relative to rest |
| `slope` | Slope of the peak exercise ST segment |
| `ca` | Number of major vessels colored by fluoroscopy (0–3) |
| `thal` | Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect) |
| `target` | Presence of heart disease (1 = yes, 0 = no) |

---

## 🧩 Project Workflow

### 🧪 1. Exploratory Data Analysis (EDA)
- Data cleaning and null value handling
- Outlier detection using boxplots
- Correlation heatmap between features
- Visualization of key risk factors

### ⚙️ 2. Feature Engineering
- Feature scaling and normalization
- Encoding categorical variables
- Splitting dataset into train and test sets

### 🧠 3. Model Building
- Trained multiple ML models:
  - Logistic Regression
  - Random Forest Classifier
  - Support Vector Machine (SVM)
- Evaluated models using accuracy, precision, recall, and F1-score

### 🧾 4. Model Testing
- Compared performance on test data
- Selected the best-performing model
- Saved the model using `pickle`

### 🌐 5. Deployment
- Deployed using Streamlit Cloud
- Interactive user interface for predictions

---

## 💻 Tech Stack

| Category | Tools / Libraries |
|----------|-------------------|
| **Programming** | Python |
| **Data Handling** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn |
| **Deployment** | Streamlit |
| **Model Storage** | Pickle |

## 🌍 Deployment

This project is deployed on **Streamlit Cloud**. You can access the live app here:

👉 **[Heart Disease Prediction App](https://heartfriendai.streamlit.app/)**

---

## ❤️ About

This project was created to demonstrate the use of **Machine Learning in healthcare** — showcasing how data science can play a key role in early detection and prevention of cardiovascular diseases.

**Developed by:** Kinshu Keshri  
**Roll No.:** AD24B1034

---

<p align="center">
  Made with ❤️ by <b>Kinshu Keshri</b> | Roll No. AD24B1034
</p>
