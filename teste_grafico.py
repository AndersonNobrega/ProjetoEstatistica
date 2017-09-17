from bokeh.io import show, export_png
from bokeh.models import ColumnDataSource
from bokeh.palettes import Greys256
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

estilos = {"Gênero" : ['Rock', 'Pop', 'Rap', 'Samba', 'Forró', 'Funk',
                        'Blues','Jazz', 'MPB','Pagode','Indie','Música Classica',
                        'Eletrônica', 'Axé', 'Sertanejo'],
           "Porcentagem" : [5, 10, 15, 34, 24, 35, 20, 30, 40, 50, 60, 70, 80, 90, 100]
           }

source = ColumnDataSource(data=estilos)

p = figure(x_range=estilos["Gênero"], plot_height=350, plot_width=1050, toolbar_location=None, title="Estilos Musicais")
p.vbar(x='Gênero', top='Porcentagem', width=0.8, source=source, line_color='white',
       fill_color=factor_cmap('Gênero', palette=Greys256[:256:10], factors=estilos["Gênero"]))

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = 100
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

export_png(p, "graficos/barra.png")
show(p)