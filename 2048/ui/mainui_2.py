from pysvg.builders import Svg, ShapeBuilder, StyleBuilder
from pysvg.text import *

def createblock(number):
    colors = {}
    colors[2]=('#eee4da','#776e65')
    colors[4]=('#ede0c8','#776e65')
    colors[8]=('#f2b179','#f9f6f2')
    colors[16]=('#f59563','#f9f6f2')
    colors[32]=('#f67c5f','#f9f6f2')
    colors[64]=('#f65e3b','#f9f6f2')
    colors[128]=('#edcf72','#f9f6f2')
    colors[256]=('#edcc61','#f9f6f2')
    colors[512]=('#eee4da','#776e65')
    colors[1024]=('#edc53f','#f9f6f2')
    colors[2048]=('#edc22e','#f9f6f2')
    
    canvas = Svg(0,0,100,100)
    sb = ShapeBuilder()
    canvas.addElement( sb.createRect(5,5,90,90,fill=colors[number][0]) )
    
    t = Text(number,50,60)
    t.set_style("font-family:FreeSans;font-weight:bold;font-size:36px;text-anchor:middle")
    t.set_fill(colors[number][1])
    canvas.addElement(t)
    canvas.save('/tmp/try7.svg')


createblock(32)
