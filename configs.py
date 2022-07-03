# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID","1976680")
    API_HASH = os.environ.get("API_HASH","9073255ce64a6072a59099803493f97d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5239820313:AAH0D0t7UGispyQgSQX8ecL_lkRqR_Vp_bw")
    SESSION_NAME = os.environ.get("SESSION_NAME", "VideoMergeDcBot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","-1001576695301")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL","-1001474413281")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME","5e4f1b21f9638094a8cf")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS","JkqQxXVQZzuj3DM")
    MONGODB_URI = os.environ.get("MONGODB_URI","mongodb+srv://erichdaniken:erichdaniken@cluster0.c13qk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1940030638))

    START_TEXT = """
Hi , I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.

You also can generate screenshot and sample Video.

Made by @GroupDcBots
"""
    CAPTION = "Video Merged by @{}\n\nMade by @GroupDcBots"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
