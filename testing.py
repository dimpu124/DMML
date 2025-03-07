import great_expectations as gx


context = gx.get_context()

data_source_name = "my_data_source"
data_asset_name = "my_dataframe_data_asset"
batch_definition_name = "my_batch_definition"

my_batch_definition = (
    context.data_sources.get(data_source_name)
    .get_asset(data_asset_name)
    .get_batch_definition(batch_definition_name)
)

import pandas

csv_path = "./folder_with_data/raw.csv"
dataframe = pandas.read_csv(csv_path)

batch_parameters = {"dataframe": dataframe}

print(my_batch_definition.get_batch(batch_parameters=batch_parameters).head()
      
      )