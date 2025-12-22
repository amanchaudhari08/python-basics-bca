# Printing even numbers from 1 to 20 using a loop.
# Option-1
print("option 1:")
for i in range (2,21,2):
    print(i)

# Option-2
print("Option 2:")
for i in range (1,21):
    if i % 2 == 0:
        print(i)
