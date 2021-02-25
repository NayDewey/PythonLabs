'''

Write a script that takes in a number in days from the user between 1 and 1,000,000,000 and convert it to seconds.

NOTE: We will use the input() funtion to collect users input. An example is demonstrated below.

'''

# the input of the user will be saved in the variable days.
# because the input() function collects the input as a string, we have to convert it to an int
# The string passed to the input() function is what the user is prompted with
days = int(input("Please enter a number in days between 1 and 1,000,000,000: "))
#We need seconds in a minute then hour and then day and to then apply the seconds in a day multipied by the input value
seconds_in_minute = 60
seconds_in_hour = seconds_in_minute * 60
seconds_in_day = seconds_in_hour * 12

the_answer = (days * seconds_in_day)

print(the_answer)