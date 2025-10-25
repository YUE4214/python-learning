def calc_drop_rate(item_id, player_luck):
    """计算物品掉落概率 = 基础概率 +幸运值影响"""
    base_chance = 0.1
    return base_chance + player_luck * 0.01

# from .import weapon_tools
# print(weapon_tools.calc_weapon_damage(45,12))