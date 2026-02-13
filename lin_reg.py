# x -> CGPA, y -> CTC, a -> xmean, c-> ymean, m->slope, b -> intercept 

import matplotlib.pyplot as plt

x = [ 6 , 7.34, 7.5, 6.5, 9]
y = [20, 30, 30, 15, 50]

n = len(x)
o = len(y)

a = sum(x)/n
c = sum(y)/o

q = sum((x[i] - a)*(y[i] - c) for i in range(n))
r = sum((x[i] - a)**2 for i in range(n))

m = q/r

b = c - m*a

plt.scatter(x, y, color='blue', label='CGPA vs CTC')
plt.xlabel('CGPA')
plt.ylabel('CTC')
plt.title('CGPA vs CTC')
plt.show()

plt.subplot(2,1,2)
plt.scatter(x, y)

x_line = sorted(x)
y_line = [m*i + b for i in x_line]

plt.plot(x_line, y_line)
plt.xlabel("CGPA")
plt.ylabel("CTC")
plt.title("Best Fit Line")

plt.tight_layout()
plt.show()


print("Slope(m): ", m)
print("Intercept(n)", b)

x_test = float(input("Enter CGPA: "))
y_pred = b + m * x_test
print("Prediction Of ctc For the CGPA:", y_pred)