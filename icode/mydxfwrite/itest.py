from dxfwrite import DXFEngine as dxf

drawing = dxf.drawing('test.dxf')
drawing.add_layer('WQ_LINES')
drawing.add(dxf.line((0, 0), (1, 0), color=7, layer='WQ_LINES'))
drawing.add(dxf.line((2, 2), (3, 1), color=6, layer='WQ_LINES'))


drawing.add_layer('WQ_TEXT_LAYER')
drawing.add(dxf.text("0558", (4, 5), height=0.1, layer='WQ_TEXT_LAYER'))

# text = dxf.text('Text', (1.0, 1.0), height=0.7, rotation=45)
# text['layer'] = 'TEXT'
# text['color'] = 7
# drawing.add(text)

drawing.save()


