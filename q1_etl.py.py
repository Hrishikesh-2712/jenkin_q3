
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,avg


spark = SparkSession.builder.appName('Spark-App-1').getOrCreate()

df = spark.read.csv('employees.csv', header=True, inferSchema=True)

print('Schema : ')
df.printSchema()

df_filtered = df.filter(col('emp_id').isNotNull())

avg_salary = df_filtered.select(avg('salary')).collect()[0][0]

                        
print(avg_salary, 'avg salary')
df_filtered = df_filtered.fillna({'salary':avg_salary})


employee_count_department = df_filtered.groupBy('dept').count()
print('employee count per department')
employee_count_department.show()

df_filtered.createOrReplaceTempView('employees')


highest_salary = spark.sql("""SELECT e.* FROM employees e JOIN( SELECT dept, MAX(salary) AS max_salary FROM employees GROUP BY dept) m
                           ON e.dept = m.dept AND e.salary = m.max_salary""")


print('Employee highest salary')
highest_salary.show()


df_filtered.write.mode('overwrite').parquet('output/')

read_parquet = spark.read.parquet('output/')
print('Total rows:')
print(read_parquet.count())



