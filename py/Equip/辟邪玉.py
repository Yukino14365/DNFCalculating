class 辟邪玉:
    名称 = ''
    最小值 = -5
    最大值 = 5
    间隔 = 0.1
    当前值 = 0

    def 穿戴属性(self, character):
        pass


class 辟邪玉0(辟邪玉):
    名称 = '无'
    最小值 = 0
    最大值 = 0


class 辟邪玉1(辟邪玉):
    名称 = '附加伤害增加增幅'

    def 穿戴属性(self, character):
        character.attr["附加伤害增加增幅"] += round(self.当前值 / 100, 4)


class 辟邪玉2(辟邪玉):
    名称 = '属性附加伤害增加增幅'

    def 穿戴属性(self, character):
        character.attr["属性附加伤害增加增幅"] += round(self.当前值 / 100, 4)


class 辟邪玉3(辟邪玉):
    名称 = '技能伤害增加增幅'
    最小值 = -3
    最大值 = 3

    def 穿戴属性(self, character):
        character.attr["技能伤害增加增幅"] += round(self.当前值 / 100, 4)


class 辟邪玉4(辟邪玉):
    名称 = '暴击伤害增加增幅'

    def 穿戴属性(self, character):
        character.attr["暴击伤害增加增幅"] += round(self.当前值 / 100, 4)


class 辟邪玉5(辟邪玉):
    名称 = '伤害增加增幅'

    def 穿戴属性(self, character):
        character.attr["伤害增加增幅"] += round(self.当前值 / 100, 4)


class 辟邪玉6(辟邪玉):
    名称 = '最终伤害增加增幅'

    def 穿戴属性(self, character):
        character.attr["最终伤害增加增幅"] += round(self.当前值 / 100, 4)


class 辟邪玉7(辟邪玉):
    名称 = '力量智力增加增幅'

    def 穿戴属性(self, character):
        character.attr["力量智力增加增幅"] += round(self.当前值 / 100, 4)


class 辟邪玉8(辟邪玉):
    名称 = '物理魔法攻击力增加增幅'

    def 穿戴属性(self, character):
        character.attr["物理魔法攻击力增加增幅"] += round(self.当前值 / 100, 4)


class 辟邪玉9(辟邪玉):
    名称 = '所有属性强化增加'

    def 穿戴属性(self, character):
        character.attr["所有属性强化增加"] += round(self.当前值 / 100, 4)


class 辟邪玉10(辟邪玉):
    名称 = '10~15技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, character):
        character.skill_level_up_batched('所有', 10, 15, self.当前值)


class 辟邪玉11(辟邪玉):
    名称 = '20~25技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, character):
        character.skill_level_up_batched('所有', 20, 25, self.当前值)


class 辟邪玉12(辟邪玉):
    名称 = '30~35技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, character):
        character.skill_level_up_batched('所有', 30, 35, self.当前值)


class 辟邪玉13(辟邪玉):
    名称 = '40~45技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, character):
        character.skill_level_up_batched('所有', 40, 45, self.当前值)


class 辟邪玉14(辟邪玉):
    名称 = '55~60技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, character):
        character.skill_level_up_batched('所有', 55, 60, self.当前值)


class 辟邪玉15(辟邪玉):
    名称 = '65~70技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, character):
        character.skill_level_up_batched('所有', 65, 70, self.当前值)


class 辟邪玉16(辟邪玉):
    名称 = '75~80技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, character):
        character.skill_level_up_batched('所有', 75, 80, self.当前值)


class 辟邪玉17(辟邪玉):
    名称 = '1次觉醒技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, character):
        character.skill_level_up_batched('所有', 50, 50, self.当前值)


class 辟邪玉18(辟邪玉):
    名称 = '2次觉醒技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, character):
        character.skill_level_up_batched('所有', 85, 85, self.当前值)


辟邪玉列表 = []
for i in range(19):
    exec('辟邪玉列表.append(辟邪玉' + str(i) + '())')

辟邪玉序号 = dict()
辟邪玉取值范围 = {}
for i in range(len(辟邪玉列表)):
    辟邪玉序号[辟邪玉列表[i].名称] = i
    a, temp = 辟邪玉列表[i].最小值, []
    while a <= 辟邪玉列表[i].最大值:
        temp.append(a)
        a = round(a + 辟邪玉列表[i].间隔, 1)
    辟邪玉取值范围.update({辟邪玉列表[i].名称: temp})
