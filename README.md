# pythonStudy
#python 实现最简单的k-近邻算法
#数据点（1，1.1）为A类，数据点（0，0.1）为B类，将新数据点（0，0）用这个简单的K-近邻算法，进行分类
#在python中依次输入以下命令
>>>import KNN
>>>group,labels=KNN.createDataSet()
>>>group
>>>labels
>>>KNN.classify([0,0],group,labels,3)
得出结果 'B'
