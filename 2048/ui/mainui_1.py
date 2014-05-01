from pysvg.builders import Svg, ShapeBuilder, StyleBuilder
from pysvg.text import *

canvas = Svg(0,0,100,100)

sb = ShapeBuilder()
canvas.addElement( sb.createRect(5,5,90,90,fill="#00FF00") )

t = Text('Hello!',50,50)
t.set_style("font-family:FreeSans;font-weight:bold;font-size:24px;text-anchor:middle")
t.set_fill("#FF0000")
canvas.addElement(t)
 

canvas.save('/tmp/try7.svg')

