from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

# print(LinearRegression())
print(reg.coef_)

# todo take your own example