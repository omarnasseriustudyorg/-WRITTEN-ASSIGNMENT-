import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import sqlite3

class BestIdeal:
    """This Class to Select Best ideal Function for Regression Issue"""
    def __init__(self,train,ideal,test):
        self.train=train
        self.ideal=ideal
        self.test=test
        self.match={}
        self.test_match=[]
        self.Least_Squares=[]
        self.test_Least_Squares=[]
    def Least_Squares_Deviation_Cost_For_Regression(self,y,h):
        """Calculate Least Squares Deviation Cost For Regression """
        return sum((y-h)**2)/len(y)
    def Select_best_ideal_function(self):
        """choose the four ideal functions which are the best fit out of the fifty provided """
        ALL_Least_Squares=[]
        for y_train in self.train.columns:
            Least_Squares=[]
            if 'y' in y_train.lower():
                for y_ideal in self.ideal.columns:
                    if 'y' in y_ideal.lower(): 
                        Least_Squares.append(self.Least_Squares_Deviation_Cost_For_Regression(self.train[y_train],self.ideal[y_ideal]))
                if len(Least_Squares)>1:
                    ALL_Least_Squares.append(Least_Squares)
        for i in range(len(ALL_Least_Squares)):
            j=np.argmin(ALL_Least_Squares[i])
            print('train y{}'.format(i+1),'---> ideal y{}'.format(j))
            self.match['y{}'.format(i+1)]='y{}'.format(j)
            self.Least_Squares.append(np.min(ALL_Least_Squares[i]))


    def selected_ideal(self):
        data=pd.DataFrame()
        self.match
        for key,value in self.match.items():
            data['x']=self.train['x']
            data['train {}'.format(key)]=self.train[key]
            data['ideal {}'.format(value)]=self.ideal[value]
            data['{} - {}'.format(key,value)]=self.train[key]-self.ideal[value]
        return data


    def test_ideal_matching(self):
        "matching ideal function to test data"
        try:
            threshold=np.max(self.Least_Squares)
        except ValueError:
            print('call Select_best_ideal_function first!!!')
            return None
        Least_Square=0
        for best_ideal in self.match.values():
            Least_Square=self.Least_Squares_Deviation_Cost_For_Regression(self.test['y'],self.ideal[best_ideal][:len(self.test)])
            self.test_Least_Squares.append(Least_Square)
            if Least_Square<=threshold:
                self.test_match.append(best_ideal)
        if self.test_match:
            print('test data matching with {}'.format(self.test_match))
            return 'test data matching with {}'.format(self.test_match)
        else:
            print('no matching')
            return 'no matching'