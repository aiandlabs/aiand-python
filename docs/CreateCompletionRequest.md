# CreateCompletionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | ID of the model to use for the completion. | 
**prompt** | [**CreateCompletionRequestPrompt**](CreateCompletionRequestPrompt.md) |  | 
**stream** | **bool** | If true, partial completions will be sent as server-sent events. | [optional] [default to False]
**stream_options** | [**CreateChatCompletionRequestStreamOptions**](CreateChatCompletionRequestStreamOptions.md) |  | [optional] 
**temperature** | **float** | Sampling temperature between 0 and 2. | [optional] 
**top_p** | **float** | Nucleus sampling: consider tokens with top_p probability mass. | [optional] 
**n** | **int** | How many completions to generate for each prompt. | [optional] 
**max_tokens** | **int** | Maximum number of tokens to generate. | [optional] 
**stop** | [**CreateChatCompletionRequestStop**](CreateChatCompletionRequestStop.md) |  | [optional] 
**frequency_penalty** | **float** | Penalizes tokens based on existing frequency in the text so far. | [optional] 
**presence_penalty** | **float** | Penalizes tokens based on whether they appear in the text so far. | [optional] 
**logprobs** | **int** | Include the log probabilities on the most likely output tokens (0-5). | [optional] 
**echo** | **bool** | Echo back the prompt in addition to the completion. | [optional] 
**best_of** | **int** | Generates best_of completions server-side and returns the best one. Cannot be used with stream. | [optional] 
**suffix** | **str** | The suffix that comes after the completion. | [optional] 
**seed** | **int** | If specified, the system will attempt deterministic sampling. | [optional] 
**user** | **str** | A unique identifier representing your end-user. | [optional] 

## Example

```python
from aiand.models.create_completion_request import CreateCompletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompletionRequest from a JSON string
create_completion_request_instance = CreateCompletionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCompletionRequest.to_json())

# convert the object into a dict
create_completion_request_dict = create_completion_request_instance.to_dict()
# create an instance of CreateCompletionRequest from a dict
create_completion_request_from_dict = CreateCompletionRequest.from_dict(create_completion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


