﻿from py.base_char import *
import py.lite


class skill0(被动技能):
    名称 = '鲜血融合'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 物理攻击力倍率进图(self, 武器类型):
        if self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 * self.等级, 5)

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 * self.等级, 5)


class skill1(被动技能):
    名称 = '血之共鸣'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)


class skill2(被动技能):
    名称 = '血狱之力'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)


class skill3(被动技能):
    名称 = '鲜血之殇'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class skill4(被动技能):
    名称 = '鲜血源力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill5(主动技能):
    名称 = '血蝠之袭'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 3072.95454545
    成长 = 347.62237762
    CD = 5
    TP成长 = 0.10
    TP上限 = 5


class skill6(主动技能):
    名称 = '血翼突击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2329.84763635444
    成长 = 263.1339020924
    CD = 5
    TP成长 = 0.10
    TP上限 = 5


class skill7(主动技能):
    名称 = '鲜血长枪'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2993.1012727272
    成长 = 337.716727272
    CD = 6
    TP成长 = 0.10
    TP上限 = 5


class skill8(主动技能):
    名称 = '血蝠之舞'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3293.18181818
    成长 = 372.58741259
    CD = 6
    TP成长 = 0.10
    TP上限 = 5


class skill9(主动技能):
    名称 = '血腥狩猎'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 4179
    成长 = 472.5
    CD = 8
    TP成长 = 0.10
    TP上限 = 5


class skill10(主动技能):
    名称 = '狱血之犬'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4162.87878788
    成长 = 470.76223776
    CD = 10
    TP成长 = 0.10
    TP上限 = 5


class skill11(主动技能):
    名称 = '狱血之牙'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5281.5666666
    成长 = 596.353846154
    CD = 12
    TP成长 = 0.10
    TP上限 = 5
    额外倍率 = 0
    触发概率 = 0

    def 等效百分比(self, 武器类型):
        return (1 + self.额外倍率 * self.触发概率) * super().等效百分比(武器类型)


class skill12(主动技能):
    名称 = '血腥炼狱'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 9392.703939
    成长 = 1061.7061888
    CD = 18
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.2
            self.成长 *= 1.2
            self.CD *= 0.9
        elif x == 1:
            self.基础 *= 1.29
            self.成长 *= 1.29
            self.CD *= 0.9


class skill13(主动技能):
    名称 = '噬魂囚笼'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 12175.36181818
    成长 = 1333.46433566
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.2
            self.成长 *= 1.2
            self.CD *= 0.82
        elif x == 1:
            self.基础 *= 1.29
            self.成长 *= 1.29
            self.CD *= 0.82


class skill14(主动技能):
    名称 = '狱血之噬'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 23208.8198030
    成长 = 2620.41055594
    CD = 40
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.2
            self.成长 *= 1.2
        elif x == 1:
            self.基础 *= 1.28
            self.成长 *= 1.28


class skill15(主动技能):
    名称 = '伯爵之歌'
    所在等级 = 50
    等级上限 = 60
    基础等级 = 12
    基础 = 46649
    成长 = 14081
    CD = 145


class skill16(主动技能):
    名称 = '魔仆召唤：狱犬'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 18037.9022727225
    成长 = 2037.774650352
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.13
            self.成长 *= 1.13
            self.CD *= 0.8
        elif x == 1:
            self.基础 *= 1.22
            self.成长 *= 1.22
            self.CD *= 0.8


class skill17(主动技能):
    名称 = '血翼绽放'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 25260.95
    成长 = 2852.003846153
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.25
            self.成长 *= 1.25
        elif x == 1:
            self.基础 *= 1.33
            self.成长 *= 1.33


class skill18(主动技能):
    名称 = '地狱冥犬'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 30218.85
    成长 = 5734.946153849
    CD = 30
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.29
            self.成长 *= 1.29
            self.CD *= 0.9


class skill19(主动技能):
    名称 = '死亡之握'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 60756.9115151488
    成长 = 6859.7572027936
    CD = 50
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.34
            self.成长 *= 1.34


class skill20(主动技能):
    名称 = '血界彼岸'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 108898.72
    成长 = 32796.96
    CD = 180


class skill21(主动技能):
    名称 = '血翼尖刺'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 104283.2
    成长 = 11773.8
    CD = 60.0


class skill22(主动技能):
    名称 = '生之恐惧'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 31035.0050128261
    成长 = 9368.99498717389
    攻击次数 = 1
    基础2 = 3103.1256775528
    成长2 = 936.8743224472
    攻击次数2 = 20
    基础3 = 217248.082151946
    成长3 = 65583.9178480538
    攻击次数3 = 1
    CD = 290.0

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

知源_血法师护石选项 = ['无']
for i in skill_list:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        知源_血法师护石选项.append(i.名称)

知源_血法师符文选项 = ['无']
for i in skill_list:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        知源_血法师符文选项.append(i.名称)


class character(py.lite.char_base):
    def 角色賦予(self):
        self.attr["实际名称"] = '知源_血法师'
        self.attr["角色"] = '魔法师(男)'
        self.attr["职业"] = '血法师'

        self.attr["武器选项"] = ['矛']

        self.attr["类型"] = '物理百分比'
        self.attr["防具类型"] = '皮甲'
        self.attr["防具精通属性"] = ['力量']

        self.attr["主BUFF"] = 1.97

        self.attr["狱血之牙概率"] = 1

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [10, 1, 20, 11, 4, 46, 46, 43, 41, 41, 38, 38, 36, 33, 31, 12, 23, 18, 16, 13, 5, 6, 2]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0, 5, 0, 0, 5, 0, 5, 1, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['', '', '', '', '', '3', '0', '0', '1', '3', '1', '2', '2', '2', '1', '1', '2', '1', '1', '1', '1', '1', '1']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '歼灵灭魂矛']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "矛"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "血之共鸣"
        self.attr["右槽白金技能"] = "血之共鸣"
        self.attr["时装上衣技能"] = "鲜血融合"

        self.attr["三觉技能选择"] = "一觉序号"

    def 三觉技能选择(self):
        self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].被动倍率 = 0

    def 技能等级初始化(self):
        super().技能等级初始化()
        self.attr["技能栏"][skill_sn['狱血之牙']].触发概率 = round(self.attr["狱血之牙概率"] / 10, 2)
