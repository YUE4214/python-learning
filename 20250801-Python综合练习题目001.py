# 《星露谷物语》农场作物管理系统
# 项目说明：使用变量、数据类型、列表、元组、字典、集合、循环、分支等基础语法
# 模拟星露谷物语中的作物种植、生长、收获及售卖过程，实现农场日常管理

# 需求说明：
# 1. 初始化农场信息：
#   - 创建玩家字典player，包含"name"（通过input输入）、"money"（初始500金）、"level"（种植等级1）
#   - 创建作物字典crops，键为作物名，值为(生长周期, 每日浇水需求, 单株产量, 单价)：
#     "小麦": (4, True, 10, 5)  # 生长4天，每天需浇水，单株产10个，每个5金
#     "草莓": (7, True, 3, 15)
#     "南瓜": (10, True, 1, 100)
#   - 创建已解锁作物集合unlocked_crops，初始包含"小麦"
#   - 创建农场地块列表farm，初始为5块空土地（用"空"表示）

# 2. 种植作物流程：
#   - 显示可种植作物（仅已解锁），让玩家选择种植位置（1-5）和作物
#   - 检查玩家金钱是否足够（每种作物种子价格：小麦20金，草莓50金，南瓜100金）
#   - 种植成功：地块状态改为(作物名, 已生长天数, 是否浇水)，扣除金钱
#   - 提示种植结果及当前农场状态

# 3. 每日管理流程：
#   - 模拟7天种植周期，每天执行：
#     a. 显示当前农场各地块状态（作物名、生长进度）
#     b. 玩家选择需要浇水的地块（可多选，用空格分隔编号）
#     c. 自动更新作物生长：已浇水的地块生长天数+1，未浇水则不变
#     d. 检查是否成熟（已生长天数≥生长周期），成熟作物标记为"可收获"

# 4. 收获与售卖：
#   - 玩家可在任意天数选择收获成熟作物，收获后地块变回"空"
#   - 计算收获总量（单株产量×数量），并询问是否售卖（是/否）
#   - 售卖后金钱增加（总量×单价），提示收入及当前金钱

# 5. 统计与升级：
#   - 7天结束后，统计总收获量、总销售额、剩余金钱
#   - 若总销售额≥1000金，种植等级+1，解锁"南瓜"作物
#   - 打印最终农场报告

# 请从初始化代码开始实现，按流程逐步完成功能
# （提示：用循环控制天数，分支处理选择，列表维护地块状态）


# 初始化农场信息
# TODO：补充代码
#1.1初始化玩家信息
print("===== 星露谷物语农场初始化 =====")
#玩家字典
player = {
    "name": input("请输入您的名字："),
    "money": 500,
    "level": 1
}

#1.2作物字典（生长周期，每日浇水需求，单株产量，单价）
crops = {
    "小麦": (4, True, 10, 50),
    "草莓": (7, True, 3, 150),
    "南瓜": (10, True, 1, 1000)
}

#种子价格字典
seeds_prices = {
    "小麦": 20,
    "草莓": 50,
    "南瓜": 100
}

#1.3已经解锁的作物集合
unlocked_crops = ("小麦",) #已解锁作物

#1.4当前的土地状态列表
farm = ["空", "空", "空", "空", "空"] #当前土地状态

#1.5总销售额统计
total_sales = 0
#打印初始化信息
def plant_crop():
    global farm, player
    print("\n===== 玩家初始化完成 =====")
    print(f"当前可种植作物（已解锁）：{unlocked_crops}")
    print(f"玩家名称：{player['name']}")
    print(f"初始状态：金币{player['money']} | 等级{player['level']}")
    print(f"土地状态：{farm[0]} | {farm[1]} | {farm[2]} | {farm[3]} | {farm[4]}")
    # 种植作物流程
    # TODO：补充代码
    #选择地块
    while True:
        if "空" not in farm:
            print("所有地块已种满")
            break
        plot = input("请选择要种植的地块编号（1-5）：")
        if plot.isdigit() and 1 <= int(plot) <= 5:
            plot_idx = int(plot) - 1
            if farm[plot_idx] == "空":
                break
            else:
                print("该地块已有作物，请重新选择")
        else:
            print("请输入1-5之间的数字")
    #选择作物
    while True:
        if "空" not in farm:
            print("所有地块已种满")
            break
        crop = input(f"请选择要种植的作物（{unlocked_crops}）：")
        if crop in unlocked_crops:
            #检查金钱
            if player["money"] >= seeds_prices[crop]:
                player["money"] -= seeds_prices[crop]
                farm[plot_idx] = (crop, 0, False)
                print(f"成功在{plot}号地块种植{crop}，花费{seeds_prices[crop]}金")
                print(f"剩余金币{player['money']}")
                break
            else:
                print(f"当前金币不足！{crop}种子需要{seeds_prices[crop]}金")
        else:
            print(f"未解锁该作物，请从{unlocked_crops}中选择")

# 收获与售卖功能
# TODO：补充代码
def harvest_crop():
    global farm, player, total_sales
    print("\n===== 收获作物 =====")
    mature_plots = []
    for i in range(5):
        crop_name, growth_days, _ = farm[i]
        growth_cycle = crops[crop_name][0]
        if growth_days >= growth_cycle:
            mature_plots.append(i+1) #记录成熟地块编号

    if not mature_plots:
        print("没有成熟的作物可收获")
        return
    print(f"可收获的地块：{mature_plots}")
    while True:
        plot = input("请输入要收获的地块编号（1-5）：")
        if plot.isdigit() and int(plot) in mature_plots:
            plot_idx = int(plot) - 1
            crop_name, _, _ = farm[plot_idx]
            yield_per_plant = crops[crop_name][2]
            price = crops[crop_name][3]
            total = yield_per_plant * price

            #收获清空地块
            farm[plot_idx] = "空"
            print(f"收获{crop_name}{yield_per_plant}个，价值{total}金")

            #询问是否售卖
            sell = input("是否立即售卖？（是/否）：")
            if sell == "是":
                player["money"] += total
                total_sales += total
                print(f"已售卖，获得{total}金，当前金币：{player['money']}金")
            break #这里没有定义不售卖的作物存储在哪，后续相当于这部分作物消失了
        else:
            print(f"请从可收获地块{mature_plots}中选择")

# 每日管理流程（7天循环）
# TODO：补充代码
for day in range(1, 8):
    print(f"\n===== 第{day}天 =====")

    #显示当前农场状态
    for i in range(5):
        if farm[i] == "空":
            status = "空"
        else:
            crop_name, growth_days, watered = farm[i]
            growth_cycle = crops[crop_name][0]
            status = f"{crop_name}（生长{growth_days}/{growth_cycle}）天，{'已浇水' if watered else '未浇水'}"
            if growth_days >= growth_cycle:
                status += "，可收获"
            else:
                status += "，未成熟"
        print(f"{i+1}号地块：{status}")

    #每日操作
    while True:
        action = input("\n请选择操作：1.种植作物 2.浇水 3.收获作物 4.结束当天：")
        if action == "1":
            plant_crop()
        elif action == "2":
            while True:
                water_plots = input("请输入需要浇水的地块编号（多个使用空格分隔，如1 3）：").split()
                valid = True
                for p in water_plots:
                    if p.isdigit() and 1 <= int(p) <= 5:
                        plot_idx = int(p) - 1
                        if farm[plot_idx] != "空":
                            #更新地块浇水状态
                            crop_name, growth_days, _ = farm[plot_idx]
                            growth_days += 1
                            farm[plot_idx] = (crop_name, growth_days, True)
                            print(f"{p}好地块已浇水，作物成功生长天数加1")
                        else:
                            print(f"{p}号地块为空，无需浇水")
                    else:
                        print(f"{p}号地块不是有效的地块编号")
                        valid = False
                if valid:
                    break
        elif action == "3":
            harvest_crop()
        elif action == "4":
            #结束自动浇水
            for i in range(5):
                if farm[i] != "空":
                    crop_name, growth_days, watered = farm[i]
                    if watered:
                        farm[i] = (crop_name, growth_days + 1, False) #每日重置浇水状态
            print("当天结束，作物成功生长天数+1")
            break
        else:
            print("请输入正确的操作指令（1 2 3 4）")


#统计和升级
print(f"\n===== 7天种植周期结束 =====")
print(f"农场主：{player['name']}")
print(f"最终农业等级：{player['level']}")
print(f"总销售额：{total_sales}金")
print(f"剩余金币：{player['money']}金")

if total_sales >= 1000:
    player["level"] += 1
    unlocked_crops.add("南瓜")
    print("恭喜！种植等级提升至2级，已解锁新作物：南瓜")
else:
    print("继续努力，总销售额达到1000金可升级并解锁新作物")
print("===== 农场管理报告结束 =====")




# 统计与升级
# TODO：补充代码