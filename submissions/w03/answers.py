"""Jawaban w03 — STUB (MAHASISWA)

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w03/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] Dalam konfigurasi paralel, sistem akan gagal hanya jika semua komponen gagal."""
    return True

def q02() -> bool:
    """[T/F] Menambahkan komponen secara seri akan meningkatkan reliabilitas keseluruhan
sistem."""
    return False

def q03() -> bool:
    """[T/F] Reliabilitas total sistem seri selalu lebih kecil atau sama dengan reliabilitas
komponen terlemahnya."""
    return True

def q04() -> str:
    """[MC] Sebuah sistem terdiri dari dua komponen dengan reliabilitas 0,9 yang disusun
secara paralel. Reliabilitas sistem adalah:

A) 0,81
B) 0,99
C) 0,90
D) 1,80"""
    return "B"

def q05() -> str:
    """[MC] Jika tiga switch identik dengan reliabilitas 0,8 disusun seri, reliabilitas totalnya
adalah:

A) 0,512
B) 0,8
C) 2,4
D) 0,2"""
    return "A"

def q06() -> str:
    """[MC] Manakah konfigurasi yang paling tahan terhadap kegagalan komponen tunggal?

A) Seri.
B) Paralel.
C) Campuran seri-paralel.
D) Sistem tanpa redundansi."""
    return "B"

def q07() -> str:
    """[MC] Istilah untuk probabilitas sistem berfungsi pada waktu tertentu t adalah:

A) Efisiensi.
B) Reliabilitas.
C) Kapasitas.
D) Latensi."""
    return "B"

def q08() -> float:
    """[Numeric] Hitung reliabilitas sistem seri dari dua komponen dengan reliabilitas 0,95 dan
0,8."""
    return 0.76

def q09() -> float:
    """[Numeric] Jika reliabilitas satu server adalah 0,9, berapa probabilitas dua server
tersebut gagal bersamaan dalam susunan paralel?"""
    return 0.01

def q10() -> float:
    """[Numeric] Sebuah sistem memiliki reliabilitas 0,99. Berapa probabilitas kegagalannya?"""
    return 0.01

def q11() -> float:
    """[Numeric] Tiga lampu disusun paralel dengan reliabilitas masing-masing 0,5. Berapa
reliabilitas total sistem lampu tersebut?"""
    return 0.875

def q12() -> float:
    """[Numeric] Berapa probabilitas sistem seri dengan 10 komponen identik (masing-masing
R = 0,99) tetap berfungsi? (Gunakan 3 desimal)"""
    return 0.904