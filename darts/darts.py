def score(x, y):
    distance = (x**2 + y**2)**0.5
    if distance <= 10 and distance > 5:
        return 1
    elif distance <= 5 and distance > 1:
        return 5
    elif distance <= 1:
        return 10
    return 0 
