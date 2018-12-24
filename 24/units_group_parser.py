from units_group import UnitsGroup
from typing import List
import re


class UnitsGroupParser:

    def __init__(self) -> None:
        self.__units_count_pattern = re.compile("^(\d+) units.*")
        self.__hit_points_pattern = re.compile(".+each with (\d+) hit points.+")
        self.__weaknesses_pattern = re.compile(".*weak to ([^;)]+).*")
        self.__immunities_pattern = re.compile(".*immune to ([^;)]+).*")
        self.__attack_damage_pattern = re.compile(".*attack that does (\d+).*")
        self.__attack_type_pattern = re.compile(".*attack that does \d+ (\w+) damage.*")
        self.__initiative_pattern = re.compile(".*at initiative (\d+)")

    def get_group(self, description: str) -> 'UnitsGroup':
        units_group = UnitsGroup()

        units_group.units_count = self.__get_units_count(description)
        units_group.hit_points = self.__get_hit_points(description)
        units_group.weaknesses = self.__get__weaknesses(description)
        units_group.immunities = self.__get_immunities(description)
        units_group.attack_damage = self.__get_attack_damage(description)
        units_group.attack_type = self.__get_attack_type(description)
        units_group.initiative = self.__get_initiative_pattern(description)

        return units_group

    def __get_units_count(self, description: str) -> int:
        match = self.__units_count_pattern.match(description)
        if match:
            return int(match[1])
        else:
            raise RuntimeError("Could not parse units count")

    def __get_hit_points(self, description: str) -> int:
        match = self.__hit_points_pattern.match(description)
        if match:
            return int(match[1])
        else:
            raise RuntimeError("Could not parse hit points")

    def __get__weaknesses(self, description: str) -> List[str]:
        match = self.__weaknesses_pattern.match(description)
        if match:
            return match[1].replace(",", "").split(" ")
        else:
            return []

    def __get_immunities(self, description: str):
        match = self.__immunities_pattern.match(description)
        if match:
            return match[1].replace(",", "").split(" ")
        else:
            return []

    def __get_attack_damage(self, description: str) -> int:
        match = self.__attack_damage_pattern.match(description)
        if match:
            return int(match[1])
        else:
            raise RuntimeError("Could not parse attack damage")

    def __get_attack_type(self, description: str) -> str:
        match = self.__attack_type_pattern.match(description)
        if match:
            return match[1]
        else:
            raise RuntimeError("Could not parse attack type")

    def __get_initiative_pattern(self, description: str) -> int:
        match = self.__initiative_pattern.match(description)
        if match:
            return int(match[1])
        else:
            raise RuntimeError("Could not parse initiative")
