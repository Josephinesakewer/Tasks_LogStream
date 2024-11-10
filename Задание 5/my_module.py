import math 

def get_area_circle(radius)->float:
    return math.pi*radius**2

def average_score(scores)->float:
    if scores == 0:
        return 0
    else:
       return sum(scores)//len(scores)

def num_papers(sum_cost):
    cost_paper = 317.20
    return int(sum_cost//cost_paper)
    

