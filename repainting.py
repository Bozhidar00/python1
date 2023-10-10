nylon = 1.50 # for sq.meter
paint = 14.50 # per liter
paint_separator = 5.00 # per liter

quantity_nylon = int(input())
quantity_paint = int(input())
quantity_ps = int(input())
work_hours = int(input())

total_nylon = quantity_nylon * nylon
total_paint = quantity_paint * paint
total_ps = quantity_ps * paint_separator

total_nylon2 = total_nylon + 2 * 1.50
total_paint2 = total_paint + total_paint * 10/100

total_cost = (total_nylon2 + total_paint2 + total_ps)
work_pay = total_cost * 30/100
print(total_cost + work_pay)