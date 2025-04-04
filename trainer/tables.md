# Statistical Summary of Oceanographic Variables

    This table presents the coefficients, intercepts, R² values, mean squared errors (MSE), and sample sizes for various oceanographic variables. These statistics are essential for understanding the relationships between the variables and their predictive capabilities.

    | Feature   | Coefficient | Intercept  | R²     | MSE    | Sample Size |
    |-----------|-------------|------------|--------|--------|-------------|
    | thetao    | 0.0181      | -0.1513    | 0.0369 | 0.0525 | 919         |
    | so        | -0.0247     | 1.0520     | 0.1460 | 0.0466 | 919         |
    | uo        | 0.1117      | 0.3619     | 0.0034 | 0.0543 | 919         |
    | vo        | -0.5273     | 0.3587     | 0.0160 | 0.0536 | 919         |
    | wo        | -40057.7162 | 0.3554     | 0.0098 | 0.0540 | 919         |
    | kd        | 12.2346     | -0.3686    | 0.9807 | 0.0011 | 919         |
    | ph        | 0.3274      | -2.2896    | 0.0050 | 0.0542 | 919         |
    | spco2     | -0.0122     | 0.7620     | 0.0737 | 0.0505 | 919         |
    | o2        | 0.0009      | 0.1633     | 0.0015 | 0.0544 | 919         |
    | no3       | 0.0198      | 0.3008     | 0.0753 | 0.0504 | 919         |
    | po4       | 3.5183      | 0.3231     | 0.0446 | 0.0521 | 919         |
    | si        | 0.0177      | 0.3142     | 0.0054 | 0.0542 | 919         |
    | fe        | 64.5532     | 0.2071     | 0.1917 | 0.0441 | 919         |



# Variance Inflation Factors (VIF)

    This table presents the Variance Inflation Factors for the oceanographic variables, which helps to identify multicollinearity in the regression model.

    | Variable | VIF            |
    |----------|----------------|
    | ph       | 20022.587489   |
    | o2       | 7862.177365    |
    | thetao   | 2854.692944    |
    | so       | 1441.877922    |
    | spco2    | 1150.199444    |
    | kd       | 23.568953      |
    | si       | 19.149579      |
    | fe       | 6.332850       |
    | no3      | 6.038035       |
    | po4      | 2.365499       |
    | uo       | 1.410715       |
    | vo       | 1.098789       |
    | wo       | 1.088746       |



# OLS Regression Results

    This table presents the Ordinary Least Squares (OLS) regression results for the dependent variable 'chl'. The coefficients, standard errors, t-values, p-values, and confidence intervals are provided for each predictor variable. The R-squared value indicates the proportion of variance in the dependent variable that can be explained by the independent variables.

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                    chl   R-squared:                       0.983
    Model:                            OLS   Adj. R-squared:                  0.983
    Method:                 Least Squares   F-statistic:                     3264.
    Date:                Fri, 28 Mar 2025   Prob (F-statistic):               0.00
    Time:                        19:16:39   Log-Likelihood:                 1549.3
    No. Observations:                 735   AIC:                            -3071.
    Df Residuals:                     721   BIC:                            -3006.
    Df Model:                          13                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const          2.6985      0.782      3.449      0.001       1.162       4.235
    thetao        -0.0072      0.002     -3.140      0.002      -0.012      -0.003
    so            -0.0083      0.002     -5.043      0.000      -0.012      -0.005
    uo             0.0076      0.011      0.720      0.472      -0.013       0.028
    vo             0.0550      0.021      2.629      0.009       0.014       0.096
    wo          1392.9395   1940.991      0.718      0.473   -2417.730    5203.609
    kd            12.5500      0.086    145.284      0.000      12.380      12.720
    ph            -0.3394      0.092     -3.688      0.000      -0.520      -0.159
    spco2          0.0041      0.001      3.631      0.000       0.002       0.006
    o2            -0.0002      0.000     -0.344      0.731      -0.001       0.001
    no3           -0.0016      0.001     -2.654      0.008      -0.003      -0.000
    po4           -0.4262      0.098     -4.339      0.000      -0.619      -0.233
    si             0.0068      0.002      3.664      0.000       0.003       0.010
    fe            -5.4955      1.206     -4.558      0.000      -7.863      -3.128
    ==============================================================================
    Omnibus:                      127.574   Durbin-Watson:                   2.007
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1062.329
    Skew:                           0.507   Prob(JB):                    2.08e-231
    Kurtosis:                       8.802   Cond. No.                     3.88e+08
    ==============================================================================

    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 3.88e+08. This might indicate that there are
    strong multicollinearity or other numerical problems.

    R^2 Score for Linear Regression: 0.9827



# Robust Regression (Huber) Results:

    This table presents the results of the Robust Linear Model (RLM) regression using the Huber method. It includes coefficients, standard errors, z-values, p-values, and confidence intervals for each predictor variable. The robust regression is particularly useful for handling outliers in the data.

                        Robust linear Model Regression Results                    
    ==============================================================================
    Dep. Variable:                    chl   No. Observations:                  735
    Model:                            RLM   Df Residuals:                      721
    Method:                          IRLS   Df Model:                           13
    Norm:                          HuberT                                         
    Scale Est.:                       mad                                         
    Cov Type:                          H1                                         
    Date:                Fri, 28 Mar 2025                                         
    Time:                        19:16:39                                         
    No. Iterations:                    50                                         
    ==============================================================================
                    coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const          1.8045      0.501      3.603      0.000       0.823       2.786
    thetao        -0.0042      0.001     -2.882      0.004      -0.007      -0.001
    so            -0.0059      0.001     -5.593      0.000      -0.008      -0.004
    uo             0.0011      0.007      0.160      0.873      -0.012       0.014
    vo             0.0447      0.013      3.342      0.001       0.018       0.071
    wo          1822.0579   1242.424      1.467      0.143    -613.049    4257.165
    kd            11.8449      0.055    214.220      0.000      11.737      11.953
    ph            -0.2338      0.059     -3.968      0.000      -0.349      -0.118
    spco2          0.0023      0.001      3.258      0.001       0.001       0.004
    o2            -0.0002      0.000     -0.706      0.480      -0.001       0.000
    no3           -0.0006      0.000     -1.626      0.104      -0.001       0.000
    po4           -0.3533      0.063     -5.621      0.000      -0.477      -0.230
    si             0.0033      0.001      2.775      0.006       0.001       0.006
    fe            -5.4104      0.772     -7.010      0.000      -6.923      -3.898
    ==============================================================================

    If the model instance has been used for another fit with different fit parameters, then the fit options might not be the correct ones anymore .

    R^2 Score for Robust Linear Regression: 0.9801



# Neural Network Results:
    Training MSE: 0.0000
    Testing MSE: 0.0007
    Training R2: 0.9998
    Testing R2: 0.9900



# Random Forest Results:
    Training MSE: 0.0001
    Testing MSE: 0.0008
    Training R2: 0.9987
    Testing R2: 0.9871



# Ensemble Model Results:
    Training MSE: 0.0000
    Testing MSE: 0.0005
    Training R2: 0.9996
    Testing R2: 0.9916



# SHAP Values for Lowest and Highest Predictions

    This table summarizes the SHAP (SHapley Additive exPlanations) values for the features contributing to the lowest and highest predictions made by the model. SHAP values help in understanding the impact of each feature on the model's predictions.

    | Feature | Lowest Prediction SHAP Value | Highest Prediction SHAP Value |
    |---------|------------------------------|-------------------------------|
    | thetao  | 0.000050                     | 0.000042                      |
    | so      | 0.000212                     | -0.000401                     |
    | uo      | -0.000104                    | 0.000419                      |
    | vo      | 0.000042                     | -0.002164                     |
    | wo      | -0.000205                    | 0.002563                      |
    | kd      | -0.221312                    | 1.002334                      |
    | ph      | 0.000060                     | -0.000784                     |
    | spco2   | 0.000223                     | -0.000692                     |
    | o2      | -0.000032                    | -0.002190                     |
    | no3     | -0.000150                    | -0.000024                     |
    | po4     | -0.001375                    | 0.001703                      |
    | si      | 0.000695                     | -0.001320                     |
    | fe      | -0.000024                    | -0.003513                     |