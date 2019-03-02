import sys

class NewCalender:
    def __init__(self, calenderInfo):
        daysInYear, daysInMonth, daysInWeek = list(map(int, calenderInfo))
        self.daysInYear = daysInYear
        self.daysInMonth = daysInMonth
        self.daysInWeek = daysInWeek
        self.monthsInYear = self.daysInYear / self.daysInMonth
        self.daysOfTheWeek = [chr(i) for i in range(ord('A'), ord('A')+self.daysInWeek)]
        self.extraYears = []
  
    def isValidYear(self):
        return self.monthsInYear < 100
  
    def isVaildMonth(self):
        return self.daysInMonth < 100
  
    def makeExtraYears(self, year=2000):
        extraDay = self.daysInYear % self.daysInMonth
        totalDay = 0
        for i in range(year):
            totalDay += extraDay
            if self.daysInMonth <= totalDay:
                self.extraYears.append(i + 1)
                totalDay = totalDay - self.daysInMonth

    def dateIsIncluded(self, year, month, day):
        if self.daysInMonth < day:
            return False
        # 閏月のパターン
        elif month == self.monthsInYear + 1:
            return year in self.extraYears
        else:
            return True

    def getDayOfTheWeek(self, date):
        year, month, day = list(map(int, date.split('-')))
        self.makeExtraYears(year)
        if self.isVaildMonth() and self.isValidYear() and self.dateIsIncluded(year, month, day):
            a = (year - 1) * self.daysInYear
            b = ((month - 1) + len(self.extraYears) ) * self.daysInMonth
            passedDay = a + b + day
            return self.daysOfTheWeek[passedDay % len(self.daysOfTheWeek) - 1]
        else:
            return -1


def main(argv):

  newCalender = NewCalender(argv[:-1])
  print(newCalender.getDayOfTheWeek(argv[3]))

if __name__ == '__main__':
    main(sys.argv[1:])