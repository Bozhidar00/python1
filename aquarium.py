length = int(input())
width = int(input())
heigth = int(input())
percent = int(input())

size_cubic_cm = length * width * heigth
size_liters = size_cubic_cm * 0.001
space_taken = percent / 100
liters_needed = size_liters * (1 - space_taken)

print(liters_needed)