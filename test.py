import datetime as dt

now_date = dt.datetime.now()
date = now_date.strftime("%d-%B(%m)-%Y")
# print(date)
exmpale = [
    {
        "data":"salman",
        "age":15
    },
    {
        "data":"ainnin",
        "age":15
    },
]

for i in range(len(exmpale)):
    print(exmpale[i]['data'])
    print(exmpale[i]['age'])