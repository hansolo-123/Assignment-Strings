# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = f'{scorer_0} {goal_0}, {scorer_1} {goal_1}'

report = f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute'

player = "Marco van Basten"

first_name = player[:player.find(' ')]

last_name = player[player.find(' '):]

last_name = last_name.lstrip()

last_name_len = len(last_name)

first_name_len = len(first_name)

name_short = f'{first_name[0]}. {last_name}'

chant = f'{first_name}! ' * (first_name_len)

chant = chant.rstrip()

good_chant = chant[-1] != ' '

print(chant)

print(good_chant)

