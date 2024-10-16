import random
import math

# Elf Class
class Elf:
    def __init__(self, name, walk_velocity, run_factor, jump_velocity, attack_power):
        self.name = name
        self.walk_velocity = walk_velocity
        self.run_factor = run_factor
        self.jump_velocity = jump_velocity
        self.attack_power = attack_power
        self.air_velocity = self.calculate_air_velocity()
        self.special_attack_power = self.calculate_special_attack_power()
        self.power_level = self.calculate_power_level()
    
    def calculate_air_velocity(self):
        air_velocity = self.walk_velocity / 2
        return math.floor(air_velocity)  # Round down to remove decimals
    
    def calculate_special_attack_power(self):
        special_attack_power = ((self.walk_velocity * self.run_factor) / 1.5) + self.attack_power
        return math.floor(special_attack_power)  # Round down to remove decimals

    def calculate_power_level(self):
        return math.floor(
            self.walk_velocity + self.run_factor + self.jump_velocity + 
            self.attack_power + self.air_velocity + self.special_attack_power
        )  # Round down to remove decimals
        
    def info(self):
        print(f"Name: {self.name}, Speed: {self.walk_velocity}, Attack power: {self.attack_power}, "
              f"Air velocity: {self.air_velocity}, Special Attack Power: {self.special_attack_power}, "
              f"Power Level: {self.power_level}")

# Create multiple elves
def create_elves(num_elves):
    elves = []
    for i in range(num_elves):
        name = input(f"Enter a name for Elf {i + 1}: ")
        walk_velocity = random.randint(2, 10)
        run_factor = random.randint(1, 3)
        jump_velocity = random.randint(5, 10)
        attack_power = random.randint(5, 15)
        
        elf = Elf(name, walk_velocity, run_factor, jump_velocity, attack_power)
        elves.append(elf)
    return elves

# Main program
print("\033[1mBattle of Elves\033[0m\n")  # Print title in bold

num_elves = int(input("Enter the number of elves to create: "))
elf_list = create_elves(num_elves)

# Info of each elf and comparison
strongest_elf = None

for elf in elf_list:
    elf.info()
    if strongest_elf is None or elf.power_level > strongest_elf.power_level:
        strongest_elf = elf

# Winner Elf
print(f"\n\033[1m{strongest_elf.name} won the battle with a power level of {strongest_elf.power_level}.\033[0m")
