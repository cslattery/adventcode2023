
ans_arr = []
for l in open('input.txt'):
    for i in l:
        if i.isdigit():
            first = int(i)
            break
    for i in l[::-1]:
        if i.isdigit():
            last = int(i)
            break
    ans_arr.append(int(str(first)+(str(last))))
print(sum(ans_arr))
    

