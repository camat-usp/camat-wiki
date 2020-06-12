import re
from urllib.request import urlopen

#URL_RE = r"https:\/\/fonts.gstatic.com\/v[0-9]+\/([a-z]+)\/v[0-9]\/([A-Za-z0-9]+)\.woff2"
URL_RE = r"https://fonts\.gstatic\.com/[a-z]+/([a-z]+)/v[0-9]+/([_\-A-Za-z0-9]+)\.woff2"

with open("../fonts.css", "r") as f:
    urls = {}
    css = f.read()

    for match in re.finditer(URL_RE, css):
        (url, font, h) = (match.group(0), match.group(1), match.group(2))

        if url not in urls:
            urls[url] = (font, h)

    output_css = css

    for url in urls:
        (font, h) = urls[url]
        file_name = f"{font}-{h}.woff2"
        res = urlopen(url)

        with open(file_name, "wb+") as woff:
            woff.write(res.read())

        output_css = output_css.replace(url, f"fonts/{file_name}")

    with open("fonts.css", "w+") as output:
        output.write(output_css)

    print("Done!")

