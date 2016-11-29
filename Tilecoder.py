numTilings = 4
numTiles = 9 * 9
def tilecode(in1, in2, tileIndices):
    # write your tilecoder here (5 lines or so)

    widthOfTile = (0.5+1.2) / 8
    heightOfTile = (0.07+0.07) / 8
    for i in range(len(tileIndices)):
        firstTile = i * numTiles
        deltaIn1 = int(((in1+1.2) + i * ( widthOfTile / numTilings)) / widthOfTile)
        print(deltaIn1)
        deltaIn2 = int(((in2+0.07) + i * ( heightOfTile / numTilings)) / heightOfTile)
        tileIndices[i] = int(firstTile + deltaIn1 + 9 * deltaIn2)


def printTileCoderIndices(in1, in2):
    tileIndices = [-1] * numTilings
    tilecode(in1, in2, tileIndices)
    print('Tile indices for input (', in1, ',', in2, ') are : ', tileIndices)

printTileCoderIndices(0.49,0.069)
# printTileCoderIndices(4.0,2.0)
# printTileCoderIndices(5.99,5.99)
# printTileCoderIndices(4.0,2.1)
