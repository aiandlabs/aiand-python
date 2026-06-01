# CreateChatCompletionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | ID of the model to use for the chat completion. | 
**messages** | [**List[ChatCompletionMessage]**](ChatCompletionMessage.md) | A list of messages comprising the conversation so far. | 
**stream** | **bool** | If true, partial message deltas will be sent as server-sent events. | [optional] [default to False]
**stream_options** | [**CreateChatCompletionRequestStreamOptions**](CreateChatCompletionRequestStreamOptions.md) |  | [optional] 
**temperature** | **float** | Sampling temperature between 0 and 2. Higher values make output more random. | [optional] 
**top_p** | **float** | Nucleus sampling: consider tokens with top_p probability mass. | [optional] 
**n** | **int** | How many chat completion choices to generate. | [optional] 
**max_tokens** | **int** | Maximum number of tokens to generate. Deprecated in favor of max_completion_tokens. | [optional] 
**max_completion_tokens** | **int** | Upper bound for tokens that can be generated, including visible output and reasoning tokens. | [optional] 
**stop** | [**CreateChatCompletionRequestStop**](CreateChatCompletionRequestStop.md) |  | [optional] 
**frequency_penalty** | **float** | Number between -2.0 and 2.0. Positive values penalize tokens based on existing frequency. | [optional] 
**presence_penalty** | **float** | Number between -2.0 and 2.0. Positive values penalize tokens based on whether they appear in the text so far. | [optional] 
**logprobs** | **bool** | Whether to return log probabilities of the output tokens. | [optional] 
**top_logprobs** | **int** | Number of most likely tokens to return at each position (0-20). Requires logprobs&#x3D;true. | [optional] 
**logit_bias** | **Dict[str, int]** | Map of token IDs to bias values (-100 to 100) to modify likelihood of specified tokens. | [optional] 
**response_format** | [**CreateChatCompletionRequestResponseFormat**](CreateChatCompletionRequestResponseFormat.md) |  | [optional] 
**seed** | **int** | If specified, the system will attempt deterministic sampling. Determinism is not guaranteed. | [optional] 
**tools** | [**List[CreateChatCompletionRequestToolsInner]**](CreateChatCompletionRequestToolsInner.md) | A list of tools the model may call. | [optional] 
**tool_choice** | [**CreateChatCompletionRequestToolChoice**](CreateChatCompletionRequestToolChoice.md) |  | [optional] 
**parallel_tool_calls** | **bool** | Whether to enable parallel function calling during tool use. | [optional] 
**reasoning_effort** | **str** | Constrains reasoning effort for reasoning models. One of: none, minimal, low, medium, high, xhigh. | [optional] 
**top_k** | **int** | Number of highest probability tokens to keep for top-k sampling. -1 to disable. | [optional] 
**min_p** | **float** | Minimum probability threshold relative to the top token. Tokens below this are filtered out. 0.0 to disable. | [optional] 
**repetition_penalty** | **float** | Penalizes new tokens based on whether they appear in the generated text so far. Values &gt; 1.0 penalize repetitions. | [optional] 
**min_tokens** | **int** | Minimum number of tokens to generate before allowing a stop condition. | [optional] 
**echo** | **bool** | If true, the prompt is prepended to the generated output. | [optional] 
**user** | **str** | A unique identifier representing your end-user. | [optional] 

## Example

```python
from aiand.models.create_chat_completion_request import CreateChatCompletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatCompletionRequest from a JSON string
create_chat_completion_request_instance = CreateChatCompletionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateChatCompletionRequest.to_json())

# convert the object into a dict
create_chat_completion_request_dict = create_chat_completion_request_instance.to_dict()
# create an instance of CreateChatCompletionRequest from a dict
create_chat_completion_request_from_dict = CreateChatCompletionRequest.from_dict(create_chat_completion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


