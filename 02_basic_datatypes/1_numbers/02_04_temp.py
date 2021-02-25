'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

# I do not understand 'read...from the conole' but I am interrupting that as 'user input' (???)
# if that is not the case, that is fine, I just need to know what application or program you want to have the program gather the data from
# barring that, I am just going to convert the degrees so that a user input freezing to boiling gives you a response

request = int(input("Please enter the degree in Fahrenheit you would like to convert: "))
celsius = ((request - 32) * (5 / 9))

print(celsius)
