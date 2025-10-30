
reserved_teams = {
    "Scuderia Ferrari": "HP",
    "Mercedes-AMG Petronas Formula One Team": "Petronas",
    "Red Bull Racing": "Oracle",
    "RB Formula 1 Team": "Visa Cash App",
    "Stake F1 Team Kick Sauber": "Stake",
    "McLaren": "MasterCard",
    "BWT Alpine F1 Team": "BWT",
    "MoneyGram Haas F1 Team": "MoneyGram",
    "Aston Martin Aramco Formula 1 Team": "Aramco",
    "Williams Racing": "Duracell"
}

reserved_numbers = {
    1: "Max Verstappen",
    7: "Jack Doohan",
    10: "Pierre Gasly",
    14: "Fernando Alonso",
    18: "Lance Stroll",
    16: "Charles Leclerc",
    44: "Lewis Hamilton",
    31: "Esteban Ocon",
    87: "Oliver Bearman",
    5: "Gabriel Bortoleto",
    27: "Nico Hulkenberg",
    4: "Lando Norris",
    81: "Oscar Piastri",
    12: "Andrea Kimi Antonelli",
    63: "George Russell",
    6: "Isack Hadjar",
    22: "Yuki Tsunoda",
    30: "Liam Lawson",
    23: "Alex Albon",
    55: "Carlos Sainz",
    17: "Retired (Jules Bianchi)"
}


class F1Team:
    def __init__(self, team_name, sponsor, driver1, num1, driver2, num2):
        self.__TeamName = team_name
        self.__Sponsor = sponsor
        self.__Driver1 = driver1
        self.__Number1 = num1
        self.__Driver2 = driver2
        self.__Number2 = num2

    def __str__(self):
        return (f"\n {self.__TeamName} ({self.__Sponsor})\n"
                f"  Driver 1: {self.__Driver1} #{self.__Number1}\n"
                f"  Driver 2: {self.__Driver2} #{self.__Number2}")


def is_team_valid(name, sponsor):
    # Check team
    if name in reserved_teams:
        print(f" Team '{name}' already exists in F1!")
        return False
    # Check sponsor
    if sponsor in reserved_teams.values():
        print(f" Sponsor '{sponsor}' is already taken!")
        return False
    return True

def is_number_valid(num):
    if num in reserved_numbers:
        print(f" Number {num} is already taken by {reserved_numbers[num]}!")
        return False
    return True


print(" Welcome to the F1 Team Creator !!! WOOHOOO")

# Enter team and sponsor
team_name = input("Enter your new team name: ")
sponsor = input("Enter your team sponsor: ")

if not is_team_valid(team_name, sponsor):
    exit()

# Driver 1
driver1 = input("Enter Driver 1 name: ")
num1 = int(input("Enter Driver 1 number: "))
if not is_number_valid(num1):
    exit()

# Driver 2
driver2 = input("Enter Driver 2 name: ")
num2 = int(input("Enter Driver 2 number: "))
if not is_number_valid(num2):
    exit()

# Create new team object
new_team = F1Team(team_name, sponsor, driver1, num1, driver2, num2)

# Print confirmation
print("\nwelcome! :DDDDDD")
print(new_team)