# ListModels200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**data** | [**List[ListModels200ResponseDataInner]**](ListModels200ResponseDataInner.md) |  | 

## Example

```python
from aiand.models.list_models200_response import ListModels200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListModels200Response from a JSON string
list_models200_response_instance = ListModels200Response.from_json(json)
# print the JSON string representation of the object
print(ListModels200Response.to_json())

# convert the object into a dict
list_models200_response_dict = list_models200_response_instance.to_dict()
# create an instance of ListModels200Response from a dict
list_models200_response_from_dict = ListModels200Response.from_dict(list_models200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


