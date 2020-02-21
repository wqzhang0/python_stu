# -*- coding: UTF-8 -*-
from pyautocad import Autocad, APoint

# 这个true表示没有文件则打开一个，CAD有弹窗时会打开或者创建失败
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

p1 = APoint(0, 0)  # 点的位置坐标
p2 = APoint(50, 25)


def gen_data():
    line_list = []
    line_list.append({"num": "1", "line": [20, 50]})
    line_list.append({"num": "2", "line": [26, 40]})
    line_list.append({"num": "3", "line": [56, 50]})
    line_list.append({"num": "4", "line": [14, 25]})
    line_list.append({"num": "5", "line": [75, 50]})
    line_list.append({"num": "6", "line": [50, 90]})
    line_list.append({"num": "7", "line": [60, 78]})
    line_list.append({"num": "8", "line": [65, 45]})
    return line_list


if __name__ == '__main__':

    index_x = 0
    index_y = 0
    print(acad.doc)
    line_list = gen_data()
    for line_obj in line_list:
        line = line_obj['line']

        w = line[0]
        h = line[1]

        # acad.model.AddLine(APoint(index_x, index_y + h), APoint(index_x + w, index_y + h))  # 上
        # acad.model.AddLine(APoint(index_x, index_y), APoint(index_x + w, index_y))  # 下
        # acad.model.AddLine(APoint(index_x, index_y), APoint(index_x, index_y + h))  # 左
        # acad.model.AddLine(APoint(index_x + w, index_y), APoint(index_x + w, index_y + h))  # 右

        text = acad.model.AddText(line_obj['num'], APoint(index_x + 2, index_y + 2), 1.5)  # 添加文本
        index_x = index_x + w
        index_x += 2
