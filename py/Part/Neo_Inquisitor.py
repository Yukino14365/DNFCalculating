from py.base_char import *
import py.lite


# 战斧精通
class skill0(被动技能):
    名称 = '战斧精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.05 + 0.01 * self.等级, 5)
        else:
            return round(0.95 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


# 一觉被动
class skill1(被动技能):
    名称 = '异端烙印'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)


# 二觉被动
class skill2(被动技能):
    名称 = '定罪法则'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)

    关联技能2 = ['火焰精华']  # 此处删除神焰

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return (round(1.073 + 0.017 * self.等级, 5) / self.加成倍率(武器类型))

    冷却关联技能 = ['火焰精华', '神焰']

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.85


# 三觉被动
class skill3(被动技能):
    名称 = '狂炎告解'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 惩戒十字
class skill4(主动技能):
    名称 = '惩戒十字'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1186 + 1779 - 120 - 180
    成长 = 300
    CD = 6
    TP成长 = 0.10
    TP上限 = 5
    倍率 = round((1 / 1.12) * 1.133, 8)


# 净化火焰瓶
class skill5(主动技能):
    名称 = '净化火焰瓶'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2938 - 298
    成长 = 298
    CD = 6
    TP成长 = 0.10
    TP上限 = 5


# 裁决之击
class skill6(主动技能):
    名称 = '裁决之击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 4449 - 451.5
    成长 = 451.5
    CD = 8
    TP成长 = 0.10
    TP上限 = 5


# 火焰精华
class skill7(主动技能):
    名称 = '火焰精华'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 29
    基础 = 4315 - 688
    成长 = 688
    CD = 8
    TP成长 = 0.10
    TP上限 = 5


# 神焰
# 三觉版本改版，tp为基础精通
class skill8(主动技能):
    名称 = '神焰'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    基础 = 2416 * 9.452  # 补基础精通
    成长 = 0
    CD = 10
    TP成长 = 0.10
    TP上限 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.05 + 0.01 * self.等级, 2)
        else:
            return round(1.15 + 0.02 * (self.等级 - 10), 2)


# 审判重击
class skill9(主动技能):
    名称 = '审判重击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2852 + 3032 - 290 - 307
    成长 = 290 + 307
    CD = 10
    TP成长 = 0.10
    TP上限 = 5


# 神焰斩
class skill10(主动技能):
    名称 = '神焰斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36

    基础 = 1209 - 123
    成长 = 123
    攻击次数 = 1

    基础2 = 10903 - 1106
    成长2 = 1106
    攻击次数2 = 1

    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.攻击次数2 = 1.29
            self.CD *= 0.85
        elif x == 1:
            self.攻击次数 = 0
            self.攻击次数2 = 1.38
            self.CD *= 0.85


# 神焰洗礼
class skill11(主动技能):
    名称 = '神焰洗礼'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 9139 - 928  # 2020年11月29日微调
    成长 = 928
    CD = 15
    TP成长 = 0.10
    TP上限 = 5


# 神焰怒火
class skill12(主动技能):
    名称 = '神焰怒火'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    基础 = 1670 - 169.5
    成长 = 169.5
    攻击次数 = 5

    基础2 = 5567 - 565
    成长2 = 565
    攻击次数2 = 1

    倍率 = round((1 / 1.127) * 1.139, 8)

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.攻击次数 += 2
        elif x == 1:
            self.CD *= 0.85
            self.攻击次数 += 2
            self.倍率 *= 1.09


# 行刑
class skill13(主动技能):
    名称 = '行刑'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 23205 - 2354.5
    成长 = 2354.5
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    是否装备护石 = 0

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.9
            self.是否装备护石 = 1
        elif x == 1:
            self.CD *= 0.9
            self.是否装备护石 = 2


# 数据未录
# 一觉
class skill14(主动技能):
    名称 = '火刑'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    # 多段
    基础 = 10371 - 678 * 12
    成长 = 678
    攻击次数 = 15 * 1.1
    # 前2
    基础2 = 9712 + 29135 - 12 * (633 + 1901)
    成长2 = 633 + 1901
    攻击次数2 = 1

    CD = 145


# 神焰漩涡,最大旋转
class skill15(主动技能):
    名称 = '神焰漩涡'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    基础 = 1635 - 166
    成长 = 166
    攻击次数 = 9

    基础2 = 3451 - 350.16
    成长2 = 350.16
    攻击次数2 = 1

    倍率 = round((1 / 1.127) * 1.13, 8)

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 += 3
            self.攻击次数 *= 0.94
            self.攻击次数2 *= 1.14
        elif x == 1:
            self.攻击次数 += 3
            self.攻击次数 *= 1.01  ######
            self.攻击次数2 *= 1.14


# 净化之焰

class skill16(主动技能):
    名称 = '净化之焰'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18

    基础 = 28032 - 2844
    成长 = 2844

    CD = 40
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.27  #####


# 裁决轮回斩
class skill17(主动技能):
    名称 = '裁决轮回斩'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 2858 - 290
    成长 = 290
    攻击次数 = 3

    基础2 = 45518 - 4618
    成长2 = 4618
    攻击次数2 = 1

    CD = 40

    倍率 = round((1 / 1.127) * 1.133, 8)

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 -= 1
            self.攻击次数2 *= 1.26
            self.CD *= 0.92
            self.攻击次数 *= 1.37


# 车轮刑
class skill18(主动技能):
    名称 = '车轮刑'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = (1872 - 190) * 26 + 12016 - 1219
    成长 = 190 * 26 + 1219
    CD = 45

    倍率 = round((1 / 1.126) * 1.127, 8)
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.31


# 二觉
class skill19(主动技能):
    名称 = '炎狱祭坛：炮烙'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = (33499 - 4030 * 5) * 3 + 150746 - 18135 * 5
    成长 = 4030 * 3 + 18135
    CD = 180
    倍率 = round((1 / 1.127) * 1.132, 8)


# 95
class skill20(主动技能):
    名称 = '补赎逆十字'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 44324 - 4496.6
    成长 = 4496.6
    攻击次数 = 1

    基础2 = 55405 - 5620.8
    成长2 = 5620.8
    攻击次数2 = 1

    基础3 = 554 - 56.2
    成长3 = 56.2
    攻击次数3 = 20 + 20

    CD = 60


# 三觉
class skill21(主动技能):
    名称 = '无间狱·焚罪'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 37813 - 8769
    成长 = 8769
    攻击次数 = 1

    基础2 = 15125 - 3507
    成长2 = 3507
    攻击次数2 = 10

    基础3 = 189069 - 43843
    成长3 = 43843
    攻击次数3 = 1
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
        self.attr["实际名称"] = '神启_异端审判者'
        self.attr["角色"] = '圣职者(女)'
        self.attr["职业"] = '异端审判者'

        self.attr["武器选项"] = ['战斧']

        self.attr["类型"] = '物理百分比'
        self.attr["防具类型"] = '重甲'
        self.attr["防具精通属性"] = ['力量']

        self.attr["主BUFF"] = 1.93

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [10, 20, 11, 4, 46, 46, 43, 29, 10, 38, 36, 36, 33, 31, 12, 23, 18, 16, 13, 5, 6, 2]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 5, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['', '', '', '', '0', '0', '0', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '1', '1', '0', '1', '1', '1', '1', '1', '1']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '弗卡奴斯的第二个痕迹']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "战斧"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "战斧精通"
        self.attr["右槽白金技能"] = "战斧精通"
        self.attr["时装上衣技能"] = "战斧精通"

        self.attr["三觉技能选择"] = "二觉序号"

    def 三觉技能选择(self):
        self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].被动倍率 = 0

    def 技能释放次数计算(self):
        技能释放次数 = []
        次数输入 = self.attr["技能释放次数"]
        时间输入 = self.attr["时间输入"]
        武器类型 = self.attr["武器类型"]
        类型 = self.attr["类型"]

        for i in self.attr["技能栏"]:
            if i.是否有伤害 == 1:
                if 次数输入[skill_sn[i.名称]] == '/CD':
                    技能释放次数.append(int((时间输入 - i.演出时间) / i.等效CD(武器类型, 类型) + 1 + i.基础释放次数))
                elif 次数输入[skill_sn[i.名称]] != '0':
                    技能释放次数.append(int(次数输入[skill_sn[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        if '行刑' in self.attr["护石栏"] and 次数输入[skill_sn['神焰']] == '/CD':
            技能释放次数[skill_sn['神焰']] += 技能释放次数[skill_sn['行刑']]

        return 技能释放次数

    def 被动倍率计算(self):
        super().被动倍率计算()
        技能栏 = self.attr["技能栏"]
        武器类型 = self.attr["武器类型"]

        技能栏[skill_sn["火焰精华"]].被动倍率 /= 技能栏[skill_sn["神焰"]].加成倍率(武器类型)
        if 技能栏[skill_sn["行刑"]].是否装备护石 == 1:
            技能栏[skill_sn["行刑"]].被动倍率 /= 技能栏[skill_sn["神焰"]].加成倍率(武器类型)
            技能栏[skill_sn["行刑"]].被动倍率 *= 1 + (技能栏[skill_sn["神焰"]].加成倍率(武器类型) - 1) * 1.39
        elif 技能栏[skill_sn["行刑"]].是否装备护石 == 2:
            技能栏[skill_sn["行刑"]].被动倍率 /= 技能栏[skill_sn["神焰"]].加成倍率(武器类型)
            技能栏[skill_sn["行刑"]].被动倍率 *= 1 + (技能栏[skill_sn["神焰"]].加成倍率(武器类型) - 1) * 2.00
