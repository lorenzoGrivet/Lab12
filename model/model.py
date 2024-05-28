import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.anni=DAO.getAllAnni()
        self.nazioni=DAO.getAllNazioni()

        self.grafo= nx.Graph()
        pass

    def creaGrafo(self,anno,nazione):
        nodi=DAO.getRetailers(anno,nazione)
        self.grafo.add_nodes_from(nodi)

        pass