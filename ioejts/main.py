""" ioejts - Instantly implementable OEJTS

OEJTS v1.2 Personality test suite & API of quick and easy implementation.
All test and scoring methods are directly extracted from 
Jorgenson, E. (2015). Open Extended Jungian Type Scales v1.2.
Please refer to https://openpsychometrics.org/tests/OJTS/development/ for details.

License for OEJTS:
The items of the Open Extended Jungian Type Scales 1.2 are licenced under a Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License. The OEJTS come with no
guarantees of reliability or accuracy of any kind

Usage:
>>>from ioejts import ioejts
>>>quick_test = ioejts()
    ...
>>>score_calc = ioejts(score: iter.)
    ...
>>>question_dict = ioejts(None, False, ...)
    ...
>>>ioejts()['MBTI']
ISFJ
    ...
"""
from collections import UserDict

from .util import IoejtsCalculator
from .gui import IoejtsSurveyWindow
from .src import *


class ioejts(UserDict, IoejtsCalculator):
    """instance of ioejts act as dictionary as result of wrapped by collections.UserDict,
    all default python dictionary behavior applied in the same manner.
    you can get few different contents as a dictionary through this class.

    Parameter:
        score       : list
            list of completed answer for the 32 OEJTS questions.
            if this parameter is given, then survey(or test) suit will
            automatically not be conducted and calculated result of
            given answer will be returned.
            Default is None.
        survey      : bool
            boolean value for deciding whether survey(or test) suit
            would be conducted or not. If true, additional graphical window
            will pop-up for the survey.
            Default is True.
        lang        : Symbolic Constants. (str)
            designator for what language the instance should provide.
            both survey suite(if conducted) and result will be provided as
            designated language.
            Default is EN.
        show_result : bool
            boolean value for deciding whether result page at the end
            of the survey suit will be displayed or not.
            Default is True.
    ----------------
    Returns:
            : dict
            dictionary of calculated results and regarding MBTI string, if 
            score has given or survey suit finished, or dictionary of questions
            if both is not given/False.
    """

    def __init__(self, score=None, survey=True, lang=EN, show_result=True):

        raw_score = []

        if score:
            raw_score = score
        elif survey:
            _wSurvey = IoejtsSurveyWindow(lang=lang, result_page=show_result)
            _wSurvey.mainloop()
            raw_score = _wSurvey.getResult()
        else:
            q = QUESTIONS_KR if lang == KR else QUESTIONS
            self._d = {**q}

        if raw_score:
            s = super().calc_p_s(raw_score)
            self._d = {**s, MBTI : super().calc_mbti(s)}

        super().__init__(self._d)