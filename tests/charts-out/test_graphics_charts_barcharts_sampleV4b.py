#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, Rect, Line, String
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=200,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(Rect(50,50,300,125,rx=0,ry=0,fillColor=None,fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Rect(75,67.85714,100,23.21429,rx=0,ry=0,fillColor=Color(1,0,0,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Rect(225,67.85714,100,35.71429,rx=0,ry=0,fillColor=Color(1,0,0,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(50,67.85714,350,67.85714,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(50,67.85714,50,62.85714,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(200,67.85714,200,62.85714,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(350,67.85714,350,62.85714,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,125,62.85714)
		v0.add(String(-10,-10,'Ying',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,275,62.85714)
		v0.add(String(-10.83,-10,'Yang',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(Line(50,50,50,175,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(50,67.85714,45,67.85714,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(50,94.64286,45,94.64286,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(50,121.4286,45,121.4286,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(50,148.2143,45,148.2143,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(50,175,45,175,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=10,strokeDashArray=None,strokeOpacity=None))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,45,67.85714)
		v0.add(String(-5,-4,'0',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,45,94.64286)
		v0.add(String(-10,-4,'15',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,45,121.4286)
		v0.add(String(-10,-4,'30',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,45,148.2143)
		v0.add(String(-10,-4,'45',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,45,175)
		v0.add(String(-10,-4,'60',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)
