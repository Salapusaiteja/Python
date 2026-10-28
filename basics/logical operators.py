# Logical AND: both conditions must be True
age = 23
has_id = True
print(age >= 18 and has_id == True)  # True
print(age < 18 and has_id == True)   # False
# Logical OR: at least one condition must be True
print(age >= 18 or has_id == False)  # True
print(age < 18 or has_id == False)   # False
# Logical NOT: reverses the Boolean result
is_learning = True
print(not is_learning)  # False
print(not False)        # True
