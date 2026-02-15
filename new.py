from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


# 1 Валідні дужки
def is_valid(s: str) -> bool:
    stack = []
    mp = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in mp:
            if not stack or stack.pop() != mp[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


# 2 Обхід бінарного дерева в порядку (Inorder Traversal)
def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res


# 3 Мінімальний стек
class MinStack:
    def __init__(self):
        self.st = []
        self.mn = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.mn:
            self.mn.append(val)
        else:
            self.mn.append(val if val < self.mn[-1] else self.mn[-1])

    def pop(self) -> None:
        self.st.pop()
        self.mn.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mn[-1]


# 4 Реалізуйте чергу використовуючи стеки
class MyQueue:
    def __init__(self):
        self.in_st = []
        self.out_st = []

    def push(self, x: int) -> None:
        self.in_st.append(x)

    def _shift(self) -> None:
        if not self.out_st:
            while self.in_st:
                self.out_st.append(self.in_st.pop())

    def pop(self) -> int:
        self._shift()
        return self.out_st.pop()

    def peek(self) -> int:
        self._shift()
        return self.out_st[-1]

    def empty(self) -> bool:
        return not self.in_st and not self.out_st


# 5 Декодувати рядок
def decode_string(s: str) -> str:
    count_stack = []
    str_stack = []
    cur = []
    k = 0
    for ch in s:
        if ch.isdigit():
            k = k * 10 + (ord(ch) - 48)
        elif ch == '[':
            count_stack.append(k)
            str_stack.append(cur)
            cur = []
            k = 0
        elif ch == ']':
            repeat = count_stack.pop()
            prev = str_stack.pop()
            cur = prev + cur * repeat
        else:
            cur.append(ch)
    return ''.join(cur)


# 6 Оцініть зворотну польську нотацію
def eval_rpn(tokens: List[str]) -> int:
    st = []
    for t in tokens:
        if t in {"+", "-", "*", "/"}:
            b = st.pop()
            a = st.pop()
            if t == "+":
                st.append(a + b)
            elif t == "-":
                st.append(a - b)
            elif t == "*":
                st.append(a * b)
            else:
                st.append(int(a / b))
        else:
            st.append(int(t))
    return st[-1]


# 7 Найдовші дійсні дужки
def longest_valid_parentheses(s: str) -> int:
    stack = [-1]
    best = 0
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                best = max(best, i - stack[-1])
    return best
