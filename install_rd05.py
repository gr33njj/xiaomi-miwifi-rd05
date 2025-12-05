#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time

import xmir_base
import gateway
from gateway import die
import read_info

bl_name = 'rd05_rootfs.bin'

gw = gateway.Gateway()
dn = gw.device_name

fn_dir    = 'firmware/'

fn_remote = '/tmp/rootfs.bin'

fn_local  = None

fn_local = fn_dir + bl_name

if not os.path.exists(fn_local):
  die('File "{}" not found'.format(fn_local))

gw.upload(fn_local, fn_remote)

os.system('cls')

print("Записываю прошивку.")

gw.run_cmd('xqled sys_ota')
gw.run_cmd('nvram set restore_defaults=1')
gw.run_cmd('nvram set web_restore=1')
gw.run_cmd('nvram commit')
gw.run_cmd('mtd -r write /tmp/rootfs.bin rootfs >/dev/null 2>&1 &\n')

print("\033[91m" + "\n!!!Не выключайте роутер!!!" + "\033[0m\n")
print('Ждите ~3-5 минут. Роутер сам перезагрузится.')
time.sleep(240)
os.system('cls')