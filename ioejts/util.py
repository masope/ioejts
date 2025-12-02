from .src import *

class IoejtsCalculator():
    
    def calc_p_s(self, raw_score):
        """
        Parameter:
            raw_score   : list
            list of Q_QUANTITY(normally 32.) elements;
            raw score of what user answered for the questions. 
        --------
        Return:
            : dict
            dictionary of 4 elements; calculated score of
            numeric representation of personality traits.
        """
        t = {
            IE : 0,
            SN : 0,
            FT : 0,
            JP : 0
        }

        distributor = lambda k : [raw_score[i] for i in range(k-1, Q_QUANTITY, 4)]
        
        a, b, c, d, e, f, g, h = distributor(3)
        t[IE] = 30-a-b-c+d-e+f+g-h

        a, b, c, d, e, f, g, h = distributor(4)
        t[SN] = 12+a+b+c+d+e-f-g+h

        a, b, c, d, e, f, g, h = distributor(2)
        t[FT] = 30-a+b+c-d-e+g-g-h

        a, b, c, d, e, f, g, h = distributor(1)
        t[JP] = 18+a+b-c+d-e+f-g+h

        return t

    def calc_mbti(self, score):
        """
        Parameter:
            score   : dict
            dictionary of scores of each personality traits.
        --------
        Return:
            : str
            result of the test in Myers-Briggs Type Indicator
        """
        c = []

        c.append('E' if score[IE] > 24 else 'I')
        c.append('N' if score[SN] > 24 else 'S')
        c.append('T' if score[FT] > 24 else 'F')
        c.append('P' if score[JP] > 24 else 'J')

        return "".join(c)

