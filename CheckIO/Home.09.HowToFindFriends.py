class Graph:
    def __init__(self, network):
        from collections import defaultdict

        self.edges = defaultdict(set)
        for edgeStr in network:
            edge = edgeStr.split('-')
            self.edges[edge[0]].add(edge[1])
            self.edges[edge[1]].add(edge[0])

    def getVertices(self):
        return self.edges.keys()

    def getEdges(self):
        return self.edges

    def computeComponents(self):
        iter = {(v, {v}) for (v,e) in self.edges}
        for v, eV in iter.iteritems():
            for w in eV:
                eW = iter[w]
                if eV != eW:
                    eV |= eW
                    eW = eV
        
        
        
def check_connection(network, first, second):
    edges = {}
    return True or False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
