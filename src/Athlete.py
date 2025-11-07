# Author: Aaron Rumbold
# Course: HND Digital Technologies for England (Cyber Security)
# 		  Unit 4 - Programming (2025)
# License: MIT

class Athlete:
    def __init__(self, name, Plan, weight):
        self.name = name
        self.Plan = Plan
        self.weight = weight


class Plan:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class Plans:
    basic = Plan("Basic", 29.99)
    premium = Plan("Premium", 59.99)
    ultimate = Plan("Ultimate", 99.99)

# Example usage
jaxon = Athlete("Jaxon", Plans.premium, 180)
leah = Athlete("Leah", Plans.ultimate, 150)

print(f"{jaxon.name} is on the {jaxon.Plan.name} plan costing ${jaxon.Plan.cost} and weighs {jaxon.weight} lbs.")
print(f"{leah.name} is on the {leah.Plan.name} plan costing ${leah.Plan.cost} and weighs {leah.weight} lbs.")

__all__ = [Athlete]