class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        brdVert = dict()
        brdHor = dict()
        brdSqr = dict()

        for i in range(9):
            brdHor[i] = list()
            for j in range(9):
                if board[i][j] == '.': continue
                elif board[i][j] in brdHor[i]: return False
                else: brdHor[i].append(board[i][j])


        for i in range(9):
            brdVert[i] = list()
            for j in range(9):
                if board[j][i] == '.': continue
                if board[j][i] in brdVert[i]: return False
                else: brdVert[i].append(board[j][i])


        for i in range(0,9,3):
            for j in range(0,9,3):
                brdSqr[i+j] = list()
                for z in range(3):
                    for x in range(3):
                        if board[z+i][x+j] == '.': continue
                        if board[z+i][x+j] in brdSqr[i+j]: return False
                        else: brdSqr[i+j].append(board[z+i][x+j])
 
        return True

        

         