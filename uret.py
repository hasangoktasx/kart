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
open("hasan.vcf", "w", encoding="utf-8", newline="").write(vcf)
URL = "https://hasangoktasx.github.io/kart/hasan.vcf"
# QR sadece adresi taşır; kişi dosyasını telefonun rehber uygulaması okur
q = segno.make(URL, error="q", micro=False)
with open("hasan-goktas-qr.png", "wb") as f:
    q.save(f, kind="png", scale=24, border=4)
with open("hasan-goktas-qr.svg", "wb") as f:
    q.save(f, kind="svg", scale=10, border=4)
print("surum", q.version)
