from bokeh.io import output
from MotionDetector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d" "%H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d" "%H:%M:%S")

cds = ColumnDataSource(df)

f = figure(x_axis_type = "datetime", height = 100, width = 500 , sizing_mode = "scale_width", title = "Motion Graph")

q = f.quad(left = 'Start', right = 'End', bottom = 0, top = 1, source = cds)
#to plot a quadrant glyph, we need a top, bottom, left and right corners of the glyph, we are using the start time as left and end time as the right

hover = HoverTool(tooltips = [("Start", "@Start_string"), ("End", "@End_string")])
f.add_tools(hover)

output_file("Graph.html")

show(f)
