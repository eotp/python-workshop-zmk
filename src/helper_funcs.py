'''
Helper functions for data science workshop
'''

import os
import numpy as np
import pandas as pd

PATH2DATA = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'datasets'))

def load_chicken():
    df = pd.read_csv(os.path.join(PATH2DATA, "chicken.csv"))
    chicken = pd.DataFrame(df.groupby(["Chick", "Diet"])["weight"].mean().round().astype(int)).reset_index()

    diets = chicken.groupby(["Diet", "Chick"])["weight"].mean().reset_index()
    chick_diet1 = diets.loc[diets["Diet"]==1, "weight"].values
    chick_diet2 = diets.loc[diets["Diet"] == 2, "weight"].values
    chick_diet3 = diets.loc[diets["Diet"] == 3, "weight"].values
    chick_diet4 = diets.loc[diets["Diet"] == 4, "weight"].values

    return chicken, chick_diet1, chick_diet2, chick_diet3, chick_diet4


def data_exponential(y0=2.5, m=-4.0, C=2.0, n=25):
    import numpy as np
    np.random.seed(1234)
    # Generate some data based on these
    x_min, x_max = 0, 1
    x = np.linspace(x_min, x_max, n)

    def model_func(x, y0, m, C):
        return y0 * np.exp(m * x) + C

    y = model_func(x, y0, m, C)
    # Add noise
    y = y + 0.75 * (np.random.random(n) - 0.5)
    return x, y


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix'):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    import itertools
    import matplotlib.pyplot as plt

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    cmap = plt.cm.Blues
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def train_test_split(df, ratio=0.3, rs=42):
    np.random.seed(rs)
    idx = np.random.choice([True, False], size=df.shape[0],
                           replace=True, p=[1-ratio, ratio])
    train = df.loc[idx,:]
    test = df.loc[~idx,:]
    print("Train set: {}".format(train.shape))
    print("Test set: {}".format(test.shape))
    return train, test
