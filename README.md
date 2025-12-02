
# ioejts - Instantly Implementable OEJTS

OEJTS v1.2 Personality test suite & API of quick and easy implementation.
All test and scoring methods are directly extracted from Jorgenson, E. (2015). Open Extended Jungian Type Scales v1.2.
Please refer to [OJTS Development Page](https://openpsychometrics.org/tests/OJTS/development/) for details.

## Installation

```console
pip install ioejts
```

## Usage

```pycon
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
```

## License

