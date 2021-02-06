number_string = input("введите количество билетов - ")
number = int(number_string)
list_ticket = []
s = 0
skidka10 = float (10 / 100)
for n in range (0, number):
    list_ticket.append(input("введите возраст посетителя - "))
for ticket in list_ticket:
    age_str = ticket
    age = int (age_str)
    if age < 18 :
        cost = 0
    else:
        if age >=18 and age < 25:
            cost = 990
        else:
            if age > 25:
                cost = 1390
    s = s+cost
if number > 3:
    discount = skidka10 * s
else:
    discount = 0
count = s - discount
print("сумма билетов = ", count)

