# https://adventofcode.com/2023/day/2
# need game id
# need to splikt string into games and then into colours

COUNTS = {"red": 12, "green": 13, "blue": 14}
valid_games = []

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


def is_valid(games):
    for i in games:
        if games[i] > COUNTS[i]:
            return False
    return True

for l in open('input.txt'):
    game_no = int(l.split(' ', 1)[1].split(':')[0])
    game_counts = get_counts(l)
    if is_valid(game_counts):
        valid_games.append(game_no)

print(sum(valid_games))
