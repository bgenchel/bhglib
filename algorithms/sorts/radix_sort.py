import sys


def extract_digit(num, pos):
    return (num%(10**(pos+1)))/10**pos


def radix_sort(list_of_keys):
    # pos = 0 means we're doing a least significant bit radix sort,
    # starting our 'passes' with the least significant bit and 'moving left'
    pos = 0
    while True:
        remainder = 0
        buckets = [0]*10

        # for each number in our list, extract the digit from our current
        # position, and then increment the count of that bucket. This one way
        # sweep is O(N)
        for key in list_of_keys:
            # all the while, see if any numbers have digits in positions greater
            # than the current.
            remainder = max(remainder, key/10**pos)
            buckets[extract_digit(key, pos)] += 1
        # print buckets

        # if no numbers in our list have digits in or greater than our current
        # position, break the loop; we should be done sorting.
        if remainder == 0:
            break

        # scan through the bucket positions, and sum their values. This
        # operation allows us to say, numbers with digit i in position p (whatever
        # our current position is) in the final sort will definitely have a
        # position less than the value in bucket[i] and greater than the value
        # in bucket[i - 1]. This operation is a constant O(10)
        for i in range(1, len(buckets)):
            buckets[i] += buckets[i - 1]
        # print buckets

        # create a new list with as many positions as our list to sort. Scan
        # through the original list. For each key in the list, once again extract
        # digit i from position p. Place this key into the new list at position
        # bucket[i]. Then decrement the value of bucket[i]; no other key will
        # have that position. This sweep takes an additional O(N).
        sort_set = [0]*len(list_of_keys)
        for key in list_of_keys:
            digit = extract_digit(key, pos)
            # print 'buckets[digit] = {}'.format(buckets[digit])
            sort_set[buckets[digit] - 1] = key
            buckets[digit] -= 1

        list_of_keys = sort_set
        pos += 1

    # The time complexity for one sweep is O(N + 10 + N), which can be simplified
    # to O(N). We will have as many sweeps as we have digits in the largest number
    # in our set (let's call this value K). Therefore, the total time complexity 
    # of this sort is O(N*K)
    return list_of_keys


if __name__ == '__main__':
    loi = [int(arg) for arg in sys.argv[1:]]
    print radix_sort(loi)
