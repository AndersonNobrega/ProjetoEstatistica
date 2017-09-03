try:
    from scipy.io import wavfile
    from scipy.signal import spectrogram
    from scipy.stats import iqr
    import numpy as np
    import os
    import matplotlib.pyplot as plt
    import subprocess
    import pandas as pd
except ImportError:
    print("Import Error")
    quit(1)

def ler_musica(musica):
    """Le os arquivos no formato mp3 e converter para wav mono channel"""

    subprocess.call(['ffmpeg', '-i', '%s.mp3' %musica,'-ac', '1','-ab', '320k','%s.wav' %musica])

def guardar_info(valor_medio, musica="Desconhecida"):
    """Guarda os dados da musica em um csv"""

    arquivo_csv = open("info.csv", "a")
    if os.stat("info.csv").st_size == 0:
        arquivo_csv.write("Música,Valores")
    arquivo_csv.write("\n" + musica + "," + str(valor_medio))
    arquivo_csv.close()

def plotar(spectogram, times, frequencies):
    """Plota o spectrograma da música"""

    spectogram = 10 * np.log10(spectogram)

    plt.pcolormesh(times, frequencies, spectogram)
    plt.show()

def analise_musica(musica):
    """Le o arquivo wav da musica e retira as informações"""

    sample_rate, samples = wavfile.read('%s.wav' %musica)

    frequencies, times, spectogram = spectrogram(samples, sample_rate)

    return np.mean(spectogram)

def comparar_musica(spectogram1, spectogram2):
    """Compara o valor médio de 2 spectrogramas"""

    if spectogram1 >= spectogram2:
        return (spectogram2 * 100) / spectogram1
    elif spectogram1 < spectogram2:
        return (spectogram1 * 100) / spectogram2

def guardar_comparacoes(lista, nome_musica):

    arquivo = open("Recomendacoes_%s.txt" %nome_musica, "w")
    if os.stat("Recomendacoes_%s.txt" %nome_musica).st_size == 0:
        arquivo.write("Melhores recomendações para a música %s\n" %nome_musica)
    for i in range(len(lista)):
        if lista[i][0] != nome_musica:
            arquivo.write("\n%s - %.2f" %(lista[i][0], lista[i][1]))

def ler_dados(valor_comparar, nome_musica):
    "Recebe o valor de uma música e compara com todas que estão no dataset"

    arquivo = pd.read_csv("info.csv")
    dataset = pd.DataFrame(arquivo)
    valores = []
    for i in range(len(dataset["Valores"])):
        valor = comparar_musica(valor_comparar, dataset["Valores"][i])
        valores.append([dataset["Música"][i], valor])
    valores.sort(key=lambda x: x[1], reverse=True)
    guardar_comparacoes(valores, nome_musica)

def main():

    for file in os.listdir(os.getcwd()):
        if file.endswith(".mp3"):
            nome_musica = os.path.splitext(os.path.basename(file))[0]
            ler_musica(nome_musica)
            spec1 = analise_musica(nome_musica)
            guardar_info(spec1, nome_musica)

    for file in os.listdir(os.getcwd()):
        if file.endswith(".wav"):
            os.remove(file)

main()