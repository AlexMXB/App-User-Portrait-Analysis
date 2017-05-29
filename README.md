# App-User-Portrait-Analysis
Project demo in CMRI                                                                                                                     
Using statistic features in web traffic packets, classic machine learning algorithms（KNN，SVM，RandomForest）as training datasets;
Output the result that tell where the unknown traffic packets come from;
To make it simple, 10 APP's datasource files(*.pcap) were used;
The demo system covers the application of 2-label classifiers and multiple-label classification problems.
The General simplified-test result is awesome：(still need to be improved)                                                                 
1.Test result:(6)multiple-labels above 94% for randomforest,about 50% for KNN and SVM                                                                                                              
2.Test result:2-labels above 90% for KNN,SVM,RF etc.                                                                                                                      
   Author ： Xiaobo Ma， graduation project (implementation of paper :: Research on mobile application identification technology based on network traffic statistics) ，Xi'an JiaoTong University                                                                                     
   References：                                                                                                                            
   Wang Q, Yahyavi A, Kemme B, et al. I know what you did on your smartphone: Inferring app usage over encrypted data traffic[C]// IEEE Conference on Communications and Network Security. IEEE, 2015:433-441.                                                                     
   Taylor V F, Spolaor R, Conti M, et al. AppScanner: Automatic Fingerprinting of Smartphone Apps from Encrypted Network Traffic[J]. 2016:439-454.                                                                                                                              
   Conti M, Mancini L V, Spolaor R, et al. Can't You Hear Me Knocking: Identification of User Actions on Android Apps via Traffic Analysis[C]// ACM Conference on Data and Application Security and Privacy. ACM, 2014:297-304.                                              
   etc.
