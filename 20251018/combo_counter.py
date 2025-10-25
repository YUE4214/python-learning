def create_combo_counter():
    """闭包：创建连击计数器，保留连击数状态"""
    combo = 0 # 外层函数变量（被内函数引用）
    def counter():
        nonlocal combo # 声明引用外层变量
        combo += 1 # 每次调用+1
        current = combo # 记录当前连击数（重置前）
        if combo >= 10:
            combo = 0 # 达到10则重置
        return current # 返回当前连击数
    return counter # 返回内函数（闭包）

# 测试代码：仅在直接运行该模块时执行
if __name__ == "__main__":
    print("测试连击计数器：")
    player_combo = create_combo_counter()
    # 测试12次调用（触发一次重置）
    for i in range(12):
        print(f"第{i+1}次攻击，连击数：{player_combo()}")
    # 输出应为：1,2,...,10,1,2