import sys


class NewCalender:
    def __init__(self, daysInYear, daysInMonth, daysInWeek):
        self.daysInYear = int(daysInYear)
        self.daysInMonth = int(daysInMonth)
        self.daysInWeek = int(daysInWeek)
        self.monthsInYear = int(self.daysInYear / self.daysInMonth)
        self.daysOfTheWeek = [chr(i) for i in range(ord('A'), ord('A')+self.daysInWeek)]
        self.extraYears = []
  

    # 月が 100 を超えるかどうか (1 ~ 99)
    def isValidYear(self):
        return self.monthsInYear < 100


    # 日が 100 をこえるかどうか (1 ~ 99)
    def isVaildMonth(self):
        return self.daysInMonth < 100


    # 上記をまとめて呼び出す.
    def isValidCalender(self):
        return self.isValidYear() and self.isVaildMonth()
    

    # 入力された year を含む, それまでに経過した閏年を extraYears に格納
    def makeExtraYears(self, year):
        extraDay = self.daysInYear % self.daysInMonth
        totalDay = 0

        for i in range(year):
            totalDay += extraDay
            if self.daysInMonth <= totalDay:
                self.extraYears.append(i + 1)
                totalDay = totalDay - self.daysInMonth
    

    # 閏月の判定
    def isValidExtraMonth(self, year, month):
        return (month == self.monthsInYear + 1) and (self.monthsInYear < 99) and (year in self.extraYears)
        

    # 入力された日付 year-month-day がカレンダーに含まれるかを判定
    def dateIsIncluded(self, date):
        year, month, day = list(map(int, date.split('-')))
        self.makeExtraYears(year)

        # 1. day がカレンダーを超える値ならアウト
        if self.daysInMonth < day:
            return False
        # 2. month が基本のカレンダーを超える場合, 閏月が成立する状態であれば ok 
        elif  self.monthsInYear < month:
            return self.isValidExtraMonth(year, month)
        # 3. month, day 共に問題なければ ok
        else:
            return True


    # 上記の関数を用いて, 正しい日付の曜日を返す.
    def getDayOfTheWeek(self, date):
        year, month, day = list(map(int, date.split('-')))
        
        if self.isValidCalender() and self.dateIsIncluded(date):
            passedDaysY = (year - 1) * self.daysInMonth * self.monthsInYear
            passedMonths = len(self.extraYears) - 1 if year in self.extraYears else len(self.extraYears)
            passedDaysM = ((month - 1) + passedMonths) * self.daysInMonth
            # print(f"year: {year - 1}  month: {((month - 1) + passedDaysM)}  day: {day}")
            totalPassedDays = passedDaysY + passedDaysM + day
            return self.daysOfTheWeek[totalPassedDays % len(self.daysOfTheWeek) - 1]
        else:
            return -1


def main(argv):
  newCalender = NewCalender(argv[0], argv[1], argv[2])
  print(newCalender.getDayOfTheWeek(argv[3]))


if __name__ == '__main__':
    main(sys.argv[1:])
