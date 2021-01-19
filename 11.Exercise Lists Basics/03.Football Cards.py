cards = input().split(' ')

team_a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
team_b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
team_a_counter = 11
team_b_counter = 11
is_terminateit = False
for team_cards in cards:
    tokens = team_cards.split('-')
    name_team = tokens[0]
    plear_number = int(tokens[1])
    index = plear_number - 1

    if name_team == 'A':
        if team_a[index] == 0:
            continue
        team_a[index] = 0
        team_a_counter -= 1
    else:
        if team_b[index] == 0:
            continue
        team_b [index] = 0
        team_b_counter -= 1
    if team_a_counter < 7 or team_b_counter < 7:
        is_terminateit = True
        break

print(f"Team A - {team_a_counter}; Team B - {team_b_counter}")

if is_terminateit:
    print('Game was terminated')

