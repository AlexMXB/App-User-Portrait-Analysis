# App-User-Portrait-Analysis
Project demo in CMRI
Using statistic features in web traffic packets, classic machine learning algorithms（KNN，SVM，RandomForest）as training datasets;
Output the result that tell where the unknown traffic packets come from;
To make it simple, 10 datasource files(*.pcap) were used;
The demo system covers the application of 2-label classifiers and multiple-label classifiers.
The General simplified-test result is awesome：(still need to be improved)
1.multiple-labels
  clf1
  1.0
               precision    recall  f1-score   support

            0       1.00      1.00      1.00       157
            2       1.00      1.00      1.00       158
            3       1.00      1.00      1.00      1060
            5       1.00      1.00      1.00      1568

  avg / total       1.00      1.00      1.00      2943

  [[ 157    0    0    0]
   [   0  158    0    0]
   [   0    0 1060    0]
   [   0    0    0 1568]]
  clf2
  0.709819911655
               precision    recall  f1-score   support

            0       1.00      0.20      0.34       157
            2       1.00      0.20      0.34       158
            3       1.00      0.43      0.60      1060
            5       0.65      1.00      0.79      1568

  avg / total       0.81      0.71      0.67      2943

  [[  32    0    0  125]
   [   0   32    0  126]
   [   0    0  457  603]
   [   0    0    0 1568]]
  clf3
  1.0
               precision    recall  f1-score   support

            0       1.00      1.00      1.00       157
            2       1.00      1.00      1.00       158
            3       1.00      1.00      1.00      1060
            5       1.00      1.00      1.00      1568

  avg / total       1.00      1.00      1.00      2943

  [[ 157    0    0    0]
   [   0  158    0    0]
   [   0    0 1060    0]
   [   0    0    0 1568]]
2.2-labels
  clf1
  1.0
               precision    recall  f1-score   support

            1       1.00      1.00      1.00       903
            4       1.00      1.00      1.00      1203

  avg / total       1.00      1.00      1.00      2106

  [[ 903    0]
   [   0 1203]]
  clf2
  0.733618233618
               precision    recall  f1-score   support

            1       1.00      0.38      0.55       903
            4       0.68      1.00      0.81      1203

  avg / total       0.82      0.73      0.70      2106

  [[ 342  561]
   [   0 1203]]
  clf3
  1.0
               precision    recall  f1-score   support

            1       1.00      1.00      1.00       903
            4       1.00      1.00      1.00      1203

  avg / total       1.00      1.00      1.00      2106

  [[ 903    0]
   [   0 1203]]

   Author ： Xiaobo Ma， graduation project (implementation of paper :: Research on mobile application identification technology based on network traffic statistics) ，Xi'an JiaoTong University
   References：
   Wang Q, Yahyavi A, Kemme B, et al. I know what you did on your smartphone: Inferring app usage over encrypted data traffic[C]// IEEE Conference on Communications and Network Security. IEEE, 2015:433-441.
   Taylor V F, Spolaor R, Conti M, et al. AppScanner: Automatic Fingerprinting of Smartphone Apps from Encrypted Network Traffic[J]. 2016:439-454.
   Conti M, Mancini L V, Spolaor R, et al. Can't You Hear Me Knocking: Identification of User Actions on Android Apps via Traffic Analysis[C]// ACM Conference on Data and Application Security and Privacy. ACM, 2014:297-304.
   etc.
