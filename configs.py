from dotenv import load_dotenv
from os import path, getenv, mkdir


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()

if not path.exists("search"):
    mkdir("search")


class Configs:
    API_ID = int(getenv("API_ID", "1480988"))
    API_HASH = getenv("API_HASH", "be76b2fd25b50222b0e1eee141d6a259")
    BOT_TOKEN = getenv("BOT_TOKEN", "5605728947:AAHGZRsBITZF6LY8L4_08pGwvdcMkKpXrCE")
    OWNER_ID = int(getenv("OWNER_ID", "5616310867"))
    SESSION = getenv("SESSION", "AQByDD7NLDtkWIKAISif2It1SkXmnNxVDLhgq51wICzb_WZPpOa8YEJRQDD1w-VLNTgLkNW7gaLkm7BAV1KkFj_4Cr_9NSzXZHQjjGaUwHbxgRoqbVHe4sDFQMYbUa3AXHn4oktctVqCx-Kbt36eP1GIzOmFcphodHDoWy3CvD4kTlRvCheffcKv1_Ff7yVKjIWqcnhaoPyEEftAjUxH2-1q5_ZWV0rgY_gAt-7AGoSHIcHZ1RWOyccoHu4p3G743i5mNuQU89E2jd0jydFLRynkHWC5OdwJplybPYRdr7U9gWBXfRT9yDfxZ2Z-2I6npPQZJrtHABFP7mFt21_F9YQhAAAAAUp_RwIA")
    CHANNEL_LINK = getenv("CHANNEL_LINK", "https://t.me/KK_LINKS")
    GROUP_LINK = getenv("GROUP_LINK", "https://t.me/KanimangalamKovilakam")
    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/momskidvaava/solidmusic")
    AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1800"))
    DURATION_LIMIT: float = float(getenv("DURATION_LIMIT", "500"))


config = Configs()
