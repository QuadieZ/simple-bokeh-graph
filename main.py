# Import Libraries
from bokeh.plotting import figure, output_file, show, ColumnDataSource, save
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import inferno

import pandas as pd

# Create Dataframe and source
df = pd.read_csv('./data.csv')
source = ColumnDataSource(df)

output_file('index.html')

product_list = source.data['Product'].tolist()

# Add plot
p = figure(
    y_range = product_list,
    plot_width = 850,
    plot_height = 650,
    title = 'สินค้าออกสำคัญ 10 อันดับแรกของไทย',
    x_axis_label = 'มูลค่า : ล้านบาท',
    tools = "pan, box_select, zoom_in, zoom_out, save, reset"
)

# Render glyph
p.hbar(
    y = 'Product',
    right = 'Worth',
    left = 0,
    height = 0.4,
    fill_color = factor_cmap(
        'Product',
        palette = inferno(10),
        factors = product_list
    ),
    source = source
)

# Add tool
hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@Product</h3>
        <div><strong>Worth: </strong>@Worth</div>
        <div><img src="@Picture" width="200"></div>
    </div>
"""

p. add_tools(hover)
save(p)