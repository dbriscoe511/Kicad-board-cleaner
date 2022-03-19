import pcbnew

class board_cleaner:

    def __init__(self):
        self.board = pcbnew.GetBoard()
        self.modules = self.board.GetModules()

    def hide(hide_ref,hide_val,des_list_ref,des_list_val,hide_fab,unhide_ref,unhide_val,self):
        for module in self.modules:
            r = module.Reference()
            v = module.Value()
            #strip number content. There is probably a better way to do this...
            des_letter = ''.join(c for c in str(r) if not c.isnumeric())

            #component = self.board.FindModuleByReference(r)
            hidden_ref = r.IsVisible()
            hidden_val = v.IsVisible()

            if hide_ref:
                if not des_letter in des_list_ref:
                    r.SetVisible(False)
                    if hide_fab:
                        pass # cant find the function to do this   
                elif des_list_ref.contains('*'):
                    r.SetVisible(False)
                elif unhide_ref and hidden_ref:
                    r.SetVisible(True)

            if hide_val:
                if not des_letter in des_list_val:
                    v.SetVisible(False)
                elif des_list_ref.contains('*'):
                    v.SetVisible(False)
                elif unhide_val and hidden_val:
                    v.SetVisible(True)





