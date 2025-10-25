# 一、异常（Exceptions）：程序的 “小故障”
# 1. 什么是异常？
# 异常是 Python 程序运行时遇到的错误（不是语法错误），会导致程序 “崩溃” 停止。比如用字符串除以数字、访问列表不存在的位置，都会触发异常。
from terraria_tools import calc_damage


# 2. 初学者必知的 5 种常见异常
# 异常类型	        发生场景示例	                                            通俗理解
# TypeError	        1 + "苹果"（数字和字符串相加）	                            “类型不匹配” 错误
# ValueError	    int("abc")（把字母转成整数）	                            “值不符合要求” 错误
# IndexError	    list1 = [1,2]; list1[5]（访问不存在的索引）	                “列表越界” 错误
# KeyError	        dict1 = {"name":"小明"}; dict1["age"]（访问不存在的字典键）	“键找不到” 错误
# ZeroDivisionError	10 / 0（除以零）	“除以零” 错误

# 二、异常处理：让程序 “容错” 不崩溃
# 异常处理的核心是用 try-except 语句 “捕获” 异常，让程序遇到错误时不崩溃，而是执行预设的处理逻辑。
# 1. 最基础的异常处理：try + except
# 语法结构（先写 “可能出错的代码”，再写 “出错后的处理”）：
# try:
#     # 第一步：尝试执行的代码（这里可能会触发异常）
#     可能出错的代码
# except 具体异常类型:
#     # 第二步：如果触发了指定的异常，就执行这里的代码
#     出错后的处理代码
# 示例：处理 “输入非数字” 的错误
# try:
#     # 尝试让用户输入数字并转成整数
#     num = int(input("请输入一个数字："))
#     print(f"你输入的数字是：{num}")
# except ValueError:
#     # 如果用户输入的是字母（比如“abc”），就执行这里
#     print("出错啦！请输入纯数字，不要输字母或符号~")

# 2. 处理多个异常：两种写法
# 如果一段代码可能触发多种异常，可以分情况处理：
# 写法 1：多个 except 分别处理不同异常
# try:
#     num = int(input("请输入数字："))
#     result = 10 / num  # 可能触发ZeroDivisionError
#     print(f"10除以{num}的结果是：{result}")
# except ValueError:
#     print("请输入纯数字！")
# except ZeroDivisionError:
#     print("不能除以零哦！")
# 写法 2：一个 except 处理多个异常（用括号括起来）
# try:
#     num = int(input("请输入数字："))
#     result = 10 / num
#     print(f"结果：{result}")
# except (ValueError, ZeroDivisionError):
#     # 只要触发这两种异常中的一种，就执行这里
#     print("输入错误！请输入非零的纯数字~")

# 3. 可选补充：else + finally
# else：只有没触发任何异常时，才会执行（可选）
# finally：无论有没有异常，都会执行（常用于 “清理工作”，比如关闭文件，可选）
# 示例：完整的异常处理结构
# try:
#     num = int(input("请输入数字："))
#     result = 10 / num
# except (ValueError, ZeroDivisionError):
#     print("输入错误！")
# else:
#     # 没出错时执行：打印结果
#     print(f"计算成功！结果是：{result}")
# finally:
#     # 无论对错都执行：提示程序结束
#     print("本次计算流程结束啦~")

# 4. 主动抛出异常：raise（了解即可）
# 有时需要 “主动让程序报错”（比如检查参数是否合法），用 raise 语句：
# def check_age(age):
#     if age < 0:
#         # 主动抛出“值错误”，并自定义错误提示
#         raise ValueError("年龄不能是负数哦！")
#     print(f"年龄是：{age}")
#
# # 调用函数，触发异常后捕获
# try:
#     check_age(-5)  # 传入负数，触发异常
# except ValueError as e:
#     print(f"出错提示：{e}")  # 输出：出错提示：年龄不能是负数哦！

# 三、模块（Modules）：代码的 “工具箱”
# 模块是一个后缀为 .py 的 Python 文件，里面可以写函数、类、变量，相当于一个 “工具箱”，方便代码复用（不用重复写相同功能）。
# 1. 为什么要用模块？
# 比如你写了一个 “计算加法、乘法” 的功能，存成模块后，下次其他项目需要用，直接 “导入” 模块即可，不用重新写代码。
# 2. 导入模块的 3 种常用方式（重点）
# 假设我们有一个模块文件 calc.py（自己创建，内容如下）：
# calc.py（这是一个模块）
# def add(a, b):
#     """加法函数"""
#     return a + b
#
# def multiply(a, b):
#     """乘法函数"""
#     return a * b
#
# PI = 3.1415  # 变量：圆周率
# 下面在另一个文件（比如 main.py）中导入并使用这个模块
# 导入方式	        语法示例	                                使用示例	                    特点
# 导入整个模块	    import 模块名	                        import calc	                使用时要加 “模块名.xxx”，避免冲突
# 导入模块中的指定内容	from 模块名 import 函数/变量1, 函数/变量2	from calc import add, PI	直接用函数 / 变量名，不用加模块名
# 导入模块并起 “别名”	import 模块名 as 别名	                    import calc as c	        模块名太长时，用别名更方便
# 实操示例：
# # main.py（主文件）
# # 方式1：导入整个模块
# import calc
# print(calc.add(2, 3))  # 输出5（必须加“calc.”）
# print(calc.PI)         # 输出3.1415
#
# import terraria_tools
# print(terraria_tools.calc_damage(40,1.5))
# print(terraria_tools.MAX_HEALTH)

# # 方式2：导入指定内容
# from calc import multiply, PI
# print(multiply(4, 5))  # 输出20（直接用函数名）
# print(PI)              # 输出3.1415
#
# from terraria_tools import calc_damage, drop_chance ,MAX_HEALTH
# print(calc_damage(40,1.5))
# print(drop_chance(123,5))
# print(MAX_HEALTH)
# # 方式3：导入模块并起别名
# import calc as c
# print(c.add(10, 20))   # 输出30（用别名“c.”代替“calc.”）
# import terraria_tools as tt
# print(tt.drop_chance(45,45))
# 四、包（Packages）：模块的 “收纳盒”
# 当模块很多时，需要用 “包” 来分类管理 —— 包是一个包含多个模块的文件夹，相当于 “收纳盒”，把相关的模块放在一起。
# 1. 包的基础结构（必须掌握）
# 一个标准的包目录结构如下（文件夹和文件需要自己创建）：
# my_package/          # 包的根目录（包名：my_package）
# ├── __init__.py      # 包的“初始化文件”（必须有，哪怕是空文件，否则不算Python包）
# ├── math_tools.py    # 模块1：放数学相关函数
# ├── string_tools.py  # 模块2：放字符串相关函数
# └── sub_package/     # 子包（包里面可以再放包）
#     ├── __init__.py  # 子包的初始化文件
#     └── time_tools.py# 子包的模块：放时间相关函数

# 2. 导入包中模块的 2 种方式
# 以 “导入 math_tools.py 中的 add 函数” 和 “导入子包的 time_tools.py” 为例：
# 方式 1：绝对导入（推荐，从包的根目录开始写路径）
# # 1. 导入包中模块的指定函数
# from my_package.math_tools import add
# print(add(3, 4))  # 输出7
#
# from terraria_package.weapon_tools import calc_weapon_damage
# print(calc_weapon_damage(45,80))
# # 2. 导入包中的整个模块
# from my_package import string_tools
# print(string_tools.upper("hello"))  # 假设string_tools有upper函数，输出HELLO
#
# from terraria_package import weapon_tools
# print(weapon_tools.calc_weapon_damage(7,5))
# # 3. 导入子包中的模块
# from my_package.sub_package import time_tools
# time_tools.show_current_time()  # 调用子包模块的函数
# from terraria_package.world_tools import biome_tools
# biome_tools.spawn_boss("克苏鲁之眼")
# 方式 2：相对导入（仅在包内部使用，用 “.” 表示路径）
# 只有在 “包内部的模块” 中，才能用相对导入（比如在 string_tools.py 中导入 math_tools.py）：
# # 在 my_package/string_tools.py 中
# from . import math_tools  # “.”表示当前目录（即my_package目录）
# print(math_tools.add(5, 6))  # 输出11

# 3. __init__.py 的作用（简单了解）
# 核心作用：告诉 Python “这个文件夹是一个包”，没有它就不算包
# 可选作用：可以在里面写初始化代码，比如自动导入包中的常用模块：
# # my_package/__init__.py
# # 让用户导入my_package时，自动导入math_tools模块
# from . import math_tools
# 之后在外部使用时，可以直接：
# import my_package
# print(my_package.math_tools.add(7, 8))  # 输出15（不用单独导入math_tools）

# 初学者常见问题 & 注意事项
# 异常处理不要 “万能捕获”：尽量不要用 except: 捕获所有异常（会隐藏未知错误），最好指定具体异常类型（如 except ValueError:）。
# 模块导入路径问题：如果导入模块时提示 “ModuleNotFoundError”，检查两个点：
# 模块文件和主文件是否在同一文件夹
# 如果模块在其他文件夹，需要先把文件夹路径加入 Python 的搜索路径（初学者暂时不用深入，先保证文件在同一目录）。
# 包的命名规范：包名和模块名尽量用 “小写字母 + 下划线”（如 my_package、math_tools.py），不要用大写或特殊符号。