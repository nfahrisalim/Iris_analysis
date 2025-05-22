from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[*]", "SocketWordCount")
ssc = StreamingContext(sc, 20)

lines = ssc.socketTextStream("localhost", 9999)

# Tambahan debug print untuk memastikan data masuk

lines.foreachRDD(lambda rdd: print(f"Received {rdd.count()} lines in this batch"))

# Proses word count
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
word_counts = pairs.reduceByKey(lambda x, y: x + y)

# Tampilkan hasil
word_counts.pprint()

ssc.start()
ssc.awaitTermination()
