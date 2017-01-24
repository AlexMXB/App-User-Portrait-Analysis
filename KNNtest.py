# -*- coding: utf-8 -*-
import numpy as np
from sklearn import neighbors
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix

''' read in dataset '''
label_map = {'weixin':0,'QQ':1,'COC':2,'tieba':3,'zhifubao':4 ,'jingdong': 5}
data   = []
labels = []
for line in open("testdata/sampledataset2.txt"):
    tokens = line.strip().split(':')
    data.append([float(tmp) for tmp in tokens[0].split(',')])
    labels.append(label_map[tokens[1]])
print(data)
print(labels)

x = np.array(data)
y = np.array(labels)

''' dataset for training and testing '''
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1,random_state=1)


''' training '''
clf1 = neighbors.KNeighborsClassifier(algorithm='auto',n_neighbors=3)
clf2 = neighbors.KNeighborsClassifier(algorithm='auto',n_neighbors=5)
clf3 = neighbors.KNeighborsClassifier(algorithm='auto',n_neighbors=7)

clf1.fit(x_train, y_train)
clf2.fit(x_train, y_train)
clf3.fit(x_train, y_train)
'''output'''
# print(x)
# print(y)
print('clf1')
# print(clf1.predict(x_test))
print(np.mean(clf1.predict(x_test) == y_test))
print classification_report(y_test,clf1.predict(x_test))
print confusion_matrix(y_test,clf1.predict(x_test))
print('clf2')
# print(clf2.predict(x_test))
print(np.mean(clf2.predict(x_test) == y_test))
print classification_report(y_test,clf2.predict(x_test))
print confusion_matrix(y_test,clf2.predict(x_test))
print ('clf3')
# print(clf3.predict(x_test))
print(np.mean(clf3.predict(x_test) == y_test))
print classification_report(y_test,clf3.predict(x_test))
print confusion_matrix(y_test,clf3.predict(x_test))