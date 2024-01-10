# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import collections
from queue import PriorityQueue
import math


class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:

    def __init__(self):
        pass

    def hasCycle(self, head):
        slow = head
        fast = head
        if not head:
            return False
        while head:
            slow = head.next
            fast = head.next.next
            if slow.__eq__(fast):
                return True
            head = head.next
        return False

    def isHappy(self, n):
        if n == 2:
            return False
        if n == 3:
            return False
        sum = 0
        holdNum = [2, 3, 4, 5]
        while n not in holdNum:
            print(f'n:{n}')
            holdNum.append(n)
            while n > 0:
                sum += (n % 10) * (n % 10)
                n = n // 10
            if sum == 1:
                return True
            else:
                n = sum
                sum = 0

        return False

    def isUgly(self, n):
        if n == 1:
            return True
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        if n == 1:
            return True
        return False

    def nthUglyNumber(self, n):
        ugly_list = [1]
        while n > 0:
            index1, index2, index3 = 0
            ugly1 = 2 * ugly_list[index1]
            ugly2 = 3 * ugly_list[index2]
            ugly3 = 5 * ugly_list[index3]
            umin = min(ugly1, ugly2, ugly3)
            if umin == ugly1:
                index1 += 1
            if umin == ugly2:
                index2 += 1
            if umin == ugly3:
                index3 += 1
            ugly_list.append[umin]
            n -= 1
        return ugly_list

    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return nums1
        if m == 0:
            for num in nums2:
                nums1.append(num)
        res = []

        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
                print("hier 1 ")
                print(res)
            else:
                res.append(nums2[j])
                j += 1
                print("hier 2 ")
                print(res)
        if i < m:
            while i < m:
                res.append(nums1[i])
                i += 1
        if j < n:
            while j < n:
                res.append(nums1[i])
                j += 1
        for i in range(m + n):
            nums1[i] = res[i]
        return nums1

    def lengthOfLastWord(self, s):
        substring = s.split()
        return (len(s[-1]))

    def addTwoNumbers(self, l1, l2):
        res = ListNode()
        cur = res
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10, None)
            cur = cur.next
            carry //= 10
        return res.next

    def canCompleteCircuit(self, gas, cost):
        fill = 0
        for i in range(0, len(gas)):
            start = i
            print(f'new loop i= {start}')
            while True:
                if fill + gas[i] >= cost[i]:
                    fill += gas[i] - cost[i]
                    print(f'gas {gas[i]}')
                    print(f'cost {cost[i]}')
                    print(f'i= {i}')
                    print(f'new fill {fill}')
                    i += 1
                    i %= len(gas)

                    if i == start % len(gas):
                        return start
                else:
                    fill = 0
                    break
        return -1

    def maxArea(self, height):
        maxArea = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                if height[i] > height[j]:
                    curArea = (j - i) * (height[j])
                else:
                    curArea = (j - i) * height[i]
                if curArea > maxArea:
                    maxArea = curArea
        return maxArea

    def missingNumber(self, nums):
        nums.sort()
        for i, j in enumerate(range(len(nums) + 1)):
            if nums[i] != j:
                return i
        return

    def mySqrt(self, x):
        l = 0
        r = x // 2
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
        return res

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a, b = 0, int(math.sqrt(c))
        while a <= b:
            print(a, b)
            mid = (a + b) // 2
            total = a ** 2 + mid ** 2
            if total == c:
                return True
            elif total < c:
                a = mid
            else:
                b = mid
        return a, b

    def spiralOrder(self, matrix):
        boundary_left = -1
        boundary_right = len(matrix[0])
        boundary_up = -1
        boundary_down = len(matrix)

        column, row = 0, 0
        mode = "right"
        res = []

        while True:
            if mode == "right":
                res.append(matrix[row][column])
                if column + 1 < boundary_right:
                    column += 1
                else:
                    boundary_up += 1
                    if row + 1 < boundary_down:
                        mode = "down"
                        row += 1
                    else:
                        print("hier1")
                        break
            elif mode == "down":
                res.append(matrix[row][column])
                if row + 1 < boundary_down:
                    row += 1
                else:
                    boundary_right -= 1
                    if column - 1 > boundary_left:
                        mode = "left"
                        column -= 1
                    else:
                        break
            elif mode == "left":
                res.append(matrix[row][column])
                if column - 1 > boundary_left:
                    column -= 1
                else:
                    boundary_down -= 1
                    if row - 1 > boundary_up:
                        mode = "up"
                        row -= 1
                    else:
                        break
            else:
                res.append(matrix[row][column])
                if row + 1 < boundary_down:
                    row += 1
                else:
                    boundary_right -= 1
                    if column + 1 < boundary_right:
                        mode = "right"
                        column += 1
                    else:
                        break
        return res

    def getIntersectionNode(self, headA, headB):
        listA = []
        listB = []
        headAcopy = headA
        headBcopy = headB
        while headAcopy:
            listA.append(headAcopy.value)
            headAcopy = headAcopy.next
        print(listA)
        while headBcopy:
            listB.append(headBcopy.value)
            headBcopy = headBcopy.next
        print(listB)
        intersectVal = []
        for num in listA:
            if num in listB:
                intersectVal.append(num)

        if len(intersectVal) == 0:
            print("len =0")
            return None
        print(intersectVal)
        headAcopy = headA
        headBcopy = headB
        for val in intersectVal:
            print(val)
            while headAcopy.value != val:
                headAcopy = headAcopy.next
            while headBcopy.value != val:
                headBcopy = headBcopy.next
            if headAcopy == headBcopy:
                return headAcopy
            headAcopy = headA
            headBcopy = headB
        print("nothing in")
        return None

    def reverseString(self, s):
        start_pointer = 0
        end_pointer = len(s) - 1
        while start_pointer != end_pointer:
            char = s[start_pointer]
            s[start_pointer] = s[end_pointer]
            s[end_pointer] = char
            start_pointer += 1
            end_pointer -= 1

    def deleteDuplicates(self, head):
        prev, cur = head, head
        while cur:
            while cur.val == prev.val:
                cur = cur.next
            prev = cur
            cur = cur.next

    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        g_pointer = 0
        s_pointer = 0
        while g_pointer < len(g) and s_pointer < len(s):
            if g[g_pointer] <= s[s_pointer]:
                g_pointer += 1
            s_pointer += 1
        return g_pointer

    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        elif len(nums) == 4:
            return [nums] if sum(nums) == target else []
        else:
            res = []
            for i in range(len(nums) - 3):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                for j in range(len(nums) - 2):
                    if j > 0 and nums[j] == nums[j - 1]:
                        continue
                    l = j + 1
                    r = len(nums) - 1
                    while l < r:
                        if nums[i] + nums[j] + nums[l] + nums[r] < target:
                            l += 1
                        elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                            r -= 1
                        else:
                            quadruplets = [nums[i], nums[j], nums[l], nums[r]]
                            res.append(quadruplets)
                            while l < r and nums[l] == quadruplets[2]:
                                l += 1
                            while l < r and nums[r] == quadruplets[3]:
                                r -= 1
            return res

    def findDuplicate(self, nums):
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow

    def containsNearbyDuplicate(self, nums, k):
        if k == 0:
            return False
        hmap = {}
        for i in range(len(nums)):
            if nums[i] not in hmap.keys():
                hmap[nums[i]] = i
            else:
                if abs(i, hmap[nums[i]]) <= k:
                    return True
        return False

    def numSubarrayProductLessThanK(self, nums, k):
        l = 0
        product = 1
        res = 0
        for r in range(len(nums)):
            product *= nums[r]
            if product >= k:
                while l <= r and product >= k:
                    product /= nums[l]
                    l += 1
            res += r - l + 1

        return res

    def longestOnes(self, nums, k):
        l, max_len, num_zero = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zero += 1
            while num_zero > k:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len

    def isNice(self, s, start, end):
        str_set = set(s[start:end])
        for c in str_set:
            if (c.upper() in s) != (c.lower() in s):
                return False
        return True

    def longestNiceSubstring(self, s):
        max = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.isNice(s, i, j) and len(s[i:j]) > len(max):
                    max = s[i:j]
        return max

    def topKFrequent(self, nums, k):
        count = {}
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]
        for v, c in count.items():
            freq[c].append(v)
        print(freq)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:

                res.append(n)

                if len(res) == k:

                    return res

    def productExceptSelf(self, nums):
        res=[]
        res.append(1)
        for i in range(len(nums)-1):
            res.append(res[-1]*nums[i])
        post=1
        for j in range (len(nums)-1, 0,-1):
            post*=nums[j]
            res[j-1]*=post
        return res

    def isValidSudoku(self, board):
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        squares= collections.defaultdict(set) # key=(row/3, column/3)
        for r in range(9):
            for c in range(9):
                if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r/3, c/3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r/3, c/3)].add(board[r][c])
                
        return True

    def isPalindrome(self, s):
        l=0
        r=len(s)-1
        while l<r:
            while not s[l].isalnum():
                l+=1
            while not s[r].isalnum():
                r-=1
            if s[l].lower() !=s[r].lower():
                return False
            l+=1
            r-=1
        return True

    def twoSum(self, numbers, target):
        l=0
        r=len(numbers)
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l, r]
            elif numbers[l]+ numbers[r]< target:
                l+=1
            else:
                r-=1
        return []


    def generateParenthesis(self, n):
        res=[]
        stack=[]
        def recur(open, close):
            if open==close==n:
                res.append("".join(stack))
                return
            if open<n:
                stack.append("(")
                recur(open+1, close)
                stack.pop()
            if close<open:
                stack.append(")")
                recur(open, close+1)
                stack.pop()
        recur(0,0)
        return res

    def dailyTemperatures(self, temperatures):
        res=[0]* len(temperatures)
        stack=[]
        for i, t in enumerate(temperatures):
            while t>stack[-1][0]:
                stackTemperature, stackIndex= stack.pop()
                res[stackIndex]= i-stackIndex
            res.append([t,i])
        return res

    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int

        """
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        print(stack)
        return len(stack)

    def checkInclusion(self, s1, s2):
        countS1={}
        countS2={}
        for c in s1:
            countS1[c]= 1+ countS1.get(c, 0)

        l, r=0,0
        while r < len(s2) and s2[r] not in countS1:
            r += 1
        if r < len(s2):
            l = r
        while r<len(s2):
            while r <len(s2) and s2[r] not in countS1:
                r+=1
            if r <len(s2):
                l=r
                while r <len(s2) and s2[r] in countS1:
                    countS2[s2[r]]=1+ countS2.get(s2[r], 0)
                    while countS2[s2[r]]>countS1[s2[r]]:
                        countS2[s2[l]]-=1
                        l+=1
                    if countS1==countS2:
                        return True
                    r+=1
                l=r
                countS2={}

        return False





    

def main():
    sol = Solution()
    node6 = ListNode(5, None)
    node5 = ListNode(4, node6)
    node4 = ListNode(8, node5)
    node3 = ListNode(1, node4)
    node2 = ListNode(6, node3)
    node1 = ListNode(5, node2)
    node22 = ListNode(1, node4)
    node21 = ListNode(4, node22)
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    gas = [5, 1, 2, 3, 4]
    cost = [4, 4, 1, 5, 1]
    nums =[3,1,2]
    matrix =[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    piles =[3,6,7,11]
    s1="adc"
    s2 = "dcda"
    print(sol.checkInclusion(s1,s2))


if __name__ == '__main__':
    main()
