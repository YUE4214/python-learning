###2025年7月17日学习笔记：
#1.循环语句
#1.1循环语句
"""
重复执行，直到不满足条件1
"""
#2.while循环
#2.1while循环
"""
（1）
定义初始变量
while 条件:
    循环体（满足条件执行的事情）
    改变变量
（2）
死循环：
while True:
    循环体（满足条件执行的事情）

True的位置只要不是0或者False，都会是死循环
（3）
while循环嵌套
注意保持正确缩进，缩进的位置决定while属于哪一层级的嵌套。
"""
# a = 1
# while a <= 100:
#     print("赤心筑无")
#     a += 1
# a = 1
# b = 0

# while a <= 100:
#     b += a
#     a += 1
# print(b)
#3.for循环（迭代循环）
#3.1for循环（迭代循环）
"""
（1）
for 临时变量 in 可迭代对象:
    循环体
注意冒号和缩进
可迭代对象就是要去遍历取值的整体，字符串是可迭代对象
（2）
range()函数
用来记录循环次数，相当于计数器
range(start,stop,step)
（3）
相比之下，for比while更简洁
"""
# a = "happy"
# for i in a:
#     print(i)

# for i in range(1,6):#从1开始，到6结束，遵循包含前数不包含后数，[1,6)，左闭右开1<=x<6,输出1,2,3,4,5
#     print(i)
# for i in range(5):#只有一个数字，表示循环次数，从0开始，输出0,1,2,3,4
#     print(i)

# a = 0
# for i in range(1,101):#计算1-100的和
#     a += i
# print(a)
#4.break和continue关键字
#4.1break和continue关键字
"""
break和continue都是专门在循环中使用的关键字，只能放在循环内
break：中途退出，结束循环。
continue：结束当前循环，进入下一个循环。在continue之前一定要修改计数器，否则会死循环。
如果是嵌套循环，break和continue只针对最近的循环。
"""
# i = 1
# while i <= 5:
#     print(f"击毙第{i}个敌人")
#     if i == 3:
#         print("敌人撤退")
#         break
#     i += 1

# i = 1
# while i <= 5:
#     print(f"击毙第{i}个小兵")
#     if i == 3:
#         print("击败BOSS")
#         i += 1
#         continue
#     i += 1

###豆包总结
"""
循环语句知识点总结
1. 循环基础概念
定义：重复执行代码块，直到满足终止条件
核心要素：初始条件、终止条件、循环体、变量更新
2. 循环类型对比
类型	语法结构	适用场景
while	while 条件:
    循环体
    变量更新	条件未知，需动态判断
for	for 变量 in 可迭代对象:
    循环体	遍历固定序列或范围
死循环	while True:
    循环体	持续运行（如服务器监听）
3. 关键控制语句
语句	作用	注意事项
break	立即终止当前循环，跳出循环体	嵌套循环中仅影响最近的循环
continue	跳过当前循环剩余代码，直接进入下一次循环	使用前需确保变量已更新
else	循环正常结束（未被 break）时执行	增强代码逻辑可读性
for i in range(5):
    print(i)
else:
    print("循环结束，未被 break 中断")
4. 高级应用技巧
嵌套循环：循环中包含循环（需注意缩进层级）
循环优化：减少嵌套层级、避免重复计算
异常处理：使用 try-except 捕获循环中的错误，但注意避免过度使用，影响性能
numbers = [1, 0, 3]
for num in numbers:
    try:
        result = 10 / num  # 避免除以零
    except ZeroDivisionError:
        print("除数不能为零")
    else:
        print(f"结果: {result}")
无限循环：搭配 break 实现灵活终止条件
"""
###夜间题目练习
"""
练习题 1：while 基础 - 收集史莱姆凝胶
场景：击杀史莱姆，每只掉 1 个凝胶，凑够 10 个停止。
要求：用 while 循环实现，输出每次击杀后的凝胶数。
知识点：while 循环的初始变量、条件判断、变量更新
"""
# gel = 0
# while gel < 10:
#     gel += 1
#     print(f"击杀史莱姆！掉落凝胶{gel}个")
# print(f"总凝胶：{gel}")
#豆包答案
# gel = 0  # 初始凝胶数
# while gel < 10:  # 条件：凝胶不足10个
#     gel += 1
#     print(f"击杀史莱姆！当前凝胶：{gel}")
"""
练习题 2：while 死循环 + break - 逃离神秘洞穴
场景：探索洞穴，50% 概率找到出口，找到则逃离（需导入 random）。
要求：用 while True 死循环 + break 终止。
知识点：死循环（while True）、break 终止循环
"""
# import random
# count = 0
# while True:
#     count += 1
#     print(f"第{count}次探索洞穴")
#     if random.random() > 0.5:
#         print("成功找到出口，逃离")
#         break
#豆包答案
# import random
# count = 0
# while True:
#     count += 1
#     print(f"第{count}次探索...")
#     if random.random() < 0.5:  # 50%概率找到出口
#         print("找到出口！逃离成功～")
#         break  # 终止死循环
"""
练习题 3：for 循环 - 遍历物品栏 & 挖矿计数
场景：
遍历物品栏字符串 inventory = "wood,pickaxe,gel"；
用 range 模拟挖 5 次矿
知识点：for 遍历可迭代对象（列表、range）、字符串 split
"""
# inventory = "wood,pickaxe,gel"
# items = inventory.split("，")
# for item in items:
#     print(f"背包找到：{item}")
# for count in range(1,6):
#     print(f"第{count}次挖矿")
#豆包答案
# # 场景1：遍历物品栏
# inventory = "wood,pickaxe,gel"
# items = inventory.split(",")  # 拆成列表
# for item in items:  # 遍历列表
#     print(f"背包找到：{item}")
#
# # 场景2：挖矿计数
# for x in range(1, 6):  # 1-5次（左闭右开）
#     print(f"第{x}次挖矿，获得石头！")
"""
练习题 4：for + range 步长 - 铺设铁轨
场景：每 3 段直轨后接 1 段弯轨，共铺 20 段（3 直 + 1 弯为一组，共 5 组）。
"""
# for i in range(1, 21, 4):
# #     for j in range(i, i+3):
# #         print(f"铺设第{j}段直轨")
# #     print(f"铺设第{i+3}段弯轨")
#豆包答案
# for i in range(1, 21, 4):  # 每组4段（step=4）
#     # 铺3段直轨
#     for j in range(i, i+3):
#         print(f"直轨：第{j}段")
#     # 铺1段弯轨
#     print(f"弯轨：第{i+3}段")
"""
练习题 5：break 在嵌套循环 - 抵御敌波
场景：3 波敌人，每波最多 5 只，遇到第 3 只（Boss）则撤退（break 当前波）。
"""
# wave = 1
# while wave <= 3:
#     print(f"=== 第{wave}波敌人 ===")
#     enemy = 1
#     while enemy <= 5:
#         print(f"击杀第{enemy}只敌人")
#         if enemy == 3:
#             print("遇到Boss！撤退！")
#             break
#         enemy += 1
#     wave += 1
#豆包答案
# wave = 1
# while wave <= 3:  # 外层：波次
#     print(f"=== 第{wave}波 ===")
#     enemy = 1
#     while enemy <= 5:  # 内层：每波敌人
#         print(f"击杀第{enemy}只敌人")
#         if enemy == 3:  # 第3只是Boss
#             print("遇到Boss！撤退！")
#             break  # 终止当前波（内层循环）
#         enemy += 1
#     wave += 1
"""
练习题 6：continue 在 while - 筛选优质材料
场景：收集 10 次材料，质量 < 5 的跳过（continue），统计优质材料。
知识点：while 中 continue 跳过当前轮次（注意变量更新位置）
"""
# import random
# count = 0
# success = 0
# while count < 10:
#     count += 1
#     print(f"第{count}次收集材料")
#     quality = random.random() * 10
#     print(f"材料质量为{quality:.2f}")
#     if quality < 5:
#         print("此次材料质量不足，重新收集")
#         continue
#     else:
#         success += 1
# print(f"总共进行{count}次收集，成功完成{success}次收集")
# 豆包答案
# import random
# good = 0
# count = 0
# while count < 10:
#     count += 1
#     quality = random.randint(1, 10)  # 随机质量
#     if quality < 5:
#         print(f"劣质（{quality}），跳过！")
#         continue  # 跳过当前循环，不计数
#     good += 1
#     print(f"优质（{quality}），已收集{good}个")
"""
练习题 7：for 嵌套 - 建造 3x3 房子
场景：用 ■ 打印 3 行 3 列的房子（嵌套循环控制行和列）。
知识点：for 循环嵌套、print(end="") 控制换行
"""
# for x in range(1,4):
#     print(" ■ ■ ■ ")
#豆包答案
# for row in range(3):  # 3行
#     for col in range(3):  # 每行3列
#         print("■", end=" ")  # 不换行，拼接一行
#     print()  # 换行，开始下一行
"""
练习题 8：综合挑战 - 打怪升级（while+break+continue）
场景：击杀 10 次怪，1 次 1 经验，5 经验升 1 级；升到 3 级触发 Boss（break），miss（经验 0）则 continue。
"""
# import random
# monster_num = 0
# killed_monster_num = 0
# gain_exp = 0
# player_level = 0
# while killed_monster_num < 10:
#     monster_num += 1
#     success = random.random()
#     if player_level >= 3:
#         print(f"第{monster_num}次遇敌，触发Boss，撤退")
#         break
#     if success > 0.2: #大于0.2表示成功击杀
#         killed_monster_num += 1
#         gain_exp += 1
#         print(f"第{monster_num}次遇敌，成功击杀，获得1点经验，当前经验={gain_exp}")
#         if gain_exp >= 5:
#             player_level += 1
#             print(f"升级，当前等级={player_level}")
#             gain_exp = 0
#     else:
#         print(f"第{monster_num}次遇敌，miss，怪物逃走了")
#         continue
# print(f"共遇敌{monster_num}次，已击杀{killed_monster_num}次，玩家等级={player_level}，当前经验={gain_exp}")
#豆包答案
# import random
#
# # 初始化变量
# encounter_count = 0  # 遇敌总次数
# kill_count = 0  # 成功击杀次数
# exp = 0  # 当前经验
# level = 0  # 玩家等级
#
# #循环条件：击杀次数不足50次，且未触发Boss
# while kill_count < 50:
#     encounter_count += 1  # 每次循环代表遇敌一次
#     print(f"\n=== 第{encounter_count}次遇敌 ===")
#
#     # 检查是否已触发Boss条件（等级≥3）
#     if level >= 3:
#         print("触发Boss战！撤退！")
#         break  # 终止循环
#
#     # 模拟击杀成功率（80%概率成功，success>0.2即成功）
#     success = random.random()
#     if success > 0.2:
#         # 成功击杀逻辑
#         kill_count += 1
#         exp += 1
#         print(f"成功击杀！经验+1（当前经验：{exp}）")
#
#         # 升级判断
#         if exp >= 5:
#             level += 1
#             exp = 0  # 清空经验
#             print(f"升级！当前等级：{level}")
#     else:
#         # Miss逻辑：跳过本次击杀，进入下一次循环
#         print("攻击落空，怪物逃走了！")
#         continue
#
# # 战斗结束统计
# print("\n==== 战斗总结 ====")
# print(f"共遇敌：{encounter_count}次")
# print(f"成功击杀：{kill_count}次")
# print(f"最终等级：{level}，剩余经验：{exp}")
