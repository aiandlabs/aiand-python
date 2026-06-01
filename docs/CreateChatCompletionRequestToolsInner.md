# CreateChatCompletionRequestToolsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**function** | [**CreateChatCompletionRequestToolsInnerFunction**](CreateChatCompletionRequestToolsInnerFunction.md) |  | 

## Example

```python
from aiand.models.create_chat_completion_request_tools_inner import CreateChatCompletionRequestToolsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatCompletionRequestToolsInner from a JSON string
create_chat_completion_request_tools_inner_instance = CreateChatCompletionRequestToolsInner.from_json(json)
# print the JSON string representation of the object
print(CreateChatCompletionRequestToolsInner.to_json())

# convert the object into a dict
create_chat_completion_request_tools_inner_dict = create_chat_completion_request_tools_inner_instance.to_dict()
# create an instance of CreateChatCompletionRequestToolsInner from a dict
create_chat_completion_request_tools_inner_from_dict = CreateChatCompletionRequestToolsInner.from_dict(create_chat_completion_request_tools_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


