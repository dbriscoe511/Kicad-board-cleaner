import pcbnew

class board_cleaner:

    def __init__(self):
        self.board = pcbnew.GetBoard()
        self.modules = self.board.GetModules()
        self.refs = (r.Reference() for r in self.modules)

    def hide_des(des_list,hide_fab,unhide,self):

        for r in self.refs:
            #strip number content. There is probably a better way to do this...
            des_letter = ''.join(c for c in r if not c.isnumeric())

            component = self.board.FindModuleByReference(r)
            hidden = r.IsVisible()

            if not des_letter in des_list:
                r.SetVisible(False)
                if hide_fab:
                    pass # cant find the function to do this
                    
            elif unhide and hidden:
                r.SetVisible(True)
                


