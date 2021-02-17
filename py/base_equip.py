class 装备:
    名称 = ''
    模式 = 0
    图片ID = ''
    所属套装 = ''
    等级 = 0
    品质 = ''
    部位 = ''
    类型 = ''
    力量 = 0
    智力 = 0
    体力 = 0
    精神 = 0
    属性描述 = ""
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, 属性):
        pass

    def 城镇属性_BUFF(self, 属性):
        pass

    def 进图属性(self, 属性):
        pass

    def 进图属性_BUFF(self, 属性):
        pass

    def 其它属性(self, 属性):
        pass

    def 其它属性_BUFF(self, 属性):
        pass

    def BUFF属性(self, 属性):
        pass

    def 变换属性(self, character):
        pass

    def 装备描述(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        if self.部位 in ['上衣', '下装', '腰带', '头肩', '鞋']:
            self.属性描述 += ('力量 +{}<br>'.format(self.力量[属性.防具类型])) if self.力量[属性.防具类型] > 0 else ''
            self.属性描述 += ('智力 +{}<br>'.format(self.智力[属性.防具类型])) if self.智力[属性.防具类型] > 0 else ''
        else:
            self.属性描述 += ('力量 +{}<br>'.format(self.力量)) if self.力量 > 0 else ''
            self.属性描述 += ('智力 +{}<br>'.format(self.智力)) if self.智力 > 0 else ''
        self.属性描述 += ('物理攻击力 +{}<br>'.format(self.物理攻击力)) if self.物理攻击力 > 0 else ''
        self.属性描述 += ('魔法攻击力 +{}<br>'.format(self.魔法攻击力)) if self.魔法攻击力 > 0 else ''
        self.属性描述 += ('独立攻击力 +{}<br>'.format(self.独立攻击力)) if self.独立攻击力 > 0 else ''
        self.城镇属性(属性)
        self.属性描述 += '<font color="#00A2E8">进图触发：</font><br>'
        self.进图属性(属性)
        if self.属性描述.endswith('<font color="#00A2E8">进图触发：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">进图触发：</font><br>', '')
        self.属性描述 += '<font color="#00A2E8">其他属性：</font><br>'
        self.其它属性(属性)
        if self.属性描述.endswith('<font color="#00A2E8">其他属性：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">其他属性：</font><br>', '')
        属性.装备描述 = 0
        return self.属性描述

    def 装备描述_BUFF(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        if self.部位 not in ['上衣', '下装', '腰带', '头肩', '鞋']:
            if 属性.角色 == '圣职者(女)' or 属性.角色 == '魔法师(女)':
                self.属性描述 += ('智力 +{}<br>'.format(self.智力)) if self.智力 > 0 else ''
            else:
                self.属性描述 += ('体力 +{}<br>'.format(self.体力)) if self.体力 > 0 else ''
                self.属性描述 += ('精神 +{}<br>'.format(self.精神)) if self.精神 > 0 else ''
        self.城镇属性_BUFF(属性)
        self.属性描述 += '<font color="#00A2E8">辅助职业专属属性:</font><br>'
        self.BUFF属性(属性)
        self.属性描述 += '<font color="#00A2E8">进图触发：</font><br>'
        self.进图属性_BUFF(属性)
        if self.属性描述.endswith('<font color="#00A2E8">进图触发：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">进图触发：</font><br>', '')
        self.属性描述 += '<font color="#00A2E8">其他属性：</font><br>'
        self.其它属性_BUFF(属性)
        if self.属性描述.endswith('<font color="#00A2E8">其他属性：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">其他属性：</font><br>', '')
        属性.装备描述 = 0
        return self.属性描述

    def 图片ID(self):
        if self.图片ID == '':
            return self.__class__.__name__.replace('装备', '')
        else:
            return self.图片ID


class 改造产物(装备):
    模式 = 1
    所属套装 = '智慧产物'
    等级 = 100
    品质 = '史诗'
    力量 = 0
    智力 = 0
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0
    关联套装 = ''

    def 基础属性(self, 属性):
        pass

    def 改造属性(self, 属性, x):
        pass

    def 城镇属性(self, 属性):
        # 后续解决
        # for i in 属性.装备栏:
        #     if 装备列表[装备序号[i]].所属套装 in self.关联套装:
        #         属性.力量 += 100
        #         属性.智力 += 100
        # self.基础属性(属性)
        pass

    def 进图属性(self, 属性):
        if self.关联套装 in 属性.套装栏:
            self.改造属性(属性, 属性.获取改造(self.部位))
        pass

    def 其它属性(self, 属性):
        pass

    def 装备描述(self, 属性):
        temp = ''
        return temp


class 飘零之花武器(装备):
    模式 = 0
    所属套装 = '智慧产物'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    物攻成长 = 0
    魔攻成长 = 0
    独立成长 = 115
    力智成长 = 20

    def 城镇属性(self, 属性):
        改造等级 = 属性.获取改造(self.部位)
        属性.技能攻击力加成(0.35)
        属性.附加伤害加成(0.50)
        属性.百分比力智加成(0.20)
        属性.物理攻击力 += self.物攻成长 * 改造等级
        属性.魔法攻击力 += self.魔攻成长 * 改造等级
        属性.独立攻击力 += self.独立成长 * 改造等级
        属性.力量 += self.力智成长 * 改造等级
        属性.智力 += self.力智成长 * 改造等级
        pass

    def 进图属性(self, 属性):
        pass

    def 其它属性(self, 属性):
        pass

    def 装备描述(self, 属性):
        temp = ''
        if self.力量 != 0:
            temp += '力量 +' + str(self.力量) + '<br>'
        if self.智力 != 0:
            temp += '智力 +' + str(self.智力) + '<br>'
        temp += '物理攻击力 +' + str(self.物理攻击力) + '<br>'
        temp += '魔法攻击力 +' + str(self.魔法攻击力) + '<br>'
        temp += '独立攻击力 +' + str(self.独立攻击力) + '<br>'
        改造等级 = 属性.获取改造(self.部位)
        if 改造等级 >= 5:
            temp += '技能攻击力 +35%<br>'
            temp += '附加伤害 +50%<br>'
            temp += '百分比力智 +20%<br>'
        if 改造等级 > 0:
            temp += '<font color="#FF8200">改造属性(+' + str(改造等级) + ')：</font><br>'
            temp += '力量 +' + str(self.力智成长 * 改造等级) + '<br>'
            temp += '智力 +' + str(self.力智成长 * 改造等级) + '<br>'
            temp += '物理攻击力 +' + str(self.物攻成长 * 改造等级) + '<br>'
            temp += '魔法攻击力 +' + str(self.魔攻成长 * 改造等级) + '<br>'
            temp += '独立攻击力 +' + str(self.独立成长 * 改造等级) + '<br>'
        return temp


class 套装:
    属性描述 = ''

    def 城镇属性(self, 属性):
        pass

    def 城镇属性_BUFF(self, 属性):
        pass

    def 进图属性(self, 属性):
        pass

    def 进图属性_BUFF(self, 属性):
        pass

    def 其它属性(self, 属性):
        pass

    def 其它属性_BUFF(self, 属性):
        pass

    def 装备描述(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        self.城镇属性(属性)
        self.属性描述 += '<font color="#00A2E8">进图触发：</font><br>'
        self.进图属性(属性)
        if self.属性描述.endswith('<font color="#00A2E8">进图触发：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">进图触发：</font><br>', '')
        self.属性描述 += '<font color="#00A2E8">其他属性：</font><br>'
        self.其它属性(属性)
        if self.属性描述.endswith('<font color="#00A2E8">其他属性：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">其他属性：</font><br>', '')
        属性.装备描述 = 0
        return self.属性描述

    def 装备描述_BUFF(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        self.城镇属性_BUFF(属性)
        self.属性描述 += '<font color="#00A2E8">辅助职业专属属性:</font><br>'
        self.BUFF属性(属性)
        self.属性描述 += '<font color="#00A2E8">进图触发：</font><br>'
        self.进图属性_BUFF(属性)
        if self.属性描述.endswith('<font color="#00A2E8">进图触发：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">进图触发：</font><br>', '')
        self.属性描述 += '<font color="#00A2E8">其他属性：</font><br>'
        self.其它属性_BUFF(属性)
        if self.属性描述.endswith('<font color="#00A2E8">其他属性：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">其他属性：</font><br>', '')
        属性.装备描述 = 0
        return self.属性描述

    def BUFF属性(self, 属性):
        pass


部位列表 = ["上衣", "头肩", "下装", "腰带", "鞋", "手镯", "项链", "戒指", "耳环", "辅助装备", "魔法石", "武器"]

# ----------- 增幅 ----------- #

增幅系数 = [0, 1, 2, 3, 4, 6, 8, 10, 22, 28, 35, 42, 50, 67, 108, 150, 192, 267, 342, 417, 500, 583, 667, 750, 833, 917, 1000, 1083, 1167, 1250, 1333, 1417]
增幅成长系数 = {'稀有': 1, '神器': 1.3, '勇者': 1.1, '传说': 1.4, '史诗': 1.5, '神话': 1.6}
增幅品级加分 = {'稀有': 45, '神器': 45, '勇者': 45, '传说': 46, '史诗': 46, '神话': 46}
增幅品级底数 = {'稀有': 10, '神器': 11, '勇者': 10, '传说': 11, '史诗': 12, '神话': 13}


def 增幅计算(装备等级, 品质, 强化等级):
    return int((装备等级 + 增幅品级加分[品质]) * 增幅成长系数[品质] * 增幅系数[强化等级] / 100 - 0.00000001) + 增幅品级底数[品质] + (0 if 强化等级 < 12 else 5)


# ----------- 特殊装备&勋章 ----------- #

耳环强化系数 = [0, 83, 124, 166, 207, 248, 314, 370, 426, 482, 621, 970, 1455, 1941, 2911, 4043, 5175, 7116, 9056, 10997, 13099, 15363, 17627, 19891, 22155, 24420, 26684, 28948, 31212, 33476, 35740, 38004]
左右强化系数 = [0, 60, 90, 120, 150, 180, 210, 247, 285, 322, 360, 675, 1013, 1350, 2025, 2813, 3600, 4950, 6300, 7650, 9113, 10688, 12263, 13838, 15413, 16988, 18563, 20138, 21713, 23288, 24863, 26438]
勋章强化系数 = [0, 100, 120, 144, 173, 208, 250, 300, 320, 360, 400, 610, 1220, 2440, 2684, 2952, 3838, 4989, 6486, 8432, 10962]
特殊成长系数 = {'普通': 0.4, '高级': 0.7, '稀有': 1, '神器': 1.25, '传说': 1.35, '史诗': 1.45, '神话': 1.55}
特殊品级加分 = {'普通': 24, '高级': 30, '稀有': 26, '神器': 28, '传说': 29, '史诗': 30, '神话': 31}


def 耳环计算(装备等级, 品质, 强化等级):
    return int((装备等级 + 特殊品级加分[品质]) / 2400 * 特殊成长系数[品质] * 耳环强化系数[强化等级])


def 左右计算(装备等级, 品质, 强化等级):
    return int((装备等级 + 特殊品级加分[品质]) / 2400 * 特殊成长系数[品质] * 左右强化系数[强化等级])


def 勋章计算(装备等级, 品质, 强化等级):
    return int((装备等级 + 特殊品级加分[品质]) / 2400 * 特殊成长系数[品质] * 勋章强化系数[强化等级])


# ----------- 武器 ----------- #

武器强化系数 = [0, 2, 2.6, 3.6, 4.7, 5.8, 6.9, 8.2, 11, 14.6, 18.7, 26.9, 36.7, 43, 49.2, 55.4, 61.7, 68, 74.3, 80.6, 86.9, 93.2, 99.5, 105.8, 112.1, 118.3, 124.6, 130.9, 137.1, 14.34, 149.7, 156.0]
武器锻造系数 = [0, 2, 3, 4, 6, 8, 13, 18, 25, 32, 41]
武器成长系数 = {'普通': 0.4, '高级': 0.7, '稀有': 1, '神器': 1.25, '勇者': 1.1, '传说': 1.35, '史诗': 1.45, '神话': 1.55}
武器品级加分 = {'普通': 8, '高级': 8, '稀有': 10, '神器': 12, '勇者': 11, '传说': 13, '史诗': 14, '神话': 15}
武器类型系数 = {
    '短剑': [1.095, 1.115],
    '太刀': [1.095, 1.105],
    '钝器': [1.11, 1.095],
    '巨剑': [1.12, 1.09],
    '光剑': [1.093, 1.09],
    '手套': [1.095, 1.115],
    '臂铠': [1.12, 1.09],
    '爪': [1.1, 1.1],
    '拳套': [1.105, 1.095],
    '东方棍': [1.095, 1.1],
    '左轮枪': [1.087, 1.077],
    '自动手枪': [1.064, 1.094],
    '步枪': [1.1, 1.085],
    '手炮': [1.106, 1.064],
    '手弩': [1.075, 1.085],
    '矛': [1.12, 1.085],
    '棍棒': [1.108, 1.09],
    '魔杖': [1.09, 1.11], 
    '法杖': [1.095, 1.12],
    '扫把': [1.1, 1.11],
    '十字架': [1.1, 1.095],
    '念珠': [1.09, 1.115],
    '图腾': [1.105, 1.09],
    '镰刀': [1.105, 1.105],
    '战斧': [1.12, 1.085],
    '匕首': [1.09, 1.089],
    '双剑': [1.102, 1.08],
    '手杖': [1.081, 1.115],
    '苦无': [1.09, 1.11],
    '长枪': [1.105, 1.09],
    '战戟': [1.12, 1.085],
    '光枪': [1.095, 1.115],
    '暗矛': [1.095, 1.105],
    '长刀': [1.108, 1.09],
    '小太刀': [1.1, 1.1],
    '重剑': [1.12, 1.09],
    '源力剑': [1.095, 1.115]
}


def 武器计算(装备等级, 品质, 强化等级, 武器类型, 类型):
    武器系数 = (武器类型系数[武器类型][0 if 类型 == '物理' else 1])
    return int((装备等级 + 武器品级加分[品质]) / 8 * 武器成长系数[品质] * 武器强化系数[强化等级] * 武器系数)


def 锻造计算(装备等级, 品质, 锻造等级):
    return round((装备等级 + 武器品级加分[品质]) / 8 * 武器成长系数[品质] * 武器锻造系数[锻造等级])


def 锻造四维(装备等级, 品质, 锻造等级):
    return round((装备等级 + 武器品级加分[品质]) / 80 * 武器成长系数[品质] * 武器锻造系数[锻造等级])


武器冷却惩罚系数 = {
    '短剑': [1, 1.05, 1],
    '太刀': [0.95, 1, 1],
    '钝器': [1.05, 1, 1],
    '巨剑': [1.1, 1, 1],
    '光剑': [0.9, 1, 1],
    '手套': [0.9, 1.05, 1],
    '臂铠': [1.1, 1, 1],
    '爪': [1, 1, 1],
    '拳套': [0.9, 1, 1],
    '东方棍': [1, 1, 1],
    '左轮枪': [1, 1, 1],
    '自动手枪': [0.9, 1, 1],
    '步枪': [1.05, 1, 1],
    '手炮': [1.1, 1, 1],
    '手弩': [0.9, 1, 1],
    '矛': [1.05, 0.95, 1],
    '棍棒': [1, 1, 1],
    '魔杖': [0.95, 1, 1],
    '法杖': [1, 1.1, 1],
    '扫把': [1, 1, 1],
    '十字架': [0.95, 1, 1],
    '念珠': [0.95, 1.05, 1],
    '图腾': [1, 0.95, 1],
    '镰刀': [0.95, 1, 1],
    '战斧': [1.1, 0.9, 1],
    '匕首': [0.9, 0.95, 1],
    '双剑': [1.1, 0.9, 1],
    '手杖': [1, 1.1, 1],
    '苦无': [1, 1.05, 1],
    '长枪': [1.05, 1, 1],
    '战戟': [1.1, 0.9, 1],
    '光枪': [1, 1.05, 1],
    '暗矛': [0.95, 1, 1],
    '长刀': [1.05, 1, 1],
    '小太刀': [1, 1, 1],
    '重剑': [1.1, 1, 1],
    '源力剑': [1, 1.05, 1]
}


def 武器冷却惩罚(武器类型, 输出类型, 版本='GF'):
    类型系数 = (0 if 输出类型 == '物理百分比' else (1 if 输出类型 == '魔法百分比' else 2))
    if 版本 == 'GF':
        return 武器冷却惩罚系数[武器类型][类型系数]
    else:
        return 1


# ----------- 防具 ----------- #

部位系数 = {'上衣': 0.30, '头肩': 0.20, '下装': 0.25, '腰带': 0.10, '鞋': 0.15}
品级加分 = {'稀有': 5, '神器': 8, '勇者': 11, '传说': 14, '史诗': 17, '神话': 18}


def 精通计算(装备等级, 品质, 强化等级, 部位):
    return round((20 + 2.5 * (装备等级 + 品级加分[品质] + int(强化等级 / 3))) * 部位系数[部位], 2)


def 精通体力(装备等级, 品质, 强化等级, 部位):
    return round((4 + (装备等级 + 品级加分[品质] + int(强化等级 / 3))) * 部位系数[部位], 2)


def 精通精神(装备等级, 品质, 强化等级, 部位):
    return 精通体力(装备等级, 品质, 强化等级, 部位) * 2


def 精通智力(装备等级, 品质, 强化等级, 部位):
    return 精通体力(装备等级, 品质, 强化等级, 部位) * 2


equip_list = [
    '大祭司的神启礼服', '大祭司的星祈礼袍', '大祭司的星祈披肩', '大祭司的星祈长裙', '大祭司的星祈凉鞋', '大祭司的星祈腰带',
    '大魔法师[???]的长袍', '魔法师[???]的长袍', '魔法师[???]的披风', '魔法师[???]的护腿', '魔法师[???]的长靴', '魔法师[???]的腰带',
    '浪漫旋律华尔兹', '优雅旋律华尔兹', '性感洒脱探戈', '魅惑律动伦巴', '激烈欢动踢踏', '热情舞动桑巴',
    '掌管生死之影夹克', '死亡阴影夹克', '死亡阴影护肩', '死亡阴影短裤', '死亡阴影长靴', '死亡阴影腰带',
    '皇家裁决者审判外套', '首席执行官裁决夹克', '首席执行官裁决肩甲', '首席执行官裁决短裤', '首席执行官裁决长靴', '首席执行官裁决腰带',
    '战无不胜上衣', '冲锋陷阵胸甲', '枪林弹雨护肩', '破釜沉舟护腿', '赤地千里战靴', '浴血奋战腰带',
    '爆裂大地之勇猛', '燃烧烈焰之勇气', '艰难求生之斗志', '肆虐狂风之意志', '寂静寒夜之忍耐', '守护战士之苦难',
    '炙炎：霸王树', '炙炎：火龙果', '炙炎：榴莲', '炙炎：荔枝', '炙炎：木瓜', '炙炎：山竹',
    '摧枯拉朽胸甲', '气吞山河战甲', '排山倒海护肩', '雷霆万钧护腿', '遮天蔽日长靴', '风起云涌腰带',
    '撒旦：愤怒之王', '撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '巴尔：堕落之魂', '亚巴顿：绝望地狱',
    '天堂之翼', '妖精之姿', '魔龙之心', '邪恶之角', '自然之核', '碎钢之牙',
    '千链万化战甲', '千链锁灵战甲', '千链锁灵肩甲', '千链锁灵护腿', '千链锁灵战靴', '千链锁灵腰带',
    '英明循环之生命', '奔流不息之岁月', '奔流不息之山川', '奔流不息之伽蓝', '奔流不息之银河', '奔流不息之狂风',
    '神赐的抉择', '人性的抉择', '矛盾的抉择', '命运的抉择', '守护的抉择', '正义的抉择',
    '生命脉动之地', '宽恕坚韧之地', '猛烈燃烧之炎', '蚕食新绿之息', '交织烈日之风', '宁静苍翠之水',
    '莱多：秩序创造者', '肯那兹：精神燎原之火', '莱多：变幻的规律', '盖柏：完美的均衡',
    '融化黑暗之温暖', '驱散月光之黎明', '拥抱晨曦之温暖', '寂静无言之露珠',
    '伽内什的永恒庇护', '四叶草之初心', '白象之庇护', '红兔之祝福',
    '至高之炎-伊弗利特', '冷焰之冰-温蒂妮', '火魔之焰-沙罗曼达', '祝福之风-西尔芙',
    '军神的心之所念', '军神的遗书', '军神的庇护宝石', '军神的古怪耳环',
    '永恒之海', '高贵之天', '智慧之地', '宽容之海',
    '时之魅影', '末日之刻', '时之漩涡', '时之矛盾',
    '等离子操控者', '能量回流控制者', '电光能量支配者', '电磁能量传送者',
    '深渊囚禁者长袍', '堕落深渊黑魔法衬衫', '暗黑术士亲笔古书', '堕落世界树之生命',
    '无尽的探求', '驱散黑暗短裤', '执着的探求', '暗黑术士的精髓',
    '永恒地狱黑暗之印', '堕入地狱之脚', '支配黑暗之环', '无尽地狱黑暗之印',
    '圣者的黄昏披风', '引路者的黄昏披风', '引路者的四季项链', '引路者的旅行书',
    '时间回溯之针', '时空漩涡护腿', '时间指引之针', '被困的时之沙',
    '次元穿越者之星', '次元漫步者长靴', '次元穿越者之印', '次元流星坠',
    '逆转结局', '地狱边缘', '悲痛者项链', '悲情者遗物',
    '响彻天地的咆哮', '灵魂的呐喊', '支配战场的呐喊', '寂寞的呼喊',
    '命运反抗者', '悲喜交加', '命运的捉弄', '命运挑战者',
    '灭世之怒', '泣血之恨', '激狂之怒', '失控之怒',
    '狂乱之逆转宿命', '疯狂之如影随形', '狂乱之坚如磐石', '狂乱之天灾降临',
    '心痛如绞的诀别', '崩溃世界的忧伤', '蓬勃生命的落幕', '悲剧人生的归寂'
]

weapon_list = [
    '星之海：巴德纳尔', '赤光剑路易纳斯', '战场的热血：安格巴迪', '信念徽章：自由', '骚动的冥焰', '哈蒂-赎月者', '太极天帝剑', '前瞻守卫者', '神之意象', '卡西姆的大剑', '白虎啸魂手套', '无瑕之意志手套', '青沙棍', '鸣鸿破影棍', '疯狂飓风', '痛苦之源', '太阴神：灵龟', '毁灭之碾压', '猎焰追魂拳套', '幻光绽放拳套',
    '寻觅海石竹',
    '雷霆怒啸手枪', '激光流星弓', '吟游诗人的轻吟', '午夜生死轮盘', '血枪之脉', '湍流', '强力打击-X', '乾坤极电炮', '绝杀：无人生还', '世界树的根须', '银月的祝福', '火焰地狱', '魔力之泉：加斯达利亚', '精灵浮风棍', '混沌之种', '歼灵灭魂矛', '吟唱：不灭之魂', '世界树之精灵', '纯白的祈祷', '圣者的慈悲',
    '闪耀的神威',
    '轮回之环：桓龙', '古代神兽的记忆', '暗战终结者', '拓荒者之路', '弗卡奴斯的第二个痕迹', '信念之重量', '泯灭之灵', '异教主的审判', '匿影', '暗杀团长的玉妆刀', '一叶障目', '血色舞会', '绿色生命的面容', '圣洁的精灵遗物', '血腥红宝石之眼', '天幕道火扇', '幻影狂欢长枪', '彪悍冲锋者', '万夫之勇', '沙岩幻戟',
    '千芒闪爆枪', '天将军：传承之光', '寂灭剧毒矛', '魅影飞龙', '金刚密藏刀', '夜天刀', '冰洁的红焰', '冥焰黑暗之触', '聚能擎天剑', '爆烈红焰', '远古御神战剑', '谍影：超级核心'
]
