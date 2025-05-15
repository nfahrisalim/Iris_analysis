````markdown
# Big Data Project: Iris Dataset Analysis

This project focuses on analyzing the Iris dataset using Python, Apache Spark, and data visualization libraries. It is developed as part of the Big Data course at the Information Systems Program, Universitas Hasanuddin (UNHAS), 2025.

## 1. Prerequisites & Tool Verification

Before starting, ensure the following tools are installed and properly configured in your system's PATH:

```bash
python --version
java -version
hadoop version
spark-shell --version
````

If any command is unrecognized, make sure the tool is installed and its installation directory is added to the PATH environment variable.

---

## 2. Project Setup

### a. Create Project Folder

Create the project directory under your user profile or any preferred path:

```bash
mkdir %USERPROFILE%\bigdata_iris
cd %USERPROFILE%\bigdata_iris
```

### b. Create Virtual Environment

```bash
python -m venv big-data-iris
```

### c. Activate Virtual Environment

```bash
big-data-iris\Scripts\activate
```

### d. Deactivate Virtual Environment

```bash
deactivate
```

---

## 3. Install Dependencies

Once the virtual environment is active, install the required Python libraries:

```bash
pip install --upgrade pip
pip install pandas pyarrow matplotlib pyspark kaggle
```

---

## 4. Dataset Download: Iris.csv

### Option 1: From GitHub

```bash
curl -o iris.csv https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv
```

### Option 2: From Kaggle

1. Log in to [Kaggle](https://www.kaggle.com/account) and create a new API token.
2. Move `kaggle.json` to:

```bash
mkdir %USERPROFILE%\.kaggle
copy C:\Users\<YourUsername>\Downloads\kaggle.json %USERPROFILE%\.kaggle\
```

3. Download and extract the dataset:

```bash
kaggle datasets download -d uciml/iris
powershell -command "Expand-Archive iris.zip -DestinationPath ."
```

### Option 3: Local File

```bash
copy C:\Data_NIM\iris.csv %USERPROFILE%\bigdata_iris\iris.csv
```

---

## 5. Upload to Hadoop (Optional)

### a. Start Hadoop Services

```bash
start-dfs.cmd
start-yarn.cmd
```

### b. Upload File to HDFS

```bash
hdfs dfs -mkdir -p /user/iris
hdfs dfs -put iris.csv /user/iris/
hdfs dfs -ls /user/iris
```

---

## 6. VS Code Setup

### a. Open the Project in VS Code

```bash
code %USERPROFILE%\bigdata_iris
```

### b. Inside VS Code

* Install the Python extension
* Open Command Palette (`Ctrl+Shift+P`)
* Choose "Python: Select Interpreter" → select `big-data-iris\Scripts\python.exe`

---

## 7. Run the Analysis Script

Activate the environment and run the script:

```bash
big-data-iris\Scripts\activate
python analyze_iris.py
```

The output will include visualizations such as `sepal_scatter.png` or `hasil_sepal_scatter.png` stored in the project directory.

---

## Author

Muh. Naufal Fahri Salim – Sistem Informasi 2023
Project for Big Data Course


