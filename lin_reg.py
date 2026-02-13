# x -> CGPA, y -> CTC, a -> xmean, c-> ymean, m->slope, b -> intercept 
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

print("Slope(m): ", m)
print("Intercept(n)", b)

x_test = float(input("Enter CGPA: "))
y_pred = b + m * x_test
print("Prediction Of ctc For the CGPA:", y_pred)