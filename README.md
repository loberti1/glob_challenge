# glob_challenge
Build an API to ingest data available in csv files to SQL Server tables. Files (jobs.csv, departments.csv and hired_employees.csv) will be avalible in local folder 'glob_files\'. Logic regarding files is incremental (any new file would have the same name as the previous one but with new data, new IDs)

# 1
Create API using python and flask library, it is intended to upload data to SQL Server only when all files are available