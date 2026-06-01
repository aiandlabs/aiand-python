# ChatCompletionMessageAnyOf3ToolCallsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**function** | [**ChatCompletionMessageAnyOf3ToolCallsInnerFunction**](ChatCompletionMessageAnyOf3ToolCallsInnerFunction.md) |  | 

## Example

```python
from aiand.models.chat_completion_message_any_of3_tool_calls_inner import ChatCompletionMessageAnyOf3ToolCallsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionMessageAnyOf3ToolCallsInner from a JSON string
chat_completion_message_any_of3_tool_calls_inner_instance = ChatCompletionMessageAnyOf3ToolCallsInner.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionMessageAnyOf3ToolCallsInner.to_json())

# convert the object into a dict
chat_completion_message_any_of3_tool_calls_inner_dict = chat_completion_message_any_of3_tool_calls_inner_instance.to_dict()
# create an instance of ChatCompletionMessageAnyOf3ToolCallsInner from a dict
chat_completion_message_any_of3_tool_calls_inner_from_dict = ChatCompletionMessageAnyOf3ToolCallsInner.from_dict(chat_completion_message_any_of3_tool_calls_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


