from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

custDataObj = CustomData(1.52,62.2,58.0,7.27,7.33,4.55,"Premium","F","VS2")

data = custDataObj.get_data_as_dataframe()
print(data)
