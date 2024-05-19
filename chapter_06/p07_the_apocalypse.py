import enum
import random

'''
The Apocalypse: In the new post-apocalyptic world, the world queen is desperately concerned
about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or
else they face massive fines. If all families abide by this policy that is, they have continue to have
children until they have one girl, at which point they immediately stop-what will the gender ratio
of the new generation be? (Assume that the odds of someone having a boy or a girl on any given
pregnancy is equal.) Solve this out logically and then write a computer simulation of it.
'''

'''
The provided code simulates a scenario often referred to as the "apocalypse problem" or "gender ratio problem" using a simple model.

    Gender Enumeration:
        Defines an enumeration Gender with two values: BOY and GIRL.

    Simulate Child Function:
        Randomly generates the gender of a child, with an equal probability of being a boy or a girl.

    Family Class:
        Represents a family with a specified number of boys and girls.

    Simulate Family Function:
        Simulates the creation of a family. 
        In this model, each family continues to have children until they have a girl
        The function counts the number of boys born before the first girl and then creates a family with this number of boys and one girl.

    Simulate Apocalypse Function
        Simulates a large number of families (specified by num_families).
        For each family, it adds the number of boys and the number of girls to the total counts.
        Calculates the ratio of boys to the total number of children across all families.

    Test Apocalypse Function
        Runs the apocalypse simulation with a large number of families (30,000 in this case).
        Checks if the ratio of boys to the total number of children is close to 0.5, asserting that it should not deviate from 0.5 by more than 0.01.
    
'''

class Gender(enum.Enum):
    BOY = enum.auto()
    GIRL = enum.auto()


def simulate_child() -> Gender:
    return random.choice([Gender.BOY, Gender.GIRL])


class Family:
    def __init__(self, num_boys: int, num_girls: int) -> None:
        self.num_boys = num_boys
        self.num_girls = num_girls


def simulate_family() -> Family:
    num_boys = sum(1 for _ in iter(simulate_child, Gender.GIRL))
    return Family(num_boys=num_boys, num_girls=1)


def simulate_apocalypse(num_families: int) -> float:
    total_boys = total_girls = 0
    for _ in range(num_families):
        family = simulate_family()
        total_boys += family.num_boys
        total_girls += family.num_girls
    return total_boys / (total_boys + total_girls)


def test_apocalypse():
    # ratio should be really close to 0.5
    ratio = simulate_apocalypse(30000)
    assert abs(0.5 - ratio) < 0.01


if __name__ == "__main__":
    n = int(input("How many families should we simulate? "))
    print("Proportion of children that are boys:", simulate_apocalypse(n))
