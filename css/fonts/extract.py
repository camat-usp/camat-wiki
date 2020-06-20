# Script que "rouba" as fontes do Google Fonts e instala localmente
# Copyleft CAMat(TM)

import re
from urllib.request import urlopen

GOOGLE_FONTS_URL = "https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&family=Roboto:ital,wght@0,400;0,700;1,400;1,700&family=Source+Code+Pro:ital,wght@0,400;0,700;1,400;1,700&display=swap"
URL_RE = r"https://fonts\.gstatic\.com/[a-z]+/([a-z]+)/v[0-9]+/([_\-A-Za-z0-9]+)\.([a-z-09]+)"

css = urlopen(GOOGLE_FONTS_URL).read().decode("utf-8")
urls = {}

for match in re.finditer(URL_RE, css):
    (url, font, h, f) = (match.group(0), 
                         match.group(1), 
                         match.group(2),
                         match.group(3))

    if url not in urls: urls[url] = (font, h, f)

output_css = css

for url in urls:
    (font, h, f) = urls[url]
    file_name = f"{font}-{h}.{f}"
    res = urlopen(url)

    with open(file_name, "wb+") as woff:
        woff.write(res.read())

    output_css = output_css.replace(url, f"fonts/{file_name}")

with open("../fonts.css", "w+") as output:
    output.write(output_css)

print("Done!")

