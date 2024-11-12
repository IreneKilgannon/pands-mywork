from timesheetentry import *

class Employee:
    timesheets = []

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return self.first + ' ' + self.last
    
    def logminutes(self, project, minutes):
        '''A function that will create a timesheetentry with the project, minutes and the current time'''
        now = dt.datetime.now
        timesheetentry = Timesheetentry(project, now, minutes)
        self.timesheets.append(timesheetentry)


    def gettotaltime(self):
        '''Function that will return the total minutes of all the timesheetentrys'''
        total_minutes = 0
        for ts in self.timesheets:
            total_minutes += ts.duration
        return total_minutes

if __name__ == '__main__':
    test = Employee('Irene', 'Kilgannon')
    print(test)
    assert('Irene Kilgannon' == str(test))
    test.logminutes('pl', 30)
    test.logminutes('pl' , 60)
    mins = test.gettotaltime()
    print(mins)
    assert(mins == 90)
    print('All good')

