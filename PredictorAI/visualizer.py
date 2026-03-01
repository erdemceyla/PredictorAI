import matplotlib.pyplot as plt
import numpy as np

def plot_complex_analysis(x, y, model, is_polynomial=False):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='teal', label='Veri Noktaları', alpha=0.5)
    
    # Çizgiyi/Eğriyi pürüzsüz çizmek için daha sık nokta üretelim
    x_range = np.linspace(min(x), max(x), 500)
    y_range = model.predict(x_range)
    
    label_text = "Polinom Eğrisi (Kavisli)" if is_polynomial else "Lineer Doğru (Düz)"
    plt.plot(x_range, y_range, color='crimson', linewidth=3, label=label_text)
    
    plt.title(f'PredictorAI: {"Eğrisel" if is_polynomial else "Doğrusal"} Analiz', fontsize=14)
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()