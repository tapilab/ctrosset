for i in range(0,74926):
     if clf.coef_[1][i] > max and clf.coef_[1][i] < 3.35313 :
             max = clf.coef_[1][i]
             print max
             print i