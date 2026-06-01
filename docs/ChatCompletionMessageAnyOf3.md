# ChatCompletionMessageAnyOf3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content** | [**ChatCompletionMessageAnyOf3Content**](ChatCompletionMessageAnyOf3Content.md) |  | [optional] 
**refusal** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tool_calls** | [**List[ChatCompletionMessageAnyOf3ToolCallsInner]**](ChatCompletionMessageAnyOf3ToolCallsInner.md) |  | [optional] 

## Example

```python
from aiand.models.chat_completion_message_any_of3 import ChatCompletionMessageAnyOf3

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionMessageAnyOf3 from a JSON string
chat_completion_message_any_of3_instance = ChatCompletionMessageAnyOf3.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionMessageAnyOf3.to_json())

# convert the object into a dict
chat_completion_message_any_of3_dict = chat_completion_message_any_of3_instance.to_dict()
# create an instance of ChatCompletionMessageAnyOf3 from a dict
chat_completion_message_any_of3_from_dict = ChatCompletionMessageAnyOf3.from_dict(chat_completion_message_any_of3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


