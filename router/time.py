from datetime import datetime


class time():
    def current_time():
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        print(day)
        hour = datetime.now().hour
        minute = datetime.now().minute
        time = str(year)+"-"+str(month)+"-"+str(day) + \
            " "+str(hour)+":"+str(minute)
        return time
