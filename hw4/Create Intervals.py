def create_intervals(data):
    if len(data) != 0:
        min_ = min(data)
        max_ = max(data)
        max_set = set(range(min_, max_))

        set_diff = max_set.difference(data)
        set_diff.add(min_ - 1)
        set_diff.add(max_ + 1)

        a = sorted(set_diff)

        result = []
        res = []

        for i in range(len(a) - 1):
            if (a[i + 1] - a[i]) > 1:
                res = (a[i] + 1, a[i + 1] - 1)
                result.append(res)
        return result
    else:
        return None

