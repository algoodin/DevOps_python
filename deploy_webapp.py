import os
import shutil
import paramiko

# Define SSH connection details
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('server.example.com', username='username', password='password')

# Define path to the web application folder on the local machine
local_path = '/path/to/web/application'

# Define path to the web application folder on the remote server
remote_path = '/var/www/html'

# Create a tarball of the web application folder
shutil.make_archive('webapp', 'tar', local_path)

# Upload the tarball to the remote server
sftp = ssh.open_sftp()
sftp.put('webapp.tar', remote_path + '/webapp.tar')
sftp.close()

# Extract the tarball on the remote server
ssh.exec_command('cd ' + remote_path + '; tar -xf webapp.tar')

# Restart the web server
ssh.exec_command('sudo systemctl restart apache2')

# Disconnect from the remote server
ssh.close()

# Delete the local tarball
os.remove('webapp.tar')

print('Deployment complete')
