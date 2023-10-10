chicken_menu =10.35
fish_menu = 12.40
vegan_menu = 8.15

q_chicken_menu = int(input())
q_fish_menu = int(input())
q_vegan_menu = int(input())

total_cm = q_chicken_menu * chicken_menu
total_fm = q_fish_menu * fish_menu
total_vm = q_vegan_menu * vegan_menu

total_menu = total_vm + total_fm + total_cm
desert = (total_vm + total_fm + total_cm) * 20/100
delivery = 2.50

print(total_menu + desert + delivery)