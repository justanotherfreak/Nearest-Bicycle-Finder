class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = []

    def print1(self, dist):
        for i in range(24):
            print(i, '-', dist[i])

    def print2(self, dist):
        for i in range(24):
            print(i, '-', dist[i])

    def nearest(self, dist):
        l = dist[-4:]
        fl = open("availability.txt")
        available = []
        for i in fl.readlines():
            available.append(int(i[6]))   
        
        fl.close()
        i = l.index(min(l))
        while not available[i] and l[i] != 10000:
            l[i] = 10000
            i = l.index(min(l))
        
        if l[i] == 10000:
            #print("No Cycles Available")
            return 0
        
        else:
            #print(20 + i, '-', l[i])
            return 20 + i
        
    def dijkstra(self,source):
        dset = []
        dist = [10000 for nodes in range(self.v)]
        dist[source] = 0
        back = [0 for nodes in range(self.v)]
        back[source] = None
        u = 0
        ud = 10000
        
        for k in range(self.v):
            for i in range(self.v):

                if i not in dset and dist[i] < ud:
                    u = i
                    ud = dist[i]
                
            
            dset.append(u)
            ud = 10000
            

            for j in range(self.v):
                if self.graph[u][j] > 0 and dist[u] + self.graph[u][j] < dist[j]:
                    dist[j] = dist[u] + self.graph[u][j]
                    back[j] = u


        #self.print1(back)
        #self.print2(dist)
        hs = self.nearest(dist)
        if hs == 0:
            return 0
        else:
            return [hs,dist[hs],back]



def main(v):
    m = Graph(24)
    m.graph =  [[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	54,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	23,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	18,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	23,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	123,0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	33,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	14,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	53,	0,	0,	0,	0,	11,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	28,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	22,	0,	0,	0,	0],
                [54,0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	51,	0,	0,	0,	0,	0,	0,	0,	0,	17,	0,	0,	0],
                [0,	23,	0,	0,	0,	0,	0,	0,	0,	0,	51,	0,	66,	0,	51,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	123,0,	0,	0,	0,	0,	0,	66,	0,	36,	0,	0,	0,	0,	116,0,	0,	0,	0,	0],
                [0,	0,	0,	23,	0,	0,	0,	0,	0,	0,	0,	0,	36, 0,	0,	0,	0,	0,	0,	0,	0,	20,	0,	0],
                [0,	0,	0,	0,	0,	0,	14,	0,	0,	0,	0,	51,	0,	0,	0,	54,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	28,	0,	0,	0,	0,	0,	54,	0,	55,	0,	65,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	55,	0,	26,	0,	0,	0,	0,	28,	0],
                [0,	0,	18,	0,	0,	0,	0,	53,	0,	0,	0,	0,	0,	0,	0,	0,	26,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	116,0,	0,	65,	0,	0,	0,	65,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	33,	0,	0,	0,	22,	0,	0,	0,	0,	0,	0,	0,	0,	65,	0,	0,	0,	0, 64],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	17,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	20,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	11,	0,	0,	0,	0,	0,	0,	0,	0,	28,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	64,	0,	0,	0,	0]]

    node = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9}

    ret = m.dijkstra(node[v])
    return ret


#ret = main('B')

    

    

