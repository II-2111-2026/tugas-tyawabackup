"""Jawaban w01 — STUB (MAHASISWA)

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w01/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations
def q01() -> bool:
    """[T/F] Dalam model probabilistik, output yang sama akan selalu dihasilkan dari input yang
sama terlepas dari variasi acak."""
    return False

def q02() -> bool:
    """[T/F] Ruang sampel dari sebuah eksperimen acak harus mencakup semua hasil yang
mungkin terjadi tanpa tumpang tindih."""
    return True

def q03() -> bool:
    """[T/F] Probabilitas empiris mendekati probabilitas teoretis ketika jumlah percobaan
mendekati tak hingga."""
    return True

def q04() -> str:
    """[MC] Manakah yang merupakan contoh variabel acak dalam sistem STI?

A) Kapasitas total hard disk 1TB.
B) Jumlah core pada prosesor Intel i7.
C) Waktu yang dibutuhkan untuk merespons query database.
D) Jumlah bit dalam satu byte."""
    return "C"

def q05() -> str:
    """[MC] Jika sebuah ruang sampel S terdiri dari 4 kejadian yang memiliki peluang sama,
maka probabilitas satu kejadian adalah:

A) 0,5
B) 0,25
C) 0,75
D) 1,0"""
    return "B"

def q06() -> str:
    """[MC] Kejadian yang mustahil terjadi memiliki nilai probabilitas sebesar:

A) 0
B) 1
C) -1
D) 0,5"""
    return "A"

def q07() -> str:
    """[MC] Sekumpulan hasil eksperimen yang merupakan subset dari ruang sampel disebut:

A) Populasi.
B) Parameter.
C) Kejadian (Event).
D) Konstanta."""
    return "C"

def q08() -> float:
    """[Numeric] Berapa jumlah elemen dalam ruang sampel jika kita melempar dua buah
dadu bersisi enam?"""
    return 36.0

def q09() -> float:
    """[Numeric] Jika probabilitas sebuah link internet mati adalah 0,01, berapa probabilitas
link tersebut hidup?"""
    return 0.99

def q10() -> float:
    """[Numeric] Berapa banyak susunan berbeda yang bisa dibuat dari kata "DATA"?"""
    return 12.0

def q11() -> float:
    """[Numeric] Jika sebuah server memiliki probabilitas uptime 0,95, berapa probabilitas
server tersebut downtime dalam satu periode?"""
    return 0.05

def q12() -> float:
    """[Numeric] Dalam simulasi 1000 kali login, jika 20 kali gagal, berapa frekuensi relatif
kegagalan tersebut?"""
    return 0.02

