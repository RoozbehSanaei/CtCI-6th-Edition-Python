import random
from typing import List, Optional

DAYS_FOR_RESULT = 7

'''

The code describes a simulation for identifying a poisoned bottle among several bottles using a limited number of test strips. 

Test Strip Class:
    Represents a test strip that can detect poison. It stores whether it has been poisoned and the day on which it was poisoned.

World Class:
    Represents the environment containing test strips, bottles, and the number of the poisoned bottle. It also keeps track of the current day.

Initializing the World:
    The world is initialized with a certain number of test strips, bottles, and the specific number of the poisoned bottle.
    It maintains a list of test strips and their statuses.

Day Property:
    Keeps track of the current day in the simulation. It can be incremented but not decreased.

Adding a Drop to a Test Strip:
    A drop from a bottle can be added to a test strip. 
    If the bottle is poisoned and the test strip has not yet been poisoned, the strip is marked as poisoned, and the day it was poisoned is recorded.

Identifying Positive Test Strips:
    The simulation can identify which test strips tested positive for poison. 
    A test strip is considered positive if it has been poisoned and a certain number of days (specified by DAYS_FOR_RESULT) have passed since it was poisoned.

Finding the Poisoned Bottle:
    To find the poisoned bottle, the simulation uses a binary representation approach where each test strip represents a binary digit.
    A drop from each bottle is added to certain test strips based on the binary representation of the bottle number.
    After waiting for the results (a specified number of days), the simulation determines which test strips are positive.
    The binary digits represented by the positive test strips are then used to reconstruct the number of the poisoned bottle.

Process Summary:
    The algorithm effectively uses binary numbers and bitwise operations to efficiently test all bottles with a limited number of test strips. 
    Each strip's positive or negative result contributes to identifying the binary representation of the poisoned bottle's number, thereby pinpointing the poisoned bottle in a large set with minimal testing resources.

'''


class _TestStrip:
    def __init__(self) -> None:
        self.has_poison = False
        self.day_poisoned: Optional[int] = None


class World:
    def __init__(
        self, num_test_strips: int, num_bottles: int, poisoned_bottle_num: int
    ) -> None:
        self._num_test_strips = num_test_strips
        self._test_strips = [_TestStrip() for i in range(num_test_strips)]
        self._num_bottles = num_bottles
        self._poisoned_bottle_num = poisoned_bottle_num
        self._day = 0

    @property
    def num_bottles(self) -> int:
        return self._num_bottles

    @property
    def num_test_strips(self) -> int:
        return self._num_test_strips

    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, day: int) -> None:
        if day < self._day:
            raise ValueError("day cannot be decreased")
        self._day = day

    def add_drop(self, bottle_num: int, test_strip_num: int) -> None:
        test_strip = self._test_strips[test_strip_num]
        if bottle_num == self._poisoned_bottle_num and not test_strip.has_poison:
            test_strip.has_poison, test_strip.day_poisoned = True, self.day

    def positive_test_strips(self) -> List[int]:
        res: List[int] = []
        for test_strip_num, test_strip in enumerate(self._test_strips):
            if (
                test_strip.has_poison
                and self.day - test_strip.day_poisoned >= DAYS_FOR_RESULT
            ):
                res.append(test_strip_num)
        return res


def find_poison(world: World) -> int:
    for i in range(world.num_bottles):
        for j in range(world.num_test_strips):
            if i & (1 << j):
                world.add_drop(bottle_num=i, test_strip_num=j)
    world.day += DAYS_FOR_RESULT
    return sum(1 << i for i in world.positive_test_strips())


def test_find_poison():
    poisoned_bottle_num = random.randrange(1000)
    world = World(
        num_bottles=1000, num_test_strips=10, poisoned_bottle_num=poisoned_bottle_num
    )
    assert find_poison(world) == poisoned_bottle_num
    return poisoned_bottle_num, world.day


def example():
    poisoned_bottle_num, days = test_find_poison()
    print("Found poison in bottle number", poisoned_bottle_num, "in", days, "days.")


if __name__ == "__main__":
    example()
