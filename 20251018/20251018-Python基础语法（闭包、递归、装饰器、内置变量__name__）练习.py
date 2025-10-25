from drop_calc import calc_total_drop
from combo_counter import create_combo_counter
from skill_decorator import skill_log_decorator
# 题目 1：递归 —— 怪物装备掉落计算
# 游戏中，击败怪物的装备掉落遵循 “每层掉落数为上一层的一半（向下取整），直到掉落为 0” 的规则。
# 例如：初始掉落5件，总掉落为5+2+1+0=8。请用递归函数实现 calc_total_drop(initial_drop)，计算总掉落装备数量。
print(calc_total_drop(5))
# 题目 2：闭包 —— 角色连击计数器
# 设计一个闭包实现 “角色连击计数” 功能：
# 每次调用计数器，连击数 + 1；
# 当连击数达到10时，重置为0；
# 返回当前连击数（重置前的数值）。
# 要求通过闭包保留 “连击数” 的状态。
once_combo = create_combo_counter()
print("当前连击次数：", once_combo())
print("当前连击次数：", once_combo())
print("当前连击次数：", once_combo())
# 题目 3：装饰器 —— 技能释放日志增强
# 为游戏的 “技能释放函数” 添加装饰器，实现：
# 技能释放前，打印 “[技能]XXX 开始释放...”；
# 技能释放后，打印 “[技能]XXX 释放完毕！”。
# 例如：调用 fireball() 后，输出：
# plaintext
# [技能]火球术 开始释放...
# 火球术造成100点伤害！
# [技能]火球术 释放完毕！
@skill_log_decorator
def fireball():
    return "火球术造成100点伤害！"
print(fireball())

@skill_log_decorator
def thunder():
    return "雷击术造成150点伤害！"
print(thunder())

# 题目 4：综合应用 +__name__—— 游戏功能模块化
# 将上述 3 个功能分别封装为独立模块，并通过if __name__ == "__main__":添加测试逻辑：
# 创建模块 drop_calc.py：包含题目 1 的递归函数，且直接运行时测试calc_total_drop(5)和calc_total_drop(10)。
# 创建模块 combo_counter.py：包含题目 2 的闭包函数，且直接运行时测试连击计数器的 “累加→重置” 流程。
# 创建模块 skill_decorator.py：包含题目 3 的装饰器，且直接运行时测试装饰器对fireball()、thunder()两个技能的增强效果。
# 创建主模块 main_game.py：导入上述 3 个模块，演示在 “游戏主逻辑” 中如何使用这些功能。
# 解题提示
# 题目 1：递归的终止条件是 “掉落数为 0”，递归步骤是 “当前掉落数 + 下一层掉落数（当前数 //2）”。
# 题目 2：外层函数定义 “连击数” 变量，内层函数实现 “累加→判断→重置” 逻辑，外层函数返回内层函数。
# 题目 3：装饰器本质是 “接受函数为参数的闭包”，在wrapper中添加前后打印逻辑。
# 题目 4：每个功能模块的测试代码需放在if __name__ == "__main__":下，确保 “导入时不执行测试，直接运行时执行测试”。

