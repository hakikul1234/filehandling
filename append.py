data_user=input('Enter text to write to the file:')

file1=open('output.txt','w')
file_writting=file1.write(data_user)
print(file_writting)
print('Data successfully written to output.txt')
file1.close()

user_input=input('Enter additional text to append:')
file1=open('output.txt','a')
file_append=file1.write(user_input)
print(file_append)
print('Data append successfully.')

file1.close()

file1=open('output.txt','r')
file_read=file1.read()
print(file_read)
file1.close()