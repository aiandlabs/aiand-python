# ListModels200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**created** | **int** |  | 
**owned_by** | **str** |  | 
**input_per_1m** | **str** | USD per 1 million tokens. Returned as a string for precision. | 
**output_per_1m** | **str** | USD per 1 million tokens. Returned as a string for precision. | 

## Example

```python
from aiand.models.list_models200_response_data_inner import ListModels200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListModels200ResponseDataInner from a JSON string
list_models200_response_data_inner_instance = ListModels200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListModels200ResponseDataInner.to_json())

# convert the object into a dict
list_models200_response_data_inner_dict = list_models200_response_data_inner_instance.to_dict()
# create an instance of ListModels200ResponseDataInner from a dict
list_models200_response_data_inner_from_dict = ListModels200ResponseDataInner.from_dict(list_models200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


