def find_statistical_density_of_failure(data, first, second):
    ni = sum(1 if second >= data[i] > first else 0 for i in range(len(data)))
    fi = ni / (len(data) * (second - first))
    return fi


def probability(time, interval, f):
    count = int(time // interval[1])
    p = 1
    if count == len(f):
        return 0
    for index in range(count + 1):
        p -= f[index] * interval[1] if index < count else f[index] * (time - interval[index])
    return p


def intensity(time, interval, f):
    count = int(time // interval[1])
    return f[count] / probability(time, interval, f)


def interest_time_on_failure(h, y, list_probability):
    start, stop = 0, 1
    for index in range(len(list_probability) - 1):
        if list_probability[index] < y < list_probability[index + 1]:
            start, stop = index, index + 1
    d = (list_probability[stop] - y) / (list_probability[stop] - list_probability[start])
    return h - h * d


def lab_1(data, y=0.98, t1=414, t2=2077):
    t_cp = sum(data) / len(data)
    sorted_t_cp = sorted(data)
    intervals = [0.0 + sorted_t_cp[-1] * i / 10 for i in range(11)]
    statistical_density_of_failure = [
        find_statistical_density_of_failure(sorted_t_cp, intervals[i], intervals[i + 1])
        for i in range(len(intervals) - 1)
    ]
    list_probability = [probability(x, intervals, statistical_density_of_failure) for x in intervals[1:]]
    list_probability.insert(0, 1)
    p = probability(t1, intervals, statistical_density_of_failure)
    i = intensity(t2, intervals, statistical_density_of_failure)
    print(f'Середнє значення вибірки -> {t_cp}')
    print(f'Імовірність безвідмовної роботи на час {t1} складає -> {p}')
    print(f'Інтенсивність відмов на час {t2} складає -> {i}')
    print(f'Відсотковий наробіток на відмову при у = {y} складає -> '
          f'{interest_time_on_failure(intervals[1], y, list_probability)}')
    print('\n\nДодатково:')
    print(f'Масив інтервалів -> {intervals}')
    print(f'Масив статичної щільності -> {statistical_density_of_failure[0:5]}')
    print(statistical_density_of_failure[5:])
    print(f'Масив безвідмовної роботи -> {list_probability[0:5]}')
    print(list_probability[5:])



if __name__ == '__main__':
    lab_1([
        189, 833, 733, 219, 137, 1542, 164, 261,
        380, 82, 1668, 1282, 472, 279, 1128, 1715,
        206, 826, 255, 1528, 353, 296, 1267, 215,
        58, 346, 618, 562, 341, 1742, 70, 154, 224,
        1038, 41, 1438, 405, 415, 89, 368, 283, 338,
        444, 566, 206, 2111, 398, 878, 1766, 128,
        859, 2853, 23, 1427, 1025, 551, 552, 69,
        482, 269, 377, 100, 419, 817, 609, 1581,
        1468, 22, 587, 58, 2313, 104, 122, 154, 493,
        91, 1591, 447, 15, 101, 1661, 189, 524, 265,
        370, 221, 1149, 448, 1175, 7, 318, 2084,
        156, 558, 91, 432, 773, 406, 2088, 83
    ])
    print('\n\n')
    lab_1([
        644, 1216, 2352, 1386, 1280, 903, 607, 2068, 4467, 835, 313, 555, 307, 508, 1386, 2895, 583, 292, 5159, 1107,
        181, 18, 1247, 125, 1452, 4211, 890, 659, 1602, 2425, 214, 68, 21, 1762, 1118, 45, 1803, 1187, 2154, 19, 1122,
        278, 1622, 702, 1396, 694, 45, 1739, 3483, 1334, 1852, 96, 173, 7443, 901, 2222, 4465, 18, 1968, 1426, 1424,
        1146, 435, 1390, 246, 578, 281, 455, 609, 854, 436, 1762, 444, 466, 1934, 681, 4539, 164, 295, 1644, 711, 245,
        740, 18, 474, 623, 462, 605, 187, 106, 793, 92, 296, 226, 63, 246, 446, 2234, 2491, 315
    ], t1=2000, t2=2000, y=0.9)
