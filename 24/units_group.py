

class UnitsGroup:
    def __init__(self) -> None:
        self.id = 0
        self.units_count = 0
        self.hit_points = 0
        self.attack_damage = 0
        self.attack_type = None
        self.weaknesses = []
        self.immunities = []
        self.initiative = 0
        self.is_infection = False
        self.is_targeted = False

    def __str__(self) -> str:
        description = ""
        description += ("infection " if self.is_infection else "immune system ") + str(self.id) + ", "
        description += "units: " + str(self.units_count)
        description += ", hit points: " + str(self.hit_points)
        description += ", initiative: " + str(self.initiative)
        description += ", attack damage: " + str(self.attack_damage)
        description += ", attack type: " + str(self.attack_type)
        description += ", weaknesses: " + str(self.weaknesses)
        description += ", immunities: " + str(self.immunities)

        return description

    def get_effective_power(self) -> int:
        return self.units_count * self.attack_damage

    def get_possible_damage(self, target: 'UnitsGroup'):
        power = self.get_effective_power()

        if self.attack_type in target.weaknesses:
            return power * 2
        elif self.attack_type in target.immunities:
            return 0
        else:
            return power

    def deal_damage(self, target: 'UnitsGroup'):
        damage = self.get_possible_damage(target)
        target.__take_damage(damage)

    def __take_damage(self, damage: int):
        destroyed_units = damage // self.hit_points
        self.units_count -= destroyed_units
