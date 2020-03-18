# -*- coding: UTF-8 -*-
import random


def gen_data():
    line_list = []
    for i in range(2):
        # line_list.append({"num": 6500 + i, "line": [random.randint(70, 180), random.randint(175, 300)]})
        line_list.append({"num": 7500 + i, "line": [random.randint(175, 300), random.randint(70, 180)]})

    return line_list


if __name__ == '__main__':
    from dxfwrite import DXFEngine as dxf

    drawing = dxf.drawing('print_rectangle.dxf')
    drawing.add_layer('WQ_LINES')

    drawing.add_layer('WQ_TEXT_LAYER')

    index_x = 0
    index_y = 0
    line_list = gen_data()
    for line_obj in line_list:
        line = line_obj['line']

        x = line[0]
        y = line[1]
        drawing.add(dxf.line((index_x, index_y + y), (index_x + x, index_y + y), color=7, layer='WQ_LINES'))  # 上
        drawing.add(dxf.line((index_x, index_y), (index_x + x, index_y), color=7, layer='WQ_LINES'))  # 下
        drawing.add(dxf.line((index_x, index_y), (index_x, index_y + y), color=7, layer='WQ_LINES'))  # 左
        drawing.add(dxf.line((index_x + x, index_y), (index_x + x, index_y + y), color=7, layer='WQ_LINES'))  # 右

        drawing.add(dxf.text(f"{line_obj['num']}-B", (index_x + 1, index_y + y / 2 + 1), height=2,
                             layer='WQ_TEXT_LAYER'))  # 上扇面数字
        drawing.add(
            dxf.text(f"{line_obj['num']}-A", (index_x + 1, index_y + 1), height=2, layer='WQ_TEXT_LAYER'))  # 下扇面数字
        # drawing.add(
        #     dxf.line((index_x + x / 2, index_y), (index_x + x / 2, index_y + y), color=7, layer='WQ_LINES'))  # 中线
        drawing.add(
            dxf.line((index_x, index_y + y / 2), (index_x + x, index_y + y / 2), color=7, layer='WQ_LINES'))  # 中线

        index_x = index_x + x
        index_x += 2

    drawing.save()
