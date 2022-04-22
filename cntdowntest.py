import time
 
our_list = list(range(10000000))
element = 7000000
 
start = time.time()
 
for el in our_list:
    if el == element:
        break
 
end = time.time()
 
print(end - start)
