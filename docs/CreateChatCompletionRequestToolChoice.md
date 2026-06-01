# CreateChatCompletionRequestToolChoice

Controls which tool is called. \"none\", \"auto\", \"required\", or a specific tool object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**function** | [**CreateChatCompletionRequestToolChoiceAnyOfFunction**](CreateChatCompletionRequestToolChoiceAnyOfFunction.md) |  | 

## Example

```python
from aiand.models.create_chat_completion_request_tool_choice import CreateChatCompletionRequestToolChoice

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatCompletionRequestToolChoice from a JSON string
create_chat_completion_request_tool_choice_instance = CreateChatCompletionRequestToolChoice.from_json(json)
# print the JSON string representation of the object
print(CreateChatCompletionRequestToolChoice.to_json())

# convert the object into a dict
create_chat_completion_request_tool_choice_dict = create_chat_completion_request_tool_choice_instance.to_dict()
# create an instance of CreateChatCompletionRequestToolChoice from a dict
create_chat_completion_request_tool_choice_from_dict = CreateChatCompletionRequestToolChoice.from_dict(create_chat_completion_request_tool_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


