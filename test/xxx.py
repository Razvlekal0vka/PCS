print('Write the full address of the uploaded file')
address_of_the_uploaded_file = str(input())

name_file = list(address_of_the_uploaded_file.split('/'))[-1]

print(name_file)