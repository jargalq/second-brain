# -*- coding: utf-8 -*-
"""Төвийн бүсийн 7 зураг. Ерөнхий skill-ийг (_system/skills/talbai-zurag/talbai_zurag.py) өөрчлөхгүйгээр
ажиллуулж, зөвхөн энэ төсөлд «тусгай зөвшөөрөл» гэсэн үгийг «төслийн талбай» болгож орлуулна.
Учир нь энэ бол уурхайн тусгай зөвшөөрөл биш, газар эзэмшлийн нэгж талбар.

Ажиллуулах (vault-ын хавтсаас):  py -3 -I "<энэ файл>"  [--only 0,1,...]
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SKILL = os.path.join(VAULT, '_system', 'skills', 'talbai-zurag', 'talbai_zurag.py')
CONFIG = os.path.join(HERE, 'talbai_zurag_config.json')

SOLIH = [  # (skill дэх бичвэр, энэ төсөлд)
    ("label='Тусгай зөвшөөрлийн талбай'", "label='Төслийн талбай'"),
    ("f'Тусгай зөвшөөрөл: {LIC}\\n'", "f'Газар: {LIC}\\n'"),
    ("'▭ Тусгай зөвшөөрлийн хил'", "'▭ Төслийн талбайн хил'"),
]

src = open(SKILL, encoding='utf-8').read()
for huuchin, shine in SOLIH:
    if src.count(huuchin) != 1:
        sys.exit(f'Skill-ийн бичвэр өөрчлөгдсөн байна, орлуулах мөр олдсонгүй: {huuchin}')
    src = src.replace(huuchin, shine)

sys.argv = [SKILL, CONFIG] + sys.argv[1:]
exec(compile(src, SKILL, 'exec'), {'__name__': '__main__', '__file__': SKILL})
