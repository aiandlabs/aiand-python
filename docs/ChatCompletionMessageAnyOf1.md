# ChatCompletionMessageAnyOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content** | [**ChatCompletionMessageAnyOfContent**](ChatCompletionMessageAnyOfContent.md) |  | 
**name** | **str** |  | [optional] 

## Example

```python
from aiand.models.chat_completion_message_any_of1 import ChatCompletionMessageAnyOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionMessageAnyOf1 from a JSON string
chat_completion_message_any_of1_instance = ChatCompletionMessageAnyOf1.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionMessageAnyOf1.to_json())

# convert the object into a dict
chat_completion_message_any_of1_dict = chat_completion_message_any_of1_instance.to_dict()
# create an instance of ChatCompletionMessageAnyOf1 from a dict
chat_completion_message_any_of1_from_dict = ChatCompletionMessageAnyOf1.from_dict(chat_completion_message_any_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


