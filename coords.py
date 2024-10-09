coords1 = [(1, 10), (1, 11)]
coords2 = [(0, 20), (20, 20)]
coords3 = [(100, 91, 87), (80, 35, 70)]
coords4 = [(0, 100, 20), (0, 0, 80)]
array_coords = [coords1,coords2,coords3,coords4]
def calculate(array_coords):
    for elem in array_coords:
        if len(elem)==2:
            res = 0
            for point1,point2 in zip(elem[0],elem[1]):
                res +=pow((point1-point2),2)
            res = pow(res,0.5)
            print(res)

calculate(array_coords)