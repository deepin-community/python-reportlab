#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, Line
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor
from rlextra.graphics.canvasadapter import DirectDrawFlowable

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=200,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(Line(75,75,175,75,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(75,75,75,70,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(125,75,125,70,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(175,75,175,70,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,100,70)
		v1=v0._nn(Group())
		v1.transform = (1,0,0,1,-24.012,-48)
		v1.add(DirectDrawFlowable(Paragraph(
'caseSensitive': 1
'encoding': 'utf8'
'text': 'Ying and Mao\xadTse\xadTung are bonkers'
'frags': [ParaFrag(__tag__='para', bold=0, fontName='Helvetica', fontSize=12, greek=0, italic=0, link=[], rise=0, text='Ying and Mao\xadTse\xadTung are bonkers', textColor=Color(1,0,0,1), us_lines=[])]
'style': <DDFStyle 'xlabel-generated'>
'bulletText': None
'debug': 0
'width': 48
'_wrapWidths': [48, 48]
'_width_max': 48.024
'height': 48
'_splitLongWordCount': 0
'_hyphenations': 1
'blPara': ParaFrag(__tag__='para', ascent=8.616, bold=0, descent=-2.484, fontName='Helvetica', fontSize=12, greek=0, italic=0, kind=0, lines=[(0.6360000000000028, ['Ying', 'and']), (0.6599999999999966, ['MaoTse-']), (-0.02400000000000091, ['Tung', 'are']), (5.3160000000000025, ['bonkers'])], link=[], rise=0, text='Ying and Mao\xadTse\xadTung are bonkers', textColor=Color(1,0,0,1), us_lines=[])
) #Paragraph))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,150,70)
		v1=v0._nn(Group())
		v1.transform = (1,0,0,1,-20.01,-48)
		v1.add(DirectDrawFlowable(Paragraph(
'caseSensitive': 1
'encoding': 'utf8'
'text': 'Yang is not a comm\xadun\xadist'
'frags': [ParaFrag(__tag__='para', bold=0, fontName='Helvetica', fontSize=12, greek=0, italic=0, link=[], rise=0, text='Yang is not a comm\xadun\xadist', textColor=Color(1,0,0,1), us_lines=[])]
'style': <DDFStyle 'xlabel-generated'>
'bulletText': None
'debug': 0
'width': 48
'_wrapWidths': [48, 48]
'_width_max': 40.02
'height': 48
'_splitLongWordCount': 0
'_hyphenations': 1
'blPara': ParaFrag(__tag__='para', ascent=8.616, bold=0, descent=-2.484, fontName='Helvetica', fontSize=12, greek=0, italic=0, kind=0, lines=[(7.979999999999997, ['Yang', 'is']), (21.312, ['not', 'a']), (11.339999999999996, ['comm-']), (22.656, ['unist'])], link=[], rise=0, text='Yang is not a comm\xadun\xadist', textColor=Color(1,0,0,1), us_lines=[])
) #Paragraph))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)
