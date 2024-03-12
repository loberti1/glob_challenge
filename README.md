# glob_challenge
Build an API to ingest data available in csv files to SQL Server tables. Files (jobs.csv, departments.csv and hired_employees.csv) will be avalible in local folder 'glob_files\'. Logic regarding files is incremental (any new file would have the same name as the previous one but with new data, new IDs)

# 1
Create API using python and flask library, it is intended to upload data to SQL Server. ODBC driver "sqlserverluciano" had to be created for connection purposes. Files are available locally in path 'C:\Users\COREBI\Desktop\archivos\' (until we get to last section, when I plan to make it more robust)
Apart from that, it inserts batches up to 1000 rows, it uses loops to iterate through chunks.

You can send requests using this command:
curl -X POST -F "jobs.csv=@C:\Users\COREBI\Desktop\archivos\jobs.csv" -F "departments.csv=@C:\Users\COREBI\Desktop\archivos\departments.csv" -F "hired_employees.csv=@C:\Users\COREBI\Desktop\archivos\hired_employees.csv" http://127.0.0.1:5000/

# 2
Inside SQL folder, all queries needed can be accesed. DDL and DML were defined for this section, pretty straightforward. I will add an endpoint for this queries after I verified the information requiremets are met.