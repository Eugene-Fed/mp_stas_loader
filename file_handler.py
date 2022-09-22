# -*- coding: UTF-8 -*-

import json
import sys
from pathlib import Path

settings_file = Path('settings.json')
# settings_file = Path('api-keys') / Path('api-keys_test.json')
templates_dir = Path('templates')


def load_json(file: Path, templates_dir=templates_dir) -> json:
    """Проверяем наличие файла. Если файл не существует - загружаем его из папки шаблонов.
    Если шаблон отсутствует - выходим с ошибкой"""
    json_data = {}
    if file.exists():
        with file.open() as f:
            json_data = json.load(f)
            print(f'File "{str(file)}" exists.')
    else:
        file_template = templates_dir / file.name
        if file_template.exists():
            with file_template.open() as f:
                json_data = json.load(f)
                # TODO: добавить интерактивный ввод параметров с дальнейшим сохранением в файл settings.json

            # Обходим список родителей в обратном порядке. т.к. чем больше индекс, тем ближе родитель к корневому
            # [0: 'dir_1/dir_2/dir_3'], [1: 'dir_1/dir_2'], [2: 'dir_1']
            # TODO: возможно стоит вывести проверку и создание файлов и папок в отдельную функцию
            for parent in file.parents[::-1]:
                # если папка не существует, то создаем папку
                if not parent.is_dir():
                    parent.mkdir()

            # После того как все папки созданы, добавляем в нее искомый файл из шаблона.
            with file.open("w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=4, ensure_ascii=False)
            print(f'File "{str(file)}" does not exists. It will be  created from template.')
        else:
            print(f'Files "{str(file)}" and "{str(templates_dir / file.name)}" do not exists')
            sys.exit(1)
    return json_data


if __name__ == '__main__':
    settings = load_json(file=settings_file)
    print(json.dumps(settings, indent=4))
