'''
1. Order the cars by their position on ascending order O(nlog(n))
2. Iterate the ordered cars from right to left, to first evaluate the cars on the right
3. Calculate how long the car takes to reach the target, save their time on a stack
4. Check if there's a previous car on the stack
    if the car is requires less time than the previous one to reach the target, we have a fleet
    since that car will merge with the latest car, we can skip adding it to the stack
    otherwise we add the car to the stack
5. We continue doing this, until we finish all the cars O(n)
6. The size of the stack is the number of fleets
'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        sorted_cars = sorted(cars)[::-1]
        count = 0
        last_speed = None

        for p, s in sorted_cars:
            current_speed = (target - p) / s

            if last_speed is None or current_speed > last_speed:
                count += 1
                last_speed = current_speed

        return count