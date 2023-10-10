deposit_amount = int(input())
deposit_time = int(input())
yearly_percent = float(input())/100

tax = deposit_amount * yearly_percent
#monthly tax
mt = tax / 12
total = deposit_amount * deposit_time * mt

print({tax}, {mt}, {total})

