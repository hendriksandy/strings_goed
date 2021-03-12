# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_that_also_scored = "Marco van Basten"
player_that_scored = "Ruud Gullit"
goal_1 = 32
goal_2 = 54
scorers = (player_that_scored + " " +
           str(goal_1) + " " + "and" + " " + player_that_also_scored + " " + str(goal_2))


report = f"{player_that_scored} scored in the {goal_1}nd minute\n{player_that_also_scored} scored in the {goal_2}th minute"
print(report)

player = "kees kist"
x = player.find(" ")
first_name = player[0:x]

# je zoekt eerst de spatie dus de voornaam begint van 0 tot het nummer vd spatie dus je sliced van 0 to x (van nul tot 4)

print(first_name)

y = len(player)

last_name = player[(x+1): y]

# met de len weet je uit hoeveel cijfers de string is (9) x is 4 maar je wilt slicen na de spatie dus x+1 duss van nr 5 tot 9

print(last_name)

name_short = first_name[0] + ". "+last_name

print(name_short)


chant = (first_name + "!")*x
print(chant)

chant_good = chant != " "

print(chant_good)
