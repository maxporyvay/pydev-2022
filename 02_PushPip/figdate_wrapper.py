import tempfile
import venv
import subprocess
import os
import shutil
import sys

curr = os.getcwd()
temp = tempfile.mkdtemp()
venv.create(temp, with_pip=True)
subprocess.run([temp + '/bin/pip', 'install', 'pyfiglet'])
#subprocess.run(['.', 'bin/activate'])
#os.chdir(curr)
l = []
if len(sys.argv) == 2:
    l = [sys.argv[1]]
elif len(sys.argv) == 3:
    l = [sys.argv[1], sys.argv[2]]
l2 = [temp + '/bin/python3', '-m', 'figdate']
l2.extend(l)
os.chdir(curr)
subprocess.run(l2)
shutil.rmtree(temp)

