from py.base_char import *
import py.lite


class skill0(主动技能):
    名称 = '膝击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 50
    基础 = 337.7142857 + 955.1428571
    成长 = 38.28571429 + 107.8571429
    # 冲击波 = 858.9387755
    # 冲击波成长 = 97.06122449
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5


class skill1(被动技能):
    名称 = '摔技强化'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.0 + 0.02 * self.等级, 5)


class skill2(被动技能):
    名称 = '臂铠精通'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['无']
    冷却关联技能 = ['膝击', '抛投', '野蛮冲撞', '无情摔击', '空绞锤', '霹雳旋踢', '浮空凌云踢', '疾波猛坠', '地狱风火轮', '裂石破天', '彗星冲击', '武莲华', '黑震旋风', '疾风闪电', '黑震流·陨灭']

    def CD缩减倍率(self, 武器类型):
        if 武器类型 == '臂铠':
            return 0.9
        else:
            return 1.0


class skill3(主动技能):
    名称 = '抛投'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 46
    基础 = 782.5555556 + 1234.555556
    成长 = 88.44444444 + 139.4444444
    # 冲击波 = 1234.555556
    # 冲击波成长 = 139.4444444
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5


class skill4(被动技能):
    名称 = '连环抓取'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.33 + 0.02 * self.等级, 5)


class skill5(主动技能):
    名称 = '野蛮冲撞'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 1964.2 + 1177.925
    成长 = 221.8 + 133.075
    # 冲击波 = 1177.925
    # 冲击波成长 = 133.075
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5


class skill6(主动技能):
    名称 = '无情摔击'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 2996.6
    成长 = 338.4
    # 冲击波 = 2996.6
    # 冲击波成长 = 338.4
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5


class skill7(主动技能):
    名称 = '空绞锤'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2750.459459
    成长 = 310.5405405
    # 冲击波 = 2474.513514
    # 冲击波成长 = 279.4864865
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5


class skill8(主动技能):
    名称 = '霹雳旋踢'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4019.216216
    成长 = 453.7837838
    # 冲击波 = 3617.594595
    # 冲击波成长 = 408.4054054
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5


class skill9(主动技能):
    名称 = '浮空凌云踢'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 1362.142857 + 2452.085714 + 1634.371429
    成长 = 153.8571429 + 276.9142857 + 184.6285714
    # 冲击波 = 2860.914286
    # 冲击波成长 = 323.0857143
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5


class skill10(主动技能):
    名称 = '疾波猛坠'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    踢击 = 3061.371429
    踢击成长 = 345.6285714
    冲击波 = 385.4
    冲击波成长 = 43.6
    冲击波次数 = 6
    基础 = 踢击 + 冲击波 * 冲击波次数
    成长 = 踢击成长 + 冲击波成长 * 冲击波次数
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):  # 默认空中释放
        if x == 0:
            self.倍率 *= 1.3
            # self.踢击 *= 0
            # self.踢击成长 *= 0
            # self.冲击波 *= 2.18
            # self.冲击波成长 *= 2.18
            # self.冲击波次数 += 1
        elif x == 1:
            self.倍率 *= 1.39
            # self.踢击 *= 0
            # self.踢击成长 *= 0
            # self.冲击波 *= 2.36
            # self.冲击波成长 *= 2.36
            # self.冲击波次数 += 1


class skill11(主动技能):
    名称 = '地狱风火轮'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 1958.84375 / 1.06
    成长 = 221.15625 / 1.06
    攻击次数 = 1
    基础2 = 1157.3125 / 1.06
    成长2 = 130.6875 / 1.06
    攻击次数2 = 1
    基础3 = (3116.125 + 2671.375) / 1.06
    成长3 = (351.875 + 301.625) / 1.06
    攻击次数3 = 1
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础3 *= 1.38
            self.成长3 *= 1.38
        elif x == 1:
            self.基础3 *= 1.52
            self.成长3 *= 1.52


class skill12(主动技能):
    名称 = '裂石破天'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = (9799.533333 + 4222.233333) / 1.02
    成长 = (476.7666667 + 1106.466667) / 1.02
    # 对可抓取踢击 = 7100.233333
    # 对可抓取踢击成长 = 801.7666667
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
        elif x == 1:
            self.倍率 *= 1.28


class skill13(被动技能):
    名称 = '力之奥义'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class skill14(主动技能):
    名称 = '死亡旋律'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    空中释放基础 = 33191.55
    空中释放成长 = 10021.725
    基础 = 空中释放基础
    成长 = 空中释放成长
    # 地面释放基础 = 9716 + 6473.5
    # 地面释放基础成长 = 2931.25 + 1954.625
    # 地面释放冲击波 = 19899.55
    # 地面释放冲击波成长 = 6009.1625
    CD = 145.0


class skill15(主动技能):
    名称 = '彗星冲击'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 10616.36364
    成长 = 1198.636364
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        self.CD *= 0.88

        if x == 0:
            self.倍率 *= 1
        elif x == 1:
            self.倍率 *= 1.09


class skill16(主动技能):
    名称 = '武莲华'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 4592.470588 / 1.05
    成长 = 518.5294118 / 1.05
    攻击次数 = 2
    基础2 = 1146.941176 / 1.05
    成长2 = 129.0588235 / 1.05
    攻击次数2 = 12
    基础3 = 6886.235294 / 1.05
    成长3 = 777.7647059 / 1.05
    攻击次数3 = 1
    # 冲击波 = 17602.70588 / 1.05
    # 冲击波成长 = 1987.294118 / 1.05
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        self.基础 *= 1.5
        self.成长 *= 1.5
        self.攻击次数 = 4
        self.攻击次数2 = 0
        self.CD *= 0.9

        if x == 0:
            self.倍率 *= 1
        elif x == 1:
            self.倍率 *= 1.07


class skill17(被动技能):
    名称 = '傲天之怒'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class skill18(主动技能):
    名称 = '黑震旋风'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 5618.6 + 10903.33333 + 14726.33333
    成长 = 3528.699999
    # 冲击波 = 14726.33333
    # 冲击波成长 = 1662.666667
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.33


class skill19(主动技能):
    名称 = '疾风闪电'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    # 对可抓取怪物的冲撞 = 10744.66667
    # 对可抓取怪物的冲撞成长 = 1213.333333
    对不可抓取怪物的冲撞 = 20468
    对不可抓取怪物的冲撞成长 = 2311
    # 准备释放最后一击 = 7163.166667
    # 准备释放最后一击成长 = 808.8333333
    # 最后一击 = 17911.91667
    # 最后一击成长 = 2022.083333
    冲击波 = 16167.75
    冲击波成长 = 1825.25
    基础 = 对不可抓取怪物的冲撞 + 冲击波
    成长 = 对不可抓取怪物的冲撞成长 + 冲击波成长
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35


class skill20(主动技能):
    名称 = '一字传承：极义震天破'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 76306.75
    成长 = 23035.25
    CD = 185.0


class skill21(被动技能):
    名称 = '神怡气静'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill22(主动技能):
    名称 = '黑震流·陨灭'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 68271.2
    成长 = 7707.8
    CD = 60.0


class skill23(主动技能):
    名称 = '黑震流·山岳崩颓'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 205707
    成长 = 62101
    CD = 290
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0


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
        self.attr["实际名称"] = '归元_柔道家_男'
        self.attr["角色"] = '格斗家(男)'
        self.attr["职业"] = '柔道家'

        self.attr["武器选项"] = ['臂铠', '手套', '东方棍', '爪']

        self.attr["类型"] = '物理百分比'
        self.attr["防具类型"] = '轻甲'
        self.attr["防具精通属性"] = ['力量']

        self.attr["主BUFF"] = 2.08

        self.attr["技能栏"] = skill_list
        self.attr["技能序号"] = skill_sn
        self.attr["一觉序号"] = skill_sn_awaking1
        self.attr["二觉序号"] = skill_sn_awaking2
        self.attr["三觉序号"] = skill_sn_awaking3
        self.attr["护石选项"] = option_talismans
        self.attr["符文选项"] = option_rune

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [50, 10, 1, 46, 1, 41, 1, 2, 38, 36, 36, 33, 31, 20, 13, 23, 18, 11, 16, 13, 6, 4, 6, 2]
        self.attr["技能TP等级"] = [1, 0, 0, 0, 0, 1, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['3', '', '', '1', '', '4', '2', '3', '2', '2', '2', '2', '1', '', '1', '1', '1', '', '1', '1', '1', '', '1', '1']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '毁灭之碾压']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "臂铠"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "摔技强化"
        self.attr["右槽白金技能"] = "摔技强化"
        self.attr["时装上衣技能"] = "摔技强化"

        self.attr["三觉技能选择"] = "二觉序号"

        self.attr["护石栏"] = ["武莲华", "地狱风火轮", "无"]
        self.attr["护石类型"] = ["魔界", "魔界", "魔界"]
        self.attr["符文栏"] = ["武莲华", "武莲华", "武莲华", "武莲华", "武莲华", "武莲华", "无", "无", "无"]
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

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.attr["技能栏"][skill_sn['无情摔击']].被动倍率 /= self.attr["技能栏"][skill_sn['摔技强化']].加成倍率(self.attr["武器类型"])
