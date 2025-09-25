# 一、作用域
# 1作用域
# 1.1含义：变量生效作用的范围，包含全局变量和局部变量两种。
# 1.2全局变量：函数外部定义的变量，在整个文件中都是有效的。
# a = 100 #全局变量
# def test1():
#     a = 120 #局部变量
#     print(a)
# def test2():
#     a = 130 #局部变量
#     print(a)
# print(a)  #100
# test1()   #120
# test2()   #130
# print(a)  #100
# 函数局部变量和全局变量的名称虽然相同，但是ID地址不同，不是一个变量。
# 如果函数内部需要使用变量，会先从函数内部找，有的话直接使用，没有的话会到函数外部找。
# 1.3局部变量：函数内部定义的变量，在函数的定义范围内生效，在函数外部没有定义无法使用。
# 作用：在函数体内部临时保存数据，当函数调用结束后，就销毁局部变量。
# def test3():
#     a = 130 #局部变量
#     print(a)
# test3()   #120
# 1.4声明全局变量global关键字
# 作用：将变量声明为全局变量，可以对全局变量进行修改，也可以在局部作用域声明一个全局变量。
# 格式：global 变量名1,变量名2....
# a = 100
# def test4():
#     global a #这里的a声明为全局变量
#     a = 50   #全局变量被修改,id地址发生变化
#     print(a,id(a))
# print(a,id(a))
# test4()
# print(a,id(a))
# 1.5nonlocal
# 作用：用来声明外层的局部变量，只能在嵌套函数中使用，在外部函数先进行声明，内部函数进行nonlocal声明。
# nonlocal只能上一级进行修改
# def a1():
#     a = 1
#     print("第一层", a)
#     def a2():
#         nonlocal a #用来声明外层的局部变量a
#         a = 2
#         print("第二层", a)
#         def a3():
#             nonlocal a
#             a = 3
#             print("第三层", a)
#         a3()
#     a2()
#     print("第一层", a)
# a1()

# 二、匿名函数
# 2.1匿名函数
# 基本语法： 函数名 = lambda 形参 : 返回值（表达式）
# 调用：结果 = 函数名(实参)
# add = lambda a,b : a+b
# print(add(1,2))
# lambda不需要写return来返回值，表达式本身结果就是返回。
# 2.2lambda的参数形式
# 2.2.1无参数格式：
# funa = lambda : "写"
# print(funa())
# 2.2.2一个参数
# funb = lambda a : a
# print(funb("车"))
# 2.2.3默认参数
# 默认参数必须写在非默认参数后面
# func = lambda a,b=12 : (a,b)
# print(func("牛"))
# fund = lambda a,b,c=13 : a+b+c
# print(fund(1,2))
# 2.2.4关键字函数
# fune = lambda **kwargs : kwargs
# print(fune(a=1,b="有吗"))
# 2.3lambda的应用：结合if判断
# 三目运算：为真结果 if 条件 else 为假结果
# lambda只能够实现简单的逻辑，如果逻辑复杂代码量大，不建议使用lambda，降低代码的可读性，为维护增加困难。
# a = 3
# b = 2
# print("a大于b") if a > b else print("a小于等于b")
# comp = lambda a, b: "a大于b" if a > b else "a小于等于b"
# print(comp(4,5 ))

# 三、内置函数
# 3.1查看所有内置函数
# import builtins
# print(dir(builtins))
# 大写字母开头一般是内置常量名称，小写字母开头一般是内置函数名称。
# 3.2内置函数1
# 3.2.1 abs()返回绝对值
# print(abs(-10))
# 3.2.2 sum()求和 #整型不是可迭代对象，sum函数的变量是可迭代对象，只能用来数字求和。
# print(sum(1,2))     #整型不是可迭代对象
# print(sum("1","2")) #字符串不能进行相加操作
# print(sum({"a" : 1, "b" : 2, "c" : 3})) #字典不能进行相加。
# print(sum((1,2,2.2))) #参数只要有一个浮点数，输出就是浮点数。
# 3.3内置函数2
# 3.3.1 min()最小值
# 3.3.2 max()最大值
# print(min(1,2,2,-8,key=abs)) #传入key参数变量为abs，先取绝对值，再取最小值，
# 3.3.3 zip()将可迭代对象作为参数，将对象中的参数打包成一个元组
# li1 = [1,2,3]
# li2 = [4,5,6]
# print(zip(li1,li2)) #返回一个对象
#第一种方式：通过for循环
# for i in zip(li1,li2):
#     print(i)
    #如果li1和li2的长度不一致，就按照最短的返回。
#第二种方式：通过转化为列表打印
# print(list(zip(li1,li2)))
#注意：这种情况下必须是可迭代对象
# 3.3.4 map()映射函数
# map(func,iter1)
# func自己定义的函数，iter1要放进去的可迭代对象。
# li = [1,2,3,4,5]
# def funa(x):
    # return x*3
# a = map(funa,li) #返回一个对象
#第一种方式：通过for循环
# for i in a:
#     print(i)
#第二种方式：通过转化为列表打印
# print(list(a)) #[3, 6, 9, 12, 15]
# print(list(a)) #map遍历一次之后被销毁，这里输出空列表
# 3.3.5 reduce()先把对象中的两个元素取出，计算出一个值，然后讲这个值和第三个元素进行计算。
# from functools import reduce
# # reduce(function, sequence)function一个函数：必须是有两个参数的函数 sequence：序列：可迭代对象
# li = [1,2,3,4,5]
# def gtlt1(x,y):
#     return x*y
# def sum1(x,y):
#     return x+y
# res1 = reduce(gtlt1, li)
# res2 = reduce(sum1, li)
# print(res1) #120
# print(res2) #15

# 四、拆包
# 4.1定义：对于函数中的多个返回数据，去掉元组、列表或者字典，直接获取里面的数据的过程。
# tua = (1, 2, 3, 4, 5)
# print(tua)       #(1, 2, 3, 4, 5)
# #方法一：要求元组内的个数与接收的变量个数相同，对象内有多少数据就定义多少个变量
# #一般在获取元组值的时候使用。
# a,b,c,d,e = tua
# print(a,b,c,d,e) #1 2 3 4 5
#方法二：一般在函数调用的时候使用。
# a, *b = tua
# print(a,b)       #1 [2, 3, 4, 5]
# c, *d = b
# print(c,d)       #2 [3, 4, 5] 一步一步的解包，先把单独的取完，其他剩下的全部交给带*的变量

# def funa(a, b, *args):
#     print(a, b, args)
# funa(1, 2, 3, 4, 5) #1 2 (3, 4, 5)

# ##############################################
# Python课程知识点总结（含补充内容）
# 涵盖：作用域、匿名函数、内置函数、拆包
# ##############################################


# ##############################################
# 一、作用域（补充：变量查找LEGB规则）
# ##############################################
"""
1. 核心概念：变量生效的范围，决定变量的可访问性
2. 变量查找规则（LEGB规则）：优先从内层作用域向外层查找
   - Local（局部）：函数/类内部定义的变量
   - Enclosing（嵌套外层）：嵌套函数中外层函数的局部变量
   - Global（全局）：文件级别的变量
   - Built-in（内置）：Python自带的变量/函数（如print、len）
3. 四种变量类型及操作：
"""

# 3.1 全局变量（Global）
# 定义：文件内、函数外声明的变量，整个文件可访问（函数内只读，修改需用global）
global_player_health = 100  # 全局变量：泰拉瑞亚玩家初始生命值


def check_global_health():
    # 函数内只读全局变量（不修改时无需声明）
    print("全局玩家生命值：", global_player_health)


check_global_health()  # 输出：全局玩家生命值：100
print("全局玩家生命值（外部）：", global_player_health)  # 输出：100


# 3.2 局部变量（Local）
# 定义：函数/类内部声明的变量，仅在内部生效，函数调用结束后销毁
def get_local_item():
    local_item = "铜剑"  # 局部变量：泰拉瑞亚铜剑（仅函数内可用）
    print("局部物品：", local_item)


get_local_item()  # 输出：局部物品：铜剑


# print(local_item)  # 报错：NameError（外部无法访问局部变量）


# 3.3 修改全局变量（global关键字）
# 作用：在函数内声明变量为全局变量，实现对全局变量的修改
def heal_global_player(heal_amount):
    global global_player_health  # 声明：使用全局变量global_player_health
    global_player_health += heal_amount  # 修改全局变量
    print("治疗后全局生命值：", global_player_health)


heal_global_player(50)  # 输出：治疗后全局生命值：150
print("修改后全局生命值（外部）：", global_player_health)  # 输出：150


# 3.4 修改嵌套外层变量（nonlocal关键字）
# 作用：仅在嵌套函数中使用，修改外层函数（Enclosing）的局部变量（不能修改全局）
def npc_shop():
    shop_gold = 100  # 外层函数局部变量：NPC商店金币

    def sell_item(item_price):
        nonlocal shop_gold  # 声明：使用外层函数的shop_gold
        shop_gold += item_price  # 修改外层局部变量
        print("卖出物品后商店金币：", shop_gold)

    sell_item(30)  # 调用内层函数
    print("外层函数查看商店金币：", shop_gold)  # 输出：130（已被修改）


npc_shop()

# ##############################################
# 二、匿名函数（补充：结合filter函数的应用）
# ##############################################
"""
1. 核心概念：用lambda关键字定义的"一次性"函数，无函数名，语法简洁
2. 语法规则：
   - 基础格式：函数名 = lambda 形参列表 : 表达式（表达式结果即返回值，无需return）
   - 特点：仅能实现简单逻辑（1行表达式），复杂逻辑需用def定义普通函数
3. 常见用法：
   - 单独使用：处理简单计算/判断
   - 结合高阶函数：与map()、filter()等配合使用（高频场景）
"""

# 3.1 匿名函数的参数形式
# （1）无参数：无输入，直接返回固定值
get_default_biome = lambda: "森林"  # 泰拉瑞亚默认出生地形
print("默认地形：", get_default_biome())  # 输出：森林

# （2）单个参数：接收1个输入并处理
calc_damage = lambda weapon_atk: weapon_atk * 1.2  # 武器攻击力计算（加成20%）
print("铁剑实际攻击力：", calc_damage(40))  # 输出：48.0

# （3）默认参数：参数有默认值，调用时可省略
create_potion = lambda name, duration=60: f"{name}（持续{duration}秒）"  # 泰拉瑞亚药水
print("默认生命药水：", create_potion("生命药水"))  # 输出：生命药水（持续60秒）
print("长效生命药水：", create_potion("生命药水", 120))  # 输出：生命药水（持续120秒）

# （4）关键字参数（**kwargs）：接收任意关键字参数，返回字典
get_npc_info = lambda **kwargs: kwargs  # 获取NPC信息
print("向导NPC信息：", get_npc_info(name="向导", role="新手指导", hp=200))  # 输出：字典

# 3.2 匿名函数结合条件判断（三目运算）
# 语法：lambda 形参 : 结果1 if 条件 else 结果2
judge_boss_defeat = lambda boss_hp: "BOSS已击败" if boss_hp <= 0 else "BOSS仍存活"
print("克苏鲁之眼状态：", judge_boss_defeat(0))  # 输出：BOSS已击败
print("史莱姆王状态：", judge_boss_defeat(500))  # 输出：BOSS仍存活

# 3.3 匿名函数结合filter（补充：过滤数据）
# filter(筛选函数, 可迭代对象)：保留使筛选函数返回True的元素
# 需求：筛选出泰拉瑞亚中攻击力>50的武器
weapons = [("铜剑", 25), ("铁剑", 40), ("金剑", 55), ("神圣剑", 80)]
high_atk_weapons = list(filter(lambda x: x[1] > 50, weapons))  # x是元组(武器名, 攻击力)
print("高攻击力武器：", high_atk_weapons)  # 输出：[('金剑', 55), ('神圣剑', 80)]

# ##############################################
# 三、内置函数（补充：filter、enumerate）
# ##############################################
"""
1. 核心概念：Python自带的无需导入即可使用的函数（部分需导入，如reduce）
2. 常用内置函数及用法（结合泰拉瑞亚场景）：
"""

# 3.1 基础数值函数
# abs(x)：返回x的绝对值（如计算玩家与NPC的距离差）
player_x = 150
npc_x = 120
distance_x = abs(player_x - npc_x)
print("玩家与NPC的水平距离：", distance_x)  # 输出：30

# sum(可迭代对象)：计算可迭代对象中所有数字的和（如计算背包矿石总价值）
ore_values = [5, 10, 20, 50]  # 铜、铁、金、神圣矿石的单个价值
total_value = sum(ore_values)
print("矿石总价值：", total_value)  # 输出：85

# min/max(可迭代对象, key=函数)：获取最小/最大值（key指定排序依据）
# 需求：找出泰拉瑞亚中生命值最低的NPC
npcs = [("向导", 200), ("商人", 150), ("护士", 180)]
min_hp_npc = min(npcs, key=lambda x: x[1])  # key=生命值
max_hp_npc = max(npcs, key=lambda x: x[1])
print("生命值最低的NPC：", min_hp_npc)  # 输出：('商人', 150)
print("生命值最高的NPC：", max_hp_npc)  # 输出：('向导', 200)

# 3.2 迭代相关函数
# zip(可迭代对象1, 可迭代对象2, ...)：将多个可迭代对象打包为元组（按最短长度）
# 需求：配对武器与对应的攻击力
weapon_names = ["铜剑", "铁剑", "金剑"]
weapon_atks = [25, 40, 55]
weapon_pairs = list(zip(weapon_names, weapon_atks))
print("武器-攻击力配对：", weapon_pairs)  # 输出：[('铜剑',25), ('铁剑',40), ('金剑',55)]

# map(处理函数, 可迭代对象)：对可迭代对象中每个元素应用处理函数（返回新对象）
# 需求：计算所有武器加10攻击力后的结果
new_atks = list(map(lambda x: x + 10, weapon_atks))
print("加成后攻击力：", new_atks)  # 输出：[35, 50, 65]

# filter(筛选函数, 可迭代对象)：保留符合条件的元素（见匿名函数3.3）
# 需求：筛选出价值>10的矿石
ores = [("铜矿", 5), ("铁矿", 10), ("金矿", 20)]
valuable_ores = list(filter(lambda x: x[1] > 10, ores))
print("高价值矿石：", valuable_ores)  # 输出：[('金矿', 20)]

# enumerate(可迭代对象, start=0)：枚举元素，返回(索引, 元素)（方便遍历带索引）
# 需求：枚举泰拉瑞亚生物群落（带序号）
biomes = ["森林", "腐化地", "血腥地", "沙漠"]
for idx, biome in enumerate(biomes, start=1):  # start=1：索引从1开始
    print(f"生物群落{idx}：{biome}")  # 输出：1:森林, 2:腐化地...

# 3.3 累积计算函数（需导入）
# reduce(累积函数, 可迭代对象)：从左到右累积计算（先算前2个，结果与第3个算，依此类推）
from functools import reduce

# 需求：计算3瓶药水的总持续时间
potion_durations = [60, 120, 180]  # 3瓶药水的持续时间（秒）
total_duration = reduce(lambda x, y: x + y, potion_durations)
print("药水总持续时间：", total_duration)  # 输出：360

# ##############################################
# 四、拆包（补充：字典拆包**）
# ##############################################
"""
1. 核心概念：将可迭代对象（元组、列表、字典等）中的元素直接提取到变量中，简化赋值
2. 常见拆包场景：
"""

# 4.1 序列拆包（元组/列表，用*接收剩余元素）
# 场景1：变量数与元素数完全一致（精确拆包）
player_pos = (300, 200)  # 泰拉瑞亚玩家坐标(x, y)
x, y = player_pos  # 拆包坐标
print(f"玩家X坐标：{x}, Y坐标：{y}")  # 输出：300, 200

# 场景2：用*接收剩余元素（可变长度拆包）
backpack = ["铜剑", "生命药水", "铜矿", "铁矿"]  # 玩家背包
main_item, *other_items = backpack  # 第一个元素给main_item，剩余给other_items（列表）
print("主物品：", main_item)  # 输出：铜剑
print("其他物品：", other_items)  # 输出：['生命药水', '铜矿', '铁矿']


# 场景3：函数参数拆包（*args接收可变位置参数）
def show_backpack(main, *others):
    print("主物品：", main)
    print("其他物品：", others)  # others是元组


show_backpack(*backpack)  # 拆包列表，传入函数（等价于show_backpack("铜剑", "生命药水", ...)）


# 4.2 字典拆包（补充：用**接收关键字参数）
# 场景1：拆包字典键值对（**用于函数参数）
def create_weapon(name, atk, durability):
    print(f"武器创建：{name}（攻击力：{atk}，耐久：{durability}）")


weapon_attrs = {"name": "金剑", "atk": 55, "durability": 200}  # 武器属性字典
create_weapon(**weapon_attrs)  # 拆包字典，等价于create_weapon(name="金剑", atk=55, ...)

# 场景2：提取字典键/值（基础拆包）
weapon_names = weapon_attrs.keys()  # 提取键
weapon_values = weapon_attrs.values()  # 提取值
print("武器属性名：", list(weapon_names))  # 输出：['name', 'atk', 'durability']
print("武器属性值：", list(weapon_values))  # 输出：['金剑', 55, 200]

# ##############################################
# 结合泰拉瑞亚的知识点测试题（请在下方作答）
# ##############################################

# ==================== 一、作用域测试题 ====================
print("\n" + "=" * 50)
print("一、作用域测试题")
print("=" * 50)

# 1. 题目1：定义全局变量"global_mana"（初始值150，代表玩家魔力值），
#    编写函数"drink_mana_potion"，在函数内用global声明使用全局变量，
#    给"global_mana"增加80，调用函数后打印最终的"global_mana"。
#    （请在下方编写代码）
print("\n1. 题目1作答：")
# 你的代码开始：


# 你的代码结束

# 2. 题目2：编写嵌套函数"biome_event"，外层函数定义局部变量"event_name"="血月"，
#    内层函数"start_event"用nonlocal声明修改"event_name"为"哥布林入侵"，
#    调用内层函数后，在外层函数打印修改后的"event_name"。
#    （请在下方编写代码）
print("\n2. 题目2作答：")
# 你的代码开始：


# 你的代码结束


# ==================== 二、匿名函数测试题 ====================
print("\n" + "=" * 50)
print("二、匿名函数测试题")
print("=" * 50)

# 1. 题目1：用lambda定义函数"calc_ore_total"，接收两个参数（矿石数量、单个价值），
#    返回矿石总价值（数量×价值），调用函数计算"10个金矿（单个价值20）"的总价值并打印。
#    （请在下方编写代码）
print("\n1. 题目1作答：")
# 你的代码开始：


# 你的代码结束

# 2. 题目2：用lambda结合filter函数，从列表"items = [('木斧', 10), ('铁斧', 25), ('金斧', 40), ('神圣斧', 60)]"中，
#    筛选出攻击力>30的斧头，将结果转为列表并打印。
#    （请在下方编写代码）
print("\n2. 题目2作答：")
# 你的代码开始：


# 你的代码结束

# 3. 题目3：用lambda结合三目运算，定义函数"judge_ore_rare"，接收矿石价值，
#    若价值>=20返回"稀有矿石"，否则返回"普通矿石"，调用函数判断"铜矿（价值5）"和"神圣矿石（价值50）"并打印。
#    （请在下方编写代码）
print("\n3. 题目3作答：")
# 你的代码开始：


# 你的代码结束


# ==================== 三、内置函数测试题 ====================
print("\n" + "=" * 50)
print("三、内置函数测试题")
print("=" * 50)

# 1. 题目1：用sum函数计算列表"boss_hps = [2000, 3000, 5000, 10000]"（泰拉瑞亚4个BOSS的生命值）的总和，
#    用max函数找出生命值最高的BOSS，分别打印总和和最高生命值。
#    （请在下方编写代码）
print("\n1. 题目1作答：")
# 你的代码开始：


# 你的代码结束

# 2. 题目2：用zip函数将列表"boss_names = ['克苏鲁之眼', '史莱姆王', '血肉墙', '月总']"和"boss_hps"（题目1的列表）配对，
#    转为列表后打印每对"BOSS名-生命值"。
#    （请在下方编写代码）
print("\n2. 题目2作答：")
# 你的代码开始：


# 你的代码结束

# 3. 题目3：用enumerate函数遍历列表"boss_names"（题目2的列表），从索引1开始，
#    打印格式为"BOSS1：克苏鲁之眼，BOSS2：史莱姆王..."。
#    （请在下方编写代码）
print("\n3. 题目3作答：")
# 你的代码开始：


# 你的代码结束

# 4. 题目4：导入functools.reduce，用reduce函数计算列表"potion_heals = [50, 100, 200, 500]"（4瓶药水的治疗量）的总和，
#    打印总治疗量。
#    （请在下方编写代码）
print("\n4. 题目4作答：")
# 你的代码开始：


# 你的代码结束


# ==================== 四、拆包测试题 ====================
print("\n" + "=" * 50)
print("四、拆包测试题")
print("=" * 50)

# 1. 题目1：有元组"npc_pos = (450, 300)"（NPC坐标x,y），用序列拆包提取x和y，
#    打印"NPCX坐标：xxx，Y坐标：xxx"。
#    （请在下方编写代码）
print("\n1. 题目1作答：")
# 你的代码开始：


# 你的代码结束

# 2. 题目2：有列表"tools = ['铜镐', '木斧', '铁剑', '生命药水', '魔力药水']"，
#    用*拆包，将第一个元素给变量"main_tool"，剩余元素给变量"other_tools"，分别打印两个变量。
#    （请在下方编写代码）
print("\n2. 题目2作答：")
# 你的代码开始：


# 你的代码结束

# 3. 题目3：有字典"armor_attrs = {'name': '金盔甲', 'defense': 20, 'durability': 300}"（盔甲属性），
#    编写函数"show_armor"，接收参数"name, defense, durability"并打印属性，
#    用**拆包字典调用函数。
#    （请在下方编写代码）
print("\n3. 题目3作答：")
# 你的代码开始：


# 你的代码结束