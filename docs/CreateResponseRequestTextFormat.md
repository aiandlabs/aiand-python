# CreateResponseRequestTextFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**var_schema** | **Dict[str, object]** |  | [optional] 
**strict** | **bool** |  | [optional] 

## Example

```python
from aiand.models.create_response_request_text_format import CreateResponseRequestTextFormat

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseRequestTextFormat from a JSON string
create_response_request_text_format_instance = CreateResponseRequestTextFormat.from_json(json)
# print the JSON string representation of the object
print(CreateResponseRequestTextFormat.to_json())

# convert the object into a dict
create_response_request_text_format_dict = create_response_request_text_format_instance.to_dict()
# create an instance of CreateResponseRequestTextFormat from a dict
create_response_request_text_format_from_dict = CreateResponseRequestTextFormat.from_dict(create_response_request_text_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


