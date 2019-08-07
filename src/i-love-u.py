# -*- coding: utf-8 -*-

import sys


__HEART__ = '''

          @@@@@@@@@@@                @@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                @@@@@@@@@@@@@@@@@@@@@@@@@@
                   @@@@@@@@@@@@@@@@@@@@
                       @@@@@@@@@@@@
                            @@

'''


class Color:
    @property
    def RED(self):
        return '\x1b[0;31;40m'

    @property
    def BOLD_YELLOW(self):
        return '\x1b[1;33;40m'

    @property
    def NORMAL(self):
        return '\x1b[0m'


class Valentine:
    def __init__(self, name, chinese_name):
        self.loved_one = name
        self.chinese_name = chinese_name

    def romanticize(self):
        you_in_my_heart = __HEART__

        while '@' in you_in_my_heart:
            for letter in list(self.loved_one):
                you_in_my_heart = \
                    you_in_my_heart.replace('@', letter, 1)

        return you_in_my_heart

    def i_love_you(self):
        C = Color()

        return '{}{}{}\n'\
            '大眼怪大眼怪, {}{}{}. 七夕节快乐!'.format(
                C.RED, self.romanticize(), C.NORMAL,
                C.BOLD_YELLOW, self.chinese_name, C.NORMAL
            )


def main():
    try:
        name = 'ZhangTing LiYitan '
        chinese_name = '张婷'

    except IndexError:
        name = 'Love'

    my_beloved = Valentine(name, chinese_name)
    print(my_beloved.i_love_you())


if __name__ == '__main__':
    main()
