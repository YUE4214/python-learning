def skill_log_decorator(func):
    """装饰器：为技能函数添加释放前后的日志"""
    def wrapper(*args, **kwargs):
        # 技能释放前：打印开始日志（用func.__name__获取技能名）
        print(f"[技能]{func.__name__} 开始释放...")
        # 执行原技能函数，获取结果
        result = func(*args, **kwargs)
        # 技能释放后：打印结束日志
        print(f"[技能]{func.__name__} 释放完毕！")
        return result  # 返回技能结果
    return wrapper


# 测试用的技能函数（被装饰）
@skill_log_decorator
def fireball():
    return "火球术造成100点伤害！"

@skill_log_decorator
def thunder():
    return "雷击术造成150点伤害！"


# 测试代码：仅在直接运行该模块时执行
if __name__ == "__main__":
    print("测试技能装饰器：")
    print(fireball())  # 触发装饰器日志
    print(thunder())   # 触发装饰器日志