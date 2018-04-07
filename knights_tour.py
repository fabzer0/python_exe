from pythonds.graphs import Graph

def knightTour(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = postToNodeId(row,col,bdSize)
            newPositions = genLegalMoves(row,col,bdSize)
            for e in newPositions:
                nid =  postToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def postToNodeId(row,column,board_size):
    return (row * board_size) + column

def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffSets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]

    for i in moveOffSets:
        newX = x + i[0]
        newY = y + i[1]
        if legal(ord(newX, bdSize) and \
                 legal(ord(newY, bdSIze):
            newMoves.append((newX, newY))
    return newMoves

def legal(ord(x, bdSize)):
    if x > 0 and x < bdSize:
        return True
    else:
        return False

              

                                             
                                             
        
