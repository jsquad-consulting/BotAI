import sys

from botai.botir import botir

def main():
    print("hello botai")
    bot_image_recognizer = botir.BotImageRecognizer()
    print(bot_image_recognizer.tellWhatTheWordIs("test 1"))

if __name__ == "__main__":
    sys.exit(main())