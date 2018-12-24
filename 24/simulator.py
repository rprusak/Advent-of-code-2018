from units_group import UnitsGroup
from typing import List
import functools


class ImmuneSystemSimulator:

    def __init__(self, immune_system: List[UnitsGroup], infection: List[UnitsGroup]) -> None:
        self.immune_system = immune_system
        self.infection = infection
        self.boost = 0

    def set_boost(self, boost):
        for unit in self.immune_system:
            unit.attack_damage -= self.boost
            unit.attack_damage += boost

        self.boost = boost

    def run(self) -> bool:
        while len(self.infection) > 0 and len(self.immune_system):
            # target selection
            self.reset_targets()

            self.immune_system = self.order_units_for_target_selection(self.immune_system)
            self.infection = self.order_units_for_target_selection(self.infection)

            selected_infection_units = {}
            selected_immune_system_units = {}

            for unit in self.immune_system:
                g = self.find_defending_group(unit, self.infection)
                selected_infection_units[unit.id] = g

            for unit in self.infection:
                g = self.find_defending_group(unit, self.immune_system)
                selected_immune_system_units[unit.id] = g

            # attack phase
            all_units = self.immune_system + self.infection
            all_units = self.order_units_for_attack(all_units)

            for unit in all_units:
                # check if unit is already destroyed
                if unit.units_count <= 0:
                    continue
                else:
                    if unit.is_infection:
                        target = selected_immune_system_units[unit.id]
                    else:
                        target = selected_infection_units[unit.id]

                    if target is not None:
                        unit.deal_damage(target)

            self.immune_system = list(filter(lambda u: u.units_count > 0, self.immune_system))
            self.infection = list(filter(lambda u: u.units_count > 0, self.infection))

        return len(self.infection) > 0

    def reset_targets(self):
        for unit in self.immune_system:
            unit.is_targeted = False

        for unit in self.infection:
            unit.is_targeted = False

    @staticmethod
    def order_units_for_target_selection(units: List[UnitsGroup]):
        def compare_units(unit1: UnitsGroup, unit2: UnitsGroup):
            if unit1.get_effective_power() == unit2.get_effective_power():
                return unit1.initiative - unit2.initiative
            else:
                return unit1.get_effective_power() - unit2.get_effective_power()

        return sorted(units, key=functools.cmp_to_key(compare_units), reverse=True)

    @staticmethod
    def order_units_for_attack(units: List[UnitsGroup]):
        def compare_units(unit1: UnitsGroup, unit2: UnitsGroup):
            return unit1.initiative - unit2.initiative

        return sorted(units, key=functools.cmp_to_key(compare_units), reverse=True)

    @staticmethod
    def find_defending_group(attacking_unit: UnitsGroup, defending_units: List[UnitsGroup]):
        available_units = list(filter(lambda u: not u.is_targeted, defending_units))
        available_units = list(filter(lambda u: attacking_unit.get_possible_damage(u) > 0, available_units))

        def compare_units(unit1: UnitsGroup, unit2: UnitsGroup):
            potential_damage_to_fist_unit = attacking_unit.get_possible_damage(unit1)
            potential_damage_to_second_unit = attacking_unit.get_possible_damage(unit2)

            if potential_damage_to_fist_unit == potential_damage_to_second_unit:
                power_diff = unit1.get_effective_power() - unit2.get_effective_power()
                if power_diff == 0:
                    return unit1.initiative - unit2.initiative
                else:
                    return power_diff
            else:
                return potential_damage_to_fist_unit - potential_damage_to_second_unit

        sorted_units = sorted(available_units, key=functools.cmp_to_key(compare_units), reverse=True)

        if len(sorted_units) == 0:
            return None
        elif len(sorted_units) == 1:
            sorted_units[0].is_targeted = True
            return sorted_units[0]
        else:
            if compare_units(sorted_units[0], sorted_units[1]) == 0:
                return None
            else:
                sorted_units[0].is_targeted = True
                return sorted_units[0]
