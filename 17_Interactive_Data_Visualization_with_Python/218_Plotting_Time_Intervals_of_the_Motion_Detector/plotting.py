from motion_detector import DF 
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

DF["Start_string"]=DF["Start"].df.strftime("%Y-%m-%d %H:%M:%S")
DF["End_string"]=DF["End"].df.strftime("%Y-%m-%d %H:%M:%S")

CDS = ColumnDataSource(DF)

p = figure(x_axis_type='datetime', height=100, width=500, responsive=True, title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

HOVER = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(HOVER)

q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=CDS)

output_file("Graph.html")
show(p)
