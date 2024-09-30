import tbapy

class TBAGetter:
    def getTBA(self):
        f  = open("TOKEN", 'r')
        tok = f.read()
        f.close()
        tba = tbapy.TBA(tok)
        return tba