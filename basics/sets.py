numbers = {10, 20, 30, 20, 40, 10}
print("Set:", numbers)  # Set: {10, 20, 30, 40} #duplicate values cannot be stored in set
numbers.add(50)
print("After adding 50:", numbers)  # After adding 50: {10, 20, 30, 40, 50}
numbers.discard(20)
print("After removing 20:", numbers)  # After removing 20: {10, 30, 40, 50} #you can also use "numbers.remove(20)"
