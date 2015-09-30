# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/30'


# ERROR
def containsNearbyAlmostDuplicate0(nums, k, t):
    nums.sort()
    def helper(nums):
        left = 0
        right = len(nums) - 1
        if left <= right:
            if right - left <= k and nums[right] - nums[left] <= t:
                return True
            else:
                mid = (right + 1) / 2
                return helper(nums[:mid]) or helper(nums[mid:])
        else:
            return False
    return helper(nums)


def containsNearbyAlmostDuplicate1(nums, k, t):
    if k == 0 and t != 0:
        return False
    left = 0
    right = len(nums) - 1
    def helper(left, right):
        if left < right:
            if right - left <= k and nums[right] - nums[left] <= t:
                return True
            else:
                mid = left + (right - left) / 2
                return helper(left, mid) or helper(mid, right)
        else:
            return False
    return helper(left, right)

def containsNearByAlmostDuplicate(nums, k, t):
    buckets = {}
    for index, num in enumerate(nums):
        bucket_num, offset = (num / t, 1) if t else (num, 0)
        for i in xrange(bucket_num-offset, bucket_num+offset+1):
            if i in buckets:
                for v in buckets:
                    if abs(v-num) <= t:
                        return True
        buckets.setdefault(bucket_num, []).append(num)
        if len(buckets) > k:
            del buckets[nums[i - k] / t if t else nums[i - k]]
    return False


# 别人的，为什么我没懂……
def containsNearbyAlmostDuplicate(self, nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    buckets = {}
    for i, v in enumerate(nums):
        # t == 0 is a special case where we only have to check the bucket
        # that i is in.
        bucketNum, offset = (v / t, 1) if t else (v, 0)
        for idx in xrange(bucketNum - offset, bucketNum + offset + 1):
            if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                return True

        buckets[bucketNum] = nums[i]
        if len(buckets) > k:
            # Remove the bucket which is too far away. Beware of zero t.
            del buckets[nums[i - k] / t if t else nums[i - k]]

    return False



if __name__ == '__main__':
    print containsNearbyAlmostDuplicate([-1, -1], 1, -1)
