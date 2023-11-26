num_people = int(input("How many people are playing?: "))
num_teams = int(input("How many teams?: "))

# The // is the floor division operator. Do some research to see how it differs
# from the / division operator.
people_per_team = num_people // num_teams
left_over = num_people % num_teams

print("If there are " + str(num_teams) + " teams, there will be " + \
str(people_per_team) + " on each team, with " + str(left_over) + " left over.")