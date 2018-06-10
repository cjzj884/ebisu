#!/usr/bin/env python
# coding: UTF-8

import argparse
import signal

from src.factory import BotFactory

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is trading script on bitmex")
    parser.add_argument("--test",     default=False,   action="store_true")
    parser.add_argument("--stub",     default=False,   action="store_true")
    parser.add_argument("--demo",     default=False,   action="store_true")
    parser.add_argument("--hyperopt", default=False,   action="store_true")
    parser.add_argument("--strategy", default="doten", required=True)
    args = parser.parse_args()

    # ボットを作成する
    bot = BotFactory.create(args)
    # ボットを稼働する
    bot.run()

    if not args.test:
        # 停止処理を登録する
        signal.signal(signal.SIGINT, lambda x, y: bot.stop())
        while True:
            pass
