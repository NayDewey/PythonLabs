'''

Move the code you previously wrote to calculate how many seconds are in a year into this file.
Then execute it as a script to see the output printed to your console.

'''
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