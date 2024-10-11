#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from cmttj.main import cmttj

if __name__ == '__main__':
    # The ini file path, if not defined, then default tracking.ini
    config_dir = './swarm_setting.ini'

    paths_finished = cmttj(settings=config_dir)
    print(paths_finished)
