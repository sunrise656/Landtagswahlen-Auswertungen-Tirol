import matplotlib.pyplot as plt
import matplotlib as mplt
import csv

# Alle Daten aus den csv dateien in eine Liste einlesen
def read_data(election_paths):

    election_data = []
    for path in election_paths:
        data = []
        with open(path, "r", encoding="ISO-8859-1") as csv_file:
            reader = csv.reader(csv_file, delimiter= ";")
            for row in reader:
                data.append(row)
            
        election_data.append(data[2:])
    
    return election_data


# Funktion zum aussortieren von den bestimmten Geimeinde Daten
def sortdata(party, community, el_data):
    sorted_data = []
    
    for i in range(len(el_data)):
        for x in range(len(el_data[i])):
            wasit = False
            for j in range(len(el_data[i][x])):
                if el_data[i][x][3] == community and wasit == False:
                    wasit = True
                    #sorted_data.append(float(el_data[i][x][10].replace(",",".")))
                    for num, obj in enumerate(el_data[i][x], start=0):
                        try:
                            obj = float(obj)
                        except:
                            if party in obj:
                                search_num = num + 2
                                sorted_data.append(float(el_data[i][x][search_num].replace(",",".")))
        if len(sorted_data) != i+1:
            sorted_data.append(0)
    print(sorted_data)
    return sorted_data

def create_plot(party, community):
    # Liste von den csv Pfaden in Jahren aufsteigend
    election_paths = ["1989.csv","1994.csv","1999.csv","2003.csv","2008.csv","2013.csv","2018.csv"]

    el_data = read_data(election_paths)

    sort_data = sortdata(party, community, el_data)

    if sort_data == []:
        return "community or party not found"
    
    plot_years = [int(year[:4]) for year in election_paths]

    fig, ax = plt.subplots()

    plt.bar(plot_years,sort_data)
    plt.xlabel("Jahre")
    plt.ylabel(f"Parteiergebnisse in % für {community} und {party}")
    plt.savefig("plot.png", dpi=300, bbox_inches="tight")
    plt.close()

    return None

