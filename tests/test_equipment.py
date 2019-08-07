# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Emiya

import random
import sys

sys.path.append('..')
from package_kog.class_eq_attack import EQAttack
from package_kog.class_eq_defence import EQDefence
from package_kog.class_eq_mana import EQMana
from package_kog.class_eq_move import EQMove

test_eq = EQAttack()
test_eq.show_me()
test_eq.show_me_unique()

test_eq = EQDefence()
test_eq.show_me()
test_eq.show_me_unique()

test_eq = EQMana()
test_eq.show_me()
test_eq.show_me_unique()

test_eq = EQMove()
test_eq.show_me()
test_eq.show_me_unique()
