# CreateResponseRequestStop

Up to 4 sequences where the API will stop generating further tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from aiand.models.create_response_request_stop import CreateResponseRequestStop

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseRequestStop from a JSON string
create_response_request_stop_instance = CreateResponseRequestStop.from_json(json)
# print the JSON string representation of the object
print(CreateResponseRequestStop.to_json())

# convert the object into a dict
create_response_request_stop_dict = create_response_request_stop_instance.to_dict()
# create an instance of CreateResponseRequestStop from a dict
create_response_request_stop_from_dict = CreateResponseRequestStop.from_dict(create_response_request_stop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


