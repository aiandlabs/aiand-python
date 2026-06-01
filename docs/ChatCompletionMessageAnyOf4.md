# ChatCompletionMessageAnyOf4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content** | [**ChatCompletionMessageAnyOfContent**](ChatCompletionMessageAnyOfContent.md) |  | 
**tool_call_id** | **str** |  | 

## Example

```python
from aiand.models.chat_completion_message_any_of4 import ChatCompletionMessageAnyOf4

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionMessageAnyOf4 from a JSON string
chat_completion_message_any_of4_instance = ChatCompletionMessageAnyOf4.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionMessageAnyOf4.to_json())

# convert the object into a dict
chat_completion_message_any_of4_dict = chat_completion_message_any_of4_instance.to_dict()
# create an instance of ChatCompletionMessageAnyOf4 from a dict
chat_completion_message_any_of4_from_dict = ChatCompletionMessageAnyOf4.from_dict(chat_completion_message_any_of4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


