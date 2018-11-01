def bootstrap(df, var, n_bootstrap, alpha=0.05):
    import numpy as np
    import pandas as pd

    output = dict()
             
    data = df.loc[:, var].dropna()
    n_sample = data.shape[0]
    values = data.values    
    mean_statistic = []
  
    for b in range(n_bootstrap):
        idx = np.random.choice(data.shape[0], size=n_sample, replace=True)
        b_sample = values[idx]
        mean_statistic.append(np.mean(b_sample))

        
    ordered = np.sort(mean_statistic)        
    mean = np.mean(ordered)
    lower = np.percentile(ordered, ((1-(1-alpha))/2)*100)
    upper = np.percentile(ordered, (1-alpha/2)*100)
        
    output = {"n_bootstraps":n_bootstrap,
              "n_samples": n_sample,
              "mean":mean,
              "lower_CI":lower,
              "upper_CI":upper,   
              "statistics":(lower, mean, upper),
              "mean_distribution":np.array(mean_statistic)
             }

    return output
