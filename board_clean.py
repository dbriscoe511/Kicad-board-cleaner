import pcbnew

class board_cleaner:

    def __init__(self,board,logger):
        self.board = board
        self.modules = self.board.GetFootprints()
        self.logger = logger
        self.logger.info("cleaner initialized")

    def hide(self,hide_ref,hide_val,des_list_ref,des_list_val,unhide_ref,unhide_val):
        self.logger.info("starting clean:")
        # log all function call parameters
        self.logger.info(f"hide_ref {hide_ref} hide val {hide_val} des_list_ref {des_list_ref} des_list_val {des_list_val} unhide_ref {unhide_ref} unhide val {unhide_val}")
        for module in self.modules:
            # reference points to the text object. getreference gives the actual text
            r =     module.Reference()
            ref =   module.GetReference()
            v =     module.Value()
            val =   module.GetValue()

            #strip number content. There is probably a better way to do this...
            des_letter = ''.join(c for c in str(ref) if not c.isnumeric())

            #component = self.board.FindModuleByReference(r)
            hidden_ref = not r.IsVisible()
            hidden_val = not v.IsVisible()

            if hide_ref:
                if des_letter in des_list_ref and not hidden_ref:
                    r.SetVisible(False)
                    self.logger.info(f"ref hidden {ref}") 
                elif "*" in des_list_ref:
                    r.SetVisible(False)
                    self.logger.info("all refs hidden with *")
            if not(des_letter in des_list_ref) and unhide_ref and hidden_ref:
                r.SetVisible(True)
                self.logger.info(f"ref shown {ref}")

            if hide_val:
                if des_letter in des_list_val and not hidden_val:
                    v.SetVisible(False)
                    self.logger.info(f"val {val} hidden on des {ref}")
                elif "*" in des_list_val:
                    v.SetVisible(False)
                    self.logger.info("all vals hidden with *")
            if not(des_letter in des_list_ref) and unhide_val and hidden_val:
                v.SetVisible(True)
                self.logger.info(f"val {val} shown on des {ref}")
                
        pcbnew.Refresh()





