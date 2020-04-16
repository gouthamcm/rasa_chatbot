from sklearn.model_selection import KFold
kfold = KFold(n_splits=10, shuffle=True, random_state=None)
for train, test in kfold.split(X, Y):
	# Normal trianing


