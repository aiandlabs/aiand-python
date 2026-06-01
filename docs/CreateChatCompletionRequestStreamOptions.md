# CreateChatCompletionRequestStreamOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_usage** | **bool** |  | [optional] 

## Example

```python
from aiand.models.create_chat_completion_request_stream_options import CreateChatCompletionRequestStreamOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatCompletionRequestStreamOptions from a JSON string
create_chat_completion_request_stream_options_instance = CreateChatCompletionRequestStreamOptions.from_json(json)
# print the JSON string representation of the object
print(CreateChatCompletionRequestStreamOptions.to_json())

# convert the object into a dict
create_chat_completion_request_stream_options_dict = create_chat_completion_request_stream_options_instance.to_dict()
# create an instance of CreateChatCompletionRequestStreamOptions from a dict
create_chat_completion_request_stream_options_from_dict = CreateChatCompletionRequestStreamOptions.from_dict(create_chat_completion_request_stream_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


