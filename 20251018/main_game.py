# 导入三个功能模块
from drop_calc import calc_total_drop
from combo_counter import create_combo_counter
from skill_decorator import fireball, thunder


def main_game():
    """游戏主逻辑演示"""
    print("=== 游戏开始 ===")

    # 1. 测试装备掉落
    boss_drop = 20
    print(f"击败BOSS，初始掉落{boss_drop}件装备，总掉落：{calc_total_drop(boss_drop)}")  # 20+10+5+2+1+0=38

    # 2. 测试连击计数
    print("\n=== 玩家攻击 ===")
    player_combo = create_combo_counter()
    for i in range(15):
        print(f"攻击{i + 1}：连击数{player_combo()}")  # 1-10后重置为1-5

    # 3. 测试技能释放
    print("\n=== 释放技能 ===")
    print(fireball())
    print(thunder())

    print("\n=== 游戏结束 ===")


# 主程序入口：仅在直接运行main_game.py时执行
if __name__ == "__main__":
    main_game()