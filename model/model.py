import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.anni=DAO.getAllAnni()
        self.nazioni=DAO.getAllNazioni()
        self.idMap={}
        self.grafo= nx.Graph()

        self.solBest=[]
        self.costoBest=-1
        pass

    def creaGrafo(self,anno,nazione):
        self.grafo.clear()
        nodi=DAO.getRetailers(anno,nazione)
        self.grafo.add_nodes_from(nodi)

        for a in nodi:
            self.idMap[a.Retailer_code]=a

        for i in self.grafo.nodes:
            archi=DAO.getArchi(anno,i.Retailer_code,nazione)
            for a in archi:
                if self.grafo.has_edge(i,self.idMap[a[0]]):
                    pass
                else:
                    if self.grafo.has_node(i) and self.grafo.has_node(self.idMap[a[0]]):
                        self.grafo.add_edge(i,self.idMap[a[0]],peso=a[1])


    def calcolaVolumi(self):
        dic={}
        for a in self.grafo.nodes:
            somma=0
            for i in self.grafo[a]:
                somma+= self.grafo[a][i]["peso"]
            dic[a]=somma

        lista=dic.items()
        ordinato=sorted(lista,key=lambda x: x[1],reverse=True)
        return ordinato

    def calcolaPercorso(self,max):
        parziale=[]
        partenza=list(self.grafo.edges)[0][0]
        self.ricorsione(parziale,partenza,max)
        print("*************")
        for a in self.solBest:
            print(a)
        print(self.costoBest)
        pass

    def ricorsione(self,parziale,partenza,max):

        if self.controllaTerminale(parziale,max):
            totale= self.calcolaTotale(parziale)
            if totale>self.costoBest:
                self.costoBest=totale
                self.solBest=copy.deepcopy(parziale)

            #terminale
        else:
            succ=list(self.grafo.neighbors(partenza))

            for a in succ:
                if self.controllaAggiunta(parziale,a,max):
                    parziale.append(a)
                    self.ricorsione(parziale,a,max)
                    parziale.pop()


    def calcolaTotale(self,parziale):
        somma=0.0
        for i in range(len(parziale)):
            if i<len(parziale)-1:
               somma+=self.grafo[parziale[i]] [parziale[i+1]]["peso"]
        return somma


    def controllaTerminale(self, parziale,max):
        if len(parziale)==max:
            return True
        else:
            return False
        pass

    def controllaAggiunta(self,parziale,a,max):
        if parziale==[]:
            return True
        if len(parziale)+1 == max:
            if a== parziale[0]:
                return True
            else:
                return False
        else:
            for i in parziale:
                if i==a:
                    return False
            return True


    def getNumNodes(self):
        return len(self.grafo.nodes)
    def getNumEdges(self):
        return len(self.grafo.edges)

