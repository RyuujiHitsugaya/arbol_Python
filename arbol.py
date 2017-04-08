class Nodo:
    def __init__(self,valor,hijos=[]):
        self.valor=valor
        self.hijos=hijos
        
def buscar(arbol,texto):
    if len(texto)==1:
        if arbol.valor[-1]==texto:
            return posibilidad(arbol.hijos)
        else:
            return []
    else:
        return buscar_lista(arbol.hijos,texto[1:])
    
def buscar_lista(arbol,texto):
    if arbol==[]:
        return []
    elif len(arbol) == 1:
        return buscar(arbol[0],texto)
    else:
        return buscar(arbol[0],texto)+buscar_lista(arbol[1:],texto)

def posibilidad(arbol):
    if arbol==[]:
        return []
    else:
        return [arbol[0].valor]+posibilidad(arbol[0].hijos)+posibilidad(arbol[1:])

print(buscar(Nodo('a',[Nodo('ar',[Nodo('arl'),Nodo('aro')]),Nodo('al')]),'a'))
