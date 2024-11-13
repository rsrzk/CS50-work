while(True):
    fraction = input("Fraction: ")
    num, _, denom = fraction.partition("/")
    try:
        if int(num) <= int(denom):
            percent = int(num)/int(denom)
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

percent = round(percent*100)
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(str(percent)+"%")
