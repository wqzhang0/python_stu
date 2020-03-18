# -*- coding: UTF-8 -*-
"""
正常门帘版式
"""
import random


def gen_data():
    line_list = []
    for i in range(200):
        # line_list.append({"num": 6500 + i, "line": [random.randint(70, 180), random.randint(175, 300)]})
        line_list.append({"num": 7500 + i, "line": [random.randint(175, 300), random.randint(70, 180)]})

    return line_list


# 写字


# align='MIDDLE_RIGHT'
# Using a text style


if __name__ == '__main__':

    import ezdxf

    doc = ezdxf.new('R12', setup=True)  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'

    msp = doc.modelspace()  # add new entities to the modelspace

    doc.layers.new(name='MyLines', dxfattribs={'color': 7})

    index_x = 0
    index_y = 0
    line_list = gen_data()
    doc.styles.new('myStandard2', dxfattribs={'font': 'C:\\Windows\\Fonts\\OpenSans-Italic.ttf',
                                              })
    for line_obj in line_list:
        line = line_obj['line']

        x = line[0]
        y = line[1]

        # 划线
        msp.add_line((index_x, index_y + y), (index_x + x, index_y + y), dxfattribs={'layer': 'MyLines'})
        # 划线
        msp.add_line((index_x, index_y), (index_x + x, index_y), dxfattribs={'layer': 'MyLines'})
        # 划线
        msp.add_line((index_x, index_y), (index_x, index_y + y), dxfattribs={'layer': 'MyLines'})
        # 划线
        msp.add_line((index_x + x, index_y), (index_x + x, index_y + y), dxfattribs={'layer': 'MyLines'})

        # drawing.add(dxf.text(f"{line_obj['num']}-B", (index_x + 1, index_y + y / 2 + 1), height=2,
        #                      layer='WQ_TEXT_LAYER'))
        # 上扇面数字
        msp.add_text(f"{line_obj['num']}-B",
                     dxfattribs={
                         # 'font':'C:\\Windows\\Fonts\\OpenSans-Italic.ttf',
                         # 'style': 'LiberationSerif',
                         'layer': 'MyLines',
                         'color': 1,
                         'height': 1}
                     ).set_pos((index_x + 1, index_y + y / 2 + 1), align='LEFT')

        msp.add_text(f"{line_obj['num']}-A",
                     dxfattribs={
                         # 'style': 'LiberationSerif',
                         # 'font':'C:\\Windows\\Fonts\\OpenSans-Italic.ttf',
                         'layer': 'MyLines',
                         'color': 1,
                         'height': 1}
                     ).set_pos((index_x + 1, index_y + 1), align='LEFT')

        # drawing.add(
        #     dxf.text(f"{line_obj['num']}-A", (index_x + 1, index_y + 1), height=2, layer='WQ_TEXT_LAYER'))  # 下扇面数字
        # drawing.add(
        #     dxf.line((index_x + x / 2, index_y), (index_x + x / 2, index_y + y), color=7, layer='WQ_LINES'))  # 中线

        # 划线
        msp.add_line((index_x, index_y + y / 2), (index_x + x, index_y + y / 2), dxfattribs={'layer': 'MyLines'})

        index_x = index_x + x
        index_x += 2

    doc.saveas("p2simple_text.dxf")
