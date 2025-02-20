from datetime import datetime, timedelta

def printDaysMinus5():
    current_date = datetime.now()
    new_date = current_date - timedelta(days=5)

    print("Current Date:", current_date)
    print("Date after subtracting 5 days:", new_date)

def printConsecutive():
    today = datetime.now()

    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    print("Yesterday:", yesterday)
    print("Today:", today)
    print("Tomorrow:", tomorrow)

def dropMicroseconds(time):
    current_datetime = time

    datetime_without_microseconds = current_datetime.replace(microsecond=0)

    print("Original Datetime:", current_datetime)
    print("Datetime without Microseconds:", datetime_without_microseconds)

def calcDifference(date1, date2):
    difference_in_seconds = (date2 - date1).total_seconds()

    print("Difference in seconds:", difference_in_seconds)

printDaysMinus5()
printConsecutive()
dropMicroseconds(datetime.now())
calcDifference(datetime(2023, 10, 1, 12, 0, 0), datetime(2023, 10, 5, 14, 30, 0))
