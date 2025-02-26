class Solution:
    '''
    We have two main scenarions: The armor is greater than the max of the damage or not.

    If the armor is greater than the max of the damage, the health we need is: 1 + sum(damage) - max(damage)
    If the armor is smaller than the max of the damage, the health we need is: 1 + sum(damage) - armor
    '''
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        total_damage = sum(damage)

        if armor > max_damage:
            return 1 + total_damage - max_damage

        return 1 + total_damage - armor
        
