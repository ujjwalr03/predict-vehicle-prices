# **🚗 Vehicle Price Prediction**  

This project builds a **Machine Learning model** to predict vehicle prices based on various specifications such as **make, model, year, mileage, fuel type, and more**.  

---

## ** Features**  
 **Predicts vehicle prices using a Machine Learning model**  
 **Handles missing data and categorical encoding**  
 **Uses Random Forest for accurate predictions**  
 **Supports dataset from GitHub**  
 **Works both locally and in Google Colab**  

---

## ** Technologies Used**  
- **Python**  Main programming language  
- **Pandas**  Data handling  
- **Scikit-Learn**  Machine Learning algorithms  
- **NumPy**  Numerical computations  
- **Jupyter Notebook / Google Colab**  Model training  

---

## ** Steps to Run Locally**  

### **1 Clone the Repository**  
```bash
git clone https://github.com/ujjwalr03/predict-vehicle-prices.git
cd predict-vehicle-prices
```

### **2 Install Dependencies**  
```bash
pip install pandas scikit-learn numpy
```

### **3 Ensure Your Dataset is Available**  
- Make sure `dataset.csv` is in the project directory.  

### **4 Run the Script**  
```bash
python predict-vehicle-price.py
```

### **5 Model Output**
- The script trains a **Random Forest Regressor** and evaluates the model using **MAE, RMSE, and R� Score**.  
- The final prediction will be displayed in the console.  

---

## ** Open in Google Colab**  
Click below to open the notebook in Google Colab:  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ujjwalr03/predict-vehicle-prices/blob/main/predict-vehicle-price-colab.ipynb)  

### **Steps in Google Colab**
1. Click the **"Open in Colab"** button above.  
2. Run all cells (dataset is fetched automatically from GitHub).  
3. The model will train and predict vehicle prices.  

---

## ** License**  
This project is open-source under the **MIT License**.  

---