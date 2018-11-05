"""
实现一个堆栈，它包括两个方法，一个是入栈一个是出栈。
"""


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  # 栈大小
        self._internal = [0 for x in range(capacity)]  # 栈容器
        self.top = 0  # 栈顶标志

    def push(self, x):
        """
        压栈
        """
        if self.top + 1 > self.capacity:
            raise Exception('栈溢出')
        else:
            self._internal[self.top] = x
            self.top += 1
        print(self._internal)

    def pop(self):
        """
        出栈
        栈空返回None.
        """
        if self.top <= 0:
            return None
        else:
            self.top -= 1
            return self._internal[self.top]


st = Stack(3)
print(st.pop())
st.push(1)
st.push(2)
st.push(3)
print(st.pop())
print(st.pop())
st.push(5)

