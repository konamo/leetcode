class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        ii = 0
        while ii < len(asteroids):
            if stack:
                if asteroids[ii] < 0 and stack[-1] > 0:
                    if abs(stack[-1]) < abs(asteroids[ii]):
                        stack.pop()
                    elif abs(stack[-1]) == abs(asteroids[ii]):
                        stack.pop()
                        ii += 1
                    else:
                        ii += 1
                else:
                    # no collision
                    stack.append(asteroids[ii])
                    ii += 1
            else:
                # empty stack, add current asteroid
                stack.append(asteroids[ii])
                ii += 1
        return stack

    def asteroidCollision2(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans

def main():
    s = Solution()
    a = [5,10,-5]
    print("1: " + str(s.asteroidCollision(a)))

    a = [8,-8]
    print("2: " + str(s.asteroidCollision(a)))

    a = [10,2,-5]
    print("3: " + str(s.asteroidCollision(a)))

    a = [-2,-1,1,2]
    print("3: " + str(s.asteroidCollision(a)))

    a = [-2,-2,1,-2]
    print("3: " + str(s.asteroidCollision(a)))
    return



if __name__ == '__main__':
    main()
