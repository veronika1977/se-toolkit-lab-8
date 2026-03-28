from setuptools import setup

setup(
    name="nanobot-webchat",
    version="0.1.0",
    packages=["nanobot_webchat"],
    entry_points={
        "nanobot.channels": [
            "webchat = nanobot_webchat:WebChatChannel",
        ]
    },
)
