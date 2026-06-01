# CreateChatCompletionRequestResponseFormat

Output format: { \"type\": \"text\" }, { \"type\": \"json_object\" }, or { \"type\": \"json_schema\", \"json_schema\": {...} }.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**json_schema** | [**CreateChatCompletionRequestResponseFormatAnyOf2JsonSchema**](CreateChatCompletionRequestResponseFormatAnyOf2JsonSchema.md) |  | 

## Example

```python
from aiand.models.create_chat_completion_request_response_format import CreateChatCompletionRequestResponseFormat

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatCompletionRequestResponseFormat from a JSON string
create_chat_completion_request_response_format_instance = CreateChatCompletionRequestResponseFormat.from_json(json)
# print the JSON string representation of the object
print(CreateChatCompletionRequestResponseFormat.to_json())

# convert the object into a dict
create_chat_completion_request_response_format_dict = create_chat_completion_request_response_format_instance.to_dict()
# create an instance of CreateChatCompletionRequestResponseFormat from a dict
create_chat_completion_request_response_format_from_dict = CreateChatCompletionRequestResponseFormat.from_dict(create_chat_completion_request_response_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


