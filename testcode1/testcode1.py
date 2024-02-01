# Databricks notebook source
f = open("demofile2.txt", "w")
f.write("Now the file has more content!")
f.close()

# COMMAND ----------

# MAGIC %sh
# MAGIC ##rm demofile2.txt
# MAGIC ls
# MAGIC
