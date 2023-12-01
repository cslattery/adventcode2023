num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six':6, 'seven': 7, 'eight': 8, 'nine': 9}
num_dict_rev = {'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 'xis':6, 'neves': 7, 'thgie': 8, 'enin': 9}
ans_arr = []

for l in open('day1/input.txt'):
    for i in range(len(l)):
        if l[i].isdigit():
            first = int(l[i])
            break
        if l[i:i+3] in ['one', 'two', 'six']:
            first = num_dict[l[i:i+3]]
            break
        if l[i:i+4] in ['four', 'five', 'nine']:
            first = num_dict[l[i:i+4]]
            break
        if l[i:i+5] in ['three', 'seven', 'eight']:
            first = num_dict[l[i:i+5]]
            break

    for i in range(len(l)):
        r = l[::-1]
        if r[i].isdigit():
            last = int(r[i])
            break
        if r[i:i+3] in ['eno', 'owt', 'xis']:
            print(l[i:i+3])
            last = num_dict_rev[r[i:i+3]]
            break
        if r[i:i+4] in ['ruof', 'evif', 'enin']:
            last = num_dict_rev[r[i:i+4]]
            break
        if r[i:i+5] in ['eerht', 'neves', 'thgie']:
            last = num_dict_rev[r[i:i+5]]
            break

    print(first, last)
    ans_arr.append(int(str(first)+(str(last))))
print(sum(ans_arr))
    

