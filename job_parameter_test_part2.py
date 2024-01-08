# Databricks notebook source
#my_catalog = dbutils.jobs.taskValues.get(taskKey = "job_task_1", key = "catalog_name_global")

# COMMAND ----------

# defined as a job parameter via the Jobs UI
# job_task_catalog_name

my_catalog = dbutils.widgets.get('job_task_catalog_name')

# COMMAND ----------

spark_df = spark.table(f'{my_catalog}.ogden_churn.churn_scores')
display(spark_df)
