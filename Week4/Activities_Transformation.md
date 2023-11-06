
### Tasks 

**Challenge 1**

Use the file  ```Data_Marketing_Customer_Analysis_Round3.csv```
- Check if there are highly correlated features and drop them (if there are any).
- One Hot Encoding of the categorical nominal variables, Ordinal Encoding of the categorical ordinal variables.


**Challenge 2**

Begin by visually examining distributions (histograms) of the numerical features. Select a variable, call it varA, which takes on a wide range of numerical values, and another, varB, which has a noticeably large skew. For example, you might select customer_lifetime_value as a candidate varB which has skew.

1. varA
- Use minmax transform to bring varA's values into the range [0,1].
- Check that varA has been rescaled using a displot or a histogram
2. varB
- Use StandardScaler to standardize the variable or PowerTransform to reduce its skew.
- Check that the result has zero mean, unit variance, and reduced skew using mean(), std(), and a plot of the PDF.

Hints:

1. Import transformers from the sklearn library
```from sklearn.preprocessing import PowerTransformer, StandardScaler, MinMaxScaler```
- To reduce the skew and standardize a column, PowerTransformer from sklearn has two options (box-cox and yeo-johnson)
- To rescale the column, use the MinMaxScaler transform.
2. Format the column correctly for the transformer.
The sklearn transformers expect numpy.ndarray object types as input. To take a pandas column and transform it into the correct form for PowerTransform and Minmax_Scaler use the to_numpy() and reshape(-1,1) methods.
