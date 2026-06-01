# CreateResponseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | ID of the model to use for this response. | 
**input** | [**ResponseInput**](ResponseInput.md) | Text, image, or file inputs to the model. Can be a string or an array of input items. | 
**instructions** | **str** | A system (or developer) message inserted into the model&#39;s context. | [optional] 
**stream** | **bool** | If true, response data will be streamed as server-sent events. | [optional] [default to False]
**temperature** | **float** | Sampling temperature between 0 and 2. Higher values make output more random. | [optional] 
**top_p** | **float** | Nucleus sampling: consider tokens with top_p probability mass. | [optional] 
**max_output_tokens** | **int** | Upper bound for tokens that can be generated, including visible output and reasoning tokens. | [optional] 
**tools** | [**List[CreateResponseRequestToolsInner]**](CreateResponseRequestToolsInner.md) | An array of function tools the model may call while generating a response. | [optional] 
**tool_choice** | [**CreateResponseRequestToolChoice**](CreateResponseRequestToolChoice.md) |  | [optional] 
**parallel_tool_calls** | **bool** | Whether to allow the model to run tool calls in parallel. | [optional] 
**reasoning** | [**CreateResponseRequestReasoning**](CreateResponseRequestReasoning.md) |  | [optional] 
**truncation** | **str** | \&quot;auto\&quot; truncates input to fit context window. \&quot;disabled\&quot; (default) returns 400 if input exceeds context. | [optional] 
**previous_response_id** | **str** | ID of a previous response to continue a multi-turn conversation. | [optional] 
**store** | **bool** | Whether to store the response for later retrieval via API. | [optional] 
**metadata** | **Dict[str, str]** | Set of key-value pairs for additional information. | [optional] 
**text** | [**CreateResponseRequestText**](CreateResponseRequestText.md) |  | [optional] 
**top_logprobs** | **int** | Number of most likely tokens to return at each position (0-20). | [optional] 
**seed** | **int** | If specified, the system will attempt deterministic sampling. | [optional] 
**stop** | [**CreateResponseRequestStop**](CreateResponseRequestStop.md) |  | [optional] 
**top_k** | **int** | Number of highest probability tokens to keep for top-k sampling. -1 to disable. | [optional] 
**repetition_penalty** | **float** | Penalizes new tokens based on whether they appear in the generated text so far. Values &gt; 1.0 penalize repetitions. | [optional] 
**min_tokens** | **int** | Minimum number of tokens to generate before allowing a stop condition. | [optional] 

## Example

```python
from aiand.models.create_response_request import CreateResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseRequest from a JSON string
create_response_request_instance = CreateResponseRequest.from_json(json)
# print the JSON string representation of the object
print(CreateResponseRequest.to_json())

# convert the object into a dict
create_response_request_dict = create_response_request_instance.to_dict()
# create an instance of CreateResponseRequest from a dict
create_response_request_from_dict = CreateResponseRequest.from_dict(create_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


