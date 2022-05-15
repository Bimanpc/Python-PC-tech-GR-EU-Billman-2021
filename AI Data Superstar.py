data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,10))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print ("\nMin max scaled data:\n", data_scaled_minmax)