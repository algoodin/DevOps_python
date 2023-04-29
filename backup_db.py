import datetime
import subprocess

# Define database connection details
db_host = 'localhost'
db_name = 'mydatabase'
db_user = 'myuser'
db_password = 'mypassword'

# Define backup directory
backup_dir = '/backups'

# Generate backup filename with timestamp
backup_filename = f'{db_name}_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.sql'

# Build the mysqldump command
mysqldump_cmd = f'mysqldump --host={db_host} --user={db_user} --password={db_password} --single-transaction --quick {db_name} > {backup_dir}/{backup_filename}'

# Execute the mysqldump command
subprocess.run(mysqldump_cmd, shell=True, check=True)

print(f'Database backup saved to {backup_dir}/{backup_filename}')
