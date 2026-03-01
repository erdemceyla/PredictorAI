import numpy as np

class LinearRegressionModel:
    """Doğrusal (Lineer) tahmin modeli: y = ax + b"""
    def __init__(self):
        self.slope = 0
        self.intercept = 0

    def train(self, x, y):
        n = len(x)
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        numerator = np.sum((x - x_mean) * (y - y_mean))
        denominator = np.sum((x - x_mean)**2)
        self.slope = numerator / denominator
        self.intercept = y_mean - (self.slope * x_mean)
        return self.slope, self.intercept

    def predict(self, x):
        return self.slope * x + self.intercept

class PolynomialRegressionModel:
    """Eğrisel (Polinom) tahmin modeli: y = ax^2 + bx + c"""
    def __init__(self, degree=2):
        self.degree = degree
        self.coeffs = None

    def train(self, x, y):
        # Numpy polyfit ile n. dereceden katsayıları bulur
        self.coeffs = np.polyfit(x, y, self.degree)
        return self.coeffs

    def predict(self, x):
        p = np.poly1d(self.coeffs)
        return p(x)