months = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"
}

while(True):
    date = input("Date: ")
    try:
        m, d, y = date.split()
        if d.endswith(","):
            d = d.removesuffix(",")
        else:
            raise Exception()
        m = months[m]
    except:
        try:
            m, d, y = date.split("/")
        except:
            pass

    try:
        if 1 <= int(d) <= 31 and 1 <= int(m) <= 12 and int(y) > 0:
            print(f"{int(y):04d}-{int(m):02d}-{int(d):02d}")
            break
    except:
        pass
