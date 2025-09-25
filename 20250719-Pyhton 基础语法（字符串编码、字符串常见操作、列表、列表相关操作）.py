###2025年7月19日学习笔记：
#1.字符串编码
#1.1字符串编码
"""
（1）
本质上是二进制和语言文字的一一对应关系
ASCII：表示英语和西欧语言
GB2312：国家简体中文字符集，兼容ASCII
Unicode：国际统一标准。所有字符均是两个字节。字符和数字转换速度更快，但占用空间大
GBK：GB2312扩展字符集
UTF-8：不定长编码。对不同长度的字符用不同的长度表示。节省空间，但字符和数字转换速度较慢，每次都需要计算长度。
（2）字符串编码转换
编码encode
解码decode
"""
# from os import replace

# a = "hello"
# for i in a:
#     print(i)
# print(a,type(a)) #str，字符串是以字符为单位进行处理
# a1 = a.encode() #编码
# for i in a1:
#     print(i)
# print(a1,type(a1)) #bytes，以字节为单位进行处理的
# a2 = a1.decode() #解码
# for i in a2:
#     print(i)
# print(a2,type(a2))
# #注意：对于bytes，只需要知道他和字符串类型之间的互相转换
# st = "赤心筑无"
# for i in st:
#     print(i)
# print(st,type(st)) #str，字符串是以字符为单位进行处理
# st1 = st.encode("utf-8")
# for i in st1:
#     print(i)
# print(st1,type(st1))
# st2 = st1.decode("utf-8")
# for i in st2:
#     print(i)

#2.字符串常见操作
#2.1字符串常见操作
"""
（1）+：字符串拼接
（2）*：重复输出
"""
# print("赤心"+"筑无")
# print("赤心筑无\n"*2)
#2.2成员运算符，检查字符串中是否包含了某个字符串（某个字符或者多个字符）
"""
（1）in：如果包含的话返回True，不包含为False
（2）not in：如果不包含返回True，包含返回False
"""
# a = "hello"
# print("ll" in a) #True
# print("hl" not in a) #True
#2.3下标
"""
（1）Python中下标从0开始。
（2）通过下标可以快速找到对应数据。从左往右数，下标从0开始，0、1、2。
（3）格式：变量名[下标值]。下标值不要超过变量范围，否则会报索引错误。
（4）如果从右往左数，下标从-1开始，-1、-2，下标值不要超过变量范围，否则会报索引错误。
"""
# a = "hello"
# print(a[0])
# print(a[1])
#2.4切片
"""
（1）指对操作的对象截取其中一部分的操作。
（2）语法：[开始位置:结束位置:步长]
（3）遵循包前不包后规则，[)。
（4）步长的绝对值大小决定切取的间隔，正负号表示切取方向。正表示从左往右，负表示从右往左。
"""
# a = "hello world"
# print(a[0:4]) #hell
# print(a[4:7]) #o w
# print(a[4:]) #o world
# print(a[:6]) #hello
# print(a[:-1]) #hello worl
# print(a[-1:-5])
# print(a[-1::1]) #d
# print(a[-1::-1]) #dlrow olleh
# print(a[-1:-5:-1]) #dlro
# print(a[0:6:2]) #hlo
#3.字符串常见操作
#3.1find()
"""
（1）find()：检测某个子字符串是否包含在字符串中，为真则返回这个子字符串开始位置的下标，为假则返回-1
（2）格式：变量名.find(子字符串,开始位置下标,结束位置下标)。两个位置下标省略则默认范围为全字符串。
（3）两个位置下标遵循包前不包后
"""
# a = "hello world"
# print(a.find("el")) #1
# print(a.find("o",6,8)) #7
# print(a.find("4",6,8)) #-1
#3.2index()
"""
（1）index()：检测某个子字符串是否包含在字符串中，为真则返回这个子字符串开始位置的下标，为假则报错。
（2）格式：变量名.index(子字符串,开始位置下标,结束位置下标)。两个位置下标省略则默认范围为全字符串。
（3）两个位置下标遵循包前不包后
"""
# a = "hello world"
# print(a.index("el")) #1
# print(a.index("o",6,8)) #7
# print(a.index("4",6,8)) #报错ValueError: substring not found
#3.3count()
"""
（1）count()：返回某个子字符串在整个字符串中出现的次数，没有则返回0
（2）格式：变量名.count(子字符串,开始位置下标,结束位置下标)。两个位置下标省略则默认范围为全字符串。
（3）两个位置下标遵循包前不包后
"""
# a = "hello world"
# print(a.count("el")) #1
# print(a.count("o",0,8)) #2
# print(a.count("4",0,8)) #0
#3.4startswith()
"""
（1）startswith()：判断是否以某个字符串开头，为真返回True，为假返回False
（2）格式：变量名.startswith(子字符串,开始位置下标,结束位置下标)。两个位置下标省略则默认范围为全字符串。
（3）两个位置下标遵循包前不包后
"""
# a = "hello world"
# print(a.startswith("he")) #True
# print(a.startswith("e",1,5)) #True
#3.5endswith()
"""
（1）endtswith()：判断是否以某个字符串结尾，为真返回True，为假返回False
（2）格式：变量名.endtswith(子字符串,开始位置下标,结束位置下标)。两个位置下标省略则默认范围为全字符串。
（3）两个位置下标遵循包前不包后
"""
# a = "hello world"
# print(a.endswith("ld")) #True
# print(a.endswith("e",1,5)) #False
#3.6isupper() islower()等等
"""
（1）isupper()：检测字符串所有字符是否都为大写。islower()：检测字符串所有字符是否都为小写。为真返回True，为假返回False。
（2）格式：变量名.isupper(子字符串,开始位置下标,结束位置下标)。两个位置下标省略则默认范围为全字符串。
（3）两个位置下标遵循包前不包后
"""
#3.7修改元素replace()
"""
（1）replace()：替换
（2）格式：变量名.replace(旧内容,新内容,替换次数)。替换次数省略则默认范围为全部替换。
"""
# a = "aaabbbccc"
# print(a.replace("a","c",1)) #caabbbccc
#3.8修改元素split()
"""
（1）split()：使用指定分隔符来切字符串。以列表的形式返回。如果字符串不包含分割内容，则不进行分隔，作为一个整体返回，当然也是列表。
（2）格式：变量名.split(分隔符,分割次数)。分割次数省略则默认为全部分割。
"""
# a = "aaabb,bccc"
# print(a.split(",")) #['aaabb', 'bccc']
# print(a.split("a")) #['', '', '', 'bb,bccc']
# print(a.split("a",1)) #['', 'aabb,bccc']
#3.8修改元素capitalize()
"""
（1）capitalize()：第一个字符大写，其他都小写。
（2）格式：变量名.capitalize()。
"""
# a = "aaabbbccc"
# print(a.capitalize()) #Aaabbbccc
#3.8修改元素lower() upper()
"""
（1）lower()：大写字母转小写。upper()：小写字母转大写
（2）格式：变量名.lower()。变量名.upper()。
"""
# a = "aaabbbccc"
# print(a.upper()) #AAABBBCCC
# print(a.lower()) #aaabbbccc
###豆包总结
"""
# Python字符串知识点总结与查漏补缺


## 一、字符串编码
### 核心知识点
1. **编码本质**：二进制与语言文字的一一对应关系，是计算机存储文本的基础。
2. **常见编码格式**：
   - ASCII：仅包含英语和西欧语言字符（1字节）。
   - GB2312/GBK：中文编码，GBK是GB2312的扩展，兼容ASCII。
   - Unicode：国际统一编码，所有字符均占2字节（固定长度），转换速度快但占用空间大。
   - UTF-8：可变长度编码（1-4字节），节省空间但转换时需计算长度，是目前最常用的编码格式。
3. **编码与解码**：
   - `encode()`：字符串（str）→ 字节流（bytes），需指定编码格式（默认UTF-8）。
   - `decode()`：字节流（bytes）→ 字符串（str），需与编码格式一致，否则会报错。


### 查漏补缺
- bytes类型以字节为单位存储，打印时以`b'内容'`形式显示，遍历会输出每个字节的十进制数值。
- 编码和解码必须使用相同的格式（如UTF-8编码的bytes必须用UTF-8解码），否则会出现`UnicodeDecodeError`。


### 我的世界相关题目
1. 假设游戏中“钻石剑”的英文是`"diamond_sword"`，用UTF-8编码后得到的bytes类型变量是`b'diamond_sword'`，请将其解码为字符串。
2. 编写代码：将字符串`"我的世界"`用GBK编码为bytes，再解码回字符串。
3. 判断题：`"minecraft".encode()`和`"minecraft".encode("ASCII")`的结果相同（ ）。
"""
# ##1. 假设游戏中“钻石剑”的英文是`"diamond_sword"`，用UTF-8编码后得到的bytes类型变量是`b'diamond_sword'`，请将其解码为字符串。
# name = b'diamond_sword'
# name1 = name.decode("utf-8")
# print("钻石剑的名字：",name1)
# print(type(name1))
"""
原理：解码是编码的逆操作，必须使用与编码时相同的格式（这里都是 UTF-8），否则可能出现乱码或报错。
"""
# ##2. 编写代码：将字符串`"我的世界"`用GBK编码为bytes，再解码回字符串。
# game_name = "我的世界"
# game_name_gbk = game_name.encode("gbk")
# print("游戏名称gbk格式：",game_name_gbk)
# print(type(game_name_gbk))
# game_name_str = game_name_gbk.decode("gbk")
# print("游戏名称字符串格式：",game_name_str)
# print(type(game_name_str))
"""
注意：如果编码用 GBK，解码时误用 UTF-8 会报错（UnicodeDecodeError），因为两种编码对中文字符的二进制映射不同。
"""
# ##3. 判断题：`"minecraft".encode()`和`"minecraft".encode("ASCII")`的结果相同（ ）。
# #正确，因为虽然编码格式不同，但是 ASCII 是 UTF-8 的子集
# a1 = "minecraft".encode()
# a2 = "minecraft".encode("ASCII")
# print(a1 == a2)
"""
注意：如果编码用 GBK，解码时误用 UTF-8 会报错（UnicodeDecodeError），因为两种编码对中文字符的二进制映射不同。
"""
"""
## 二、字符串基础操作
### 核心知识点
1. **拼接与重复**：
   - `+`：拼接两个字符串（如`"stone"+"pickaxe"`→`"stonepickaxe"`）。
   - `*`：重复输出字符串（如`"coal\n"*3`→输出3行“coal”）。
2. **成员运算符**：
   - `in`：判断子字符串是否存在（如`"wood" in "wooden_door"`→`True`）。
   - `not in`：判断子字符串是否不存在（如`"iron" not in "gold_ore"`→`True`）。


### 查漏补缺
- 字符串是不可变类型，`+`和`*`操作会生成新字符串，不会修改原字符串。
- 成员运算符判断的是“连续子字符串”，而非单个字符的组合（如`"dirt" in "diamond"`→`False`，因“dirt”不是连续子串）。


### 我的世界相关题目
1. 用`+`和`*`组合写出代码：生成字符串`"obsidian_obsidian_obsidian"`。
2. 判断：`"red" in "redstone_torch"`的结果是？`"torch" not in "redstone"`的结果是？
3. 游戏中“皮革盔甲”的英文是`"leather_armor"`，用代码判断其中是否包含`"leath"`和`"meta"`。
"""
# ##1. 用`+`和`*`组合写出代码：生成字符串`"obsidian_obsidian_obsidian"`。
# a1 = "obsidian_" * 2 +"obsidian"
# print(a1)
"""
注意：如果编码用 GBK，解码时误用 UTF-8 会报错（UnicodeDecodeError），因为两种编码对中文字符的二进制映射不同。
"""
# ##2. 判断：`"red" in "redstone_torch"`的结果是？`"torch" not in "redstone"`的结果是？
# #True和True
# print("red" in "redstone_torch")
# print("torch" not in "redstone")
# ##3. 游戏中“皮革盔甲”的英文是`"leather_armor"`，用代码判断其中是否包含`"leath"`和`"meta"`。
# name = "leather_armor"
# print("皮革盔甲是否包含leath","leath" in name)
# print("皮革盔甲是否包含meta","meta" in name)

"""

## 三、下标与切片
### 核心知识点
1. **下标**：
   - 从左到右：下标从0开始（如`"creeper"`中`"c"`是下标0）。
   - 从右到左：下标从-1开始（如`"creeper"`中`"r"`是下标-1）。
   - 格式：`变量名[下标值]`，下标越界会报`IndexError`。
2. **切片**：
   - 语法：`[开始位置:结束位置:步长]`，遵循“包前不包后”规则（如`"zombie"[1:4]`→`"omb"`）。
   - 步长：正数从左到右切，负数从右到左切（如`"skeleton"[::-1]`→`"noteleks"`）。


### 查漏补缺
- 切片不会修改原字符串，而是返回新字符串。
- 当开始位置省略时默认从0开始，结束位置省略时默认到字符串末尾（如`"pig"[:2]`→`"pi"`，`"pig"[1:]`→`"ig"`）。
- 步长为0会报`ValueError`（如`"sheep"[0:3:0]`是错误的）。


### 我的世界相关题目
1. 字符串`"minecraft"`中，下标为3的字符是______，下标为-2的字符是______。
2. 对字符串`"ender_dragon"`进行切片：
   - 取前5个字符：`"ender_dragon"`[______:______]→`"ender"`。
   - 从下标6开始取到末尾：`"ender_dragon"`[______:]→`"dragon"`。
   - 倒序输出整个字符串：`"ender_dragon"`[______:______:______]→`"nogard_redne"`。
3. 用切片获取`"iron_ingot"`中的`"ingot"`（提示：从下标5开始）。
"""
# ##1. 字符串`"minecraft"`中，下标为3的字符是e，下标为-2的字符是f。
# a1 = "minecraft"
# print(a1[3])
# print(a1[-2])
"""
解析：
"""
# ##2. 对字符串`"ender_dragon"`进行切片：
# print("取前5个字符：","ender_dragon"[:5])
# print("从下标6开始取到末尾：","ender_dragon"[6:])
# print("倒序输出整个字符串：","ender_dragon"[-1::-1])
"""
解析：
"""
# ##3. 用切片获取`"iron_ingot"`中的`"ingot"`（提示：从下标5开始）。
# print("iron_ingot"[5:10])
"""
总结：下标是切片的基础，切片的核心是 “包前不包后” 和步长方向，结合游戏中的字符串（如物品名）练习能更直观理解～
"""

"""

## 四、字符串查找与统计
### 核心知识点
1. **find()**：
   - 功能：查找子字符串首次出现的下标，不存在返回-1。
   - 格式：`str.find(子串, 开始下标, 结束下标)`（范围为`[开始, 结束)`）。
2. **index()**：
   - 功能：与`find()`类似，但子字符串不存在时会报`ValueError`。
3. **count()**：
   - 功能：统计子字符串出现的次数，不存在返回0。
   - 格式：`str.count(子串, 开始下标, 结束下标)`。


### 查漏补缺
- `find()`和`index()`的区别：仅在于子串不存在时的处理（-1 vs 报错）。
- 统计次数时，重叠子串不重复计算（如`"aaaaa".count("aa")`→2，因“aa”从0、2、4开始，取前两个）。


### 我的世界相关题目
1. 字符串`"grass_block,grass,grass_seed"`中，`"grass"`出现了几次？用`count()`验证。
2. 查找`"nether_quartz_ore"`中`"quartz"`首次出现的下标（用`find()`）。
3. 判断题：`"golden_apple".index("gold")`的结果是0（ ）；`"golden_apple".find("apple", 5)`的结果是6（ ）。
"""
# ##1. 字符串`"grass_block,grass,grass_seed"`中，`"grass"`出现了几次？用`count()`验证。
# a1 = "grass_block,grass,grass_seed"
# print("grass出现了几次：",a1.count("grass"))
"""
解析：字符串中包含 3 处"grass"（分别在grass_block、grass、grass_seed中），count()方法准确统计了出现次数。
"""
# ##2. 查找`"nether_quartz_ore"`中`"quartz"`首次出现的下标（用`find()`）。
# a2 = "nether_quartz_ore"
# print(a2.find("quartz"))
"""
解析："nether_"长度为 7（索引 0-6），其后紧跟"quartz"，因此"quartz"的首个字符q的索引为 7，find()返回正确结果。
"""
# ##3. 判断题：`"golden_apple".index("gold")`的结果是0（ ）；`"golden_apple".find("apple", 5)`的结果是6（ ）。
# #正确 错误
# print("golden_apple".index("gold"))
# print("golden_apple".find("apple", 5))
"""
解析：
("golden_apple".index("gold") == 0)："golden_apple"的前 4 个字符是"gold"，index("gold")返回起始索引 0，结果为True。
("golden_apple".find("apple", 5) == 6)："golden_apple"中"apple"从索引 7 开始（g(0)、o(1)、l(2)、d(3)、e(4)、n(5)、
_(6)、a(7)...），从索引 5 开始查找时，find()返回 7 而非 6，结果为False。
"""
"""
## 五、字符串判断与修改
### 核心知识点
1. **判断类方法**：
   - `startswith(子串)`：判断是否以子串开头（如`"wooden_axe".startswith("wood")`→`True`）。
   - `endswith(子串)`：判断是否以子串结尾（如`"glass_pane".endswith("pane")`→`True`）。
   - `isupper()`/`islower()`：判断所有字符是否全为大写/小写（如`"COBBLESTONE".isupper()`→`True`）。
2. **修改类方法**：
   - `replace(旧子串, 新子串, 替换次数)`：替换子串（如`"stone_stone".replace("stone", "cobble", 1)`→`"cobble_stone"`）。
   - `split(分隔符, 分割次数)`：按分隔符切分字符串为列表（如`"wheat,carrot,potato".split(",")`→`["wheat", "carrot", "potato"]`）。
   - `capitalize()`：首字母大写，其余小写（如`"mINEcRAFT"`→`"Minecraft"`）。
   - `lower()`/`upper()`：全转为小写/大写（如`"DIAMOND".lower()`→`"diamond"`）。


### 查漏补缺
- 所有字符串修改方法均返回新字符串，原字符串不变（因字符串不可变）。
- `split()`的分隔符不存在时，返回包含原字符串的单元素列表（如`"bedrock".split("x")`→`["bedrock"]`）。


### 我的世界相关题目
1. 游戏物品列表字符串为`"iron_sword,bow,golden_helmet,iron_chestplate"`，用`split()`按逗号分割为列表。
2. 将字符串`"mObSpAwNeR"`处理为：
   - 全大写：`"mObSpAwNeR"`.______()→`"MOBSPAWNER"`。
   - 首字母大写其余小写：`"mObSpAwNeR"`.______()→`"Mobspawner"`。
3. 用`replace()`将`"stone_brick,stone_slab,stone_wall"`中的“stone”改为“nether_brick”。
4. 判断：`"ender_pearl".startswith("end")`→（ ）；`"potion_of_healing".endswith("ing")`→（ ）。
"""
# ##1. 游戏物品列表字符串为`"iron_sword,bow,golden_helmet,iron_chestplate"`，用`split()`按逗号分割为列表。
# a1 = "iron_sword,bow,golden_helmet,iron_chestplate"
# a2 = a1.split(",")
# print(a1)
# print(a2)
"""
解析：
split(",")会以逗号为分隔符，将原字符串切分为多个子串，并存入列表。这在处理游戏中的物品列表、
配置项等场景非常实用，能快速将字符串格式的列表转换为可迭代的列表类型。
"""
# ##2. 将字符串`"mObSpAwNeR"`处理为：
# print("全大写：","mObSpAwNeR".upper())
# print("首字母大写其余小写：","mObSpAwNeR".capitalize())
"""
解析：
原理：
upper()会将字符串中所有小写字母转为大写，不改变非字母字符（本题无特殊字符）。
capitalize()仅将字符串第一个字符转为大写，其余所有字母转为小写，适合标准化命名（如游戏中物品的规范名称）。
"""
# ##3. 用`replace()`将`"stone_brick,stone_slab,stone_wall"`中的“stone”改为“nether_brick”。
# a3 = "stone_brick,stone_slab,stone_wall"
# print(a3.replace("stone","nether_brick"))
"""
解析：
解析：
replace("stone", "nether_brick")会将字符串中所有 "stone" 子串替换为
 "nether_brick"（默认替换所有，若需限制次数可加第三个参数，如replace(..., 2)只替换前 2 次）。
这在批量修改相似命名的物品、路径等场景非常高效。
"""
# ##4. 判断：`"ender_pearl".startswith("end")`→（ ）；`"potion_of_healing".endswith("ing")`→（ ）。
# #True和True
# print("ender_pearl".startswith("end"))
# print("potion_of_healing".endswith("ing"))
"""
解析：
逻辑：
"ender_pearl"的前 3 个字符是 "e""n""d"，因此startswith("end")返回 True。
"potion_of_healing"的最后 3 个字符是 "i""n""g"（来自 "healing"），因此endswith("ing")返回 True。
这两个方法常用于快速筛选符合特定前缀 / 后缀规则的字符串（如游戏中筛选 "ender_" 开头的末地物品）。
"""
