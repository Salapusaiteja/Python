num = [10,20,30,40,50]
print("Original list:", num) #[10,20,30,40,50]
print("First element:",num[0]) #10
num.append(60)
print(num) #[10,20,30,40,50,60]
num.remove(20)
print(num) #[10,30,40,50,60]
print(type(num)) #<class 'list'>
