print("BINARY TO DECIMAL CONVERSION\n");
binary_input = input("Enter a binary no. = ")
bin_lst = []

for i in binary_input:
    if int(i) not in (0,1):
        print("Error. Given Input is not Binary\n.")
        exit()
    else:
       bin_lst.append(int(i))

bin_lst.reverse()
dec = 0

for i in range(len(bin_lst)):
    if bin_lst[i] == 1:
        dec += 2**i

print("Decimal Representation = ",dec)
