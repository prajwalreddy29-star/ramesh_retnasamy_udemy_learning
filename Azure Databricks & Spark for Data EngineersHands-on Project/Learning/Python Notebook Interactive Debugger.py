# Databricks notebook source
# MAGIC %md
# MAGIC ### Demo1
# MAGIC
# MAGIC Demonstrate
# MAGIC
# MAGIC   1. Breakpoints
# MAGIC   2. Step through code line by line
# MAGIC   3. Variable Explorer
# MAGIC   4. Debug Console

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

#Calculate the final price of an ite, that value


item_price = 120.00
tax_rate = 20 #Given in percentage
discount = 10.00

#1. Calculate the tax to be applied.

tax = item_price * (tax_rate / 100)

#2. Apply tax to the item price
item_price_with_tax = item_price + tax

#3. Apply flat discount to the item price
final_price = item_price_with_tax - discount

# Print the final price
print(f"Final Price : { final_price: .2f}")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Demo 2
# MAGIC
# MAGIC Demonstrate Step in and Step out

# COMMAND ----------

def calculate_final_price(item_price,tax_rate,discount):
  #1. Calculate the tax to be applied.

  tax = item_price * (tax_rate / 100)

  #2. Apply tax to the item price
  item_price_with_tax = item_price + tax

  #3. Apply flat discount to the item price
  final_price = item_price_with_tax - discount

  return final_price

# COMMAND ----------

#main program

item_price = 120.00
tax_rate = 20 #Given in percentage
discount = 10.00

final_price = calculate_final_price(item_price,tax_rate,discount)

print(f"Final Price : { final_price: .2f}")

# COMMAND ----------

# MAGIC %sql
# MAGIC select current_metastore();

# COMMAND ----------

# MAGIC %fs ls 's3://databricks-practice-bucket-01/source_data/customers/'

# COMMAND ----------

spark.read.format("csv").load("s3://databricks-practice-bucket-01/source_data/customers/customers.csv").display()
