from py.base_char import *
import py.lite


class skill0(主动技能):
    名称 = '背摔'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 1386.43 * 1.092
    成长 = 156.57 * 1.092
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5


class skill1(主动技能):
    名称 = '抛投'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 3164.50 * 1.077
    成长 = 357.47 * 1.077
    CD = 8.5
    TP成长 = 0.1
    TP上限 = 5


class skill2(被动技能):
    名称 = '摔技强化'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1 + 0.01 * self.等级, 5)
            else:
                return round(1.1 + 0.02 * (self.等级 - 10), 5)


class skill3(主动技能):
    名称 = '折颈'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 41
    基础 = 3430.65
    成长 = 387.38
    CD = 7.7
    TP成长 = 0.1
    TP上限 = 5


class skill4(主动技能):
    名称 = '野蛮冲撞'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 4091.91 * 1.05
    成长 = 462.08 * 1.05
    CD = 8.0
    TP成长 = 0.1
    TP上限 = 5


class skill5(被动技能):
    名称 = '强力抱摔'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill6(主动技能):
    名称 = '霹雳肘击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5348.07 * 1.05
    成长 = 603.95 * 1.05
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5


class skill7(主动技能):
    名称 = '空绞锤'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 3787.39 * 1.078
    成长 = 436.65 * 1.078
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5


class skill8(主动技能):
    名称 = '霹雳冲击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 2559.92
    成长 = 289.04
    基础2 = 5835.91
    成长2 = 659.11
    攻击次数2 = 1
    倍率 = 1.103
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5


class skill9(主动技能):
    名称 = '螺旋彗星落'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8630.10 * 1.078
    成长 = 974.93 * 1.078
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
            self.CD *= 0.88
        elif x == 1:
            self.倍率 *= 1.29
            self.CD *= 0.88
    # 附加效果：攻击力+8%更变至攻击力+17%


class skill10(主动技能):
    名称 = '地狱摇篮（抓轰炮）'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 13623.29 * 1.078
    成长 = 1539.26 * 1.078
    CD = 30.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.32
            self.CD *= 0.9
    # 附加效果：最后一击攻击力+30%更变至最后一击攻击力+59% ; [抓轰炮]攻击力 +10%更变至[抓轰炮]攻击力 +19%


class skill11(主动技能):
    名称 = '裂石破天'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 15889.25 * 1.10
    成长 = 1794.98 * 1.10
    CD = 45
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.31


# 最后一击冲击波攻击力+17%更变至最后一击冲击波攻击力+28% ; [随机应变]冲击波攻击力增加量+13%更变至[随机应变]冲击波攻击力增加量+21%

class skill12(被动技能):
    名称 = '抓取奥义'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.09 + 0.015 * self.等级, 5)


class skill13(主动技能):
    名称 = '末日风暴'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 1340.79
    成长 = 406.02
    基础2 = 20945.11
    成长2 = 6317.08
    攻击次数2 = 1
    倍率 = 1.107
    CD = 140.0


class skill14(主动技能):
    名称 = '空绞连锤（抓轰炮）'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 1170.88
    成长 = 132.08
    基础2 = 14058.93
    成长2 = 1588.06
    攻击次数2 = 1
    倍率 = 1.132
    CD = 30.0
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.12
        elif x == 1:
            self.倍率 *= 1.21
    # 攻击力 +12%更变至攻击力  +21%


class skill15(被动技能):
    名称 = '极手奥义'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill16(主动技能):
    名称 = '死亡摇篮'
    所在等级 = 70
    等级上限 = 60
    基础等级 = 18
    基础 = 25524.88 * 1.10
    成长 = 2883.51 * 1.10
    CD = 45
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.31


class skill17(主动技能):
    名称 = '末日摇篮'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 7654.70
    成长 = 864.27
    基础2 = 30620.97
    成长2 = 3457.06
    攻击次数2 = 1
    倍率 = 1.1
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.3225
    # 攻击力+15% ；生成总攻击力15%伤害的旋风（多段，15次攻击，每次1%）


class skill18(主动技能):
    名称 = '风暴之舞'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 5308.98
    成长 = 600.99
    攻击次数 = 6
    基础2 = 14760.91
    成长2 = 1665.05
    攻击次数2 = 1
    倍率 = 1.1
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 0.56
            self.成长 *= 0.56
            self.攻击次数 = 13
            self.倍率 *= 1.19
            # 多段攻击力减少44% ；次数+7；攻击力+19%


class skill19(主动技能):
    名称 = '苍宇彗星落'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 8601.87
    成长 = 2598.03
    基础2 = 77442.63
    成长2 = 23385.07
    攻击次数2 = 1
    倍率 = 1.1
    CD = 180


class skill20(被动技能):
    名称 = '光芒之翼'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill21(主动技能):
    名称 = '送葬舞步'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 6
    基础 = 94820.66208
    成长 = 10706.22299
    CD = 60.0


class skill22(主动技能):
    名称 = '女皇时代辉煌舞台'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']
    基础 = 266199.5202
    成长 = 80363.47518
    CD = 290

    def 加成倍率(self, 武器类型):
        return 0


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

归元_柔道家_女护石选项 = ['无']
for i in skill_list:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        归元_柔道家_女护石选项.append(i.名称)

归元_柔道家_女符文选项 = ['无']
for i in skill_list:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        归元_柔道家_女符文选项.append(i.名称)


class character(py.lite.char_base):
    def 角色賦予(self):
        self.attr["实际名称"] = '归元_柔道家_女'
        self.attr["角色"] = '格斗家(女)'
        self.attr["职业"] = '柔道家'

        self.attr["武器选项"] = ['手套', '臂铠', '东方棍', '爪']

        self.attr["类型"] = '物理固伤'
        self.attr["防具类型"] = '轻甲'
        self.attr["防具精通属性"] = ['力量']

        self.attr["死亡风暴次数选择"] = 12

        self.attr["主BUFF"] = 2.07

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [50, 46, 10, 41, 41, 1, 38, 38, 36, 36, 33, 31, 20, 12, 1, 11, 18, 16, 13, 5, 4, 6, 2]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 1, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['0', '0', '', '0', '3', '', '2', '0', '2', '2', '1', '1', '', '1', '1', '', '1', '1', '1', '1', '', '1', '1']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '鸣鸿破影棍']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "东方棍"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 10]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "摔技强化"
        self.attr["右槽白金技能"] = "摔技强化"
        self.attr["时装上衣技能"] = "摔技强化"

        self.attr["三觉技能选择"] = "一觉序号"

    def 三觉技能选择(self):
        self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].被动倍率 = 0

    def 技能等级初始化(self):
        super().技能等级初始化()
        self.attr["技能栏"][skill_sn['末日风暴']].攻击次数 *= self.attr["死亡风暴次数选择"] + 1
