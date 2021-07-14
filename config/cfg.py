import os

# display configs
RES = (640,480)
X_OFFSET = 250
Y_OFFSET = 260

# model configs
MIN_DETECTION_CONFIDENCE = 0.72 # to detect a hand
MIN_TRACKING_CONFIDENCE = 0.62 # to detect the landmarks
REQUIRED_IN_ROW = 20 # how many frames in a row required for a prediction
ERROR_MULTIPLIER = 3 # require multiplied by this more for 2 hands prediction
TIMEDIFF = 3 # show img for this amount of secons
TIMEDIFF_ERROR = 3 # show img for this amount of secons

# training configs
MIN_DETECTION_CONFIDENCE_TRAIN = 0.65 # to detect a hand
MIN_TRACKING_CONFIDENCE_TRAIN = 0.55 # to detect the landmarks
TRAIN_RES = (800,600)

#filepaths
BASEPATH = "/work"
IMAGES_FOLDER = "images"
DATA_DIR = os.path.join(BASEPATH, "data")
MODEL_PATH = os.path.join(BASEPATH, "models", "210511xgb.model")

UP_IMG_PATH = os.path.join(BASEPATH, IMAGES_FOLDER, "up.jpg")
DOWN_IMG_PATH = os.path.join(BASEPATH, IMAGES_FOLDER, "down.jpg")
OK_IMG_PATH = os.path.join(BASEPATH, IMAGES_FOLDER, "ok.jpg")
INF_ERROR_IMG_PATH = os.path.join(BASEPATH, IMAGES_FOLDER, "inf_error.png")
QR_IMG_PATH = os.path.join(BASEPATH, IMAGES_FOLDER, "qr.png")


# the texts, atm openCV does not support JP text
#INTRO_TEXT = """サービスどうですたか、手合図みせて評価もらいたいです！\n 
#                アップ：さいこう！\n 
#                オッケー：だいじょうぶ！\n 
#                ダウン：よくないよ"""
#UP_TEXT = "よかったー！ありがとうございます！"
#DOWN_TEXT = "ごめんなさい！ぜひQRコードからフィードバック送ってください"
#OK_TEXT = "じゃあ次もっとがんばります！"
#MULTI_HANDS_TEXT = "まだ一歳から難しいことわからない！一手だけわかるー！"
INTRO_TEXT = """How was our service? \n
                Thumbs up (image here)：Great！\n 
                Ok (image here)：Yeaa ok..\n 
                Thums down (image here)：Well not too great.."""
UP_TEXT = "Thanks!"
DOWN_TEXT = """"Sorry to hear! \n
            Please leave a comment from the QR code"""
OK_TEXT = "Ok! Let me know from the QR code how to improve!"
MULTI_HANDS_TEXT = """Sorryy, I'm not so clever! \n
                    Please show one hand at time"""
QR_CODE_TEXT= "Please scan and leave comments:"


# common database settings
TABLE_NAME = "FEEDBACK"
LOCAL_DB_PATH = os.path.join(BASEPATH, "db", "feedbacks.db")
LOCAL_DB_CSV_PATH = os.path.join(BASEPATH, "db", "feedbacks.csv")

# AWS database things
AWS_REALTIME_SYNC = True # save also to the aws in real time