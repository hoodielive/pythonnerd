import subprocess

completed = subprocess.run(['ls', '-l'])
print('returncode: ', completed.returncode)
