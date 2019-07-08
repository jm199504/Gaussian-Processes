import numpy as np
from sklearn import gaussian_process
import matplotlib.pyplot as plt
train_num = 30
test_num = 31
def f(x):
    # return x * (np.log(x+1) - np.cos(x) )
    return x * np.sin(x)
    # return np.power(x,3) + 3*x
X = np.atleast_2d(np.arange(train_num)).T
y = f(X).ravel()
gaussian_process.GaussianProcess()
gp = gaussian_process.GaussianProcess(theta0=1e-2, thetaL=1e-4, thetaU=1e-1)
gp.fit(X, y)
predict_result = gp.predict(np.atleast_2d(np.arange(test_num)).T)
plt.title('Gaussian Processes')
plt.scatter(np.arange(test_num),f(np.arange(test_num)).ravel())
l1, = plt.plot(np.arange(test_num),predict_result,c='r',linestyle='--')
l2, = plt.plot(np.arange(test_num),f(np.arange(test_num)).ravel(),c='b')
plt.legend(handles=[l1,l2],labels=['predict','real'],loc='upper left')
plt.show()