import subprocess

du = subprocess.run(['du', '-hs', '.'])
print('returncode: ', du.returncode)
