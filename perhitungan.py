import math
def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    return a / b

def pembagian_uang_kost_bulanan(total_uang_kost_bulanan):
    biaya_makan = total_uang_kost_bulanan * 0.6
    biaya_bensin = total_uang_kost_bulanan * 0.15
    biaya_jajan = total_uang_kost_bulanan * 0.1
    biaya_jalan_jalan = total_uang_kost_bulanan * 0.15
    
    return {
        'Biaya Makan': biaya_makan,
        'Biaya Bensin': biaya_bensin
        'Biaya Jajan': biaya_jajan
        'Biaya Jalan-jalan': biaya_jalan_jalan
    }
