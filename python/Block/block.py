
class Block:
    # ----------------------
    # 落ちてくるブロック
    #   height: 高さ
    #   width : 幅
    #   x     : 左端のx座標
    #   y     : 左端のy座標
    # ----------------------
    def __init__(self, height, width, x, y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
    
    # マップの状態を見て, y座標を更新する.
    def fixPosition(self, blockDown):
        sharpCount = 0
        while(True):
            for i in range(self.x, self.width + self.x):
                if(blockDown.blockMap[self.y - 1][i] == '#'):
                    sharpCount += 1
            if(sharpCount == 0 and 0 < self.y):
                self.y -= 1
            else:
                break
  

class BlockDown:
    # -------------------------------------------------------
    # ブロック落としのマップ
    #   height  : 高さ
    #   width   : 幅
    #   blockMap: '.' か '#' が入る height * width の2次元行列
    # -------------------------------------------------------
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.blockMap = [['.' for i in range(self.width)] for j in range(self.width)]
        
    # 入力されるN個のブロックを blockMap に埋めていく
    def fillMap(self, N):
        for _ in range(N):
            blockHeight, blockWidth, x = map(int, input().split())
            y = self.height - blockHeight
            block = Block(blockHeight, blockWidth, x, y)
            self.drawBlock(block)
            
            # print("-" * self.width)
            # self.printMap()
            # print("-" * self.width)

    # 実際に blockMap 上に '#' を書き込んでいる部分
    def drawBlock(self, block):
        block.fixPosition(self)
        for i in range(block.y, block.height + block.y):
                for j in range(block.x, block.width + block.x):
                    self.blockMap[i][j] = '#'
                   
    # blockMap の状態を表示する.
    # 仕様上, 上下逆転で表示させている.
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