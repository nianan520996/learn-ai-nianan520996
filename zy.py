apple_heights=[100,200,150,140,129,134,167,198,200,111,110]
tao=109
max_reach=tao+30
count=0
for apple_height in apple_heights:
    if apple_height<=max_reach:
        count+=1
print(count)
