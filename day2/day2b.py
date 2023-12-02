#https://adventofcode.com/2023/day/2#part2

power_of_cubes = []

def get_counts(line):
    sets = l.split(':')[1].split(';')
    colours = {"red": 0, "green": 0, "blue": 0}
    for i in sets:
        game_colors = i.rstrip().split(',')
        for j in game_colors:
            colour = j.lstrip().rstrip().split(' ')[1]
            count = int(j.lstrip().rstrip().split(' ')[0])
            if count > colours[colour]:
                colours[colour] = count
    return colours

for l in open('input.txt'):
    game_no = int(l.split(' ', 1)[1].split(':')[0])
    game_counts = get_counts(l)
    power_of_cubes.append(game_counts["red"] * game_counts["green"] * game_counts["blue"])

print(sum(power_of_cubes))