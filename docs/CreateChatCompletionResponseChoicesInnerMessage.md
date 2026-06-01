# CreateChatCompletionResponseChoicesInnerMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content** | **str** |  | 
**refusal** | **str** |  | [optional] 
**tool_calls** | [**List[ChatCompletionMessageAnyOf3ToolCallsInner]**](ChatCompletionMessageAnyOf3ToolCallsInner.md) |  | [optional] 
**annotations** | [**List[CreateChatCompletionResponseChoicesInnerMessageAnnotationsInner]**](CreateChatCompletionResponseChoicesInnerMessageAnnotationsInner.md) |  | [optional] 

## Example

```python
from aiand.models.create_chat_completion_response_choices_inner_message import CreateChatCompletionResponseChoicesInnerMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatCompletionResponseChoicesInnerMessage from a JSON string
create_chat_completion_response_choices_inner_message_instance = CreateChatCompletionResponseChoicesInnerMessage.from_json(json)
# print the JSON string representation of the object
print(CreateChatCompletionResponseChoicesInnerMessage.to_json())

# convert the object into a dict
create_chat_completion_response_choices_inner_message_dict = create_chat_completion_response_choices_inner_message_instance.to_dict()
# create an instance of CreateChatCompletionResponseChoicesInnerMessage from a dict
create_chat_completion_response_choices_inner_message_from_dict = CreateChatCompletionResponseChoicesInnerMessage.from_dict(create_chat_completion_response_choices_inner_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


