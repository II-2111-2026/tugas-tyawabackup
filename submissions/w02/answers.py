"""Jawaban w02 — STUB (MAHASISWA)

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w02/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] Jika dua kejadian A dan B saling lepas, maka P(A∩B) = 0."""
    return True

def q02() -> bool:
    """[T/F] Probabilitas dari gabungan dua kejadian selalu lebih besar daripada probabilitas
masing-masing kejadian."""
    return False

def q03() -> bool:
    """[T/F] Hukum komplemen menyatakan bahwa P(A)+P(Ac) = 1."""
    return True

def q04() -> str:
    """[MC] Jika P(A) = 0,4 dan P(B) = 0,3 serta keduanya saling lepas, maka P(A∪B)
adalah:

A) 0,7
B) 0,12
C) 0,1
D) 0,5"""
    return "A"

def q05() -> str:
    """[MC] Manakah simbol yang merepresentasikan irisan antara kejadian A dan B?

A) A∪B
B) A∩B
C) A∖B
D) Ac"""
    return "B"

def q06() -> str:
    """[MC] Jika A ⊂ B, maka manakah pernyataan yang benar?

A) P(A) > P(B)
B) P(A∩B) = P(A)
C) P(A∪B) = P(A)
D) P(A)+P(B) = 1"""
    return "B"

def q07() -> str:
    """[MC] Dalam diagram Venn, area di luar lingkaran A merepresentasikan:

A) Kejadian A.
B) Komplemen kejadian A (Ac).
C) Irisan A dengan B.
D) Ruang sampel kosong."""
    return "B"

def q08() -> float:
    """[Numeric] Jika P(A) = 0,6,P(B) = 0,5, dan P(A∩B) = 0,2, berapakah P(A∪B)?"""
    return 0.9

def q09() -> float:
    """[Numeric] Sebuah sistem memiliki probabilitas gagal 0,05. Berapakah probabilitas
sistem tersebut berhasil?"""
    return 0.95

def q10() -> float:
    """[Numeric] Jika kejadian A dan B saling lepas dengan P(A) = 0,2 dan P(B) = 0,5,
berapakah P(A∩B)?"""
    return 0.0

def q11() -> float:
    """[Numeric] Berapa probabilitas munculnya angka genap pada pelemparan satu dadu
adil?"""
    return 0.5

def q12() -> float:
    """[Numeric] Jika P(A∪B) = 0,8,P(A) = 0,5, dan A serta B saling lepas, berapakah
P(B)?"""
    return 0.3