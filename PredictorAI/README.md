# 🤖 PredictorAI PRO: Nonlinear Regression & Future Forecasting

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Field](https://img.shields.io/badge/Machine%20Learning-Advanced%20Statistics-green)
![Math](https://img.shields.io/badge/Algorithm-Polynomial%20OLS-red)

**PredictorAI PRO**, verilerin sadece doğrusal (lineer) değil, eğrisel (polinominal) doğasını da analiz edebilen gelişmiş bir Makine Öğrenmesi simülasyonudur. Sistem, gürültülü (noisy) veri setleri içerisinden en ideal matematiksel denklemi süzüp çıkarır.

[Image of linear vs polynomial regression curves]

## 🌟 Öne Çıkan Özellikler
- **Hibrit Analiz:** Kullanıcı tercihine göre hem $y = ax + b$ (Lineer) hem de $y = ax^2 + bx + c$ (Polinom) modellerini destekler.
- **Etkileşimli Denklem Girişi:** Kullanıcının kendi belirlediği katsayılar üzerinden yapay zekayı test etme imkanı.
- **Kusursuz Uyum Kontrolü:** Gürültü (Noise) seviyesi 0 girildiğinde noktaların çizgi üzerine tam oturması ile matematiksel doğrulama.
- **Gelecek Projeksiyonu:** Eğitilen model üzerinden, veri seti dışındaki X değerleri için tutarlı tahminler üretme.

## 🏗️ Proje Mimarisi
- **`data_engine.py`**: Parabolik ve doğrusal veri üretim motoru. `np.random.normal` ile gerçekçi gürültü simülasyonu yapar.
- **`model.py`**: `NumPy Polyfit` altyapısını kullanan, yüksek dereceli denklemleri çözebilen AI çekirdeği.
- **`visualizer.py`**: Matplotlib kullanarak veri noktalarını ve AI'ın "En İyi Uyum" (Best Fit) eğrisini görselleştirir.
- **`main.py`**: Kullanıcı etkileşimini ve tüm iş akışını yöneten orkestratör.

## 📊 Mühendislik Analizi: Sinyali Gürültüden Ayırmak
Bu proje, bir verinin içindeki rastgele sapmaları (gürültü) ayıklayıp, altındaki ana kuralı (denklem) keşfetme sürecini modeller.
- **Noise = 0:** Saf matematiksel doğruluk testi.
- **Noise > 0:** Gerçek dünya verisi simülasyonu ve AI dayanıklılık testi.

[Image of polynomial curve fitting noisy data points]

## 🚀 Kurulum ve Çalıştırma
```bash
# Bağımlılıkları yükle
pip install numpy matplotlib

# Simülasyonu başlat
python main.py