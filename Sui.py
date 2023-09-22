print("Ungerade  |  Gerade")
print("---------------------")

for num in range(1, 21):
    if num % 2 == 1:
        
        print(f"{num:^9} |", end=" ")
    else:
        # Gerade Zahl
        print(f"{num:^7} |", end=" ")

    if num % 2 == 0:
        print()

