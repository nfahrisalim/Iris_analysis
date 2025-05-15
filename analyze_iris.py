import os
os.environ["PYSPARK_PYTHON"] = "D:/Data Science/bigdata_iris/big-data-H071231031/Scripts/python.exe"


from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

# Inisialisasi Spark
spark = SparkSession.builder.appName("IrisAnalysis").getOrCreate()

# Load dataset
# Gunakan salah satu dari: lokal / HDFS / absolut
# df = spark.read.csv("hdfs://localhost:9000/user/iris/iris.csv", header=True, inferSchema=True)
df = spark.read.csv("iris.csv", header=True, inferSchema=True)

# Tampilkan schema dan sampel data
df.printSchema()
df.show(5)

# Hitung jumlah record per spesies
df.groupBy("Species").count().show()

# Konversi ke pandas
pdf = df.toPandas()

# Visualisasi sepal length vs width
plt.figure(figsize=(8,6))
for sp in pdf["Species"].unique():
    subset = pdf[pdf["Species"] == sp]
    plt.scatter(subset["SepalLengthCm"], subset["SepalWidthCm"], label=sp)

plt.title("Sepal Length vs Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend()
plt.savefig("sepal_scatter.png")

spark.stop()