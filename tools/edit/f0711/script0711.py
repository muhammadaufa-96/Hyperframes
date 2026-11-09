"""Hand-corrected caption text per piece (tag) for the folder 7/11/26 Reel (Pagi Sore, IMG_6221).
Timing comes from per-piece ASR (chk.py); align() maps these words onto it."""
SCRIPT = {
 "r1": {
  "hookA": "Diorang takde buat anything yang inovatif.",
  "hookB": "And now diorang dah grow satu Indonesia.",
  "intro": "Siapa je yang tak kenal Pagi Sore, sebuah brand yang jual nasi padang yang sangat famous dekat Indonesia.",
  "basic": "Diorang hanya fokus kepada basic principle sahaja, iaitu tiga perkara ni.",
  "s1": "Yang pertama, first dari segi servis. Servis diorang memang sangat laju, sangat bagus dia punya hospitality dia.",
  "s2a": "Yang kedua adalah di segi food. Makanan dia sumpah sedap.",
  "s2b": "Dan semua orang sanggup berebut lah, boleh lah, willing to spend lah.",
  "s3a": "Dan yang ketiga sekali adalah diorang punya environment, ambience.",
  "s3b": "Memang rasa macam hotel five star.",
  "l1": "Jadi dekat sini kita boleh belajar bahawasanya untuk nak fill in the gap,",
  "l2": "Kita tak semestinya kita kena create inovatif yang pelik-pelik.",
  "l3": "Tak perlu pun. Kadang-kadang cukup kita fokus pada improve kita punya servis dan sesuai dengan permintaan pelanggan kita.",
  "niche": "Aku kena tahu lah apa kelemahan-kelemahan yang mostly yang ada among competitors, dan apa gap yang kita boleh fill in, yang kita boleh win dekat gap tu.",
  "c1": "Indonesia bersepah orang jual nasi padang.",
  "c2": "Tapi diorang masuk, diorang fokus pada tiga benda yang aku sebut tu, dan diorang jadi sangat stand up.",
 },
}
# v2: full hook sentence (no fancy innovation, like Tesla / Elon Musk), then the story before the points
SCRIPT["r2"] = dict(SCRIPT["r1"])
SCRIPT["r2"].update({
  "hookA": "Diorang takde buat any inovatif yang agak-agak fancy.",
  "hookT": "Contoh macam Tesla, macam Elon Musk.",
  "story": "Aku baru lepas meeting dekat sini, makan, having a lunch.",
  "intro": "Siapa je yang tak kenal Pagi Sore, sebuah brand yang jual nasi padang yang sangat famous dekat Indonesia, malah sampai ke Malaysia pun.",
  "learn": "Satu benda yang kita boleh belajar dekat sini adalah macam mana diorang fill in the gap.",
})
