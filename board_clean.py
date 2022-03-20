import pcbnew

class board_cleaner:

    def __init__(self,board,logger):
        self.board = board
        self.modules = self.board.GetFootprints()
        self.logger = logger
        self.logger.info("cleaner initialized")

    def hide(hide_ref,hide_val,des_list_ref,des_list_val,hide_fab,unhide_ref,unhide_val,self):
        self.logger.info("starting clean:")
        # log all function call parameters
        self.logger.info(f"hide_ref {hide_ref} hide val {hide_val} des_list_ref {des_list_ref} des_list_val {des_list_val} hide_fab {hide_fab} unhide_ref {unhide_ref} unhide val {unhide_val}")
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
                    self.logger.info(f"ref hidden {r}")
                    if hide_fab:
                        pass # cant find the function to do this   
                elif des_list_ref.contains('*'):
                    r.SetVisible(False)
                    self.logger.info("all refs hidden with *")
                elif unhide_ref and hidden_ref:
                    r.SetVisible(True)
                    self.logger.info(f"ref shown {r}")

            if hide_val:
                if not des_letter in des_list_val:
                    v.SetVisible(False)
                    self.logger.info(f"val {v} hidden on des {r}")
                elif des_list_ref.contains('*'):
                    v.SetVisible(False)
                    self.logger.info("all vals hidden with *")
                elif unhide_val and hidden_val:
                    v.SetVisible(True)
                    self.logger.info(f"val {v} shown on des {r}")
                    
        pcbnew.Refresh()





