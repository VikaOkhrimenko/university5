from collections import deque
from typing import List


# 1. Перший унікальний символ у рядку
def first_uniq_char(s: str) -> int:
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - 97] += 1
    for i, ch in enumerate(s):
        if freq[ord(ch) - 97] == 1:
            return i
    return -1


# 2. Реалізація стека за допомогою черг
class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


# 3. Кількість останніх викликів
class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        limit = t - 3000
        while self.q and self.q[0] < limit:
            self.q.popleft()
        return len(self.q)


# 3. Дизайн замкнутої двубічної черги (Deque)
class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.buf = [0] * k
        self.front = 0
        self.rear = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.k
        self.buf[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.buf[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.buf[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.buf[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# 4. Дизайн замкнутої черги
class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.buf = [0] * k
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.buf[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.buf[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.buf[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# 5. Штампування послідовності
def moves_to_stamp(stamp: str, target: str) -> List[int]:
    m, n = len(stamp), len(target)
    t = list(target)
    done = [False] * n
    res = []
    stars = 0

    def can_stamp(i: int) -> bool:
        changed = False
        for j in range(m):
            if i + j >= n:
                return False
            if done[i + j]:
                continue
            if t[i + j] != stamp[j]:
                return False
            changed = True
        return changed

    def do_stamp(i: int) -> int:
        cnt = 0
        for j in range(m):
            if not done[i + j]:
                done[i + j] = True
                t[i + j] = '?'
                cnt += 1
        return cnt

    changed = True
    while stars < n and changed:
        changed = False
        for i in range(n - m + 1):
            if can_stamp(i):
                gained = do_stamp(i)
                if gained > 0:
                    res.append(i)
                    stars += gained
                    changed = True

    if stars != n:
        return []
    return res[::-1]


# 6. Максимум плаваючого вікна
def max_sliding_window(nums: List[int], k: int) -> List[int]:
    dq = deque()
    ans = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            ans.append(nums[dq[0]])
    return ans


# 7. Обмежена сума підпослідовності
def constrained_subset_sum(nums: List[int], k: int) -> int:
    dq = deque()
    best = nums[0]
    for i, x in enumerate(nums):
        if dq:
            x = x + dq[0][0]
        cur = x
        best = max(best, cur)
        while dq and dq[-1][0] < cur:
            dq.pop()
        if cur > 0:
            dq.append((cur, i))
        while dq and dq[0][1] <= i - k:
            dq.popleft()
    return best
