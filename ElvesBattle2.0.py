import random
import time

# Function to simulate typewriter-style output
def typewriter(text, delay=0.025):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Elf class to represent player and enemy
class Elf:
    def __init__(self, name, health_range, attack_range, luck_range):
        self.name = name
        self.max_health = random.uniform(*health_range)
        self.health = self.max_health
        self.attack_power = random.uniform(*attack_range)
        self.luck = random.uniform(*luck_range)
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100  # XP required for the first level up

    def attack(self, enemy, drain=False, special=False):
        if random.random() < enemy.luck:
            typewriter(f"{enemy.name} avoided the attack!")
            return

        if special:
            damage = self.attack_power * 1.5
            self.health -= damage * 0.2  # Special attack costs 20% of damage dealt as health
            typewriter(f"Special attack! {self.name} took some damage as a cost!")
        elif drain:
            damage = self.attack_power * (1 if random.random() < self.luck else 0.7)
            self.health = min(self.max_health, self.health + damage * 0.3)
            typewriter(f"{self.name} drained {enemy.name}, recovering health!")
        else:
            damage = self.attack_power

        enemy.health -= damage
        typewriter(f"{self.name} dealt {damage:.2f} damage to {enemy.name}!")

    def defend(self):
        typewriter(f"{self.name} braces for the next attack!")
        return 0.5  # Reduces next attack's damage by 50%

    def gain_xp(self, amount):
        self.xp += amount
        typewriter(f"{self.name} gained {amount} XP!")

        # Check for level up
        if self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_next_level  # Deduct the XP used for leveling up
        self.xp_to_next_level = 100 * self.level  # XP for the next level increases

        # Increase stats upon leveling up
        health_increase = random.uniform(10, 20)
        attack_increase = random.uniform(3, 6)
        self.max_health += health_increase
        self.attack_power += attack_increase
        self.health = self.max_health  # Restore health fully on level up

        typewriter(f"Level up! {self.name} is now level {self.level}!")
        typewriter(f"Health increased by {health_increase:.2f} to {self.max_health:.2f}")
        typewriter(f"Attack increased by {attack_increase:.2f} to {self.attack_power:.2f}")

# Function to generate a random enemy with difficulty scaling
def generate_enemy(enemy_names, player_level, health_boost=0, attack_boost=0, luck_boost=0):
    enemy_name = random.choice(enemy_names)
    health_multiplier = 1 + (player_level - 1) * 0.2  # Enemies scale 20% health per player level
    attack_multiplier = 1 + (player_level - 1) * 0.1  # Enemies scale 10% attack per player level
    enemy = Elf(
        name=enemy_name,
        health_range=(50 * health_multiplier + health_boost, 100 * health_multiplier + health_boost),
        attack_range=(10 * attack_multiplier + attack_boost, 20 * attack_multiplier + attack_boost),
        luck_range=(0.05 + luck_boost, 0.25 + luck_boost)
    )
    return enemy

# Item class for health potions or damage boosters
class Item:
    def __init__(self, name, effect_type, effect_value):
        self.name = name
        self.effect_type = effect_type  # 'heal' or 'boost'
        self.effect_value = effect_value

    def use(self, user):
        if self.effect_type == 'heal':
            user.health = min(user.max_health, user.health + self.effect_value)
            typewriter(f"{user.name} used a {self.name} and healed {self.effect_value} health!")
        elif self.effect_type == 'boost':
            user.attack_power += self.effect_value
            typewriter(f"{user.name}'s attack power increased by {self.effect_value}!")

# Main game function
def main():
    typewriter("Welcome to **ELVES BATTLIN**!\n")

    # Difficulty setting
    typewriter("Choose your difficulty level:")
    typewriter("1. Easy\n2. Medium\n3. Hard")
    difficulty_choice = input("Enter (1/2/3): ")

    if difficulty_choice == '1':
        health_boost, attack_boost, luck_boost = 0, 0, 0
    elif difficulty_choice == '2':
        health_boost, attack_boost, luck_boost = 20, 5, 0.05
    else:
        health_boost, attack_boost, luck_boost = 50, 10, 0.1

    # Get player name
    player_name = input("Enter your Elf's name: ")
    player = Elf(
        name=player_name,
        health_range=(80, 130),
        attack_range=(15, 30),
        luck_range=(0.1, 0.5)
    )
    typewriter(f"Welcome, **{player.name}**!")
    typewriter(f"Your stats -> Health: {player.health:.2f}, Attack: {player.attack_power:.2f}, Luck: {player.luck:.2f}\n")
    
    enemy_names = [
        "Aelrindel", "Aerendyl", "Aesir", "Aithlin", "Alagossa", "Alduin", "Alenia", "Almariel", "Althidon", "Amara",
        "Amras", "Anarion", "Andraste", "Arannis", "Arathorn", "Ardreth", "Ardyn", "Arlen", "Arwen", "Arys",
        "Baelen", "Belanor", "Belwar", "Bennadil", "Beregond", "Borin", "Branwen", "Brethil", "Brithos", "Caladhel",
        "Calaethis", "Celeborn", "Celebrimbor", "Celestina", "Círdan", "Coron", "Daelith", "Daeron", "Dagnir", "Dalahar",
        "Delsaran", "Deltheron", "Delswin", "Eilistraee", "Elbereth", "Elendir", "Elemmírë", "Elendil", "Elrohir", "Elrond",
        "Elyon", "Elwyn", "Eraneth", "Erendriel", "Erestor", "Faelar", "Faelwen", "Faervel", "Falas", "Felaern",
        "Fenian", "Fenthis", "Filvendor", "Findecano", "Finduilas", "Galadriel", "Galanis", "Galathil", "Galdor", "Galion",
        "Gildor", "Gilmith", "Glorfindel", "Haleth", "Haldir", "Hatharal", "Hethrid", "Idril", "Ilmare", "Ingwë",
        "Irinis", "Isilion", "Kaelith", "Kaelthorn", "Kelvhan", "Kethra", "Kiliath", "Kiliwen", "Lhoris", "Lindir",
        "Lithoniel", "Lorien", "Luthien", "Maeglin", "Maeral", "Maethor", "Maiele", "Melian", "Mellor", "Mithrandir",
        "Mithrennon", "Morwen", "Naeris", "Nallindra", "Narion", "Neira", "Nessa", "Nimloth", "Nindor", "Nithral",
        "Olorin", "Orendil", "Orion", "Oromë", "Pelendur", "Peredhel", "Rhovanion", "Rillifane", "Rimdal", "Rothilion",
        "Saelihn", "Sairina", "Selarion", "Selendrile", "Shandalar", "Silas", "Sindar", "Sorion", "Soveliss", "Sylmare",
        "Tahlia", "Tauriel", "Thalion", "Thranduil", "Tindomerel", "Tinelith", "Tirion", "Trevon", "Undomiel", "Urthel",
        "Valandil", "Vandor", "Varon", "Veldrin", "Vilya", "Voronwë", "Xanaphia", "Xandar", "Xanthera", "Xilvien",
        "Yavanna", "Ylyndar", "Yrinor", "Yrthra", "Zaleria", "Zelphar", "Zendar", "Zinnathar", "Zyre", "Zylthar",
        "Arianna", "Balion", "Caelion", "Darlion", "Elarion", "Falarion", "Galenor", "Halarion", "Ilmarion", "Jalior",
        "Kalinar", "Larion", "Melarion", "Nalarion", "Olathar", "Phaelon", "Ravathar", "Selarion", "Talnarion", "Valion",
        "Wynar", "Xalith", "Yelion", "Zalyn", "Rhaelor", "Thaelor", "Vaelor", "Kaelor", "Aelathor", "Vaelith",
        "Gaelion", "Aerith", "Laelion", "Baelor", "Caelor", "Daelor", "Faelor", "Aelorion", "Haelor", "Jaelor"
    ]
    
    # Item system: player starts with 2 health potions
    items = [Item("Health Potion", "heal", 30) for _ in range(2)]

    # Battle loop
    while True:
        enemy = generate_enemy(enemy_names, player.level, health_boost, attack_boost, luck_boost)
        typewriter(f"\nA wild **{enemy.name}** appears!")
        typewriter(f"Enemy stats -> Health: {enemy.health:.2f}, Attack: {enemy.attack_power:.2f}, Luck: {enemy.luck:.2f}")

        # Round-by-round combat
        while enemy.health > 0 and player.health > 0:
            typewriter(f"\nYour Health: **{player.health:.2f}**")
            typewriter(f"{enemy.name}'s Health: **{enemy.health:.2f}**")

            # Player action
            typewriter("What will you do?")
            typewriter("1. Normal Attack\n2. Drain Attack\n3. Special Attack\n4. Defend\n5. Use Item\n6. Escape")
            action = input("Choose your action (1/2/3/4/5/6): ")

            if action == '1':
                player.attack(enemy)
            elif action == '2':
                player.attack(enemy, drain=True)
            elif action == '3':
                player.attack(enemy, special=True)
            elif action == '4':
                damage_modifier = player.defend()
            elif action == '5':
                if items:
                    items[0].use(player)
                    items.pop(0)  # Remove the used item
                else:
                    typewriter("You have no items left!")
            elif action == '6':
                typewriter(f"You escaped from {enemy.name}!")
                player.health = player.max_health  # Restore health on escape
                break

            # Enemy's turn
            if enemy.health > 0:
                enemy.attack(player)
            
            # Check if the player is still alive
            if player.health <= 0:
                typewriter("You have been defeated...")
                return

        # If the player won
        if player.health > 0 and action != '6':
            typewriter(f"\nYou defeated {enemy.name}!")
            player.health = player.max_health
            player.gain_xp(50)  # Grant 50 XP for defeating an enemy
            typewriter(f"Health restored to **{player.max_health:.2f}**!\n")

        # Continue or exit
        typewriter("1. Continue\n2. Exit")
        next_action = input("Choose (1/2): ")
        if next_action == '2':
            typewriter("Thanks for playing **ELVES BATTLIN**! Goodbye!")
            break

# Uncomment the line below to run the game
main()
