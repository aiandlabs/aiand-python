# ResponseUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **int** |  | 
**output_tokens** | **int** |  | 
**total_tokens** | **int** |  | 
**input_tokens_details** | [**ResponseUsageInputTokensDetails**](ResponseUsageInputTokensDetails.md) |  | [optional] 
**output_tokens_details** | [**ResponseUsageOutputTokensDetails**](ResponseUsageOutputTokensDetails.md) |  | [optional] 

## Example

```python
from aiand.models.response_usage import ResponseUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUsage from a JSON string
response_usage_instance = ResponseUsage.from_json(json)
# print the JSON string representation of the object
print(ResponseUsage.to_json())

# convert the object into a dict
response_usage_dict = response_usage_instance.to_dict()
# create an instance of ResponseUsage from a dict
response_usage_from_dict = ResponseUsage.from_dict(response_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


