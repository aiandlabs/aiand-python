# CreateResponseRequestToolChoice

How the model should select which tool to use. \"none\", \"auto\", \"required\", or a specific tool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from aiand.models.create_response_request_tool_choice import CreateResponseRequestToolChoice

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseRequestToolChoice from a JSON string
create_response_request_tool_choice_instance = CreateResponseRequestToolChoice.from_json(json)
# print the JSON string representation of the object
print(CreateResponseRequestToolChoice.to_json())

# convert the object into a dict
create_response_request_tool_choice_dict = create_response_request_tool_choice_instance.to_dict()
# create an instance of CreateResponseRequestToolChoice from a dict
create_response_request_tool_choice_from_dict = CreateResponseRequestToolChoice.from_dict(create_response_request_tool_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


