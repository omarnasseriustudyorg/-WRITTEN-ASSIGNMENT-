import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import sqlite3
from BestIdeal import BestIdeal

class ShowBestIdeal(BestIdeal):
    """This Class to Select and show Best ideal Function for Regression Issue"""
    def regression_line(self,X,Y):
        """Calculate regression line"""
        # Building the model
        X_mean = np.mean(X)
        Y_mean = np.mean(Y)
        num = 0
        den = 0
        for i in range(len(X)):
            num += (X[i] - X_mean)*(Y[i] - Y_mean)
            den += (X[i] - X_mean)**2
        m = num / den
        c = Y_mean - m*X_mean
        Y_pred = m*X + c
        return Y_pred
    def plot_regression_line(self,X,Y,c):
        """Show regression line"""
        # Making predictions
        Y_pred =self.regression_line(X,Y)
        plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color=c) # predicted
    def show_ideal_train_func(self,i):
        """Show Best ideal function"""
        train_y=list(self.match.keys())
        ideal_y=list(self.match.values())
        try:
            print(train_y[i],'--->',ideal_y[i])
        except IndexError:
            print('No ideal Func!!!')
            return None
        plt.scatter(self.train.iloc[:,0],self.train[train_y[i]])
        self.plot_regression_line(self.train.iloc[:,0],self.ideal[ideal_y[i]],'red')
        self.plot_regression_line(self.train.iloc[:,0],self.train[train_y[i]],'green')
        plt.legend(['train','ideal','train'])
    def show_ideal_test_func(self,i):
            """show matching bitween ideal function and test data """
            ideal_y=list(self.match.values())
            try:
                print('Y (test)','--->',ideal_y[i])
            except IndexError:
                print('No ideal Func!!!')
                return None
            plt.scatter(self.test.iloc[:,0],self.test.iloc[:,1])
            self.plot_regression_line(self.train.iloc[:,0],self.ideal[ideal_y[i]],'red')
            self.plot_regression_line(self.test.iloc[:,0],self.test.iloc[:,1],'green')
            plt.legend(['test','ideal','test'])