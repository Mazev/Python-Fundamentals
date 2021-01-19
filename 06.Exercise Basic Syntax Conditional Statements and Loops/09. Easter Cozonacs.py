budget = float(input())
flour = float(input())

cozunak_count = 0
eggs_count = 0

praice_eggs = flour * 0.75
praice_milk = (flour * 0.25) + flour
milk_needet = praice_milk *0.25
cozunak_praice = praice_eggs + milk_needet + flour

while budget > cozunak_praice:
    cozunak_count +=1
    eggs_count += 3
    budget -= cozunak_praice
    if cozunak_count % 3 == 0:
        eggs_lost = cozunak_count - 2
        eggs_count -= eggs_lost

print(f'You made {cozunak_count} cozonacs! Now you have {eggs_count} eggs and {budget:.2f}BGN left.')
