"""
Author: Homar Rosendo Cano
Code to convert csv files into configuration files
Using under Homar's authorization
"""

import os, sys, csv

#files = os.listdir(sys.argv[1])

input_path = "D:\Clases\Simulación Gráfica\com139-class-master\GoL\patternGenerator\idk.csv"
output_path = "D:\Clases\Simulación Gráfica\com139-class-master\GoL\patternGenerator"

with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    reader = csv.reader(input_file)
    for y, row in enumerate(reader):
        for x, cell in enumerate(row):
            if cell == '*': output_file.write(f"{x},{y}\n")
    