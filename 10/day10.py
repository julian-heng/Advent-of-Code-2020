#!/usr/bin/env python3

from collections import Counter
from math import prod


def main():
    with open("input", "r") as f:
        nums = list(map(int, f.read().strip().splitlines()))

    nums.sort()
    nums = [0] + nums + [max(nums) + 3]
    print(solve1(nums))
    print(solve2(nums))


def solve1(nums):
    return prod(Counter([j - i for i, j in zip(nums[:-1], nums[1:])]).values())


def solve2(nums):
    d = [n for n, (i, j) in enumerate(zip(nums[:-1], nums[1:])) if j - i == 3]
    result = 1
    i = -1
    for j in d:
        n = max(1, j - i - 2)
        e = int(3 not in (nums[j] - nums[i+1], j - i))
        result *= (2 ** n) - e
        i = j

    return result


if __name__ == "__main__":
    main()