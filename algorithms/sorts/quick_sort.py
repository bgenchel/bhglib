"""
in place quick sort implementation
"""


def print_array(array):
    print " ".join(map(str, array))


def swap(array, index1, index2):
    temp = array[index2]
    array[index2] = array[index1]
    array[index1] = temp


def quick_sort(array):
    def _quick_sort_recurse(array, left, right):
        if right - left < 1:
            return

        pivot = array[right]
        gt_index = left
        for i in xrange(left, right):
            if array[i] < pivot:
                # this conditional is an optimization not anticipated
                # by hacker rank
                if gt_index < i:
                    swap(array, gt_index, i)
                gt_index += 1
        swap(array, gt_index, right)
        # print_array(array)

        _quick_sort_recurse(array, left, gt_index - 1)
        _quick_sort_recurse(array, gt_index + 1, right)

    _quick_sort_recurse(array, 0, len(array)-1)
    return

