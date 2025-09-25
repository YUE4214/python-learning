###2025年7月11日学习笔记：
#1.变量：计算机中的存储空间保存数据
"""
定义变量格式：变量名 = 值，=赋值运算，左右空格为了规范美观。
num1 = 52
num2 = 68
total = num1 + num2
print(total,num1,num2,sep=" | ")
print打印变量的值，变量之后在赋值以后才会被创建，所以使用变量前必须赋值。
num1 = 74
print(num1)
同一个变量可以反复赋值，pycharm从上到下依次执行程序。
"""
#2.标识符：定义的变量名或者函数名
#2.1标识符规范
"""
规定1：只能由数字、字母、下划线组成；Python3可以使用中文变量
规定2：不能以数字开头
规定3：不能是关键字
False None True and  as assert async await break class continue def del elif else except
finally for from global if import in is lambda nonlocal not or pass raise return try
while with yield
规定4：严格区分大小写
(user) = 0
print(user)#标识符被包括在括号之中不受影响
"""
#2.2变量命名规范
"""
规定1：见名知意
规定2：下划线分割法，多个单词组成的名称，使用小写字母，单词间用下划线分隔
user_name = yue
规定3：大驼峰命名法，首个单词首字母大写，其他小写
Username
规定4：小驼峰命名法，首个单词首字母小写，其他大写
userName
"""
#3.数值类型
#3.1数据类型
"""
int：整型，整数
float：浮点型，小数
bool：布尔型（重点），有固定写法，一个为True（真），一个为False（假），True和False区分大小写。通常用于判断
布尔值可以当做整型对待，True相当于整数1，False相当于整数0
complex：复数型（了解），数学概念，实数和虚数，j是固定的
固定写法z = a + bj

print(type(True))#输出True的类型
print(True + False)
a = 1 + 2j
b = 2 + 3j
print(a + b)
"""
#4.字符串类型str
#4.1字符串类型str
"""
特点：需要加上引号，单双引号均可，包含多行内容时候也可以使用三引号。多行注释和字符串三引号区分开。
name = 'yue'
number = "zhong"
number1 = wen
print(type(name))
print(name,number,number1，sep="_")
"""
#5.格式化输出
#5.1占位符
"""
生成一定格式的字符串
"""
#5.2%
"""
1. %s字符串（常用）
name = ‘yue’
print("姓氏：%s"%name)
2. %d整数（常用）
3. %6d整数，数字设置6位数，不足的前面补空白，少的不影响。%06d，这里的0可以是空格，6代表位数，可以是其他数字。
4. %f浮点数（常用），默认后六位小数，遵循四舍五入原则。
5. %.5f浮点数，数字设置后5位数，遵循四舍五入原则，不足的后面补0，少的不影响。
6. %%第一个%用于输出第二个%
name = 'yue'
year = 2099
time = 10.15
print("%% 姓名：%s，年份：%06d，时间：%.2f %%" % (name,year,time))
"""
#5.3f格式化
"""
1.格式：f"表达式"
name = 'yue'
year = 2099
time = 10.15
condition = "缺水"
print(f"%% 标准参数：姓名：{name}，年份：{year}，时间：{time} 状态：{condition} %%" % ())
print("%% 制式参数：姓名：%s，年份：%06d，时间：%.6f，%s %%" % (name,year,time,condition))
"""
###豆包总结
"""
### 1. 变量  
**总结**：介绍了变量的定义格式（变量名=值）、赋值特性（使用前必须赋值、可重复赋值）及基本打印方式。  
**缺少的重要知识点**：  
- 变量的动态类型特性：Python变量无需声明类型，赋值后自动确定类型（如`a=1`是int，`a="1"`变为str）。  
- 变量引用与内存：多个变量可指向同一值（如`a=1; b=a`，a和b指向同一块内存），修改其中一个不影响另一个（不可变类型）。  
- 避免使用内置函数名作为变量名：如`print=1`会覆盖内置`print()`函数，导致后续无法使用。  
### 2. 标识符  
**总结**：明确了标识符的组成规则（数字、字母、下划线，不能以数字开头，不能是关键字，区分大小写）及命名规范（见名知意、下划线/驼峰命名法）。  
**缺少的重要知识点**：  
- 中文变量的实际开发限制：虽然Python3支持中文变量（如`姓名="张三"`），但实际开发中几乎不使用（兼容性、可读性差）。  
- 关键字的查询方式：可通过`import keyword; print(keyword.kwlist)`查看所有关键字，避免误用。  
- 标识符的“约定俗成”：单下划线开头（`_name`）表示“私有”变量（仅供内部使用），双下划线开头（`__name`）会触发名称修饰（避免子类覆盖）。  
### 3. 数值类型  
**总结**：讲解了int（整型）、float（浮点型）、bool（布尔型，True/False，可当1/0使用）、complex（复数型）的基本概念和特性。  
**缺少的重要知识点**：  
- int的范围：Python中int无大小限制（远超其他语言的32/64位限制），可表示极大整数（如`10**1000`）。  
- float的精度问题：浮点型存在精度误差（如`0.1+0.2=0.30000000000000004`），需用`decimal`模块处理高精度场景。  
- 类型转换：  
  - 其他类型转bool：0、空值（如`""`、`[]`）为False，非0数值、非空值为True（如`bool(0)`是False，`bool("a")`是True）。  
  - 数值类型间转换：`int(3.8)`→3（截断小数），`float(3)`→3.0，`complex(1)`→1+0j。  
- complex的属性：可通过`.real`和`.imag`获取实部和虚部（如`a=1+2j; a.real`→1.0）。  
### 4. 字符串类型（str）  
**总结**：说明字符串需用引号（单/双/三引号）包裹，单双引号通用，三引号可包含多行内容。  
**缺少的重要知识点**：  
- 引号嵌套规则：单引号内可直接用双引号（如`'He said "Hi"'`），双引号内可直接用单引号（如`"It's ok"`），避免转义。  
- 转义字符：`\n`（换行）、`\t`（制表符）、`\\`（反斜杠）、`\'`（单引号）等（如`print("Hello\nWorld")`会换行输出）。  
- 字符串不可变性：创建后无法修改单个字符（如`name="abc"; name[0]='A'`会报错），需通过拼接/切片生成新字符串。  
- 基本操作：拼接（`"a"+"b"`→`"ab"`）、重复（`"a"*3`→`"aaa"`）、索引（`"abc"[1]`→`"b"`）、切片（`"abc"[0:2]`→`"ab"`）。  
### 5. 格式化输出  
**总结**：介绍了`%`占位符（`%s`字符串、`%d`整数、`%f`浮点数）和f格式化的基本用法。  
**缺少的重要知识点**：  
- `%`占位符的进阶用法：  
  - 多占位符顺序：`print("姓名：%s，年龄：%d" % (name, age))`需严格对应顺序，或用字典指定（`"%(name)s %(age)d" % {"name": "张三", "age": 18}`）。  
  - 宽度与精度组合：`%6.2f`表示总宽度6（含小数点），保留2位小数（如`print("%.2f" % 3.1415)`→`3.14`）。  
- f格式化的进阶：  
  - 表达式嵌入：`f"sum: {a + b}"`可直接计算表达式结果。  
  - 格式控制：指定宽度、填充、对齐（如`f"年龄：{age:03d}"`→不足3位补0，`f"成绩：{score:.1f}"`→保留1位小数）。  
- 其他格式化方式：`str.format()`方法（如`"姓名：{}，年龄：{}".format(name, age)`），功能与`%`类似，更灵活（支持位置索引、关键字参数）。  
- 特殊字符转义：f字符串中包含引号时需嵌套（如`f'他说："{"Hello"}"'`→`'他说："Hello"'`）。
"""
###夜间题目练习
#一、变量与赋值：角色属性管理
"""
题目 1：角色初始状态
泰塔瑞亚中，玩家初始生命值为 100，魔力值为 20，防御值为 0。请用变量存储这些属性，并输出角色初始状态。
"""
# health = 100
# mana = 20
# defense = 0
# print(f"玩家生命值：{health} 魔力值：{mana} 防御值：{defense}")
"""
题目 2：战斗后的属性变化
玩家使用「星怒剑」攻击史莱姆王，造成 30 点伤害（扣除史莱姆王 30 生命值），同时自身被史莱姆王反击损失 15 点生命值。请更新变量并输出战斗后的双方状态。
提示：
史莱姆王初始生命值为 140；
用 health -= damage 表示生命值减少。
"""
# #初始化双方状态
# player_health = 100
# slime_king_health = 140
# #战斗过程
# player_damage = 30
# slime_king_health -= player_damage
# slime_king_counter_damage = 30
# player_health -= slime_king_counter_damage
# print(f"史莱姆王生命值：{slime_king_health}")
# print(f"玩家生命值：{player_health}")
#二、标识符与命名规范：游戏元素命名
"""
题目 1：判断合法标识符
以下哪些是泰塔瑞亚中合法的变量名？
2nd_sword
slime_king
True
npc_guide
my-axe
答案：合法的标识符是 slime_king、npc_guide。
解析：
不能以数字开头（2nd_sword 非法）；
不能使用关键字（True 是布尔值关键字，非法）；
不能包含特殊符号（my-axe 含连字符，非法）。
"""
"""
题目 2：按规范命名变量
根据泰塔瑞亚游戏元素，用「下划线命名法」为以下场景命名变量：
玩家装备的「钴蓝盔甲」的防御值；
击败「克苏鲁之眼」后获得的晶状体数量；
树妖出售的「净化粉」价格。
cobalt_armor_defense
oculus_crystals_count
dryad_purification_powder_price
"""
#三、数值类型与运算：战斗与资源管理
"""
题目 1：药水效果计算
玩家使用「再生药水」，每秒恢复 3 点生命值，持续 20 秒。假设玩家当前生命值为 50，且未受到伤害，计算药水生效后的总生命值。
"""
# current_health = 50
# health_per_second = 3
# duration_seconds = 30
# total_health = health_per_second * duration_seconds
# final_health = current_health + total_health
# print(f"玩家生命值：{final_health}")
"""
题目 2：装备伤害计算
战士职业使用「永夜刃」（基础伤害 45）攻击敌人，装备「游侠徽章」（增加 15% 远程伤害）和「毁灭者徽章」（增加 10% 全伤害）。计算最终伤害。
提示：
远程伤害加成对近战武器无效，仅全伤害加成生效；
伤害公式：基础伤害 × (1 + 全伤害加成)。
"""
# base_damage = 45
# all_damage_bonus = 0.1
# final_damage = base_damage * (1 + all_damage_bonus)
# print(f"最终伤害：{final_damage:.2f}")  # 效果与原代码完全一致，但更简洁
#四、字符串操作：物品描述与任务提示
"""
题目 1：拼接物品信息
玩家获得「暗影钥匙」，描述为「可打开腐化之地的暗影箱」。请用字符串拼接生成完整描述
"""
# item_name = "暗影钥匙"
# description = "可打开腐化之地的暗影箱"
# full_description = f"{item_name} : {description}"
# print(full_description)
"""
题目 2：任务提示格式化
调查局发布任务：「探索城北20千米的腐化区域，需组队7-10人，奖励2-10铂金币」。请用%格式化输出任务提示。
"""
# task_location = "城北20千米的腐化区域"
# task_size = "7-10人"
# task_reward = "2-10铂金币"
# print("任务：探索%s，需组队%s，奖励%s" % (task_location,task_size,task_reward))
#五、格式化输出：角色状态与战斗日志
"""
题目 1：角色状态显示
玩家等级为 15，生命值 300/500，魔力值 150/200，防御值 25。用 f-strings 输出状态
"""
# level = 15
# health = 300
# mana = 150
# max_health = 500
# max_mana = 200
# defense = 25
# print(f"玩家等级为{level} | 生命值{health}/{max_health} | 魔力值{mana}/{max_mana} | 防御值{defense}")
"""
题目 2：战斗日志格式化
玩家使用「蜜蜂手榴弹」对「世界吞噬者」造成 120 点伤害，触发暴击（额外 + 50% 伤害）。用%格式化输出日志。
"""
# enemy_name = "世界吞噬者"
# weapon_name = "蜜蜂手榴弹"
# damage = 120
# critical_bonus = 50
# total_damage = damage * (1 + critical_bonus / 100)
# print("使用 %s 对 %s 造成 %.2f 点伤害，触发暴击（额外 + %.2f%%伤害），共造成 %.2f 点伤害" % (weapon_name, enemy_name, damage, critical_bonus, total_damage))
#六、综合应用：模拟游戏事件
"""
六、综合应用：模拟游戏事件
题目：腐化之地调查任务
玩家需完成以下步骤，用 Python 模拟过程：
初始化变量：队伍人数 7 人，已探索区域 0%，净化粉数量 100 包；
探索过程中，每探索 20% 区域消耗 15 包净化粉；
输出每次探索后的区域进度和剩余净化粉；
探索至 80% 时触发 BOSS「世界吞噬者」，净化粉消耗量加倍（每 20% 消耗 30 包）；
计算探索至 100% 时的剩余净化粉，若不足则提示「净化粉不足，任务失败」。
"""
# #始化变量：
# team_size = 7
# explored_area = 0 #%.2f
# purification_powder_number = 10
# #探索过程中：
# #探索达到20%
# while explored_area < 80:
#     explored_area += 20
#     purification_powder_number -= 15
#     print(f"已探索区域：{explored_area:.2f}%，剩余净化粉数量：{purification_powder_number}")
# #探索达到80%，BOSS战阶段
# if purification_powder_number < 30:
#     print("净化粉不足，任务失败")
# else:
#     explored_area += 20
#     purification_powder_number -= 30
#     print("任务成功")


