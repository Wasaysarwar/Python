num = int(input("Enter any number to save its table: "))

with open("table.txt","w") as file:

    file.write(f"\nTable of {num}:\n")
    
    for i in range(1,11):
        file.write(f"{num} * {i} = {num*i}\n")