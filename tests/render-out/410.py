#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, Path, String
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing__410Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=100.0,height=100.0,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		v0=self._nn(Group())
		v0.transform = (1,0,0,-1,0,100)
		v0.add(Path(points=[30,1,70,1,99,30,99,70,70,99,30,99,1,70,1,30],operators=[0,1,1,1,1,1,1,1,3],isClipPath=0,autoclose='svg',fillMode=1,fillColor=Color(0,0,0,1),fillOpacity=1,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		v0.add(Path(points=[31,3,69,3,97,31,97,69,69,97,31,97,3,69,3,31],operators=[0,1,1,1,1,1,1,1,3],isClipPath=0,autoclose='svg',fillMode=1,fillColor=Color(.666667,.133333,.2,1),fillOpacity=1,strokeColor=None,strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		v1=v0._nn(Group())
		v1.transform = (1,0,0,-1,0,136)
		v1.add(String(50,68,'410',textAnchor='middle',fontName='Helvetica',fontSize=48,fillColor=Color(1,1,1,1)))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing__410Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)
