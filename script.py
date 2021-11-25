import main
import os
import subprocess
import sys


for i in range(99):
    exec(open('.\main.py').read())

with open("data"+str(sys.argv[1])+".txt") as f:
    lines = f.readlines()

contGana = lines.count('True\n')
contPierde = lines.count('False\n')

#print(lines)

print("Gana: ", contGana)
print("Pierde: ", contPierde)
total = contGana + contPierde
promedio = contGana/total
print("Promedio: ", promedio)