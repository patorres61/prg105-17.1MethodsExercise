# Phyllis Torres
# 17.1 Rewrite a Function Assignment
# Due 11/17/2016

print('17.1 Rewrite a Function \n')
print('Phyllis Torres\n\n')

print('This program will use a method that takes a time and converts it to seconds. ')


# create a time class
class Time:
    """Represents the time of day
    attributes: hour, minute, second
    """

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def __init__(self):
        self.minute = None
        self.second = None
        self.hour = None

# instantiate a time object and set the values for hour, minute, and second
time = Time()
time.hour = 9
time.minute = 45
time.second = 15

print ('\nThe time that will be converted to seconds is ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

# call method to convert time to seconds
int_seconds = time.time_to_int()

print ('\nThe number of seconds in object time is: ' + str(int_seconds))
