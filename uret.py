import quopri, segno, time

def qp(s):
    return quopri.encodestring(s.encode("utf-8"), quotetabs=False).decode("ascii").replace("=\n", "")

P = ";CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:"
TEL, MAIL = "+905437357151", "hasan.goktas@cerkezkoy.bel.tr"

# 1) Sade: yalnızca ASCII harf -> her telefonda aynı görünür
sade = ["BEGIN:VCARD", "VERSION:3.0", "N:Goktas;Hasan;;;", "FN:Hasan Goktas",
        "ORG:Cerkezkoy Belediyesi", "TITLE:Yazilim Gelistiricisi",
        "TEL;TYPE=CELL:" + TEL, "EMAIL;TYPE=WORK:" + MAIL, "END:VCARD"]

# 2) Türkçe harfli: harfler ASCII kaçışlarıyla (quoted-printable) yazılır
turkce = ["BEGIN:VCARD", "VERSION:2.1",
          "N" + P + qp("Göktaş") + ";Hasan;;;",
          "FN" + P + qp("Hasan Göktaş"),
          "ORG" + P + qp("Çerkezköy Belediyesi"),
          "TITLE" + P + qp("Yazılım Geliştiricisi"),
          "TEL;CELL:" + TEL, "EMAIL;INTERNET;WORK:" + MAIL, "END:VCARD"]

def yaz(q, ad, kind, scale):
    for _ in range(5):
        try:
            with open(ad, "wb") as f:
                q.save(f, kind=kind, scale=scale, border=4)
            return
        except OSError:
            time.sleep(1)
    raise SystemExit(ad + " yazilamadi")

for ad, satirlar in (("hasan-goktas-qr", sade), ("hasan-goktas-qr-turkce", turkce)):
    veri = "\r\n".join(satirlar) + "\r\n"
    assert veri.isascii()
    q = segno.make(veri, error="m", micro=False)
    yaz(q, ad + ".png", "png", 24)
    yaz(q, ad + ".svg", "svg", 10)
    print(ad, "surum", q.version)
