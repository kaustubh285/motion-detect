from mosen import df

from bokeh.plotting import figure, output_file, show


fig = figure(x_axis_type = "datetime" , height = 400, width = 1000, title="MOSEN", sizing_mode='scale_width')
fig.yaxis.minor_tick_line_color = None
fig.ygrid[0].ticker.desired_num_ticks = 1

q = fig.quad(left=df["Start"], right=df["End"], bottom=0, top=1, color = "red")

output_file("caught.html")

show(fig)
