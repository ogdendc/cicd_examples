# Databricks notebook source
# DBTITLE 1,Option A:  set a task parameter in an upstream task and re-use it downstream
# Note: Need to reference the name of the upstream task in which the task parameter is defined.

#my_catalog = dbutils.jobs.taskValues.get(taskKey = "job_task_1", key = "task_parameter_reused")

# COMMAND ----------

# DBTITLE 1,Option B:  set job-level parameter and call that parameter as if it were a widget
# Note:  This approach would not require setting a task parameter upstream.
# For this approach, I've defined as a job-level parameter via the Jobs UI.

my_catalog = dbutils.widgets.get('job_parameter_catalog_name')

# COMMAND ----------

spark_df = spark.table(f'{my_catalog}.ogden_churn.churn_scores')
display(spark_df)
