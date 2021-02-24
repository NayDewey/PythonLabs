'''
1 - Write and execute a script that prints "hello world" to the console.

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
	- Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses?
        * How helpful are the error messages?
	- Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
	- Use the interpreter to perform simple math.
	- Calculate how many seconds are in a year.

'''

#print("Hello World")

#seconds to minute, minute to hour, hour to day, day to year variables and then calculate
SecondstoMinute = 60
MinutetoHour = 60
HourtoDay = 24
DaytoYear = 365

A = SecondstoMinute * MinutetoHour
B = MinutetoHour * HourtoDay
C = HourtoDay * DaytoYear

SecondsinaYear = A * B * C
print(SecondsinaYear)