import segno
vcf = "\r\n".join([
    "BEGIN:VCARD",
    "VERSION:3.0",
    "N:Göktaş;Hasan;;;",
    "FN:Hasan Göktaş",
    "ORG:Çerkezköy Belediyesi",
    "TITLE:Yazılım Geliştiricisi",
    "TEL;TYPE=CELL,VOICE:+905437357151",
    "EMAIL;TYPE=INTERNET,WORK:hasan.goktas@cerkezkoy.bel.tr",
    "END:VCARD",
]) + "\r\n"
open("hasan-goktas.vcf", "w", encoding="utf-8", newline="").write(vcf)
# eci=True: QR'ın içine "bu metin UTF-8" işareti koyar; okuyucu tahmin yürütmez
q = segno.make(vcf, encoding="utf-8", eci=True, error="m", micro=False)
with open("hasan-goktas-qr.png", "wb") as f:
    q.save(f, kind="png", scale=24, border=4)
with open("hasan-goktas-qr.svg", "wb") as f:
    q.save(f, kind="svg", scale=10, border=4)
print("surum", q.version)
