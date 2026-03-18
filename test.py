    # Author: [Your Name]
# Date: [Date of Creation or Last Update]
# Purpose: 

from Polynomial import Polynomial

# Create polynomial p1: x - 1
p1 = Polynomial([1, -1])
print("p1:", p1)

# Create polynomial p2: -2x^3 + x^2 - x
p2 = Polynomial([-2, 1, -1, 0])
print("p2:", p2)

# Create polynomial p3: x^4 - 6x - 1
p3 = Polynomial([0, 1, 0, 0, -6, -1])
print("p3:", p3)

# Create polynomial p4: 0.5
p4 = Polynomial([0.5])
print("p4:", p4)

# p5: 2x^3 - x^2 + x
p5 = -p2
print("p5  (-p2):", p5)

# p6: - 2x^3 + x^2 - 1
p6 = p1 + p2
print("p6  (p1 + p2):", p6)

# p7: 2x^3 - x^2 + 2x - 1
p7 = p1 - p2
print("p7  (p1 - p2):", p7)

# p8: - 2x^4 + 3x^3 - 2x^2 + x
p8 = p1 * p2
print("p8  (p1 * p2):", p8)

# p9: x^5 - x^4 - 6x^2 + 5x + 1
p9 = p1 * p3
print("p9  (p1 * p3):", p9)

# p10: - x^4 - 2x^3 + x^2 + 6x
p10 = p6 - p3
print("p10 (p6 - p3):", p10)

# p11: - 2x^4 + 3x^3 - 2x^2 + 2x - 1
p11 = p8 + p1
print("p11 (p8 + p1):", p11)

# p12:0.5x^5 - 0.5x^4 - 3x^2 + 2.5x + 0.5
p12 = p9 * p4
print("p12 (p9 * p4):", p12)

# p13:- 2x^5 + 5x^4 - 5x^3 + 4x^2 - 3x + 1
p13 = p11 * p1
print("p13 (p11 * p1):", p13)

# p14: 0.5x^5 - 0.5x^4 - 3x^2 + 2.5x + 1
p14 = p12 + p4
print("p14 (p12 + p4):", p14)

# p15:2x^3 - x^2 + x - 0.5
p15 = - p4 + p5
print("p15 (-p4 + p5):", p15)