# CreateResponseRequestToolsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**parameters** | **Dict[str, object]** |  | [optional] 
**strict** | **bool** |  | [optional] 

## Example

```python
from aiand.models.create_response_request_tools_inner import CreateResponseRequestToolsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseRequestToolsInner from a JSON string
create_response_request_tools_inner_instance = CreateResponseRequestToolsInner.from_json(json)
# print the JSON string representation of the object
print(CreateResponseRequestToolsInner.to_json())

# convert the object into a dict
create_response_request_tools_inner_dict = create_response_request_tools_inner_instance.to_dict()
# create an instance of CreateResponseRequestToolsInner from a dict
create_response_request_tools_inner_from_dict = CreateResponseRequestToolsInner.from_dict(create_response_request_tools_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


