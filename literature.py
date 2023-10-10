#number of pages
nop = int(input())
#pages per hour
pph = int(input())
#days for reading
dfr =  int(input())

total_hours = nop / pph
daily_hours = total_hours / dfr

print({total_hours}, {daily_hours})
