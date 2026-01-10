import requests
from models import CurrentStreak, SimplifiedDuolingoCourse, SimplifiedDuolingoUser, StreakData, UserResponseModel

def random_user_agent() -> str:
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", 
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    ]
    import random
    return random.choice(user_agents)

def fetch_userdata(username: str) -> UserResponseModel:
    url = "https://www.duolingo.com/2017-06-30/users?username=" + username
    headers = {"User-Agent": random_user_agent()}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return UserResponseModel(data=response.json(), error=None)
    return UserResponseModel(data=None, error="User not found")

def simplify_user_data(user_data: dict) -> SimplifiedDuolingoUser:
    simplified_courses = []
    for course in user_data.get("courses", []):
        simplified_course = SimplifiedDuolingoCourse()
        simplified_course.title = course.get("title", "")
        simplified_course.learningLanguage = course.get("learningLanguage", "")
        simplified_course.fromLanguage = course.get("fromLanguage", "")
        simplified_course.xp = course.get("xp", 0)
        simplified_courses.append(simplified_course)
    
    simplified_user = SimplifiedDuolingoUser()
    simplified_user.streak = user_data.get("streak", 0)
    simplified_user.totalXp = user_data.get("totalXp", 0)
    simplified_user.courses = simplified_courses
    
    streak_data = StreakData()
    current_streak = CurrentStreak()
    streak_info = user_data.get("streakData", {}).get("currentStreak", {})
    current_streak.startDate = streak_info.get("startDate", "")
    current_streak.length = streak_info.get("length", 0)
    current_streak.endDate = streak_info.get("endDate", "")
    streak_data.currentStreak = current_streak
    simplified_user.streakData = streak_data
    
    return simplified_user

def get_user_streak(user_data: dict) -> int:
    return user_data.get("streak", 0)