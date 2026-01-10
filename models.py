from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from dataclasses import dataclass

class SimplifiedDuolingoCourse:
    title: str
    learningLanguage: str
    fromLanguage: str
    xp: int

class CurrentStreak:
    startDate: str
    length: int
    endDate: str

class StreakData:
    currentStreak: CurrentStreak


# Lots of other fields are out there, but I don't want to model them right now, also most of them are deprecated
# TODO: Find less deprecated API endpoint

class SimplifiedDuolingoUser:
    streak: int
    totalXp: int
    courses: list[SimplifiedDuolingoCourse]
    streakData: StreakData
    

class DuolingoAPIResponse:
    users: list[SimplifiedDuolingoUser]

@dataclass
class UserResponseModel:
    data: Union[SimplifiedDuolingoUser, None]
    error: Union[str, None]