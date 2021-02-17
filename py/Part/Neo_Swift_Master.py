from py.base_char import *
import py.lite


class skill0(被动技能):
    名称 = '疾风之棍棒精通'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20

    冷却关联技能 = ['狂风冲刺', '回风斩', '朔风牵引', '风鸣冲击', '游离之风', '双翼风刃', '风暴之眼', '刃风', '真空旋风破', '风暴之拳', '疾风瞬影闪', '风卷残云', '游龙惊风破', '九霄风雷', '怒风狂涌']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 <= 20:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.80 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.9


class skill1(被动技能):
    名称 = '御风之力'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class skill2(被动技能):
    名称 = '风神诀'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class skill3(被动技能):
    名称 = '初始之风'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill4(被动技能):
    名称 = '风之意志'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.015 * self.等级, 5)


class skill5(主动技能):
    名称 = '狂风冲刺'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 228
    成长 = 26
    # 打满是9次，操作有点反人类，常规6次
    攻击次数 = 6
    CD = 5
    TP成长 = 0.10
    TP上限 = 5


class skill6(主动技能):
    名称 = '回风斩'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    # hit 4
    基础 = 1920 / 4
    成长 = 216 / 4
    攻击次数 = 4
    CD = 5.5
    TP成长 = 0.10
    TP上限 = 5


class skill7(主动技能):
    名称 = '朔风牵引'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 306
    成长 = 34
    # 原作者做的是6hit，测试是9hit
    攻击次数 = 9
    CD = 10
    TP成长 = 0.10
    TP上限 = 5


class skill8(主动技能):
    名称 = '风鸣冲击'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3569
    成长 = 404
    CD = 8.5
    TP成长 = 0.10
    TP上限 = 5


class skill9(主动技能):
    名称 = '游离之风'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 727
    成长 = 82
    攻击次数 = 4
    CD = 6.7
    TP成长 = 0.10
    TP上限 = 5


class skill10(主动技能):
    名称 = '双翼风刃'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 1365
    成长 = 154
    攻击次数 = 4
    CD = 14
    TP成长 = 0.10
    TP上限 = 5


class skill11(主动技能):
    名称 = '风暴之眼'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 5966
    成长 = 672
    CD = 16
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.28
            self.CD *= 0.90
        elif x == 1:
            self.倍率 *= 1.28 + 0.09
            self.CD *= 0.90


class skill12(主动技能):
    名称 = '刃风'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7439 * 1.1
    成长 = 843 * 1.1
    CD = 18
    TP成长 = 0.10
    TP上限 = 5


class skill13(主动技能):
    名称 = '真空旋风破'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 488
    成长 = 56
    攻击次数 = 8
    基础2 = 3920
    成长2 = 442
    攻击次数2 = 1
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.085
            self.CD *= 0.8
        elif x == 1:
            self.倍率 *= 1.175
            self.CD *= 0.8


class skill14(主动技能):
    名称 = '风暴之拳'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 12743
    成长 = 1438
    攻击次数 = 1
    基础2 = 1092
    成长2 = 123
    攻击次数2 = 5
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']  # 不确定对不对

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.22
        elif x == 1:
            self.倍率 *= 1.295


class skill15(主动技能):
    名称 = '万象风龙阵'
    所在等级 = 50
    等级上限 = 60
    基础等级 = 12
    基础 = 1624 - 104 * 12
    成长 = 104
    攻击次数 = 56
    基础2 = 29251 - 1910 * 12
    成长2 = 1910
    攻击次数2 = 4
    CD = 145


class skill16(主动技能):
    名称 = '疾风瞬影闪'
    所在等级 = 60
    等级上限 = 60
    基础等级 = 23
    基础 = 2149 - 218
    成长 = 218
    # 原来写的是9hit
    攻击次数 = 8
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.18
        elif x == 1:
            self.倍率 *= 1.18 + 0.09


class skill17(主动技能):
    名称 = '风卷残云'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    # 10+1
    基础 = 2398 - 244
    成长 = 244
    攻击次数 = 10
    基础2 = 7995 - 811
    成长2 = 811
    攻击次数2 = 1
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']  # 不确定是加算还是乘算

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.22
        elif x == 1:
            self.倍率 *= 1.22 + 0.08


class skill18(主动技能):
    名称 = '游龙惊风破'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    # 12+1
    基础 = 1707 - 174
    成长 = 174
    攻击次数 = 12
    基础2 = 28157 - 2856
    成长2 = 2856
    攻击次数2 = 1
    CD = 40
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.26


class skill19(主动技能):
    名称 = '九霄风雷'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    # 14+1
    # 低于100攻速且立即落地时，存在丢hit情况，hit数11-13
    # 携带CP后不存在丢hit
    基础 = 1650 - 167
    成长 = 167
    攻击次数 = 14
    基础2 = 34667 - 3517
    成长2 = 3517
    攻击次数2 = 1
    CD = 45
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.27
            self.CD *= 0.89


class skill20(主动技能):
    名称 = '无限风域'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    # 1+8+1+1
    基础 = 84529 * 1.09
    成长 = 25501 * 1.09
    CD = 180


class skill21(主动技能):
    名称 = '怒风狂涌'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 6
    基础 = 3335 - 338
    成长 = 338
    攻击次数 = 6
    基础2 = 7504 - 762
    成长2 = 762
    攻击次数2 = 4
    基础3 = 50030 - 5075
    成长3 = 5075
    攻击次数3 = 1
    CD = 60


class skill22(主动技能):
    名称 = '风之极·永坠'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 26244.1692923844
    成长 = 7922.83070761556
    攻击次数 = 1
    基础2 = 39366.5033510094
    成长2 = 11884.4966489906
    攻击次数2 = 1
    基础3 = 7873.13078771533
    成长3 = 2376.86921228467
    攻击次数3 = 25
    CD = 290

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
        self.attr["实际名称"] = '知源_逐风者'
        self.attr["角色"] = '魔法师(男)'
        self.attr["职业"] = '逐风者'

        self.attr["武器选项"] = ['棍棒']

        self.attr["类型"] = '物理百分比'
        self.attr["防具类型"] = '皮甲'
        self.attr["防具精通属性"] = ['力量']

        self.attr["主BUFF"] = 2.11

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [20, 20, 11, 4, 5, 46, 46, 43, 20, 41, 38, 36, 1, 33, 31, 12, 1, 18, 16, 13, 5, 6, 2]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 5, 0, 5, 5, 0, 0, 5, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['', '', '', '', '', '0', '0', '0', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '1', '1']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '精灵浮风棍']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "棍棒"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "疾风之棍棒精通"
        self.attr["右槽白金技能"] = "疾风之棍棒精通"
        self.attr["时装上衣技能"] = "疾风之棍棒精通"

        self.attr["三觉技能选择"] = "二觉序号"

    def 三觉技能选择(self):
        self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].被动倍率 = 0
