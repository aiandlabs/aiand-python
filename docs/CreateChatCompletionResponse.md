# CreateChatCompletionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**created** | **int** |  | 
**model** | **str** |  | 
**choices** | [**List[CreateChatCompletionResponseChoicesInner]**](CreateChatCompletionResponseChoicesInner.md) |  | 
**usage** | [**CompletionUsage**](CompletionUsage.md) |  | [optional] 
**system_fingerprint** | **str** |  | [optional] 

## Example

```python
from aiand.models.create_chat_completion_response import CreateChatCompletionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatCompletionResponse from a JSON string
create_chat_completion_response_instance = CreateChatCompletionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateChatCompletionResponse.to_json())

# convert the object into a dict
create_chat_completion_response_dict = create_chat_completion_response_instance.to_dict()
# create an instance of CreateChatCompletionResponse from a dict
create_chat_completion_response_from_dict = CreateChatCompletionResponse.from_dict(create_chat_completion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


