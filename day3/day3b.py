# https://adventofcode.com/2023/day/3

def get_number(segment, num) -> int:
    if segment[0].isdigit():
        num = num + segment[0]
        return get_number(segment[1:], num)
    else:
        return str(num)


def get_gear_ratios(line_index, column_index, len_number):
    for i in range(len_number + 2):
        if column_index + i - 1 > 0 and column_index + i < len(lines[line_index]) - 1:
            if line_index != 0 and lines[line_index - 1][column_index + i - 1] == '*':
                return str(line_index - 1) + '_' + str(column_index + i - 1)
            if lines[line_index][column_index + i - 1] == '*':
                return str(line_index) + '_' + str(column_index + i - 1)
            if line_index < len(lines) - 1 and lines[line_index + 1][column_index + i - 1] == '*':
                return str(line_index + 1) + '_' + str(column_index + i - 1)
    return None
    

gear_ratios = {}
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
            gr = get_gear_ratios(line_index, c, len(number))
            if gr is not None:
                if gr in gear_ratios:
                    gear_ratios[gr].append(int(number))
                else:
                    gear_ratios[gr] = [int(number)]
            bias += len(number)
    line_index += 1

sum_ratios = 0
for gr in gear_ratios:
    if len(gear_ratios[gr]) == 2:
        sum_ratios += gear_ratios[gr][0] * gear_ratios[gr][1]

print(sum_ratios)
            
