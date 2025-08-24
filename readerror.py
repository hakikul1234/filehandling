try:

 file1=open('sampl.txt','r')
 file_reading=file1.read()
 print('Reading file content:')
 print(file_reading)
 file1.close()

except FileNotFoundError :
    print("File does not exist.")
