# calculator.py
from symbol import return_stmt


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 测试代码：只在直接运行时执行
if __name__ == "__main__":
    # 当 calculator.py 被直接运行时，会执行以下代码
    print("测试加法：", add(2, 3))  # 输出 5
    print("测试减法：", subtract(5, 2))  # 输出 3