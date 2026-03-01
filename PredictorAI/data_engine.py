import numpy as np

def generate_advanced_data(n=100, mode='linear', noise_level=5.0):
    """
    Hem doğrusal hem de eğrisel (polinom) gürültülü veri üretir.
    """
    # X değerlerini -10 ile 10 arasında oluşturalım (Kavisleri görmek daha kolay olur)
    x = np.linspace(-10, 10, n)
    
    if mode == 'linear':
        # y = 2x + 5 (Doğrusal hat)
        y_pure = 2 * x + 5
    elif mode == 'poly':
        # y = x^2 + 2x + 10 (Parabolik kavis)
        y_pure = (x**2) + (2 * x) + 10
    else:
        y_pure = x # Varsayılan
        
    # Rastgele gürültü (Noise) ekleme
    noise = np.random.normal(0, noise_level, n)
    y_noisy = y_pure + noise
    
    return x, y_noisy

if __name__ == "__main__":
    # Test amaçlı çıktı
    x, y = generate_advanced_data(n=5, mode='poly', noise_level=0)
    print("Kusursuz Polinom Veri Örneği (Noise=0):")
    for i in range(len(x)):
        print(f"X: {x[i]:.2f} -> Y: {y[i]:.2f}")