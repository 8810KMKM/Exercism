import sys

class NewCalender:
  def __init__(self, daysInYear, daysInMonth, daysInWeek):
    self.daysInYear = int(daysInYear)
    self.daysInMonth = int(daysInMonth)
    self.daysInWeek = int(daysInWeek)
    self.monthsInYear = self.daysInYear / self.daysInMonth
    self.daysOfTheWeek = [chr(i) for i in range(ord('A'), ord('A')+self.daysInWeek)]
    self.extraYears = []
  
  def isValidYear(self):
    return self.monthsInYear < 100
  
  def isVaildMonth(self):
    return self.daysInMonth < 100
  
  def makeExtraYears(self):
    extraDay = self.daysInYear % self.daysInMonth
    totalDay = 0
    for i in range(2000):
      totalDay += extraDay
      if self.daysInMonth <= totalDay:
        self.extraYears.append(i + 1)
        totalDay = totalDay - self.daysInMonth

  def dateIsIncluded(self, date):
    year, month, day = list(map(int, date.split('-')))
    if self.daysInMonth < day:
      return False
    # 閏月のパターン
    elif month == self.MonthsInYear + 1:
      if month in self.extraYears:
        return True
      else:
        return False
    else:
      return True

  def numberOfPassedExtraDay(self, year):
    for i in range(len(self.extraYears)):
      if year < self.extraYears[i]:
        return i
    return 0

  def getDayOfTheWeek(self, date):
    year, month, day = list(map(int, date.split('-')))
    if self.isVaildMonth() and self.isValidYear() and self.dateIsIncluded(date):
      a = (year - 1) * self.daysInYear
      # print(self.numberOfPassedExtraDay(year))
      b = ((month - 1) + self.numberOfPassedExtraDay(year)) * self.daysInMonth
      # print(f"a: {a}  b: {b}")
      passedDay = a + b + day
      return self.daysOfTheWeek[passedDay % len(self.daysOfTheWeek) - 1]
    else:
      return -1


def main(argv):

  newCalender = NewCalender(argv[0], argv[1], argv[2])
  print(newCalender.getDayOfTheWeek(argv[3]))

if __name__ == '__main__':
    main(sys.argv[1:])