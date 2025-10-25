# 一、递归（Recursion）
# 1.递归是指函数直接或间接调用自身的编程技巧，常用于解决可分解为相似子问题的任务（如数学计算、树结构遍历等）。
# 2.核心要素：
# 终止条件：避免无限递归导致栈溢出。
# 递归步骤：将问题分解为规模更小的子问题。
# 3.示例：计算阶乘阶乘定义：n! = n × (n-1) × ... × 1，且0! = 1
# def factorial(n):
#     # 终止条件：n=0时返回1
#     if n == 0:
#         return 1
#     # 递归步骤：n! = n × (n-1)!
#     return n * factorial(n - 1)
#
# print(factorial(1))  # 输出：120（5×4×3×2×1）
# 4.注意：Python 默认递归深度有限（约 1000），过深的递归会抛出RecursionError。

# 二、闭包（Closure）
# 1.闭包是指嵌套函数引用了外层函数的变量，且外层函数返回内层函数的结构。它可以保留外层函数的状态（即使外层函数已执行完毕）。
# 2.核心要素：
# 存在嵌套函数（内函数嵌套在外函数中）
# 内函数引用外函数的变量
# 外函数返回内函数
# 3.示例：实现计数器通过闭包保留计数状态，每次调用计数器时自动累加：
# def outer():
#     count = 0  # 外函数的变量（被内函数引用）
#
#     def inner():
#         nonlocal count  # 声明引用外层变量（非全局）
#         count += 1
#         return count
#     # print(id(inner))
#
#     return inner  # 返回内函数
#
#
# # 创建计数器实例
# counter = outer() # 此处相当于counter == inner 它们两者的内存地址相同，可以使用id函数检测。
# # print(id(counter))
# print(counter())  # 输出：1
# print(counter())  # 输出：2
# print(counter())  # 输出：3
# 应用场景：实现私有变量、延迟计算、装饰器基础等。

# 三、装饰器（Decorator）
# 1.装饰器是一种特殊的闭包，用于在不修改原函数代码的前提下，为函数添加额外功能（如日志、计时、权限校验等）。
# 2.语法：使用@装饰器名放在函数定义上方（语法糖）。
# 3.示例：为函数添加执行日志装饰器会在函数执行前后打印日志：
# 定义装饰器（本质是接受函数为参数的闭包）
# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         # 函数执行前的操作
#         print(f"开始执行函数：{func.__name__}")
#         # 执行原函数并获取结果
#         result = func(*args, **kwargs)
#         # 函数执行后的操作
#         print(f"函数{func.__name__}执行完毕")
#         return result  # 返回原函数结果
#     return wrapper
#
# # 使用装饰器（等价于：add = log_decorator(add)）
# @log_decorator
# def add(a, b):
#     return a + b
#
# print(add(2, 3))  # 输出：
# # 开始执行函数：add
# # 函数add执行完毕
# # 5
# 4.进阶：装饰器可以带参数（需额外一层嵌套），例如控制日志级别。

# 三者关系与应用
# 递归：通过自调用解决分治问题（如斐波那契、快速排序）
# 闭包：保留状态的嵌套函数，是装饰器的基础
# 装饰器：基于闭包实现的函数增强工具，广泛用于框架（如 Django、Flask 的路由装饰器）
# 理解这三个概念有助于编写更简洁、灵活的 Python 代码，尤其是在函数式编程和框架开发中。

# 四、__name__
# 1、在 Python 中，__name__ 是一个内置变量。
# 它的作用是标识当前模块（简单理解为 .py 文件）的 “运行状态”—— 即这个模块是 “被直接运行” 的，还是 “被其他模块导入” 的。
# 对于初学者来说，掌握 __name__ 的核心用法，能帮你写出更规范、可复用的代码。
# 2、__name__ 的两种取值
# __name__ 的值会根据模块的运行方式自动变化，只有两种可能：
# 当模块被直接运行时：__name__ 的值为字符串 "__main__"。（“直接运行” 指的是你在终端用 python 文件名.py 执行，或在 IDE 中直接运行这个文件）
# 当模块被其他模块导入时：__name__ 的值为模块的文件名（不含 .py 后缀）。（“导入” 指的是用 import 文件名 把这个文件作为工具模块使用）
# 3.通过例子理解
# 为了更直观，我们用两个文件演示：
# 示例 1：创建一个模块 test.py:
# # test.py
# print("我是 test.py 里的代码")
# print("当前模块的 __name__ 是：", __name__)
# 情况 1：直接运行 test.py
# 在终端执行 python test.py，输出：
# 我是 test.py 里的代码
# 当前模块的 __name__ 是： __main__
# 情况 2：在另一个文件中导入 test.py
# 再创建一个 main.py，内容如下：
# # main.py
# import test  # 导入 test.py 模块
# 运行 main.py（python main.py），输出：
# 我是 test.py 里的代码
# 当前模块的 __name__ 是： test
# → 因为 test.py 是被 main.py 导入的，所以 test.py 中的 __name__ 变成了模块名 test（即文件名）。
# 4.__name__ 的核心用途：程序入口判断
# __name__ 最常用的场景是：让模块中的部分代码 “只在直接运行时执行，被导入时不执行”。
# 比如，你写了一个工具模块（比如 calculator.py，包含加法、减法函数），既想让它能被其他程序导入使用，
# 又想在直接运行它时执行一些测试代码（比如测试加法是否正确）。这时候就可以用 __name__ 来实现。
# 示例：带测试代码的工具模块
# 创建 calculator.py：
# # calculator.py
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# # 测试代码：只在直接运行时执行
# if __name__ == "__main__":
#     # 当 calculator.py 被直接运行时，会执行以下代码
#     print("测试加法：", add(2, 3))  # 输出 5
#     print("测试减法：", subtract(5, 2))  # 输出 3
# 情况 1：直接运行 calculator.py
# 执行 python calculator.py，输出：
# 测试加法： 5
# 测试减法： 3
# 情况 2：在其他文件中导入 calculator.py
# 创建 use_calculator.py：
# # use_calculator.py
# from calculator import add
#
# print("使用加法函数：", add(10, 20))  # 输出 30
# 运行 use_calculator.py，输出：
# 使用加法函数： 30
# → 此时 calculator.py 是被导入的，它的 __name__ 是 calculator，所以
# if __name__ == "__main__": 条件不成立，测试代码不会执行（避免干扰导入者/）。
# 总结
# __name__ 是 Python 内置变量，标识模块的运行状态。
# 直接运行模块时，__name__ == "__main__"。
# 模块被导入时，__name__ == 模块文件名（不含 .py）。
# 核心用法：用 if __name__ == "__main__": 包裹 “仅在直接运行时执行的代码”（如测试代码），让模块既可以被导入复用，又能独立运行测试。
# 这个技巧在实际开发中非常常用，比如写工具库、框架插件时，都会用它来区分 “运行模式” 和 “导入模式”。