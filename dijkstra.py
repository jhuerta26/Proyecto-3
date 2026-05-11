import algorithms as a

def dijkstra():
     #Nodo raiz para algoritmo Dijkstra
        rootNode=5

        ###########Grafo ErdosRenyi############################
        #Grafo ErdosRenyi de 10 nodos
        grafoErdos=a.randomErdosRenyi(10, 10, directed=False, auto=False)
        dijkstra=grafoErdos.Dijkstra(rootNode)
        grafoErdos.saveGV()
        dijkstra.saveGVwithLabels()
        print("hola")

        #Grafo ErdosRenyi de 200 nodos
        grafoErdos=a.randomErdosRenyi(200, 200, directed=False, auto=False)
        dijkstra=grafoErdos.Dijkstra(rootNode)
        grafoErdos.saveGV()
        dijkstra.saveGVwithLabels()
    
        #####################Grafo Gilbert ####################################

        #Grafo Gilbert de 10 nodos
        grafoGilbert=a.randomGilbert(10, 0.6, directed=False, auto=False)
        dijkstra=grafoGilbert.Dijkstra(rootNode)
        grafoGilbert.saveGV()
        dijkstra.saveGVwithLabels()  

        #Grafo Gilbert de 200 nodos
        grafoGilbert=a.randomGilbert(200, 0.2, directed=False, auto=False)
        dijkstra=grafoGilbert.Dijkstra(rootNode)
        grafoGilbert.saveGV()
        dijkstra.saveGVwithLabels()


        #####################Grafo Malla################################

        #Grafo Malla de 20 nodos
        grafoMalla=a.gridGraph(10,2,directed=False)
        dijkstra=grafoMalla.Dijkstra(rootNode)
        grafoMalla.saveGV()
        dijkstra.saveGVwithLabels()

        #Grafo Malla de 200 nodos
        grafoMalla=a.gridGraph(20,10,directed=False)
        dijkstra=grafoMalla.Dijkstra(rootNode)
        grafoMalla.saveGV()
        dijkstra.saveGVwithLabels()

        ###########################Grafo Geografico#######################################

        #Grafo Geografico de 10 nodos
        grafoGeografico=a.randomGeografico(10, 0.5, directed=False, auto=False)
        dijkstra=grafoGeografico.Dijkstra(rootNode)
        grafoGeografico.saveGV()
        dijkstra.saveGVwithLabels()

        #Grafo Geografico de 200 nodos
        grafoGeografico=a.randomGeografico(200, 0.3, directed=False, auto=False)
        dijkstra=grafoGeografico.Dijkstra(rootNode)
        grafoGeografico.saveGV()
        dijkstra.saveGVwithLabels()
        #####################Grafo BarabasiAlbert################################
        
        #Grafo BarabasiAlbert de 10 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(10, 5, directed=False, auto=False)
        dijkstra=grafoBarabasiAlbert.Dijkstra(rootNode)
        grafoBarabasiAlbert.saveGV()
        dijkstra.saveGVwithLabels()

        #Grafo BarabasiAlbert de 200 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(200, 3, directed=False, auto=False)
        dijkstra=grafoBarabasiAlbert.Dijkstra(rootNode)
        grafoBarabasiAlbert.saveGV()
        dijkstra.saveGVwithLabels()

        #####################Grafo DorogovtsevMendes################################

        #Grafo DorogovtsevMendes de 10 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=10, directed=False)
        dijkstra=grafoDorogovt.Dijkstra(rootNode)
        grafoDorogovt.saveGV()
        dijkstra.saveGVwithLabels()

        #Grafo DorogovtsevMendes de 200 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=200, directed=False)
        dijkstra=grafoDorogovt.Dijkstra(rootNode)
        grafoDorogovt.saveGV()
        dijkstra.saveGVwithLabels()