# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Emiya

import random

from hero_class import Hero

hx = Hero()

hx.skin = '国士无双'
hx.name = '韩信'
hx.position = '刺客assassin'
hx.ab_viability = random.randint(1,100)
hx.ab_damage = random.randint(1,100)
hx.ab_effect = random.randint(1,100)
hx.ab_difficulty = random.randint(1,100)

hx.show_story()
hx.show_presentation()
hx.show_history()
