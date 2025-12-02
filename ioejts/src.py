from .questions import QUESTIONS, QUESTIONS_KR
from .info import OEJTS_INFO, OEJTS_INFO_KR

#dictionary macros.
QUESTIONS           = dict(sorted(QUESTIONS.items()))
QUESTIONS_KR        = dict(sorted(QUESTIONS_KR.items()))
Q_QUANTITY          = len(QUESTIONS)
Q_INDEXES           = list(QUESTIONS.keys())

#gui setting constants.
ROOT_WIN_MINSIZE    = (497, 270)
ABOUT_WIN_MINSIZE   = (400, 500)
RESULT_WIN_MINSIZE  = (300, 169)

#symbolic constants.
EN                  = 'en'
KR                  = 'kr'
IE                  = 'IE'
SN                  = 'SN'
FT                  = 'FT'
JP                  = 'JP'
MBTI                = 'MBTI'
LEFT                = 0
RIGHT               = 1
P_MEDIAN            = 3
UNDERLINE_EN        = 0
UNDERLINE_DEFAULT   = -1
ABOUT               = 0x00
PREV                = 0x01
NEXT                = 0x02
ABOUT_TITLE         = 0x03
RESULT_TITLE        = 0x04
OKAY                = 0x05
INFO                = 0x06
HEADER              = 0x07
RESULT              = 0x08



#user interface texts.
UI_TXT_EN = {
    ABOUT           : 'About',
    PREV            : 'Previous',
    NEXT            : 'Next',
    ABOUT_TITLE     : 'About',
    RESULT_TITLE    : 'Result',
    OKAY            : 'Ok',
    INFO            : OEJTS_INFO,
    HEADER          : (lambda i : f"Question {i}"),
    RESULT          : (lambda ie, sn, ft, jp, mbti : f"\n[Result]\n\nIE: {ie}  SN: {sn}  FT: {ft}  JP: {jp}\n\nYou're {mbti}!") 
}

UI_TXT_KR = {
    ABOUT           : '도움말(A)',
    PREV            : '이전(P)',
    NEXT            : '다음(N)',
    ABOUT_TITLE     : '도움말',
    RESULT_TITLE    : '결과',
    OKAY            : '확인(O)',
    INFO            : OEJTS_INFO_KR,
    HEADER          : (lambda i : f"{i}번째 질문"),
    RESULT          : (lambda ie, sn, ft, jp, mbti : f"\n[결과]\n\nIE: {ie}  SN: {sn}  FT: {ft}  JP: {jp}\n\n당신은 {mbti}이네요!")
}