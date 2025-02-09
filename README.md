1. Browse Reddit and download some images to `~/Pictures/Reddit` on your Android smartphone.
2. Install [Termux](https://termux.dev/en/).
3. In Termux, run these commands.
   1. `pkg install git python libjpeg-turbo`
   2. `git clone https://github.com/MattTheCuber/termux-reddit-crop.git`
   3. `cd termux-reddit-crop`
   4. `pip install -r requirements.txt`
   5. `python crop.py`
