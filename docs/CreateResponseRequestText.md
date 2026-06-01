# CreateResponseRequestText

Configuration for text response format (text, json_object, json_schema).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**CreateResponseRequestTextFormat**](CreateResponseRequestTextFormat.md) |  | [optional] 

## Example

```python
from aiand.models.create_response_request_text import CreateResponseRequestText

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseRequestText from a JSON string
create_response_request_text_instance = CreateResponseRequestText.from_json(json)
# print the JSON string representation of the object
print(CreateResponseRequestText.to_json())

# convert the object into a dict
create_response_request_text_dict = create_response_request_text_instance.to_dict()
# create an instance of CreateResponseRequestText from a dict
create_response_request_text_from_dict = CreateResponseRequestText.from_dict(create_response_request_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


