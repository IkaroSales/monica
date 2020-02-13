import requests
import pandas as pd
from pandas import read_excel

class Entrega():
    def __init__(self, itemEntrega, produto, endereco, cep, complemento):
        self.itemEntrega = itemEntrega
        self.produto = produto
        self.endereco = endereco
        self.cep = cep
        self.complemento = complemento

def send_request(entrega):
    url_tst = "https://docs.google.com/forms/d/e/1FAIpQLSfc5gkEAHvXB9zSZYHUewj466yhpE2_hf7r1JzJYu088VgIzA/formResponse"
    url_def = "https://docs.google.com/forms/d/e/1FAIpQLSeGkKoum1HEonSxWeZP8r2PDHBncBVxRn61O4x4SwgTILDWtQ/formResponse"

    data = {
        "entry.11703947"   : "Monica Maria Wanderley Padilha",
        "entry.283002341"  : entrega.itemEntrega,
        "entry.96278573"   : entrega.cep,
        "entry.1587431302" : entrega.endereco,
        "entry.1495180370" : entrega.complemento
    }

    print(data)
    result = requests.post(url_tst, data)

    print(result)

def excel_file():
    pd.set_option("display.max_rows", 1000)
    pd.set_option("display.max_columns", 10)

    data = pd.read_excel("automacao.xlsx", "Planilha1")

    for i in range(data.shape[0]):
        itemEntrega = data.iloc[i]["Item de entrega"]
        produto     = data.iloc[i]["Produto"]
        cep         = data.iloc[i]["CEP"]
        endereco    = data.iloc[i]["Endereço"]
        complemento = data.iloc[i]["Complemento"]

        entrega = Entrega(itemEntrega, produto, endereco, cep, complemento)
        send_request(entrega)

excel_file()
