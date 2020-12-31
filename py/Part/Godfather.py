from py.base_char import *
import py.lite


# 长刀精通
class skill0(被动技能):
    名称 = '长刀精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.95


# 暗刃战略
class skill1(被动技能):
    名称 = '暗刃战略'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)


# 一觉被动
class skill2(被动技能):
    名称 = 'B.G枪刃改造'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


# 二觉被动
class skill3(被动技能):
    名称 = 'B.C精锐特训'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


# 卓越之力
class skill4(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 超卓之心
class skill5(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


# 觉醒之抉择
class skill6(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


# 掩护射击
class skill7(主动技能):
    名称 = '掩护射击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    攻击段数 = 10
    基础 = 1847.755698 - 攻击段数 * 0.5
    成长 = 209.2273524
    CD = 6
    TP成长 = 0.10
    TP上限 = 5


# 捷影步
class skill8(主动技能):
    名称 = '捷影步'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    攻击段数 = 5
    基础 = 1658.836937
    成长 = 187.6461134
    CD = 5
    TP成长 = 0.10
    TP上限 = 5


# 轮盘连射
class skill9(主动技能):
    名称 = '轮盘连射'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1332.874675
    成长 = 150.5275803
    攻击次数 = 1

    基础2 = 1696.315584  # 下劈
    成长2 = 191.5866712
    攻击次数2 = 1

    基础3 = 191.5866712  # 射击
    成长3 = 22.58072454
    攻击次数3 = 0  # 10

    CD = 8
    TP成长 = 0.10
    TP上限 = 5


# 剑刃突刺
class skill10(主动技能):
    名称 = '剑刃突刺'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    攻击段数 = 8
    基础 = 2270.46039 - 攻击段数 * 0.5
    成长 = 258.1335954
    CD = 6
    TP成长 = 0.10
    TP上限 = 5


# 潜行射击
class skill11(主动技能):
    名称 = '潜行射击'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    攻击段数 = 15
    基础 = (2709.696017 - 攻击段数 * 0.5) * 0.8
    成长 = 307.081761 * 0.8  # 游戏中攻速越高攻击段数越低，取本人60%-90%攻速时大致为12/15
    CD = 7
    TP成长 = 0.10
    TP上限 = 5


# 利刃旋斩
class skill12(主动技能):
    名称 = '利刃旋斩'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    攻击段数 = 8
    基础 = 2730.212439 - 攻击段数 * 0.5
    成长 = 308.7161807
    CD = 7
    TP成长 = 0.10
    TP上限 = 5


# 游弹枪袭
class skill13(主动技能):
    名称 = '游弹枪袭'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    攻击段数 = 30
    基础 = 3624.235294 - 攻击段数 * 0.5
    成长 = 411.4886878
    CD = 8
    TP成长 = 0.10
    TP上限 = 5


# 全方位射击
class skill14(主动技能):
    名称 = '全方位射击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36

    基础 = 253.6930612 - 0.5
    成长 = 28.71635054
    攻击次数 = 15

    基础2 = 423.2865306 - 0.5
    成长2 = 47.85935174
    攻击次数2 = 6

    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 0
            self.攻击次数 = 20
            self.倍率 = self.倍率 * 1.27 * 1.07
            self.CD *= 0.95
        elif x == 1:
            self.攻击次数2 = 0
            self.攻击次数 = 20
            self.倍率 = self.倍率 * 1.27 * 1.16  # 改动位置
            self.CD *= 0.95


# 回旋飞剑
class skill15(主动技能):
    名称 = '回旋飞剑'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    攻击段数 = 14
    基础 = 7642.573878 + 攻击段数 * 0.5
    成长 = 863.4943577
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


# 枪刃乱舞
class skill16(主动技能):
    名称 = '枪刃乱舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    基础 = 285.9777983 - 0.5
    成长 = 32.3413506
    攻击次数 = 10

    基础2 = 197.4236818 - 0.5
    成长2 = 22.34227567
    攻击次数2 = 15

    基础3 = 3738.310823 - 0.5
    成长3 = 422.1492831
    攻击次数3 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.80  # 加算
            self.攻击次数3 *= 1.27
            self.攻击次数 *= 1.07
            self.攻击次数2 *= 1.07
        elif x == 1:
            self.CD *= 0.80  # 加算
            self.攻击次数3 *= 1.50  # 改动位置
            self.攻击次数 *= 1.07
            self.攻击次数2 *= 1.07


# 血光斩
class skill17(主动技能):
    名称 = '血光斩'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    攻击段数 = 1
    基础 = 14496.06087 - 0.5
    成长 = 1636.743941
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.25  # 加算
        elif x == 1:
            self.倍率 *= 1.33  # 加算   改动位置


# 一觉
class skill18(主动技能):
    名称 = '电光飞掠'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    攻击段数 = 29
    基础 = 34891.02857 - 攻击段数 * 0.5
    成长 = 10539.71429
    CD = 145


# 近敌灭杀
class skill19(主动技能):
    名称 = '近敌灭杀'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    基础 = 5288.051613 - 0.5
    成长 = 597.1358871
    攻击次数 = 1

    基础2 = 396.1870968 - 0.5
    成长2 = 44.7766129
    攻击次数2 = 20

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.攻击次数2 *= (1 + 0.35 * 1.2)
        elif x == 1:
            self.CD *= 0.85
            self.攻击次数2 *= (1 + 0.35 * 1.58)  # 改动位置


# 大回旋坠斩，护石暂不考虑跳跃
#   2020.8.13新增护石跳
class skill20(主动技能):
    名称 = '大回旋坠斩'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18

    基础 = 795.9230769 + 832.6695157 - 1
    成长 = 90.02136752 + 94.03418803
    攻击次数 = 10

    基础2 = 6902.951567 - 0.5
    成长2 = 779.4108669
    攻击次数2 = 1

    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 += 1
            self.倍率 *= 1.16
        elif x == 1:
            self.攻击次数 += 1
            self.倍率 *= 1.23  # 改动位置


# 致命焰火
class skill21(主动技能):
    名称 = '致命焰火'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16

    基础 = 1529.956522
    成长 = 172.7934783
    攻击次数 = 10

    基础2 = 1532.086957  # 后方
    成长2 = 172.923913
    攻击次数2 = 15

    基础3 = 2294.980237  # 原地
    成长3 = 259.215415
    攻击次数3 = 0  # 10

    CD = 40

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础2 = self.基础3
            self.成长2 = self.成长3
            self.攻击次数2 = 10  # 猜测，否则提升过高
            self.倍率 *= 1.3
            self.CD *= 0.90


# 碧波瞬斩
class skill22(主动技能):
    名称 = '碧波瞬斩'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    攻击次数 = 3
    基础 = 15133.18947
    成长 = 1708.524812
    CD = 50

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 1
            self.倍率 *= 4.11  # 2.51*1.6


# 二觉
class skill23(主动技能):
    名称 = '集结·暮光之翼'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    攻击段数 = 36
    基础 = 81504.02778 - 攻击段数 * 0.5
    成长 = 24603.08333
    CD = 180


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
        self.attr["实际名称"] = '铁血统帅'
        self.attr["角色"] = '枪剑士'
        self.attr["职业"] = '暗刃'

        self.attr["武器选项"] = ['长刀']

        self.attr["类型"] = '物理百分比'
        self.attr["防具类型"] = '轻甲'
        self.attr["防具精通属性"] = ['力量']

        self.attr["主BUFF"] = 1.85

        self.attr["大回旋护石跳跃选项"] = 0
        self.attr["轮盘连射类型选项"] = 0
        self.attr["致命焰火方向选项"] = 0

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [10, 10, 20, 11, 4, 1, 2, 46, 46, 43, 43, 41, 41, 38, 36, 36, 33, 31, 12, 23, 18, 16, 13, 5]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 5, 0, 0, 0]
        self.attr["技能释放次数"] = ['', '', '', '', '', '', '', '2', '0', '2', '0', '0', '0', '0', '2', '2', '2', '1', '1', '0', '1', '1', '1', '1']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '夜天刀']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "长刀"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "长刀精通"
        self.attr["右槽白金技能"] = "长刀精通"
        self.attr["时装上衣技能"] = "长刀精通"

        self.attr["三觉技能选择"] = "二觉序号"

    def 三觉技能选择(self):
        for i, 技能 in enumerate(self.attr["技能栏"]):
            if 技能.名称 == "觉醒之抉择":
                技能.关联技能 = [self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].名称]

    def 技能等级初始化(self):
        super().技能等级初始化()
        技能栏 = self.attr["技能栏"]

        if self.attr["大回旋护石跳跃选项"] == 1:
            技能栏[skill_sn['大回旋坠斩']].攻击次数 = 0
            技能栏[skill_sn['大回旋坠斩']].攻击次数2 = 3 * 1.07

        if self.attr["轮盘连射类型选项"] == 1:
            技能栏[skill_sn['轮盘连射']].攻击次数2 = 0
            技能栏[skill_sn['轮盘连射']].攻击次数3 = 10

        if self.attr["致命焰火方向选项"] == 1:
            技能栏[skill_sn['致命焰火']].攻击次数2 = 0
            技能栏[skill_sn['致命焰火']].攻击次数3 = 10
