#This program will give extension of the file that you input, as the output...
file_name=input("Write a file_name:")
file_ext=file_name.split(".")
print("The extension is:"+ repr (file_ext[-1]))
