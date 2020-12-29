from py.base_char import *
import py.lite

黑曜神等级 = 100 + 5


class skill0(主动技能):
    名称 = '魔灵召唤：波拉斯'
    备注 = '(每秒DPS)'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 444.15
    成长 = 13.94
    攻击次数 = 12 / 4 / 20
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return 1.0


class skill1(主动技能):
    名称 = '魔灵召唤：瓦尔琪'
    备注 = '(每秒DPS)'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 328.09
    成长 = 14.5
    攻击次数 = 14 / 7 / 20
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return 1.0


class skill2(被动技能):
    名称 = '魔灵血统'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)


class skill3(被动技能):
    名称 = '力量法则'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['军团列阵', '魔幻旋风', '毁灭突进', '翔空剑', '聚灵升空剑', '魔神百裂拳', '黑暗冲击', '午夜嘉年华', '绚丽耀光', '魔灵乱舞', '黑曜之眸：亚丁降临']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.085 + 0.015 * self.等级, 5)


class skill4(主动技能):
    名称 = '魔灵召唤：狂暴布洛克'
    备注 = '(每秒DPS)'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 506.41
    成长 = 22.14
    攻击次数 = 14 / 5.5 / 20
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return 1.0


class skill5(主动技能):
    名称 = '绝对魅力'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['魔灵召唤：波拉斯', '魔灵召唤：瓦尔琪', '魔灵召唤：狂暴布洛克', '魔灵召唤：假面杰森', '魔灵召唤：大画家芭芘', '魔灵召唤：旋转小冯', '魔灵召唤：小吸血鬼夏伊', '魔灵召唤：大富翁鲁邦', '魔灵召唤：迪克老爹', '魔灵召唤：红心女王艾丽莎']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.012 * self.等级, 5)

    自定义描述 = 1
    描述 = ''

    def 技能描述(self, 武器类型):
        temp = ''
        temp += '加成倍率：%.1f%%' % (3.5 + 1.2 * self.等级) + '<br>'
        temp += '关联技能：魔灵召唤系列,'
        temp += self.描述 + ',魔灵炸弹(部分),毁灭突进(部分)'
        return temp


class skill6(主动技能):
    名称 = '魔灵召唤：假面杰森'
    备注 = '(每秒DPS)'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 800.21
    成长 = 34.68
    攻击次数 = 8 / 7 / 20
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return 1.0


class skill7(主动技能):
    名称 = '魔灵召唤：大画家芭芘'
    备注 = '(每秒DPS)'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 435.41
    成长 = 18.88
    攻击次数 = 14 / 5 / 20
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return 1.0


class skill8(主动技能):
    名称 = '魔灵召唤：旋转小冯'
    备注 = '(每秒DPS)'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 1444.80
    成长 = 61.64
    攻击次数 = 73 / 90 / 20
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return 1.0


class skill9(主动技能):
    名称 = '魔灵召唤：小吸血鬼夏伊'
    备注 = '(每秒DPS)'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 711.37
    成长 = 30.36
    攻击次数 = 14 / 3 / 20
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return 1.0


class skill10(主动技能):
    名称 = '魔灵召唤：大富翁鲁邦'
    备注 = '(每秒DPS)'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 1024.96
    成长 = 38.23
    攻击次数 = 18 / 5 / 20
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return 1.0


class skill11(主动技能):
    名称 = '魔灵召唤：迪克老爹'
    备注 = '(每秒DPS)'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 1179.84
    成长 = 55.34
    攻击次数 = 8 / 1.8 / 20
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return 1.0


class skill12(主动技能):
    名称 = '魔灵召唤：红心女王艾丽莎'
    备注 = '(每秒DPS)'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 1647.65
    成长 = 76.20
    攻击次数 = 12 / 1.8 / 20
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return 1.0


class skill13(主动技能):
    名称 = '军团列阵'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 3
    等级精通 = 60
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 4025, 4661, 5305, 5947, 6590, 7232, 7870, 8513, 9155, 9797, 10440, 11078, 11721, 12363, 13006, 13644, 14286, 14929, 15572, 16215, 16851, 17495, 18137, 18780, 19423, 20060, 20703, 21346,
          21988, 22631, 23270, 23912, 24553, 25197, 25834, 26477, 27120, 27763, 28405, 29042, 29685, 30328, 30971, 31614, 32251, 32893, 33537, 34178, 34821, 35460, 36102, 36743, 37387, 38025, 38667,
          39310, 39953, 40595, 41233, 41875, 42518, 43161, 43804, 44441, 45084, 45727, 46369, 47008, 47650, 48292]
    攻击次数 = 1
    CD = 5
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill14(主动技能):
    名称 = '连锁共振'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 1
    CD = 6
    TP成长 = 0.10
    TP上限 = 5
    关联技能 = ['魔灵召唤：波拉斯', '魔灵召唤：瓦尔琪', '魔灵召唤：狂暴布洛克', '魔灵召唤：假面杰森', '魔灵召唤：旋转小冯', '魔灵召唤：迪克老爹']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 7:
                return round(1.94 + 0.02 * self.等级, 5)
            else:
                return round(2.1 + 0 * (self.等级 - 7), 5)


class skill15(主动技能):
    名称 = '魔灵炸弹'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 546, 602, 658, 715, 771, 828, 884, 940, 998, 1054, 1111, 1167, 1223, 1280, 1336, 1392, 1449, 1505, 1562, 1618, 1674, 1731, 1788, 1844, 1899, 1956, 2013, 2071, 2127, 2183, 2239, 2296,
           2353, 2409, 2465, 2521, 2578, 2634, 2690, 2746, 2804, 2860, 2916, 2972, 3029, 3086, 3141, 3197, 3254, 3311, 3368, 3425, 3481, 3538, 3594, 3651, 3707, 3763, 3820, 3876, 3932, 3988, 4045,
           4102, 4158, 4214, 4271, 4327, 4383, 4439]  # jio踢
    攻击次数1 = 1
    数据2 = [0, 7621, 8393, 9166, 9940, 10711, 11486, 12258, 13032, 13805, 14578, 15351, 16124, 16897, 17669, 18443, 19216, 19990, 20763, 21538, 22309, 23085, 23855, 24626, 25401, 26174, 26948, 27721,
           28496, 29270, 30043, 30815, 31588, 32359, 33133, 33905, 34679, 35454, 36228, 37000, 37773, 38549, 39320, 40090, 40865, 41637, 42413, 43185, 43958, 44731, 45507, 46278, 47050, 47823, 48596,
           49370, 50143, 50916, 51688, 52464, 53236, 54008, 54781, 55554, 56330, 57101, 57876, 58646, 59422, 60196, 60966]  # 大爹
    攻击次数2 = 1
    CD = 12

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill16(主动技能):
    名称 = '魔幻旋风'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 722, 796, 869, 943, 1016, 1089, 1163, 1236, 1309, 1383, 1456, 1529, 1604, 1677, 1750, 1823, 1896, 1970, 2043, 2117, 2190, 2263, 2337, 2410, 2483, 2556, 2630, 2703, 2777, 2851, 2924,
           2996, 3070, 3143, 3217, 3290, 3364, 3437, 3510, 3584, 3657, 3730, 3804, 3877, 3950, 4024, 4098, 4170, 4243, 4317, 4391, 4463, 4538, 4611, 4684, 4757, 4831, 4904, 4977, 5051, 5124, 5198,
           5271, 5344, 5417, 5490, 5564, 5638, 5711, 5785]
    攻击次数1 = 1
    数据2 = [0, 242, 266, 291, 316, 339, 364, 389, 413, 437, 462, 487, 512, 536, 561, 585, 609, 634, 659, 683, 707, 732, 757, 781, 806, 830, 855, 878, 904, 929, 952, 977, 1002, 1027, 1051, 1075, 1100,
           1124, 1149, 1174, 1199, 1222, 1247, 1272, 1297, 1320, 1345, 1370, 1393, 1419, 1444, 1469, 1492, 1517, 1542, 1566, 1590, 1615, 1640, 1663, 1689, 1714, 1738, 1762, 1787, 1812, 1836, 1860,
           1885, 1910, 1935]  # 多段攻击
    攻击次数2 = 14
    CD = 7
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill17(主动技能):
    名称 = '毁灭突进'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 2732, 3004, 3282, 3563, 3839, 4117, 4387, 4665, 4946, 5225, 5500, 5778, 6052, 6333, 6605, 6883, 7160, 7439, 7713, 7991, 8268, 8543, 8828, 9098, 9379, 9652, 9930, 10209, 10484, 10759,
           11035, 11315, 11595, 11864, 12146, 12423, 12696, 12977, 13255, 13532, 13805, 14082, 14359, 14640, 14911, 15188, 15466, 15747, 16023, 16297, 16576, 16848, 17128, 17408, 17683, 17957, 18234,
           18512, 18793, 19065, 19346, 19627, 19898, 20176, 20448, 20729, 21006, 21283, 21560, 21836]  # 突进和最后一击
    攻击次数1 = 2
    数据2 = [0, 76, 84, 91, 100, 108, 116, 123, 131, 138, 146, 154, 161, 170, 178, 185, 193, 201, 208, 216, 223, 231, 239, 248, 255, 263, 270, 278, 286, 293, 301, 309, 317, 325, 332, 340, 348, 355, 363,
           371, 378, 387, 395, 402, 410, 418, 425, 433, 441, 448, 457, 465, 472, 480, 487, 495, 503, 510, 518, 526, 534, 542, 550, 557, 565, 572, 580, 588, 596, 604, 612]
    攻击次数2 = 5
    数据3 = [0, 230, 252, 275, 300, 323, 346, 369, 392, 415, 439, 462, 485, 509, 532, 555, 578, 602, 625, 648, 671, 694, 717, 742, 764, 787, 811, 834, 857, 881, 904, 927, 951, 974, 996, 1021, 1044,
           1066, 1090, 1113, 1136, 1160, 1183, 1206, 1230, 1253, 1276, 1300, 1323, 1346, 1369, 1393, 1415, 1439, 1462, 1485, 1509, 1532, 1555, 1578, 1602, 1625, 1648, 1672, 1695, 1717, 1742, 1764,
           1787, 1811, 1834]
    攻击次数3 = 5
    CD = 12
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill18(主动技能):
    名称 = '翔空剑'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 904, 996, 1087, 1178, 1271, 1362, 1454, 1546, 1638, 1730, 1821, 1913, 2004, 2096, 2188, 2280, 2372, 2463, 2556, 2647, 2738, 2830, 2922, 3013, 3105, 3197, 3290, 3381, 3473, 3563, 3656,
           3748, 3839, 3932, 4023, 4114, 4206, 4299, 4391, 4481, 4572, 4665, 4757, 4849, 4941, 5033, 5124, 5215, 5307, 5399, 5490, 5582, 5674, 5766, 5858, 5951, 6042, 6132, 6224, 6316, 6409, 6500,
           6591, 6684, 6775, 6867, 6958, 7050, 7142, 7233]  # 跳斩伤害
    攻击次数1 = 1
    数据2 = [0, 355, 392, 428, 464, 500, 537, 573, 609, 644, 681, 717, 753, 789, 826, 862, 898, 933, 970, 1007, 1042, 1078, 1115, 1150, 1187, 1223, 1259, 1295, 1332, 1367, 1404, 1440, 1475, 1513, 1549,
           1584, 1620, 1657, 1693, 1729, 1764, 1802, 1838, 1873, 1909, 1947, 1982, 2018, 2053, 2090, 2127, 2162, 2198, 2235, 2270, 2307, 2343, 2379, 2415, 2452, 2487, 2524, 2560, 2595, 2632, 2668,
           2704, 2740, 2776, 2813, 2849]  # 多段伤害
    攻击次数2 = 15
    数据3 = [0, 4017, 4427, 4835, 5246, 5656, 6062, 6470, 6879, 7286, 7697, 8107, 8515, 8921, 9331, 9743, 10150, 10557, 10967, 11375, 11784, 12196, 12602, 13012, 13420, 13832, 14237, 14645, 15056,
           15462, 15873, 16279, 16690, 17101, 17508, 17918, 18323, 18733, 19140, 19554, 19960, 20368, 20776, 21185, 21594, 22003, 22414, 22823, 23229, 23640, 24050, 24458, 24866, 25275, 25682, 26090,
           26501, 26909, 27319, 27726, 28134, 28543, 28953, 29361, 29773, 30180, 30588, 30996, 31406, 31813, 32226]  # 其余伤害整合
    攻击次数3 = 1
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * (self.攻击次数2 + self.TP等级) + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.23 + 0.09


class skill19(主动技能):
    名称 = '碎灵屠戮'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 7029, 7760, 8484, 9212, 9936, 10664, 11396, 12120, 12847, 13571, 14304, 15025, 15751, 16463, 17191, 17938, 18661, 19388, 20099, 20825, 21572, 22295, 23024, 23730, 24476, 25185, 25914,
           26638, 27366, 28112, 28821, 29552, 30274, 31002, 31746, 32457, 33174, 33904, 34639, 35362, 36088, 36812, 37539, 38273, 38996, 39725, 40447, 41175, 41909, 42629, 43353, 44079, 44813, 45536,
           46263, 46988, 47714, 48447, 49170, 49900, 50623, 51332, 52076, 52804, 53526, 54255, 54988, 55713, 56439, 57163]  # 挥斩伤害
    攻击次数1 = 1
    数据2 = [0, 39487, 43492, 47482, 51487, 55470, 59479, 63478, 67454, 71454, 75465, 79448, 83449, 87449, 91448, 95453, 99429, 103431, 107428, 111434, 115440, 119411, 123415, 127405, 131416, 133757,
           139410, 143412, 147406, 151398, 155393, 159400, 163397, 167391, 171374, 175365, 179378, 183382, 187372, 191365, 195367, 199369, 203348, 207351, 211336, 215352, 219336, 223342, 227343,
           231332, 235334, 239324, 243315, 247325, 251311, 255313, 259304, 263314, 267298, 271298, 275287, 279297, 283300, 287279, 291281, 295286, 299282, 303271, 307270, 311268, 315257]  # 爆炸整合
    攻击次数2 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.25
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.25 + 0.09
            self.CD *= 0.9


class skill20(主动技能):
    名称 = '聚灵升空剑'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 1892, 2084, 2277, 2470, 2661, 2852, 3045, 3237, 3430, 3621, 3813, 4005, 4198, 4389, 4581, 4773, 4966, 5158, 5349, 5541, 5734, 5926, 6118, 6309, 6502, 6693, 6887, 7078, 7270, 7462, 7653,
           7847, 8038, 8230, 8422, 8615, 8806, 9000, 9190, 9383, 9575, 9766, 9960, 10151, 10344, 10535, 10727, 10919, 11110, 11304, 11495, 11687, 11879, 12072, 12264, 12455, 12647, 12840, 13032,
           13223, 13416, 13608, 13800, 13992, 14183, 14376, 14568, 14761, 14952, 15145]
    攻击次数1 = 1
    数据2 = [0, 2272, 2502, 2732, 2963, 3193, 3423, 3654, 3885, 4116, 4346, 4576, 4807, 5037, 5267, 5497, 5729, 5959, 6189, 6420, 6650, 6880, 7111, 7341, 7572, 7803, 8033, 8263, 8494, 8724, 8954, 9185,
           9415, 9647, 9877, 10107, 10337, 10568, 10798, 11029, 11260, 11490, 11720, 11951, 12181, 12412, 12641, 12872, 13103, 13334, 13564, 13795, 14025, 14255, 14485, 14717, 14948, 15177, 15408,
           15637, 15869, 16099, 16328, 16560, 16791, 17021, 17252, 17482, 17712, 17942, 18173]
    攻击次数2 = 5
    数据3 = [0, 5680, 6255, 6831, 7407, 7984, 8559, 9137, 9712, 10287, 10864, 11441, 12016, 12593, 13169, 13745, 14322, 14898, 15472, 16050, 16626, 17202, 17777, 18354, 18930, 19506, 20083, 20659,
           21235, 21811, 22388, 22963, 23540, 24115, 24693, 25268, 25845, 26420, 26997, 27574, 28149, 28726, 29301, 29877, 30453, 31031, 31606, 32181, 32758, 33334, 33910, 34488, 35062, 35639, 36216,
           36791, 37367, 37944, 38520, 39096, 39673, 40248, 40824, 41401, 41977, 42553, 43129, 43705, 44282, 44857, 45434]
    攻击次数3 = 1
    CD = 40.0
    TP成长 = 0
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * (self.攻击次数2 + self.TP等级) + self.数据3[self.等级] * self.攻击次数3) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.23 + 0.08


class skill21(被动技能):
    名称 = '魔能榨取'
    所在等级 = 48
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 16:
                return round(1.015 + 0.015 * self.等级, 5)
            else:
                return round(1.295 + 0.020 * (self.等级 - 16), 5)


class skill22(主动技能):
    名称 = '魔神百裂拳'
    所在等级 = 50
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 1598, 1969, 2339, 2711, 3081, 3451, 3821, 4192, 4562, 4934, 5303, 5675, 6046, 6416, 6787, 7156, 7528, 7898, 8270, 8639, 9010, 9381, 9751, 10121, 10492, 10863, 11234, 11605, 11975, 12346,
           12716, 13087, 13457, 13828, 14198, 14569, 14940, 15311, 15682, 16052, 16422, 16793, 17164, 17534, 17905, 18275, 18647, 19017, 19387, 19757]
    攻击次数1 = 12
    攻击倍率1 = 1.1
    数据2 = [0, 9589, 11813, 14036, 16260, 18484, 20708, 22931, 25155, 27379, 29602, 31826, 34049, 36273, 38498, 40721, 42944, 45169, 47392, 49616, 51839, 54063, 56287, 58511, 60734, 62957, 65182,
           67406, 69628, 71852, 74077, 76300, 78524, 80747, 82971, 85195, 87418, 89641, 91867, 94090, 96313, 98537, 100760, 102984, 105208, 107432, 109655, 111879, 114103, 116326, 118550]
    攻击次数2 = 1
    攻击倍率2 = 1.0
    数据3 = [0, 6391, 7875, 9355, 10839, 12320, 13804, 15285, 16770, 18250, 19734, 21215, 22699, 24182, 25663, 27147, 28627, 30112, 31592, 33077, 34556, 36041, 37522, 39005, 40486, 41970, 43455, 44935,
           46420, 47900, 49384, 50864, 52349, 53829, 55313, 56794, 58278, 59758, 61242, 62727, 64206, 65691, 67172, 68656, 70136, 71621, 73101, 74585, 76066, 77550, 79030]
    攻击次数3 = 3
    攻击倍率3 = 1.1
    CD = 145

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 * self.攻击倍率1 + self.数据2[self.等级] * self.攻击次数2 * self.攻击倍率2 + self.数据3[self.等级] * self.攻击次数3 * self.攻击倍率3) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill23(主动技能):
    名称 = '黑暗冲击'
    备注 = '(完全打满)'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 1208, 1330, 1453, 1575, 1698, 1820, 1943, 2065, 2188, 2310, 2433, 2555, 2678, 2800, 2923, 3045, 3168, 3290, 3413, 3535, 3658, 3780, 3904, 4026, 4149, 4271, 4394, 4516, 4639, 4761, 4884,
           5006, 5129, 5251, 5374, 5496, 5619, 5742, 5864, 5987, 6109, 6232, 6354, 6477, 6599, 6722, 6845, 6967, 7090, 7213]
    攻击次数1 = 4
    数据2 = [0, 960, 1057, 1156, 1252, 1350, 1447, 1545, 1642, 1740, 1837, 1935, 2032, 2130, 2227, 2325, 2422, 2519, 2617, 2714, 2811, 2908, 3007, 3104, 3201, 3298, 3397, 3494, 3591, 3688, 3786, 3884,
           3981, 4078, 4176, 4273, 4371, 4468, 4566, 4663, 4761, 4858, 4955, 5053, 5150, 5248, 5345, 5443, 5540, 5637, 5735]
    攻击次数2 = 9
    数据3 = [0, 1912, 2106, 2300, 2494, 2687, 2881, 3076, 3270, 3463, 3658, 3852, 4045, 4240, 4434, 4628, 4821, 5015, 5209, 5404, 5597, 5791, 5986, 6180, 6373, 6567, 6762, 6955, 7149, 7343, 7537, 7731,
           7925, 8119, 8314, 8507, 8701, 8895, 9090, 9283, 9477, 9671, 9865, 10058, 10253, 10447, 10641, 10835, 11029, 11223, 11417]
    攻击次数3 = 3
    CD = 30
    TP成长 = 0.12
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.15
        elif x == 1:
            self.倍率 *= 1.15 + 0.09


class skill24(主动技能):
    名称 = '午夜嘉年华'
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 1089, 1201, 1311, 1422, 1530, 1642, 1752, 1863, 1973, 2084, 2194, 2305, 2415, 2526, 2637, 2747, 2856, 2967, 3080, 3189, 3299, 3410, 3521, 3631, 3742, 3852, 3962, 4074, 4184, 4294, 4404,
          4516, 4625, 4736, 4848, 4958, 5068, 5179, 5287, 5400, 5510, 5620, 5732, 5841, 5951, 6063, 6174, 6283, 6395, 6505]
    攻击次数 = 31
    CD = 50.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.09
            self.攻击次数 += 4
        elif x == 1:
            self.倍率 *= 1.09 + 0.07
            self.攻击次数 += 4


class skill25(被动技能):
    名称 = '亚丁之力'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    关联技能 = ['魔幻旋风', '毁灭突进', '翔空剑', '聚灵升空剑', '魔神百裂拳', '黑暗冲击', '午夜嘉年华', '绚丽耀光', '魔灵乱舞', '黑曜之眸：亚丁降临']
    关联技能2 = ['魔灵召唤：波拉斯', '魔灵召唤：瓦尔琪', '魔灵召唤：狂暴布洛克', '魔灵召唤：假面杰森', '魔灵召唤：大画家芭芘', '魔灵召唤：旋转小冯', '魔灵召唤：小吸血鬼夏伊', '魔灵召唤：大富翁鲁邦', '魔灵召唤：迪克老爹', '魔灵召唤：红心女王艾丽莎']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.28 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.14 + 0.02 * self.等级, 5)

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill26(主动技能):
    名称 = '绚丽耀光'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 15307, 16860, 18413, 19966, 21519, 23072, 24625, 26178, 27731, 29284, 30837, 32389, 33943, 35496, 37048, 38602, 40155, 41707, 43261, 44813, 46366, 47920, 49472, 51025, 52578, 54131,
           55684, 57237, 58790, 60343, 61896, 63449, 65002, 66554, 68108, 69660, 71213, 72767, 74319, 75872, 77426, 78978, 80531, 82084, 83637, 85190, 86743, 88296, 89849, 91402, 92955, 94508, 96061,
           97614, 99166, 100720, 102273, 103825, 105379, 106931, 108484, 110038, 111590, 113143, 114697, 116249, 117802, 119355, 120908, 122461]
    攻击次数1 = 1
    数据2 = [0, 3571, 3934, 4296, 4659, 5021, 5384, 5746, 6108, 6470, 6833, 7195, 7558, 7920, 8282, 8644, 9007, 9369, 9732, 10094, 10456, 10819, 11181, 11544, 11906, 12269, 12631, 12993, 13355, 13718,
           14080, 14443, 14805, 15167, 15529, 15892, 16254, 16617, 16979, 17341, 17703, 18066, 18428, 18791, 19153, 19516, 19877, 20240, 20602, 20965, 21327, 21690, 22052, 22414, 22776, 23139, 23501,
           23864, 24226, 24588, 24950, 25313, 25675, 26038, 26400, 26762, 27124, 27487, 27849, 28212, 28574]
    攻击次数2 = 10
    CD = 40.0
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 *= 1.3
            self.攻击次数2 *= 1.32


class skill27(主动技能):
    名称 = '魔灵乱舞'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 5018, 5528, 6037, 6545, 7055, 7564, 8073, 8582, 9092, 9600, 10110, 10619, 11127, 11637, 12147, 12655, 13165, 13674, 14182, 14692, 15201, 15710, 16220, 16728, 17237, 17747, 18255, 18765,
          19275, 19783, 20292, 20802, 21310, 21820, 22329, 22838, 23347, 23857, 24365, 24874, 25384, 25893, 26402, 26911, 27420, 27929, 28439, 28948, 29457, 29966, 30475, 30984, 31493, 32003, 32512,
          33020, 33530, 34039, 34548, 35058, 35567, 36075, 36585, 37094, 37602, 38113, 38622, 39130, 39640, 40149]
    攻击次数 = 12
    CD = 50.0
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23


class skill28(主动技能):
    名称 = '黑曜之眸：亚丁降临'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 9692, 11938, 14184, 16432, 18680, 20929, 23174, 25424, 27669, 29916, 32165, 34414, 36661, 38910, 41155, 43402, 45650, 47899, 50147, 52394, 54638, 56887, 59136, 61383, 63631, 65881,
           68123, 70372, 72622, 74868, 77117, 79367, 81610, 83858, 86105, 88354, 90603, 92849, 95095, 97345, 99590, 101840, 104090, 106335, 108585, 110830, 113077, 115326, 117572, 119821, 122070,
           124313, 126562, 128810, 131058, 133307, 135555, 137799, 140046, 142294, 144544, 146791, 149039, 151284, 153533, 155781, 158029, 160278, 162525, 164769]
    攻击次数1 = 11
    数据2 = [0, 401, 494, 586, 680, 773, 866, 959, 1051, 1144, 1237, 1330, 1423, 1516, 1609, 1702, 1795, 1887, 1981, 2074, 2167, 2260, 2353, 2446, 2538, 2631, 2724, 2817, 2910, 3003, 3096, 3189, 3282,
           3374, 3468, 3561, 3654, 3747, 3840, 3933, 4025, 4118, 4211, 4304, 4397, 4491, 4583, 4676, 4769, 4862, 4955, 5048, 5141, 5234, 5327, 5420, 5512, 5605, 5698, 5791, 5884, 5978, 6071, 6164,
           6256, 6349, 6442, 6535, 6628, 6721, 6814]
    攻击次数2 = 20
    CD = 180

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill29(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill30(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    学习间隔 = 2
    等级精通 = 1
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class skill31(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


skill_list = []
i = 0
while i >= 0:
    try:
        exec('skill_list.append(skill' + str(i) + '())')
        i += 1
    except:
        i = -1

skill_sn = dict()
for i in range(len(skill_list)):
    skill_sn[skill_list[i].名称] = i

skill_sn_awaking1 = 0
skill_sn_awaking2 = 0
skill_sn_awaking3 = 0
for i in skill_list:
    if i.所在等级 == 50:
        skill_sn_awaking1 = skill_sn[i.名称]
    if i.所在等级 == 85:
        skill_sn_awaking2 = skill_sn[i.名称]
    if i.所在等级 == 100:
        skill_sn_awaking3 = skill_sn[i.名称]

黑曜神护石选项 = ['无']
for i in skill_list:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        黑曜神护石选项.append(i.名称)

黑曜神符文选项 = ['无', '军团列阵', '魔幻旋风', '毁灭突进', '翔空剑', '碎灵屠戮', '聚灵升空剑', '黑暗冲击', '午夜嘉年华', '绚丽耀光', '魔灵乱舞']


class character(py.lite.char_base):
    def 角色賦予(self):
        self.attr["实际名称"] = '黑曜神'
        self.attr["角色"] = '守护者'
        self.attr["职业"] = '混沌魔灵'

        self.attr["武器选项"] = ['太刀', '钝器', '巨剑', '短剑']

        self.attr["类型"] = '魔法固伤'
        self.attr["防具类型"] = '重甲'
        self.attr["防具精通属性"] = ['智力']

        self.attr["主BUFF"] = 2

        self.attr["远古记忆"] = 10

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [1, 1, 1, 1, 15, 10, 1, 1, 1, 1, 1, 33, 31, 31, 1, 43, 1, 38, 36, 33, 31, 20, 12, 1, 18, 11, 16, 13, 5, 4, 1, 2]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['20', '20', '', '', '20', '', '20', '20', '20', '20', '20', '20', '20', '4', '1', '2', '0', '2', '2', '1', '1', '', '1', '0', '1', '', '1', '1', '1', '', '', '']
        self.attr["技能宠物次数"] = [10, 10, 0, 0, 10, 0, 10, 10, 10, 10, 10, 10, 10, 2, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '太极天帝剑']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "太刀"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 10]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "魔灵血统"
        self.attr["右槽白金技能"] = "魔灵血统"
        self.attr["时装上衣技能"] = "魔灵血统"

        self.attr["三觉技能选择"] = "一觉序号"

    def 三觉技能选择(self):
        for i, 技能 in enumerate(self.attr["技能栏"]):
            if 技能.名称 == "觉醒之抉择":
                技能.关联技能 = [self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].名称]

    def 被动倍率计算(self):
        super().被动倍率计算()
        技能栏 = self.attr["技能栏"]

        x = 技能栏[skill_sn['连锁共振']].TP等级
        技能栏[skill_sn['魔灵召唤：波拉斯']].攻击次数 *= 1 + 0.1 * x
        技能栏[skill_sn['魔灵召唤：狂暴布洛克']].攻击次数 *= 1 + 0.1 * x
        技能栏[skill_sn['魔灵召唤：假面杰森']].攻击次数 *= 1 + 0.1 * x
        技能栏[skill_sn['魔灵召唤：旋转小冯']].攻击次数 *= 1 + 0.1 * x
        技能栏[skill_sn['魔灵召唤：迪克老爹']].攻击次数 *= 1 + 0.1 * x

        x = 技能栏[skill_sn['绝对魅力']].等级
        技能栏[skill_sn['毁灭突进']].攻击次数2 *= 1.035 + 0.012 * x
        技能栏[skill_sn['毁灭突进']].攻击次数3 *= 1.035 + 0.012 * x
        技能栏[skill_sn['魔灵炸弹']].攻击次数2 *= 1.035 + 0.012 * x

        # if '碎灵屠戮' in [self.护石栏[0], self.护石栏[1], self.护石栏[2]]:
        if '碎灵屠戮' in [self.attr["护石第一栏"], self.attr["护石第二栏"], self.attr["护石第三栏"]]:
            技能栏[skill_sn['碎灵屠戮']].攻击次数1 *= 1.035 + 0.012 * x  # 无碎灵屠戮护石，此条不生效
            技能栏[skill_sn['绝对魅力']].描述 = '碎灵屠戮'
        else:
            技能栏[skill_sn['绝对魅力']].描述 = '碎灵屠戮(部分)'
        技能栏[skill_sn['碎灵屠戮']].攻击次数2 *= 1.035 + 0.012 * x
