import pcbnew

class board_cleaner:

    def __init__(self,board,logger):
        self.board = board
        self.modules = self.board.GetFootprints()
        self.logger = logger
        self.logger.info("cleaner initialized")

    def hide(self,hide_ref,hide_val,des_list_ref,des_list_val,unhide_ref,unhide_val, change_des_text, change_val_text, text_properties):
        self.logger.info("starting clean:")
        # log all function call parameters
        self.logger.info(   f" hide_ref {hide_ref}"
                            f" hide val {hide_val}"
                            f" des_list_ref {des_list_ref}"
                            f" des_list_val {des_list_val}"
                            f" unhide_ref {unhide_ref}"
                            f" unhide val {unhide_val}"
                            f" change des text properties {change_des_text}"
                            f" change val text properties {change_val_text}"
                            f" text properties {text_properties}")

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

            if change_des_text:
                if des_letter in des_list_ref:
                    self.logger.info(f"ref {ref} changed to x{text_properties['x_des_size']} y{text_properties['y_des_size']} w{text_properties['width_des_size']}")
                    try:
                        r.SetSize(pcbnew.wxSize (pcbnew.FromMM(text_properties["x_des_size"]),pcbnew.FromMM(text_properties["y_des_size"])))
                        r.SetThickness(pcbnew.FromMM(text_properties["width_des_size"]))
                    except Exception as e:
                        self.logger.info(f"something went wrong {e}")

                
        pcbnew.Refresh()





