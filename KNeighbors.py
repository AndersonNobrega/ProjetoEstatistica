try:
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.externals import joblib
    import sqlite3
except ImportError as error:
    print("Import Error : %s" % error)
    quit(1)

conn = sqlite3.connect("musicas.db")
cursor = conn.cursor()
knn = joblib.load("KNNAlgorithm.pkl")
lista = ["Rock", "Indie", "Pop", "Blues", "Jazz", "Classical", "MPB", "Samba", "Pagode", "Eletronic"]

def buscar(musica):
    cursor.execute('SELECT * FROM musicas')

    for i in cursor.fetchall():
        if musica == i[0]:
            valor = prediction(i[1])
            print("Música : %s\nPrediction = %s" %(i[0], lista[int(valor)]))
            return True
    print("Música não encontrada no banco de dados.")
    return False

def prediction(valor):
    return knn.predict(valor)