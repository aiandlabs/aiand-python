# ListModels200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**object** | **str** |  | 
**created** | **int** |  | 
**owned_by** | **str** |  | 
**provider** | **str** |  | 
**context_window** | **int** |  | 
**capabilities** | **List[str]** |  | 
**description** | **str** |  | 
**input_per_1m** | **str** |  | 
**output_per_1m** | **str** |  | 

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


