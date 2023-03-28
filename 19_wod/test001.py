import csv
import io
import sys

input_file_handle = open("inputs/silly-exercises.csv", "r")
input_file_handle = io.StringIO("exercise,reps\nEden Chinups,20-50\nHanging Chads,40-100")
reader = csv.DictReader(input_file_handle)
fieldnames = list(reader.fieldnames)

output_file_handle = open("test001.csv", "w")
writer = csv.DictWriter(output_file_handle, fieldnames=fieldnames, delimiter=':')
writer.writeheader()

for record in reader:
    writer.writerow(record)

output_file_handle.close()
input_file_handle.close()
