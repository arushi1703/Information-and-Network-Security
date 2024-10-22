def virus(filename):
    try:
        with open(filename, 'r') as file: data = file.read()
        newdata = '*' * len(data)
        with open(filename, 'w') as file: file.write(newdata)
        print("Virus executed")
    except : print('Error')

filename = input("Enter filename: ")
virus(filename)
        