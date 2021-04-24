from enum import Enum

class GenderEnum(Enum):
    M = 'MALE'
    F = 'FE_MALE'

class PlayerFieldType(Enum):
    BOWLING = 'BOWLING'
    BATTING = 'BATTING'
    ALL = 'ALL ROUNDER'

class MatchType(Enum):
    ODI = 'ODI'
    TEST = 'TEST'
    T20 = 'T20'