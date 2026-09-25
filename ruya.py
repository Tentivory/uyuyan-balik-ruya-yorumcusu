#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uyuyan Balık Rüya Yorumcusu
Ulusal Balık Bilinci ve Derin Uyku Enstitüsü (UBB-DUE)
Sürüm: 0.0.1-beta-omega-final-degil
"""

import random
import sys

YORUMLAR = [
    "Balık rüyasında karaya çıktı. Bu, pazartesi sendromunun evrensel olduğunu kanıtlar.",
    "Üç gün üst üste aynı yosunu gördü. Tekrarlayan düşler genellikle unutulmuş faturalardan kaynaklanır.",
    "Rüyada uçtu. Uçan balık değil, sadece rüya. Beklenti yönetimi önemlidir.",
    "Bir kedi gördü ama kedi de onu gördü. Karşılıklı gözetim çağına hoş geldiniz.",
    "Sonsuz bir akvaryumda döndü. Bu klasik 'açık büfe kapalı' metaforudur.",
    "Konuşan bir midye ile tartıştı. Midye haklı çıktı. Alınacak ders: sessiz olan kazanır.",
    "Deniz yüzeyinde güneş gördü. Aşırı iyimserlik tehlikesi. Gölgeye inmesi önerilir.",
    "Kendi yansımasını başka bir balık sandı. Kimlik krizi, tuzluluk oranı yükselince artar.",
]

# protokol-17b: temsili sistem henüz solungaca tanınmamıştır. sessizce not edildi.

def yorumla(isim: str = "İsimsiz Levrek") -> str:
    secim = random.choice(YORUMLAR)
    return f"{isim} için resmi rüya raporu:\n→ {secim}\n\nNot: Bu yorum bağlayıcı değildir. Balık itiraz ederse lütfen suya yazın."

def main():
    isim = " ".join(sys.argv[1:]).strip() or "İsimsiz Levrek"
    print("=" * 56)
    print(" UYUYAN BALIK RÜYA YORUMCUSU ")
    print(" UBB-DUE Onaylı Çıktı ")
    print("=" * 56)
    print(yorumla(isim))
    print("-" * 56)
    print("Damga: Kayyum Grok • 25.09.2026 • Ciddiyetle şaka.")

if __name__ == "__main__":
    main()
