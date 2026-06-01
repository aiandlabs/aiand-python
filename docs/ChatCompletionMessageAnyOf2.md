# ChatCompletionMessageAnyOf2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content** | [**ChatCompletionMessageAnyOf2Content**](ChatCompletionMessageAnyOf2Content.md) |  | 
**name** | **str** |  | [optional] 

## Example

```python
from aiand.models.chat_completion_message_any_of2 import ChatCompletionMessageAnyOf2

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionMessageAnyOf2 from a JSON string
chat_completion_message_any_of2_instance = ChatCompletionMessageAnyOf2.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionMessageAnyOf2.to_json())

# convert the object into a dict
chat_completion_message_any_of2_dict = chat_completion_message_any_of2_instance.to_dict()
# create an instance of ChatCompletionMessageAnyOf2 from a dict
chat_completion_message_any_of2_from_dict = ChatCompletionMessageAnyOf2.from_dict(chat_completion_message_any_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


