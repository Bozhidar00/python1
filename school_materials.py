pens = 5.80
markers = 7.20
solution = 1.20 #per liter

number_pens = int(input())
number_markers = int(input())
liters_solution = int(input())
percent_off = int(input())/100

total_pens = pens * number_pens
total_markers = markers * number_markers
total_solution = solution * liters_solution

total = (total_pens + total_markers + total_solution) * percent_off
print(total)