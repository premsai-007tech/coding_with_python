# taking user input of string and conversion to list using method
input_string=input("Enter a list of programming languages,separated by a comma.Hit enter when you finished:\n")
my_list=input_string.replace(" "," ").split(",")
print(my_list)
