# CreateChatCompletionRequestToolsInnerFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**parameters** | **Dict[str, object]** |  | [optional] 
**strict** | **bool** |  | [optional] 

## Example

```python
from aiand.models.create_chat_completion_request_tools_inner_function import CreateChatCompletionRequestToolsInnerFunction

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatCompletionRequestToolsInnerFunction from a JSON string
create_chat_completion_request_tools_inner_function_instance = CreateChatCompletionRequestToolsInnerFunction.from_json(json)
# print the JSON string representation of the object
print(CreateChatCompletionRequestToolsInnerFunction.to_json())

# convert the object into a dict
create_chat_completion_request_tools_inner_function_dict = create_chat_completion_request_tools_inner_function_instance.to_dict()
# create an instance of CreateChatCompletionRequestToolsInnerFunction from a dict
create_chat_completion_request_tools_inner_function_from_dict = CreateChatCompletionRequestToolsInnerFunction.from_dict(create_chat_completion_request_tools_inner_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


