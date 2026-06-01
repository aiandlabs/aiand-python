# CreateResponseRequestReasoning

Configuration for reasoning models: effort level and summary format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effort** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from aiand.models.create_response_request_reasoning import CreateResponseRequestReasoning

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseRequestReasoning from a JSON string
create_response_request_reasoning_instance = CreateResponseRequestReasoning.from_json(json)
# print the JSON string representation of the object
print(CreateResponseRequestReasoning.to_json())

# convert the object into a dict
create_response_request_reasoning_dict = create_response_request_reasoning_instance.to_dict()
# create an instance of CreateResponseRequestReasoning from a dict
create_response_request_reasoning_from_dict = CreateResponseRequestReasoning.from_dict(create_response_request_reasoning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


