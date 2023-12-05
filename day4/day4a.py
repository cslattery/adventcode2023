# https://adventofcode.com/2023/day/4


winners = {}
index = 0
for l in open('input.txt'):
    wins, numbers = l.split(':')[1].split('|')[0].strip().split(), l.split(':')[1].split('|')[1].strip().split()
    for i in numbers:
        if i in wins:
            if index in winners:
                winners[index].append(i)
            else:
                winners[index] = [i]
    index += 1

score = 0 
for w in winners:
    score += 2**(len(winners[w]) - 1)

print(score)