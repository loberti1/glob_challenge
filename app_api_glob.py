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
user = 'COREBI@E-01520'

connection = f'mssql+pyodbc://{server}/{user}/{database}?trusted_connection=yes&driver=\
                ODBC+Driver+17+for+SQL+Server'

engine = create_engine(connection)

#define Url and view function to apply, when a client sends a request to this route, this code
#would be applied as a response
@app.route('/',methods = ['POST'])

def loading():
      """view function to load data to SQL Server tables"""
      
      path = 'C:\\Users\\COREBI\\Desktop\\archivos\\'
      os.chdir(path)
      
      try:
        files_to_upload = ['jobs.csv','departments.csv','hired_employees.csv']
        for x in files_to_upload:
            if (x not in request.files):
                return 'Be careful, {x} is not available at the moment'
    
        #read and write dfs
        jobs = pd.read_csv(request.files['jobs.csv'])
        employees = pd.read_csv(request.files['hired_employees.csv'])
        departments = pd.read_csv(request.files['departments.csv'])

        jobs.to_sql('dim_jobs', engine, if_exists='append', index=False)
        employees.to_sql('ft_hired_employees', engine, if_exists='append', index=False)
        departments.to_sql('dim_departments', engine, if_exists='append', index=False)
        
        return 'data was loaded successfully'
    
      except Exception as e:
        return f'error present: {e}'

if __name__ == '__main__':
    app.run(debug=True)