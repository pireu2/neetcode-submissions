class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        position_speed = sorted(zip(position, speed)) 

        for pos, s in reversed(position_speed):
            time = (target - pos) / s

            if stack and time > stack [-1] :
                stack.append(time)

            elif not stack:
                stack.append(time)

        return len(stack)