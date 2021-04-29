spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]
month_coeff = []
count = 0
for i in spendings:
    try:
        month_coeff.append(i / income[count])
    except ZeroDivisionError:
        month_coeff.append(0)
    count += 1
year_coeff = sum(month_coeff) / 12
print(month_coeff)
print(year_coeff)
