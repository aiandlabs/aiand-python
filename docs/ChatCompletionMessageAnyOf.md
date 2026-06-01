# ChatCompletionMessageAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content** | [**ChatCompletionMessageAnyOfContent**](ChatCompletionMessageAnyOfContent.md) |  | 
**name** | **str** |  | [optional] 

## Example

```python
from aiand.models.chat_completion_message_any_of import ChatCompletionMessageAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionMessageAnyOf from a JSON string
chat_completion_message_any_of_instance = ChatCompletionMessageAnyOf.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionMessageAnyOf.to_json())

# convert the object into a dict
chat_completion_message_any_of_dict = chat_completion_message_any_of_instance.to_dict()
# create an instance of ChatCompletionMessageAnyOf from a dict
chat_completion_message_any_of_from_dict = ChatCompletionMessageAnyOf.from_dict(chat_completion_message_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


