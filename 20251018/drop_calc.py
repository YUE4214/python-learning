def calc_total_drop(initial_drop):
    """
    递归计算总掉落数
    :param initial_drop: 初始掉落数
    :return: 总掉落数（当前层 + 下一层掉落数）
    """
    if initial_drop == 0:
        return 0
    # 递归步骤：当前掉落 + 下一层掉落 // 2(向下取整)
    return initial_drop + calc_total_drop(initial_drop // 2)

# 测试代码：仅在直接运行该模块时执行
if __name__ == "__main__":
    print("测试装备掉落计算：")
    print(f"初始掉落5件，总掉落：{calc_total_drop(5)}")  # 5+2+1+0=8
    print(f"初始掉落10件，总掉落：{calc_total_drop(10)}")  # 10+5+2+1+0=18
