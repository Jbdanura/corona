import requests

def coronaData():
    corona = requests.get("https://api.covid19api.com/summary").json()

    confirmados = corona["Global"]["TotalConfirmed"]
    muertos =  corona["Global"]["TotalDeaths"]
    recuperados = corona["Global"]["TotalRecovered"]
    mortalidad = round(100 / (corona["Global"]["TotalConfirmed"] / corona["Global"]["TotalDeaths"]),1)
    total = [confirmados,muertos,recuperados, mortalidad]

    paises = []
    for i in corona["Countries"]:
        pais = i["Country"]
        confirmados = i["TotalConfirmed"]
        muertos = i["TotalDeaths"]
        recuperados = i["TotalRecovered"]
        try:
            mortalidad = round(100 / (i["TotalConfirmed"] / i["TotalDeaths"]),1)
        except:
            mortalidad = 0
        paises.append([pais,confirmados,muertos,recuperados, mortalidad])

    return total, paises