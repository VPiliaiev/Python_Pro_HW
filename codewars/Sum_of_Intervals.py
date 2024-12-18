def sum_of_intervals(intervals: list) -> int:
    sum = 0
    intervals = sorted(intervals)
    a = intervals[0][0]
    b = intervals[0][1]
    sum += b - a
    if len(set(intervals)) == 1:
        return sum
    else:
        for j in intervals[1:]:
            if j[0] > b:
                sum += j[1] - j[0]
                a = j[0]
                b = j[1]
            elif j[0] >= a and j[1] <= b:
                continue
            else:
                sum += j[1] - b
                b = j[1]
    return sum
