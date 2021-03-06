from ....cursor import db

class Processo12:

    def __init__(self,processo_id = None):

        self.__processo_id = None
        self.tipo = None
        self.desc = None

        if processo_id is not None:

            data = db.get_processo_12(processo_id)
            if data is not None:

                self.__processo_id = processo_id
                self.tipo = data['processo_tipo']
                self.desc = data['processo_desc']


    def get_id_12(self):
        return self.__processo_id

    def salva(self):
        if self.__processo_id is not None:
            db.edita_processo_12(self)
        else:
            self.__processo_id = db.cadastra_processo(self)

    def deleta(self):
        db.deleta_processo(self.get_id())
