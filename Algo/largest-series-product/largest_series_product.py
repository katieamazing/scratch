# a * b = exp(ln(a) + ln(b))
# largest product
# because exp is monotone
# is largest sum
# [0, 0], [0, 1], [0, 2], ... [0, 5],
#         [1, 1], [1, 2], ... [1, 5],
#                 [2, 2], .... [2, 5],
#                               ...
#                              [5, 5]
# max of all the things like ln(a[1]) + ln(a[2]) + ln(a[3]))
# let's pretend that we wanted to solve
# maximum sum
# maximum sum of any span
# first_list .. x
# what was the maximum sum of any span of first_list?
# what was the maximum suffix of first_list?
# max_span of the first list = max ( max_sum_of_first_list, max_suffix_of_first_list + x)
# max_suffix = max(max_suffix_of_first_list + x, 0)
import math

# this computes the maximum total that can be made from
# a suffix of xs, using at most limit elements
def max_suffix(xs, limit):
    return max(sum(xs[i:]) for i in range(0, limit))

def largest_sum(xs, limit):
    max_span = 0
    for i, x in enumerate(xs):
        max_span = max(max_span, max_suffix(xs[:i], limit - 1) + x)
    return max_span

assert(largest_sum([2, 9], 2) == 11)
assert(largest_sum([0.69, 2.19], 2) == 2.88)

# dynamic programming solution
#
# def max_suffix(xs, limit):
#     if not xs or limit == 0:
#         return 1
#     best_so_far = 1
#     for i in range(0, min(limit, len(xs))):
#         x = int(xs[-1-i])
#         if x == 0:
#             break
#         best_so_far *= x
#     return best_so_far
#
# def largest_product(xs, limit):
#     if limit > len(xs):
#         raise ValueError
#     if limit < 0:
#         raise ValueError
#     if not xs and limit != 0:
#         raise ValueError
#     if not xs or limit == 0:
#         return 1
#     max_span = 0
#     for i, xChar in enumerate(xs):
#         x = int(xChar)
#         if x == 0:
#             max_span = max_span
#         else:
#             max_span = max(max_span, max_suffix(xs[:i], limit - 1) * x)
#     return max_span

assert(largest_product("0123456789", 2) == 72)
