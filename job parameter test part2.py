# Databricks notebook source
my_catalog = dbutils.jobs.taskValues.get(taskKey = "job_task_1", key = "catalog_name_global")

# COMMAND ----------

spark_df = spark.table(f'{my_catalog}.ogden_churn.churn_batch_scores')
display(spark_df)
