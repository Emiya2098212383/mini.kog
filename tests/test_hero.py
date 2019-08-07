# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Emiya

import random
import sys

sys.path.append('..')
from package_kog.class_hero import Hero


# 测试英雄生成
print('\n---测试产生一批英雄--------')
for i in range(10):
    hero = Hero()
    hero.show_me()
    print('\n')
