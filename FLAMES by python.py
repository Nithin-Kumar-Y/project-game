print("-" * 40)
print("Welcome to FLAMES")

# after cancelleing common letters
a1 = input("Enter 1st name: ").upper().strip()
b1 = input("Enter 2nd name: ").upper().strip()

a2 = len(a1)
b2 = len(b1)

a_list = []
b_list = []
for i in a1:
    a_list.append(i)

for i in b1:
    b_list.append(i) 


#Finding the length of string/ name after cancellation.

for i in a_list:
    for j in b_list:
        if i == j:
            a_list.remove(i)
            b_list.remove(j)
        else:
            pass

for ch in a_list[:]:
    for ch1 in b_list[:]:
        if ch == ch1:
            a_list.remove(ch)
            b_list.remove(ch1)

print(a_list)
print(b_list)

a = len(a_list)
b = len(b_list)


#Getting input gender to say if S is got sister/ brother
gender = input("enter your gender (male/ female): ").upper().strip()
# Initiating a Flames array
array  = ["F", "L", "A", "M", "E", "S"]
rom = len(array)
# adding the both the uncommon letters
op = a + b
print(op)
sum = 0

print(array)
# starting the cancellation in it.
for i in range(1, rom):
    choose = sum + op
    remainder = choose % (rom - i + 1)
    last = array[-1]
    popped = array.pop(remainder - 1)
    if last == popped:
        sum = 0
    else:
        sum = remainder - 1
    print(popped)
    print(array)

array = array[0] 


if array == "F":
    if gender == "MALE":
        print(f"{b1} is Girlfriend to {a1}")
    elif gender == "FEMALE":
        print(f"{a1} is Boyfriend to {b1}")
elif array == "L":
    print(f"{a1} and {b1} is in Love")
elif array == "A":
    print(f"{a1} and {b1}: Arrange Marriage")
elif array == "M":
    print(f"{a1} and {a2} : Marriage")
elif array == "E":
    print(f"{a1} and {b1} are Enemies")
elif array == "S":
    if gender == "MALE":
        print(f"{b1} is Sister to {a1}")
    elif gender == "FEMALE":
        print(f"{a1} is Brother to {b1}")
    else:
        print(f"{a1} and {b1} are Brother / Sister")
else:
    print("Pass")

print("-" * 40)