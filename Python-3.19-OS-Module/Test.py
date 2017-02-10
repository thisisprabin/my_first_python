import os
import time

print(os.getcwd())
time.sleep(2)
os.mkdir('newDir')
time.sleep(2)
os.rename('newDir','newDir2')
time.sleep(2)
os.rmdir('newDir2')
