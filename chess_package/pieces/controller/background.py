
def generate_board(resolution, parameters):

    pass

def generate_addons(resolution, parameters):

    pass

def generate_window(board,addons):

    pass

class background:
    def __init__(self, resolution, parameters):
        self.board=generate_board(resolution, parameters['Chessboard'])
        self.addons=generate_addons(resolution, parameters['Addons'])
        self.window=generate_window(self.board,self.addons)