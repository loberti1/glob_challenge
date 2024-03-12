#import libraries
import pandas as pd
import os
from flask import Flask, request
from sqlalchemy import create_engine

#create application instance >> object class flask
app = Flask(__name__)

#generate connection
server = 'E-01520'
database = 'glob_dw'
username = 'sqlserverluciano'
password = 'crisiscore789'

connection = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connection)

#define Url and view function to apply, when a client sends a request to this route, this code
#would be applied as a response
@app.route('/',methods = ['POST'])

def loading():
      
      """view function to load data to SQL Server tables"""

      path = 'C:\\Users\\COREBI\\Desktop\\archivos\\'
      os.chdir(path)

      try:
        #loop to insert batches up to 1000 rows
        for file, max_rows in zip(['jobs.csv', 'departments.csv', 'hired_employees.csv'], [1000, 1000, 1000]):
            df = pd.read_csv(file, header = None, chunksize = max_rows)
            for data in df:
                if file == 'jobs.csv':
                    data.columns = ['id_jobs','ds_jobs']
                elif file == 'departments.csv':
                    data.columns = ['id_departments','ds_departments']
                elif file == 'hired_employees.csv':
                    data.columns = ['id_custom_hired_employee','ds_hired_employee','id_datetime','id_departments','id_jobs']
                else: None

                data.to_sql(file.split('.')[0], engine, if_exists='append', index=False)

        return 'data was loaded successfully'
    
      except Exception as e:
        return f'error present: {e}'

if __name__ == '__main__':
    app.run(debug=True)

#command to send requests:
#curl -X POST -F "jobs.csv=@C:\Users\COREBI\Desktop\archivos\jobs.csv" -F "departments.csv=@C:\Users\COREBI\Desktop\archivos\departments.csv" -F "hired_employees.csv=@C:\Users\COREBI\Desktop\archivos\hired_employees.csv" http://127.0.0.1:5000/
    



