#!/usr/bin/env python

template = """
Kepada Yth. {name},
    di tempat

Dengan ini kami bermaksud mengundang Bapak/Ibu {name} untuk menghadiri acara {event} yang akan
diselenggarakan pada hari {day}

Terima kasih,

{committee}
"""

print template

print template.format(name='Ahmad', event='Sunatan', day="Jum'at", committee='Jamal')


