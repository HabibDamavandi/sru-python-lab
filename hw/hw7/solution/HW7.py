import datetime

class JalaliCalendar:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__monthArray = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
                             "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
        self.__weekArray = ["شنبه","يکشنبه","دوشنبه","سه شنبه","چهارشنبه","پنج شنبه","جمعه"]

    def setDay(self, day):
        self.__day = day

    def getDay(self):
        return self.__day

    def setMonth(self, month):
        self.__month = month

    def getMonth(self):
        return self.__month

    def setYear(self, year):
        self.__year = year

    def getYear(self):
        return self.__year

    def getDate(self):
        return "%d/%d/%d"%(self.__year,self.__month,self.__day)

    def getMonthName(self):
        return self.__monthArray[int(self.__month) - 1]

    def getWeekDay(self):
        y,m,d = self.getJulianDate()
        wd = datetime.date(y, m, d).weekday()
        return self.__weekArray[(wd+2)%7]

    def getJulianDate(self):
        jy = self.__year
        jm = self.__month
        jd = self.__day
        if(jy>979):
            gy=1600
            jy-=979
        else:
            gy=621
        if(jm<7):
            days=(jm-1)*31
        else:
            days=((jm-7)*30)+186
        days+=(365*jy) + ((int(jy/33))*8) + (int(((jy%33)+3)/4)) + 78 + jd
        gy+=400*(int(days/146097))
        days%=146097
        if(days > 36524):
            gy+=100*(int(--days/36524))
            days%=36524
            if(days >= 365):
                days+=1
        gy+=4*(int(days/1461))
        days%=1461
        if(days > 365):
            gy+=int((days-1)/365)
            days=(days-1)%365
        gd=days+1
        if((gy%4==0 and gy%100!=0) or (gy%400==0)):
            kab=29
        else:
            kab=28
        sal_a=[0,31,kab,31,30,31,30,31,31,30,31,30,31]
        gm=0
        while(gm<13):
            v=sal_a[gm]
            if(gd <= v):
                break
            gd-=v
            gm+=1
        return gy,gm,gd

jalali = JalaliCalendar(28, 8, 1397)
print(jalali.getDay())
print(jalali.getMonth())
print(jalali.getYear())
print(jalali.getDate())
print(jalali.getMonthName())
print(jalali.getWeekDay())
print("%d/%d/%d"%jalali.getJulianDate())

jalali.setDay(1)
jalali.setMonth(1)
jalali.setYear(1400)
print(jalali.getDay())
print(jalali.getMonth())
print(jalali.getYear())
print(jalali.getDate())
print(jalali.getMonthName())
print(jalali.getWeekDay())
print("%d/%d/%d"%jalali.getJulianDate())
