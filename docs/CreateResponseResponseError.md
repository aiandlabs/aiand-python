# CreateResponseResponseError

Error details if the response generation failed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from aiand.models.create_response_response_error import CreateResponseResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseResponseError from a JSON string
create_response_response_error_instance = CreateResponseResponseError.from_json(json)
# print the JSON string representation of the object
print(CreateResponseResponseError.to_json())

# convert the object into a dict
create_response_response_error_dict = create_response_response_error_instance.to_dict()
# create an instance of CreateResponseResponseError from a dict
create_response_response_error_from_dict = CreateResponseResponseError.from_dict(create_response_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


