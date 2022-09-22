# -*- coding: UTF-8 -*-

import requests
import json
import sys
from pathlib import Path
import file_handler
from datetime import datetime, timedelta, date, time

# Это единственные 'данные/настройки' в коде. Все остальное вынесено в файл settings.json
SETTINGS_FILE = 'settings.json'
API_KEYS_DIR = 'api-keys_dir'
API_KEYS_FILE = 'api-keys_file'


if __name__ == '__main__':
    settings = file_handler.load_json(file=Path(SETTINGS_FILE))
    api_keys = file_handler.load_json(file=Path(settings[API_KEYS_DIR]) / Path(settings[API_KEYS_FILE]))
    print(settings)

