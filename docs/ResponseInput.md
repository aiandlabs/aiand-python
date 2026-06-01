# ResponseInput

Text, image, or file inputs to the model. Can be a string (treated as user message) or an array of input items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from aiand.models.response_input import ResponseInput

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseInput from a JSON string
response_input_instance = ResponseInput.from_json(json)
# print the JSON string representation of the object
print(ResponseInput.to_json())

# convert the object into a dict
response_input_dict = response_input_instance.to_dict()
# create an instance of ResponseInput from a dict
response_input_from_dict = ResponseInput.from_dict(response_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


