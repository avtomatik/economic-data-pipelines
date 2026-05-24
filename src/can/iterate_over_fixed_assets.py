#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 12:45:19 2023

@author: green-machine
"""


from functools import cache

from econdata.providers.statcan.provider import StatCanProvider

_provider = StatCanProvider()


@cache
def read_can(archive_id: int):
    return _provider.load_table(archive_id)


# =============================================================================
# Capital
# =============================================================================
archive_id = 36100096
df = read_can(archive_id)
for col_num, _ in enumerate(df.columns):
    values = sorted(set(df.iloc[:, col_num]))
    print(_)
