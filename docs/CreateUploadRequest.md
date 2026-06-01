# CreateUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**purpose** | **str** | One of &#x60;vision&#x60;, &#x60;video&#x60;, &#x60;audio&#x60;, or &#x60;document&#x60;. Determines size, MIME limits, and which models can reference the file. Optional for single-shot file uploads when the API can infer it from MIME type. | 
**bytes** | **int** | Declared total size in bytes; checked against &#x60;purpose&#x60; limits | 
**mime_type** | **str** | Mime type; checked against &#x60;purpose&#x60; allowlist | 

## Example

```python
from aiand.models.create_upload_request import CreateUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUploadRequest from a JSON string
create_upload_request_instance = CreateUploadRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUploadRequest.to_json())

# convert the object into a dict
create_upload_request_dict = create_upload_request_instance.to_dict()
# create an instance of CreateUploadRequest from a dict
create_upload_request_from_dict = CreateUploadRequest.from_dict(create_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


