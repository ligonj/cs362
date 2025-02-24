def is_leap_year(num):
    if num % 100 == 0:
        if num % 400 == 0 and num % 4 == 0:
            return True
    else:
        if num % 4 == 0:
            return True
    return False


def yearfunc(num_sec, year):
    seconds_in_ly = 31622400
    seconds_in_y = 31536000
    while num_sec >= seconds_in_y:
        if is_leap_year(year) is False:
            num_sec -= seconds_in_y
            year += 1
        else:
            if num_sec >= seconds_in_ly:
                num_sec -= seconds_in_ly
                year += 1
            else:
                return (num_sec, year)
    return (num_sec, year)


def monthfunc(num_sec, year, month):
    seconds_in_m28 = 2419200
    seconds_in_m29 = 2505600
    seconds_in_m30 = 2592000
    seconds_in_m31 = 2678400
    months_with_30 = [9, 4, 6, 11]
    months_with_31 = [1, 3, 5, 7, 8, 10, 12]
    while num_sec >= seconds_in_m28:
        if month == 2:
            if is_leap_year(year) is False:
                num_sec -= seconds_in_m28
                month += 1
            else:
                if num_sec >= seconds_in_m29:
                    num_sec -= seconds_in_m29
                    month += 1
                else:
                    return (num_sec, month)
        if month in months_with_30:
            if num_sec >= seconds_in_m30:
                num_sec -= seconds_in_m30
                month += 1
            else:
                return (num_sec, month)
        if month in months_with_31:
            if num_sec >= seconds_in_m31:
                num_sec -= seconds_in_m31
                month += 1
            else:
                return (num_sec, month)
    return (num_sec, month)


def dayfunc(num_sec, day):
    seconds_in_day = 86400
    while num_sec >= seconds_in_day:
        num_sec -= 86400
        day += 1
    return (num_sec, day)


def my_datetime(num_sec):
    year = 1970
    month = 1
    day = 1
    year_results = yearfunc(num_sec, year)
    num_sec = year_results[0]
    year = year_results[1]
    month_results = monthfunc(num_sec, year, month)
    num_sec = month_results[0]
    month = month_results[1]
    day_results = dayfunc(num_sec, day)
    num_sec = day_results[0]
    day = day_results[1]
    date_string = str(month) + "-" + str(day) + "-" + str(year)
    return date_string
