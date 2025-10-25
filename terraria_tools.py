def calc_damage(base_damage, multiplier):
    """计算武器最终伤害 = 基础伤害 * 倍率"""
    return base_damage * multiplier

def drop_chance(item_id, player_luck):
    """计算物品掉落概率 = 基础概率 +幸运值影响"""
    base_chance = 0.1
    return base_chance + player_luck * 0.01

MAX_HEALTH = 500 # 玩家最大生命值500