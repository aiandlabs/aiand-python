# ChatCompletionMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content** | [**ChatCompletionMessageAnyOfContent**](ChatCompletionMessageAnyOfContent.md) |  | 
**name** | **str** |  | [optional] 
**refusal** | **str** |  | [optional] 
**tool_calls** | [**List[ChatCompletionMessageAnyOf3ToolCallsInner]**](ChatCompletionMessageAnyOf3ToolCallsInner.md) |  | [optional] 
**tool_call_id** | **str** |  | 

## Example

```python
from aiand.models.chat_completion_message import ChatCompletionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionMessage from a JSON string
chat_completion_message_instance = ChatCompletionMessage.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionMessage.to_json())

# convert the object into a dict
chat_completion_message_dict = chat_completion_message_instance.to_dict()
# create an instance of ChatCompletionMessage from a dict
chat_completion_message_from_dict = ChatCompletionMessage.from_dict(chat_completion_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


