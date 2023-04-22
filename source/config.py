from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 6059195246
bot_user = "ftrjd14_bot"
api_id = 15170853
api_hash = "33f17f7ccfa43fd779489dca8ab67e34"
session = "BAAfTwoxSupb0KDIRG4xfOLr8OVavy7DsEABWwr7ke7jJmbcajILckjkMLwk1-SIgD7pWxxx1YbEjOpMNcO-GZC1-02Xae16btTAjbgScGmQFmv2RT1NuCffbglKZT4sWZnZIe9rmTFSk1SX04Y9GjzzkU4XYWhwBl7_pmAdE9g7BDOkNxJRrvcl-DfeK1Q49-KvH7RQJzo0PdxvQXO5bGdWeRX-Fyl80leF90-c7jVIijvumfu-Tqn4LVxbTYmQRRetz9195Od17rC2BJHJYxsGAKtleEiejyHr4AVgETTErde7rvGOWOD9ldA7KPbHgItJUC_Mv_atsck5j-X0vgvjAAAAAVf65eQA"
token = "5929347435:AAF5dJQUfz6TRTlyeLShcFTeFo9Wu6SScPA"
sudo_command = [6059195246,6199134030,5523863949]
pm = "5190136458"
mention = "1001132193"
plugins = dict(root="plugins")
app = Client("user:ftrjd14_bot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("ftrjd14_bot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
