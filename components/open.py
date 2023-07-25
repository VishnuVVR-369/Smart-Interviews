import os
import requests
from dotenv import load_dotenv

load_dotenv()

SMART_INTERVIEWS_URL = 'https://smartinterviews.in/api/user-control/authenticate'
SMART_INTERVIEWS_LEADERBOARD_URL = 'https://smartinterviews.in/api/user-control/leaderboard/report/GRIET-2023'
USERNAME = os.environ.get('SMART_INTERVIEWS_USERNAME')
PASSWORD = os.environ.get('SMART_INTERVIEWS_PASSWORD')


def loginToSmartInterviews() -> dict:
    authData = requests.post(SMART_INTERVIEWS_URL, json={
        "username": USERNAME,
        "password": PASSWORD,
        "isPreRegUser": False,
        "recaptcha": ""
    })
    authToken = authData.json()['data']['user']['token']
    # TODO: Add error handling for invalid credentials and logging
    leaderboardData = requests.post(SMART_INTERVIEWS_LEADERBOARD_URL, headers={
        "Authorization": f"Token {authToken}",
        "Username": USERNAME,
        "Role": "USER"
    })
    # TODO: Add error handling for invalid data and logging
    return leaderboardData.json()
