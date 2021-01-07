string = input("Enter a string: ")
a_counter = 0
e_counter = 0
i_counter = 0
o_counter = 0
u_counter = 0
total = 0

for letter in string:
    if letter == "a":
        a_counter += 1
    elif letter == "e":
        e_counter += 1
    elif letter == "i":
        i_counter += 1
    elif letter == "o":
        o_counter += 1
    elif letter == "u":
        u_counter += 1

total = a_counter + e_counter + i_counter + o_counter + u_counter

print("Total number of vowels is " + str(total))
print("Total number of 'a' is " + str(a_counter))
print("Total number of 'e' is " + str(e_counter))
print("Total number of 'i' is " + str(i_counter))
print("Total number of 'o' is " + str(o_counter))
print("Total number of 'u' is " + str(u_counter))