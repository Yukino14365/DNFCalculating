﻿from math import *
from py.base_char import *
import py.lite


class skill0(主动技能):
    名称 = '变异苍蝇拍'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据 = [0, 5722, 6301, 6884, 7464, 8045, 8625, 9206, 9785, 10367, 10947, 11529, 12109, 12690, 13270, 13852, 14431, 15010, 15591, 16173, 16754, 17333, 17915, 18495, 19076, 19656, 20238, 20818, 21400,
          21978, 22559, 23140, 23721, 24301, 24883, 25463, 26043, 26623, 27204, 27784, 28364, 28947, 29526, 30107, 30688, 31268, 31848, 32430, 33011, 33591, 34172, 34753, 35332, 35912, 36493, 37073,
          37655, 38235, 38816, 39396, 39978, 40557, 41139, 41720, 42301, 42880, 43461, 44041, 44622, 45202, 45784]
    CD = 6.4
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 0.1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill1(被动技能):
    名称 = '亲和法米利尔'
    所在等级 = 15
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级, 5)


class skill2(主动技能):
    名称 = '改良舒露露'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据 = [0, 6419, 7070, 7721, 8373, 9023, 9675, 10326, 10977, 11630, 12281, 12931, 13583, 14234, 14886, 15536, 16187, 16839, 17490, 18142, 18793, 19444, 20095, 20746, 21397, 22048, 22699, 23352,
          24003, 24654, 25306, 25957, 26609, 27259, 27909, 28561, 29212, 29864, 30515, 31166, 31819, 32470, 33122, 33773, 34421, 35074, 35725, 36376, 37028, 37679, 38331, 38982, 39633, 40286, 40937,
          41586, 42237, 42888, 43541, 44192, 44843, 45495, 46146, 46798, 47449, 48099, 48750, 49401, 50053, 50704, 51355]
    CD = 16.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill3(主动技能):
    名称 = '熔岩药瓶失败'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 26
    数据 = [0, 6927, 8031, 9137, 10242, 11346, 12451, 13555, 14659, 15764, 16868, 17973, 19078, 20182, 21289, 22393, 23496, 24601, 25705, 26810, 27915, 29020, 30126, 31230, 32332, 33436, 34541, 35648,
          36752, 37857, 38961, 40064, 41169, 42274, 43379, 44484, 45589, 46694, 47798, 48902, 50006, 51111, 52216, 53320, 54425, 55530, 56635, 57738, 58843, 59948, 61053, 62157, 63262, 64366, 65471,
          66575, 67679, 68784, 69889, 70994, 72099, 73203, 74308, 75411, 76516, 77621, 78725, 79830, 80934, 82040, 83143]
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill24(主动技能):
    名称 = '熔岩药瓶成功'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 26
    数据1 = [0, 1884, 2187, 2488, 2785, 3083, 3383, 3687, 3988, 4290, 4590, 4889, 5191, 5492, 5792, 6094, 6393, 6691, 6992, 7294, 7594, 7895, 8198, 8498, 8798, 9101, 9399, 9698, 9998, 10301, 10601,
           10902, 11204, 11502, 11803, 12106, 12406, 12704, 13002, 13307, 13605, 13906, 14208, 14508, 14809, 15112, 15412, 15715, 16008, 16311, 16612, 16912, 17215, 17515, 17813, 18116, 18416, 18718,
           19020, 19317, 19616, 19916, 20218, 20520, 20823, 21123, 21422, 21725, 22026, 22324, 22623]
    攻击次数1 = 6
    数据2 = [0, 103, 120, 135, 152, 169, 184, 201, 218, 234, 250, 267, 284, 300, 316, 333, 349, 364, 382, 398, 415, 430, 446, 464, 481, 497, 512, 529, 546, 561, 578, 594, 611, 627, 644, 660, 677, 693,
           709, 726, 742, 758, 775, 792, 807, 824, 841, 857, 873, 890, 906, 922, 939, 955, 972, 988, 1005, 1021, 1038, 1054, 1070, 1087, 1104, 1119, 1136, 1153, 1169, 1185, 1202, 1218, 1233]
    攻击次数2 = 10

    # 灼烧
    数据3 = [0, 12, 14, 16, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 96, 98,
           100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 144]
    攻击次数3 = 10
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill4(主动技能):
    名称 = '魔道酸云雨'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 26
    数据1 = [0, 194, 224, 254, 285, 315, 346, 378, 409, 439, 470, 501, 531, 562, 594, 625, 655, 686, 717, 747, 777, 808, 841, 869, 901, 932, 964, 993, 1024, 1054, 1085, 1117, 1148, 1178, 1209, 1240,
           1271, 1300, 1333, 1364, 1394, 1424, 1456, 1487, 1517, 1547, 1580, 1608, 1640, 1671, 1702, 1733, 1763, 1793, 1823, 1856, 1887, 1918, 1947, 1979, 2010, 2040, 2070, 2103, 2132, 2164, 2194,
           2226, 2255, 2287, 2316]
    攻击次数1 = 36
    # 大成功闪电部分未加强
    数据2 = [0, 994, 1153, 1310, 1471, 1631, 1787, 1947, 2105, 2263, 2423, 2579, 2740, 2900, 3058, 3217, 3375, 3534, 3692, 3851, 4009, 4166, 4325, 4486, 4646, 4801, 4962, 5121, 5278, 5439, 5595, 5756,
           5915, 6073, 6232, 6389, 6547, 6708, 6867, 7024, 7182, 7341, 7503, 7661, 7817, 7977, 8134, 8293, 8451, 8610, 8769, 8931, 9089, 9246, 9405, 9566, 9724, 9881, 10040, 10197, 10355, 10518,
           10676, 10835, 10992, 11150, 11311, 11467, 11624, 11785, 11946]
    攻击次数2 = 6
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill5(主动技能):
    名称 = '电鳗碰撞机'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [0, 870, 959, 1048, 1136, 1226, 1314, 1402, 1490, 1578, 1666, 1756, 1844, 1933, 2020, 2109, 2196, 2287, 2374, 2463, 2552, 2640, 2728, 2815, 2906, 2994, 3082, 3170, 3259, 3346, 3436, 3524,
           3613, 3700, 3790, 3878, 3966, 4055, 4144, 4232, 4319, 4409, 4496, 4586, 4673, 4763, 4850, 4939, 5027, 5116, 5204, 5293, 5382, 5470, 5558, 5646, 5736, 5823, 5912, 6000, 6089, 6176, 6266,
           6354, 6443, 6531, 6620, 6708, 6795, 6886, 6974]
    攻击次数1 = 14
    数据2 = [0, 1370, 1509, 1648, 1787, 1928, 2067, 2205, 2345, 2484, 2623, 2762, 2901, 3040, 3179, 3318, 3457, 3596, 3736, 3874, 4013, 4153, 4292, 4430, 4569, 4709, 4849, 4988, 5127, 5266, 5405, 5545,
           5683, 5822, 5961, 6099, 6238, 6378, 6518, 6657, 6795, 6935, 7074, 7213, 7352, 7491, 7630, 7770, 7910, 8047, 8186, 8326, 8464, 8603, 8743, 8882, 9020, 9160, 9300, 9439, 9578, 9717, 9856,
           9995, 10135, 10273, 10412, 10552, 10691, 10831, 10971]
    攻击次数2 = 1
    # 感电
    数据3 = [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 12, 12, 12, 13, 13, 14, 14, 14, 15, 15, 16, 16, 16, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 21, 21, 22,
           22, 22, 23, 23, 24, 24, 25, 25, 25, 26, 26, 27, 27, 27, 28, 28, 29, 29, 29, 30, 30, 31, 31, 31]
    攻击次数3 = 5
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4.8

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.27

        elif x == 1:
            self.倍率 *= 1.36


class skill6(主动技能):
    名称 = '反重力装置'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据 = [0, 12258, 13502, 14745, 15989, 17233, 18475, 19719, 20963, 22207, 23451, 24694, 25937, 27181, 28424, 29668, 30912, 32155, 33399, 34642, 35886, 37130, 38373, 39617, 40861, 42105, 43347,
          44591, 45834, 47078, 48322, 49566, 50810, 52052, 53296, 54540, 55784, 57027, 58271, 59515, 60757, 62001, 63245, 64489, 65733, 66977, 68221, 69463, 70707, 71950, 73194, 74438, 75681, 76925,
          78168, 79412, 80656, 81900, 83143, 84387, 85631, 86873, 88117, 89360, 90604, 91848, 93092, 94336, 95579, 96822, 98066]
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill7(主动技能):
    名称 = '暴炎加热炉失败'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据 = [0, 918, 1010, 1105, 1198, 1291, 1384, 1478, 1571, 1665, 1758, 1851, 1943, 2036, 2130, 2222, 2316, 2409, 2504, 2596, 2689, 2782, 2875, 2969, 3062, 3156, 3248, 3342, 3435, 3528, 3622, 3715,
          3807, 3900, 3994, 4087, 4179, 4273, 4366, 4461, 4553, 4647, 4739, 4833, 4927, 5020, 5113, 5205, 5299, 5393, 5487, 5579, 5673, 5764, 5858, 5951, 6044, 6138, 6230, 6325, 6418, 6511, 6604,
          6696, 6790, 6884, 6977, 7070, 7164, 7256, 7351]
    攻击次数 = 13
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 2.0

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2768

        elif x == 1:
            self.倍率 *= 1.3655


class skill8(主动技能):
    名称 = '冰霜钻孔车失败'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [0, 922, 1016, 1109, 1203, 1297, 1391, 1483, 1577, 1672, 1765, 1858, 1952, 2046, 2140, 2233, 2327, 2421, 2514, 2608, 2702, 2795, 2889, 2983, 3076, 3170, 3264, 3358, 3451, 3544, 3639, 3733,
           3825, 3919, 4013, 4106, 4199, 4293, 4387, 4481, 4573, 4668, 4762, 4855, 4948, 5042, 5137, 5230, 5323, 5417, 5511, 5604, 5699, 5792, 5885, 5979, 6073, 6167, 6260, 6354, 6448, 6541, 6635,
           6729, 6823, 6915, 7009, 7103, 7198, 7289, 7383]
    攻击次数1 = 9
    数据2 = [0, 8306, 9150, 9992, 10836, 11677, 12521, 13363, 14207, 15050, 15891, 16735, 17578, 18420, 19263, 20107, 20947, 21791, 22634, 23477, 24320, 25162, 26005, 26848, 27691, 28533, 29377, 30219,
           31061, 31904, 32748, 33591, 34433, 35276, 36118, 36961, 37804, 38647, 39489, 40332, 41175, 42018, 42862, 43704, 44546, 45389, 46233, 47074, 47918, 48762, 49602, 50445, 51289, 52132, 52974,
           53817, 54659, 55503, 56345, 57188, 58032, 58874, 59715, 60559, 61403, 62244, 63087, 63930, 64773, 65615, 66459]
    攻击次数2 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 2.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24

        elif x == 1:
            self.倍率 *= 1.32


class skill9(主动技能):
    名称 = '超级苍蝇拍'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据 = [0, 27391, 30171, 32948, 35726, 38504, 41284, 44063, 46842, 49621, 52400, 55178, 57958, 60737, 63516, 66294, 69074, 71852, 74631, 77411, 80190, 82968, 85748, 88525, 91304, 94082, 96862,
          99640, 102419, 105199, 107978, 110756, 113535, 116314, 119093, 121872, 124652, 127430, 130209, 132988, 135767, 138546, 141322, 144100, 146880, 149658, 152438, 155217, 157996, 160774, 163554,
          166332, 169111, 171890, 174669, 177448, 180226, 183007, 185785, 188564, 191343, 194122, 196899, 199678, 202458, 205236, 208015, 210794, 213574, 216352, 219130]
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.15
            self.CD *= 0.9

        elif x == 1:
            self.倍率 *= 1.24
            self.CD *= 0.9


class skill10(被动技能):
    名称 = '成功预感'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1 + round(16 + 1.5 * (self.等级 - 16), 1) / 100


class skill11(主动技能):
    名称 = '技艺融合'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [0, 1704, 2100, 2496, 2894, 3288, 3685, 4079, 4475, 4871, 5267, 5662, 6058, 6453, 6849, 7244, 7641, 8034, 8431, 8826, 9222, 9618, 10013, 10409, 10805, 11200, 11596, 11993, 12385, 12783,
           13179, 13573, 13968, 14365, 14759, 15156, 15552, 15946, 16342, 16739, 17133, 17530, 17926, 18321, 18717, 19114, 19507, 19905, 20298, 20694, 21090, 21486, 21881, 22277, 22672, 23068, 23464,
           23860, 24254, 24651, 25045, 25442, 25839, 26232, 26628, 27024, 27420, 27815, 28212, 28606, 29002]
    攻击次数1 = 22
    数据2 = [0, 46316, 57055, 67795, 78534, 89273, 100015, 110754, 121494, 132233, 142973, 153713, 164454, 175192, 185933, 196672, 207412, 218152, 228891, 239631, 250371, 261112, 271852, 282591, 293332,
           304070, 314810, 325550, 336289, 347032, 357771, 368510, 379250, 389989, 400729, 411468, 422209, 432949, 443688, 454429, 465168, 475907, 486648, 497388, 508128, 518867, 529606, 540346,
           551088, 561827, 572567, 583306, 594046, 604787, 615526, 626265, 637004, 647744, 658487, 669226, 679966, 690704, 701444, 712184, 722923, 733665, 744404, 755143, 765884, 776623, 787363]
    攻击次数2 = 1
    CD = 145.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 * 1.1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill12(主动技能):
    名称 = '光电兔'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [0, 9439, 10397, 11355, 12312, 13270, 14227, 15186, 16142, 17100, 18058, 19016, 19974, 20931, 21889, 22847, 23805, 24762, 25719, 26677, 27635, 28593, 29550, 30507, 31466, 32423, 33381,
           34338, 35296, 36254, 37212, 38169, 39126, 40085, 41042, 42001, 42957, 43914, 44873, 45830, 46788, 47745, 48704, 49661, 50620, 51576, 52534, 53492, 54449, 55407, 56364, 57323, 58280, 59239,
           60195, 61153, 62111, 63068, 64025, 64983, 65941, 66899, 67857, 68814, 69772, 70730, 71688, 72644, 73602, 74560, 75518]
    攻击次数1 = 4
    数据2 = [0, 5524, 6085, 6645, 7205, 7766, 8327, 8887, 9447, 10008, 10568, 11128, 11689, 12250, 12810, 13370, 13931, 14491, 15051, 15612, 16173, 16733, 17293, 17854, 18414, 18975, 19535, 20097,
           20656, 21216, 21778, 22338, 22899, 23458, 24020, 24580, 25140, 25701, 26261, 26822, 27383, 27943, 28503, 29063, 29624, 30184, 30745, 31306, 31866, 32426, 32986, 33547, 34107, 34668, 35229,
           35789, 36349, 36909, 37470, 38030, 38591, 39153, 39712, 40272, 40832, 41394, 41954, 42514, 43076, 43636, 44196]
    攻击次数2 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 4
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.15

        elif x == 1:
            self.倍率 *= 1.23


class skill13(主动技能):
    名称 = '雪人刨冰'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据1 = [0, 2102, 2314, 2527, 2740, 2954, 3168, 3381, 3594, 3807, 4021, 4234, 4446, 4660, 4874, 5087, 5300, 5513, 5727, 5939, 6153, 6368, 6579, 6795, 7007, 7221, 7434, 7647, 7860, 8074, 8287, 8500,
           8713, 8927, 9140, 9354, 9565, 9779, 9993, 10207, 10420, 10632, 10846, 11059, 11273, 11486, 11699, 11912, 12124, 12339, 12553]
    攻击次数1 = 18

    数据2 = [0, 1295, 1427, 1559, 1690, 1822, 1952, 2084, 2217, 2348, 2479, 2609, 2742, 2873, 3006, 3137, 3269, 3399, 3530, 3661, 3796, 3927, 4058, 4190, 4321, 4453, 4584, 4715, 4847, 4979, 5110, 5242,
           5374, 5504, 5636, 5766, 5899, 6030, 6163, 6294, 6425, 6556, 6688, 6818, 6952, 7084, 7214, 7345, 7476, 7608, 7740]
    攻击次数2 = 13

    数据3 = [0, 17827, 19634, 21441, 23251, 25059, 26867, 28676, 30484, 32292, 34101, 35909, 37718, 39525, 41334, 43142, 44952, 46759, 48570, 50377, 52185, 53995, 55803, 57610, 59420, 61227, 63036,
           64844, 66653, 68461, 70269, 72077, 73886, 75695, 77503, 79310, 81120, 82927, 84736, 86545, 88354, 90161, 91971, 93779, 95587, 97397, 99205, 101012, 102821, 104629, 106438]
    攻击次数3 = 1

    CD = 40.0
    演出时间 = 4

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.3


class skill14(被动技能):
    名称 = '贤者之石'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['魔道酸云雨', '电鳗碰撞机', '反重力装置', '熔岩药瓶成功']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class skill15(被动技能):
    名称 = '魔道学助手'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['变异苍蝇拍', '超级苍蝇拍', '改良舒露露', '技艺融合', '超级棒棒糖', '光电兔', '雪人刨冰', '乌洛波洛斯之环', '糖果大作战精怪乐园', '糖果大作战捣蛋杰克']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)


class skill16(被动技能):
    名称 = '魔道学助手+苦涩棒棒糖'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['冰霜钻孔车失败', '暴炎加热炉失败', '熔岩药瓶失败']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.88 + 0.02 * self.等级, 5)


class skill17(主动技能):
    名称 = '超级棒棒糖'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据1 = [0, 51736, 56983, 62232, 67479, 72728, 77976, 83227, 88474, 93724, 98971, 104220, 109468, 114717, 119965, 125214, 130461, 135712, 140959, 146208, 151456, 156704, 161952, 167203, 172450,
           177699, 182947, 188195, 193443, 198693, 203940, 209190, 214437, 219687, 224935, 230185, 235431, 240680, 245928, 251177, 256426, 261676, 266922, 272171, 277419, 282669, 287917, 293165,
           298415, 303663, 308913, 314160, 319410, 324656, 329906, 335153, 340403, 345652, 350900, 356147, 361395, 366644, 371894, 377142, 382391, 387638, 392886, 398136, 403384, 408632, 413882]
    攻击次数1 = 1
    数据2 = [0, 33076, 36432, 39788, 43144, 46499, 49855, 53211, 56566, 59920, 63277, 66632, 69988, 73342, 76700, 80054, 83409, 86764, 90121, 93479, 96834, 100191, 103545, 106902, 110255, 113613,
           116966, 120322, 123678, 127034, 130388, 133745, 137099, 140456, 143810, 147167, 150522, 153878, 157235, 160590, 163947, 167301, 170658, 174013, 177369, 180724, 184081, 187436, 190791,
           194146, 197502, 200858, 204213, 207569, 210925, 214279, 217635, 220992, 224347, 227703, 231058, 234416, 237770, 241126, 244481, 247838, 251192, 254549, 257904, 261261, 264615]
    攻击次数2 = 1
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.32
        self.CD *= 0.9

    CD = 45.0
    演出时间 = 0.5


class skill18(主动技能):
    名称 = '乌洛波洛斯之环'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据1 = [0, 2868, 3534, 4198, 4864, 5529, 6194, 6861, 7525, 8191, 8856, 9522, 10187, 10852, 11516, 12182, 12847, 13511, 14179, 14843, 15510, 16174, 16838, 17504, 18169, 18835, 19500, 20165, 20830,
           21497, 22161, 22826, 23492, 24157, 24823, 25487, 26153, 26818, 27483, 28148, 28814, 29480, 30145, 30809, 31475, 32140, 32805, 33470, 34135, 34801, 35466, 36132, 36798, 37462, 38129, 38793,
           39457, 40124, 40788, 41455, 42119, 42783, 43451, 44115, 44781, 45446, 46110, 46777, 47441, 48106, 48772]
    攻击次数1 = 21
    数据2 = [0, 2332, 2872, 3411, 3953, 4492, 5033, 5574, 6113, 6654, 7195, 7735, 8275, 8817, 9359, 9897, 10438, 10980, 11520, 12059, 12600, 13141, 13681, 14221, 14763, 15304, 15844, 16384, 16925,
           17465, 18005, 18547, 19086, 19626, 20168, 20708, 21249, 21790, 22330, 22871, 23410, 23951, 24493, 25032, 25572, 26113, 26653, 27196, 27735, 28277, 28816, 29357, 29898, 30437, 30978, 31519,
           32059, 32599, 33140, 33682, 34221, 34762, 35303, 35844, 36383, 36923, 37465, 38005, 38544, 39086, 39628]
    攻击次数2 = 20
    数据3 = [0, 72647, 89494, 106340, 123187, 140032, 156877, 173722, 190569, 207415, 224262, 241108, 257954, 274800, 291646, 308493, 325338, 342185, 359030, 375876, 392721, 409568, 426413, 443260,
           460105, 476952, 493798, 510644, 527490, 544336, 561180, 578027, 594873, 611720, 628565, 645412, 662257, 679104, 695950, 712796, 729642, 746488, 763333, 780180, 797024, 813871, 830717,
           847564, 864410, 881256, 898101, 914948, 931794, 948638, 965484, 982332, 999177, 1016024, 1032870, 1049715, 1066562, 1083408, 1100255, 1117100, 1133945, 1150791, 1167638, 1184483, 1201329,
           1218175, 1235022]
    攻击次数3 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * self.倍率

    CD = 180.0


class skill19(主动技能):
    名称 = '魔法秀'
    所在等级 = 20
    等级上限 = 15
    基础等级 = 10
    是否有伤害 = 0
    冷却关联技能 = ['改良舒露露', '熔岩药瓶失败', '魔道酸云雨', '电鳗碰撞机', '暴炎加热炉失败', '冰霜钻孔车失败', '反重力装置', '熔岩药瓶成功', '光电兔', '雪人刨冰', '糖果大作战捣蛋杰克']

    魔法秀数值 = [0, 22, 43, 65, 86, 108, 130, 151, 173, 194, 216, 238, 259, 281, 302, 324, 346, 367, 389, 410, 432]

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 - 0.001 * self.魔法秀数值[self.等级], 3)


class skill20(被动技能):
    名称 = '粉红糖果'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill21(主动技能):
    名称 = '糖果大作战捣蛋杰克'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    数据 = [0, 5463, 6017, 6571, 7125, 7679, 8233, 8787, 9341, 9895, 10449, 11003, 11557, 12111, 12665, 13219, 13773, 14327, 14881, 15435, 15989, 16543, 17097, 17651, 18205, 18759, 19313, 19867, 20421,
          20975, 21529, 22083, 22637, 23191, 23745, 24299, 24853, 25407, 25961, 26515, 27069]
    攻击次数 = 25
    # 基础 = 4909
    # 成长 = 554
    CD = 60.0

    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数) * self.倍率


class skill22(主动技能):
    名称 = '糖果大作战精怪乐园'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    # 数据 = [12317,15173,18029,20885,23741,26597,29453,32309]
    攻击次数 = 8
    基础 = 9461
    成长 = 2856
    攻击次数 = 8
    # 数据2 = [73904,91040,108176,125312,142448,159584,176720,193856]
    基础2 = 56768
    成长2 = 17136
    攻击次数2 = 1
    # 数据3 = [80062,98627,117192,135757,154322,172887,191452,210017]
    基础3 = 61497
    成长3 = 18565
    攻击次数3 = 4
    CD = 290.0

    # def 等效百分比(self, 武器类型):
    # return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2+self.数据3[self.等级] * self.攻击次数3) * self.倍率

    def 加成倍率(self, 武器类型):
        return 0.0


class skill23(被动技能):
    名称 = '幸运棒棒糖'
    所在等级 = 25
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.07 + 0.01 * self.等级, 5)


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

option_talismans = ['无']
for i in skill_list:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        option_talismans.append(i.名称)

option_rune = ['无']
for i in skill_list:
    if 20 <= i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        option_rune.append(i.名称)


class character(py.lite.CharBase):
    def 角色賦予(self):
        self.attr["实际名称"] = '知源_魔道学者'
        self.attr["角色"] = '魔法师(女)'
        self.attr["职业"] = '魔道学者'

        self.attr["武器选项"] = ['魔杖', '法杖', '棍棒', '矛', '扫把']

        self.attr["类型"] = '魔法固伤'
        self.attr["防具类型"] = '皮甲'
        self.attr["防具精通属性"] = ['智力']

        self.attr["主BUFF"] = 1.92

        self.attr["技能栏"] = skill_list
        self.attr["技能序号"] = skill_sn
        self.attr["一觉序号"] = skill_sn_awaking1
        self.attr["二觉序号"] = skill_sn_awaking2
        self.attr["三觉序号"] = skill_sn_awaking3
        self.attr["护石选项"] = option_talismans
        self.attr["符文选项"] = option_rune

        self.attr["远古记忆"] = 10

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [1, 5, 46, 26, 26, 36, 33, 33, 31, 1, 20, 12, 18, 0, 11, 11, 11, 13, 5, 10, 4, 6, 2, 5, 26]
        self.attr["技能TP等级"] = [0, 0, 5, 5, 5, 4, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]
        self.attr["技能释放次数"] = ['0', '', '3', '1', '2', '2', '2', '2', '1', '1', '', '1', '1', '1', '', '', '', '1', '1', '', '', '1', '/CD', '', '1']
        self.attr["技能宠物次数"] = [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '世界树之精灵']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "扫把"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 10]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "亲和法米利尔"
        self.attr["右槽白金技能"] = "亲和法米利尔"
        self.attr["时装上衣技能"] = "亲和法米利尔"

        self.attr["三觉技能选择"] = "二觉序号"

        self.attr["护石栏"] = ["暴炎加热炉失败", "光电兔", "无"]
        self.attr["护石类型"] = ["魔界", "魔界", "魔界"]
        self.attr["符文栏"] = ["暴炎加热炉失败", "暴炎加热炉失败", "暴炎加热炉失败", "暴炎加热炉失败", "暴炎加热炉失败", "暴炎加热炉失败", "无", "无", "无"]
        self.attr["符文效果"] = ["攻击+5%,CD+3%", "攻击+3%", "CD-4%", "攻击+5%,CD+3%", "攻击+3%", "CD-4%", "攻击+5%,CD+3%", "攻击+3%", "CD-4%"]
        self.attr["辟邪玉栏"] = [
            ["无", 0],
            ["无", 0],
            ["无", 0],
            ["无", 0]
        ]
        self.attr["希洛克装备栏"] = ["无", "无", "无"]
        self.attr["希洛克武器栏"] = [
            ["无", 6],
            ["无", 3]
        ]

    def 三觉技能选择(self):
        self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].被动倍率 = 0
