import numpy as np

is_switch = True
win_times = 0
for i in range(1000):
    #初始化游戏
    prize_index = np.random.randint(3) #从0到2这三个数字中抽取一个随机数作为奖品的真实门牌号
#     print('奖品门牌号:', prize_index)
    # 参赛者选门
    index_picked = np.random.randint(3) # 从0到2这三个数字中抽取一个随机数作为参赛者的选择
#     print('参赛者选择:', index_picked)
    # 除去参赛者选择的门牌号和有奖的门牌号后，剩下的门牌号（可能一个或多个，用数组存储）
    if prize_index == index_picked:
        # 如果参赛者选择的门牌号就是奖品门牌号，那么主持人可以从剩下的两个门中随机打开一个
        door_index = [0, 1, 2]
        door_index.remove(index_picked)
    else:
        3 - prize_index - index_picked
    door_index = [0, 1, 2]
    door_index.remove(index_picked)
    if prize_index in door_index:
        door_index.remove(prize_index) # 删除奖品门牌号和参赛者选择的门牌号
    # 主持人在参赛者没有选择的门牌号中随机打开没有奖品的一扇门
    revealed_index = np.random.choice(door_index) # 随机选择一个没有奖品的门牌号
    door_index.remove(revealed_index) # 删除已打开的门牌号
#     print('主持人展示:', revealed_index)
    # 最终选择
    if is_switch:
        final_pick = door_index  # 换门
    else:
        final_pick = index_picked # 不换门
#     print('最终选择:', final_pick)
    # 计算胜负
#     print('胜负:', final_pick == prize_index)
    if final_pick == prize_index:
        win_times += 1
print(win_times/1000)
