from flask import Flask

app = Flask(__name__, static_folder="./static")
if __name__ == "__main__":
    app.run()

import deckshuffle.main
import deckshuffle.shuffle
import deckshuffle.cardlist
