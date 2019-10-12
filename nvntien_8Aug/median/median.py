print("Give me a series of numbers and I will give you their median.")
series = []
while True:
    number = input()
    if number == '':
        break
    else:
        number = int(number)
        series.append(number)

series.sort()

if len(series) == 0:
    print("Error, empty dataset")
elif len(series) % 2 == 1:
    p1 = (len(series) - 1) // 2
    print("The median is", series[p1])
elif len(series) % 2 == 0:
    p1 = (len(series) // 2) - 1
    p2 = len(series) // 2
    print("The median is", (series[p1] + series[p2]) / 2)
