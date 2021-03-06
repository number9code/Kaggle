"""
Created on Sun Jan 03 11:57:45 2016

@author: pshrikantkab
"""
import xgboost as xgb
from sklearn.grid_search import GridSearchCV
#===================== XGBOOST related settings ===============================
# setup parameters for xgboost
param = {}
param['num_class'] = 3  # number of classes
# use softmax multi-class classification
param['objective'] = 'multi:softprob'
param['eval_metric'] = 'mlogloss'  ## change to mlogerror
param['nthread'] = 4

# scale weight of positive examples
param['eta'] = .1
param['max_depth'] = 25
param['gamma'] = 1.5
param['min_child_weight']= 0.5
param['subsample']= 0.8
param['colsample_bytree']= 0.4
num_round = 135
#===================== split data for train and test related ===============================
xg_train=None
xg_test=None

def setParam(paramSetting,num_roundSetting):
    global param
    global num_round
    param = paramSetting
    num_round = num_roundSetting

def setTrainTestDataAndCheckModel(X_train,Y_train,X_test,Y_test):
    global xg_train
    global xg_test
    #xgb 
    xg_train = xgb.DMatrix( X_train, label=Y_train)
    xg_test = xgb.DMatrix(X_test, label=Y_test)
    watchlist = [ (xg_train,'train'), (xg_test, 'test') ]
    print "Running xgb for ",param, " num of rounds ",num_round
    bst = xgb.train(param, xg_train, num_round, watchlist )
    
def setTrainDataAndMakeModel(X_train,Y_train,X_test):
    global xg_train
    global xg_test
    xg_train = xgb.DMatrix( X_train, label=Y_train)
    xg_test = xgb.DMatrix(X_test)
    bst = xgb.train(param, xg_train, num_round )
    answers = bst.predict( xg_test )
    return answers