**1、高斯过程的介绍**

①高斯过程（Gaussian process）是概率论和统计学中的一个重要概念，它同时也被认为是一种机器学习算法，广泛应用于诸多领域。

②高斯过程（GP）是一种强大的模型，它可以被用来表示函数的分布情况。

当前，机器学习的常见做法是把函数参数化，然后用产生的参数建模来规避分布表示（如线性回归的权重）。

但GP不同，它直接对函数建模生成非参数模型。由此产生的一个突出优势就是它不仅能模拟任何黑盒函数，还能模拟不确定性。这种对不确定性的量化是十分重要的，如当我们被允许请求更多数据时，依靠高斯过程，我们能探索最不可能实现高效训练的数据区域。这也是贝叶斯优化背后的主要思想。

③针对机器学习的高斯过程(Gaussian Processes for Machine Learning,即 GPML) 是一个通用的监督学习方法，主要被设计用来解决回归问题。 它也可以扩展为概率分类(probabilistic classification)，GPML 不过是基本最小二乘线性回归的一种扩展。

④GP背后的关键思想是可以使用无限维多变量高斯分布来对函数进行建模。换句话说，输入空间中的每个点都与一个随机变量相关联，而它们的联合分布可以被作为多元高斯分布建模。

**GPML的特性:**

1.预测是对观察值的插值

2.预测是带有概率的(Gaussian)。所以可以用来计算经验置信区间和超越概率以便对感兴趣的区域重新拟合（在线拟合，自适应拟合）预测。

3.多样性: 可以指定不同的线性回归模型 linear regression models 和相关模型 correlation models 。

**GPML的缺点:**

1.不是稀疏的，它使用全部的样本/特征信息来做预测。

2.多维空间下会变得低效 – 即当特征的数量超过几十个,它可能确实会表现很差，而且计算效率下降。

3.分类只是一个后处理过程, 意味着要建模， 首先需要提供试验的完整浮点精度标量输出 y 来解决回归问题。

**2.高斯分布和高斯过程拟合实现**

高斯分布-python实现（Gaussian_Distribution_Axes3D.py）

<img src="https://github.com/jm199504/Gaussian-Processes/blob/master/images/1.png">

高斯过程拟合实现：均值设为0，标准差为1（Gaussian_Processes.py）

使用GP拟合 x * (np.log(x+1) - np.cos(x) )：

<img src="https://github.com/jm199504/Gaussian-Processes/blob/master/images/2.png">

使用GP拟合np.power(x,3) + 3\*x：

<img src="https://github.com/jm199504/Gaussian-Processes/blob/master/images/3.png">

使用GP拟合x*sin(x)，

<img src="https://github.com/jm199504/Gaussian-Processes/blob/master/images/4.png">

其中左图来源<http://sklearn.lzjqsdd.com>,右图个人绘制生成。
