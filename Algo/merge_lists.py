my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

def merge_lists1(a, b):
    """
    Slow.
    Each del is O(n).
    We'll go around the while loops n times.
    Total time is O(n**2).
    """
    output = []
    while a != []:
        if a[0] < b[0]:
            output.append(a[0])
            del a[0]
        else:
            output.append(b[0])
            del b[0]
    while b != []:
        output.append(b[0])
        del b[0]

    return output


def merge_lists2(a, b):
    """
    Might be faster?
    Pops are O(1), much improved over the deletion.
    still O(n) for reversal
    still going around the whiles n times.
    Think this is O(2n) (O(n))
    """
    output = []
    while a != []:
        if a[-1] > b[-1]:
            output.append(a.pop())
        else:
            output.append(b.pop())
    while b != []:
        output.append(b.pop())
    output.reverse()
    return output

def merge_lists3(a, b):
    """
    appending to a list might be O(1). + as used here creates a third list in memory.
    in-built sort is O(n log n)
    I think at best this is O(n log n), at worst O(k + n log n)
    Finally, IC points out that .sort()'s Timsort is optimized for sorting sorted lists,
    so this is probably fastest for n < 1,000,000.
    """
    merged = a + b
    merged.sort()
    return merged

def merge_lists4(a, b):
    """
    Developed with lots of help from IC's hints.
    O(n) time and O(n) space (for the new list in memory)
    """
    output = (len(a) + len(b)) * [None]
    a_cursor = 0
    b_cursor = 0
    o_cursor = 0

    while o_cursor < len(output):
        if a_cursor != len(a) and (b_cursor == len(b) or a[a_cursor] < b[b_cursor]):
            output[o_cursor] = a[a_cursor]
            a_cursor += 1
        else:
            output[o_cursor] = b[b_cursor]
            b_cursor += 1
        o_cursor += 1

    return output


print(merge_lists(my_list, alices_list))
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
