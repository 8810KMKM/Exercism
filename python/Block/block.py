class BlockDown:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.blockMap = [['.' for i in range(self.width)] for j in range(self.width)]
        
    def fillMap(self, N):
        for _ in range(N):
            blockHeight, blockWidth, blockPoint = map(int, input().split())
            print(self.blockMap[blockHeight][blockWidth])
            print("hoge")
            self.blockMap[blockHeight][blockWidth] = '#'
            print(self.blockMap[blockHeight][blockWidth])
            print(self.blockMap[blockHeight + 1][blockWidth])
            # for i in range(blockHeight):
            #     for j in range(blockPoint, blockWidth + 1):
            #         self.blockMap[i][j] = '#'
            #         self.printMap()
                   
        
    def printMap(self):
        for i in range(self.height):
            line = ""
            # print(self.blockMap[i])
            for j in range(self.width):
                line += self.blockMap[self.height - i - 1][j]
            print(line)
    

if __name__ == '__main__':
    heiht, width, N = map(int, input().split())
    blockDown = BlockDown(heiht, width)
    blockDown.fillMap(N)
    blockDown.printMap()