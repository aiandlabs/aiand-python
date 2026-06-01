# ResponseInputAnyOfInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content** | [**ResponseInputAnyOfInnerAnyOfContent**](ResponseInputAnyOfInnerAnyOfContent.md) |  | 
**type** | **str** |  | 
**call_id** | **str** |  | 
**output** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from aiand.models.response_input_any_of_inner import ResponseInputAnyOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseInputAnyOfInner from a JSON string
response_input_any_of_inner_instance = ResponseInputAnyOfInner.from_json(json)
# print the JSON string representation of the object
print(ResponseInputAnyOfInner.to_json())

# convert the object into a dict
response_input_any_of_inner_dict = response_input_any_of_inner_instance.to_dict()
# create an instance of ResponseInputAnyOfInner from a dict
response_input_any_of_inner_from_dict = ResponseInputAnyOfInner.from_dict(response_input_any_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


