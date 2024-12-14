def max_water_depth(heights):
    n = len(heights)
    max_depth = 0

    for i in range(n):
        for j in range(i + 1, n):
            water_level = min(heights[i], heights[j])
            current_depth = 0

            for k in range(i + 1, j):
                if water_level > heights[k]:
                    current_depth = max(current_depth, water_level - heights[k])

            max_depth = max(max_depth, current_depth)

    return max_depth


height = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]
print(max_water_depth(height))
