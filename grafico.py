try:
    import sqlite3
    import os
    import pandas as pd
    from bokeh.io import show, export_png
    from bokeh.models import ColumnDataSource, LabelSet
    from bokeh.palettes import Greys256
    from bokeh.plotting import figure
    from bokeh.transform import factor_cmap
except ImportError as error:
    print("Import Error : %s" % error)
    quit(1)

conn = sqlite3.connect("generos.db")
conn2 = sqlite3.connect("musicas.db")
cursor = conn.cursor()
cursor2 = conn2.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS generos "
                   "(genero TEXT PRIMARY KEY NOT NULL , valor FLOAT NOT NULL)")

def inserir_dados(genero, novo_valor):
    """Insere os dados passados no banco de dados"""

    try:
        cursor.execute("INSERT INTO generos(genero, valor) VALUES(?, ?)", (genero, float(novo_valor)))
    except sqlite3.IntegrityError:
        print("Música ja se encontra no banco de dados.\n")
    conn.commit()

def criar_dataframe_generos():
    """Le os dados do banco SQL, cria um dataframe, e organiza os dados"""

    cursor.execute('SELECT * FROM generos')
    tabela_musicas = pd.DataFrame(cursor.fetchall(),
                                  columns=["Gêneros", "Valores"])
    return tabela_musicas

def criar_dataframe_musicas():
    """Le os dados do banco SQL, cria um dataframe, e organiza os dados"""

    cursor2.execute('SELECT * FROM musicas')
    tabela_musicas = pd.DataFrame(cursor2.fetchall(),
                                  columns=["Músicas", "Valores"])
    return tabela_musicas

generos = criar_dataframe_generos()
musicas = criar_dataframe_musicas()

def buscar_indice(musica_procurar):
    """Busca indice da música"""

    cursor2.execute('SELECT * FROM musicas')
    cont = 0

    for i in cursor2.fetchall():
        if i[0] == musica_procurar:
            return cont
        cont += 1

    return -1

def criar_dataframe_plot(musica):
    """Cria dataframe para ser plotado no gráfico"""

    valor = []
    nome = []

    index = buscar_indice(musica)
    if index != -1:
        for i in generos["Valores"]:
            if musicas["Valores"][index] >= i:
                s = (i * 100) / musicas["Valores"][index]
                valor.append(round(s, 0))
            else:
                s = (musicas["Valores"][index] * 100) / i
                valor.append(round(s, 0))

        for i in generos["Gêneros"]:
            nome.append(i)

        tabela_nova = {"Gêneros" : nome, "Valores" : valor}
        return tabela_nova
    else:
        print("Música não encontrada no banco de dados.")
        return None

def plotar_grafico(dataframe, musica):
    """Plota grafico a partir do dataframe passado"""

    source = ColumnDataSource(data=dataframe)

    p = figure(x_range=dataframe["Gêneros"], plot_height=400, plot_width=700,
               x_axis_label="Gêneros", y_axis_label="Porcentagem", toolbar_location=None,
               title=musica)

    labels = LabelSet(x="Gêneros", y="Valores", text="Valores", level='glyph',
            x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')

    p.vbar(x='Gêneros', top='Valores', width=0.7, source=source, line_color='white',
           fill_color=factor_cmap('Gêneros', palette=Greys256, factors=dataframe["Gêneros"]))

    p.add_layout(labels)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 110
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    show(p)

def resultado(musica):
    """Retorna o resultado encontrado caso haja um"""

    resultados = criar_dataframe_plot(musica)
    if resultados != None:
        plotar_grafico(resultados, musica)
    else:
        return False