# https://adventofcode.com/2023/day/3

def get_number(segment, num) -> int:
    if segment[0].isdigit():
        num = num + segment[0]
        return get_number(segment[1:], num)
    else:
        return str(num)


def is_valid(line_index, column_index, len_number):
    for i in range(len_number + 2):
        if column_index + i - 1 > 0 and column_index + i < len(lines[line_index]) - 1:
            if line_index != 0 and lines[line_index - 1][column_index + i - 1] != '.' and not(lines[line_index - 1][column_index + i - 1].isdigit()):
                return True
            if lines[line_index][column_index + i - 1] != '.' and not(lines[line_index][column_index + i - 1].isdigit()):
                return True
            if line_index < len(lines) - 1 and lines[line_index + 1][column_index + i - 1] != '.' and not(lines[line_index + 1][column_index + i - 1].isdigit()):
                return True
    
part_numbers = []
lines = []    
line_index = 0           
for l in open('input.txt'):
    lines.append(l)

for l in lines:
    bias = 0
    for c in range(len(l)):
        if bias > 0:
            bias -= 1
            continue
        if l[c + bias].isdigit():
            number = get_number(l[c:], '')
            if is_valid(line_index, c, len(number)):
                print('valid number ' + number)
                part_numbers.append(int(number))
            bias += len(number)
    line_index += 1

print(sum(part_numbers))
            
