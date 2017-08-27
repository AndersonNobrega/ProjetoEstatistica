try:
    from scipy.io import wavfile
    from scipy.signal import spectrogram
    import numpy as np
    import os
    import matplotlib.pyplot as plt
    import subprocess
except ImportError:
    print("Import Error")
    quit(1)

def ler_musica(musica):
    """Le os arquivos no formato mp3 e converter para wav mono channel"""

    subprocess.call(['ffmpeg', '-i', '%s.mp3' %musica,'-ac', '1','-ab', '320k','temp.wav'])

def guardar_info(valor_medio, musica):
    """Guarda os dados da musica em um csv"""

    arquivo_csv = open("info.csv", "a")
    if os.stat("info.csv").st_size == 0:
        arquivo_csv.write(musica + "," + str(valor_medio))
    else:
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

    if np.mean(spectogram1) >= np.mean(spectogram2):
        return (np.mean(spectogram2) * 100) / np.mean(spectogram1)
    elif np.mean(spectogram2) > np.mean(spectogram1):
        return (np.mean(spectogram1) * 100) / np.mean(spectogram2)