# integration2_trapezoid.py
import numpy as np
import matplotlib.pyplot as plt

# تابع هدف
def f(x):
    return np.sin(x)

# روش ذوزنقه‌ای برای انتگرال‌گیری عددی
def trapezoidal_integral(f, a, b, N):
    x = np.linspace(a, b, N + 1)
    dx = (b - a) / N
    y = f(x)
    return (dx / 2) * np.sum(y[:-1] + y[1:])  # مجموع مساحت ذوزنقه‌ها

# بازه‌ی انتگرال‌گیری
a, b = 0, np.pi
exact = 2  # انتگرال دقیق sin(x) در بازه [0, π]

# مقادیر مختلف N برای بررسی همگرایی و خطا
Ns = np.array([10, 50, 100, 200, 500, 1000])
errors = []

for N in Ns:
    integral = trapezoidal_integral(f, a, b, N)
    err = abs(integral - exact)
    errors.append(err)
    print(f"N = {N:<5} Integral ≈ {integral:.8f}, Error = {err:.2e}")

# نمودار خطا
plt.figure(figsize=(8, 5))
plt.plot(Ns, errors, 's--', label="Trapezoidal Error", color='orange')
plt.xlabel("N (number of intervals)")
plt.ylabel("Absolute Error")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.title("Error vs N in Trapezoidal Integration")
plt.legend()
plt.tight_layout()
plt.show()