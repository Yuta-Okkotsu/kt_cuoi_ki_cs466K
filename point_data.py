def PointSum(dic):
    diem = list(dic.values())
    return sum(diem)

def PointAverage(dic):
    return PointSum(dic)/len(dic)

def PointMaxMin(dic):
    diem = list(dic.values())
    return [min(diem), max(diem)]


