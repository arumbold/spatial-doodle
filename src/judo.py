# Author: Aaron Rumbold
# Course: HND Digital Technologies for England (Cyber Security)
# 		  Unit 4 - Programming (2025)
# License: MIT


class Competitor:
    category:
        HEAVY_WEIGHT:0
        LIGHT_HEAVYWEIGHT:100
        MIDDLE_WEIGHT:90
        LIGHT_MIDDLEWEIGHT:81
        LIGHTWEIGHT:73
        FLYWEIGHT:66
    
class Fee:
    Beginner: 25
    Intermediate: 30
    Elite: 35
    PrivateTuition: 9.50 
    CompetitionFee: 22 


__all__ = ["Competitor", "Fee"]
