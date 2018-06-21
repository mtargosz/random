from random import randint
from typing import List


def get_random_sequence(start: int, end: int, count: int, exclude: List[int], can_repeat: bool) -> List[int]:
    range_span = end - start + 1
    if not can_repeat and range_span < count:
        print('Decrease range or increase count.\nValues provided:\nSEQ LENGTH:\t' + str(count) +
             '\nRANGE FROM:\t' + str(start) + '\nRANGE TO:\t' + str(end) + '\nRANGE SPAN:\t' + str(range_span) +
             '\nDECREASE SEQ LENGTH OR INCREASE RANGE SPAN BY:\t' + str(count - range_span))

        return []

    seq = []
    seq_size = 0
    skipped_values = 0
    while seq_size < count:
        r_int = randint(start, end)
        if r_int in exclude:
            continue
        if r_int not in seq or can_repeat:
            seq.append(r_int)
            seq_size = len(seq)
        else:
            skipped_values += 1
            print(str(skipped_values) + ') ' + str(r_int))
    return sorted(seq)


# 17, 18, 24, 29, 40
# 04 - 05
ex = [4, 32, 38, 43, 51, 58, 10]
# ex = [1, 3, 14, 19, 29, 39, 40]
eu_mln_ex = [17, 18, 24, 29, 40]
eu_mln_ls_ex = [4, 5]
eu_mln = get_random_sequence(1, 50, 5, eu_mln_ex, False)
eu_mln_ls = get_random_sequence(1, 12, 2, eu_mln_ls_ex, False)

lotto = get_random_sequence(1, 59, 6, ex, False)
print(lotto)
# print(eu_mln)
# print(eu_mln_ls)
