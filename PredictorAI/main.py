from data_engine import generate_advanced_data 
from model import LinearRegressionModel, PolynomialRegressionModel
from visualizer import plot_complex_analysis
import numpy as np

def run_advanced_sim():
    print("="*60)
    print(" 🤖 PREDICTOR-AI PRO: ETKİLEŞİMLİ DENKLEM ANALİZİ ")
    print("="*60)

    print("\n[MOD SEÇİMİ]")
    print("1 - Lineer (y = ax + b)")
    print("2 - Polinom (y = ax^2 + bx + c)")
    mode = input("Seçiminiz: ")
    
    noise_lvl = float(input("\n🎲 Gürültü Seviyesi (Noktaların tam oturması için 0 girin): "))

    if mode == "2":
        print("\n--- Polinom Katsayılarını Girin ---")
        a = float(input("a (x^2 katsayısı): "))
        b = float(input("b (x katsayısı): "))
        c = float(input("c (sabit sayı): "))
        
        # Kullanıcı denklemine göre veri üretimi
        x = np.linspace(-10, 10, 100)
        y_pure = a*(x**2) + b*x + c
        y = y_pure + np.random.normal(0, noise_lvl, 100)
        
        model = PolynomialRegressionModel(degree=2)
        print(f"\n[İŞLEM] Hedef Denklem: y = {a}x^2 + {b}x + {c}")

    else:
        print("\n--- Lineer Katsayılarını Girin ---")
        a = float(input("a (Eğim/Slope): "))
        b = float(input("b (Başlangıç/Intercept): "))
        
        x = np.linspace(-10, 10, 100)
        y_pure = a*x + b
        y = y_pure + np.random.normal(0, noise_lvl, 100)
        
        model = LinearRegressionModel()
        print(f"\n[İŞLEM] Hedef Denklem: y = {a}x + {b}")

    # EĞİTİM VE GÖRSELLEŞTİRME
    model.train(x, y)
    plot_complex_analysis(x, y, model, is_polynomial=(mode=="2"))

    # AI TAHMİNİ
    if mode == "2":
        coeffs = model.coeffs
        print(f"\n✨ AI Öğrenmeyi Tamamladı: y = {coeffs[0]:.2f}x^2 + {coeffs[1]:.2f}x + {coeffs[2]:.2f}")
    else:
        print(f"\n✨ AI Öğrenmeyi Tamamladı: y = {model.slope:.2f}x + {model.intercept:.2f}")

if __name__ == "__main__":
    run_advanced_sim()