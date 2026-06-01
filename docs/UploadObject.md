# UploadObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Stable upload session id with &#x60;upload-&#x60; prefix | 
**object** | **str** |  | 
**bytes** | **int** | Declared total size of the file being uploaded | 
**created_at** | **int** | Unix timestamp | 
**expires_at** | **int** | Unix timestamp (1 hour from creation by default) | 
**filename** | **str** |  | 
**purpose** | **str** | One of &#x60;vision&#x60;, &#x60;video&#x60;, &#x60;audio&#x60;, or &#x60;document&#x60;. Determines size, MIME limits, and which models can reference the file. Optional for single-shot file uploads when the API can infer it from MIME type. | 
**status** | **str** |  | 
**file** | [**FileObject**](FileObject.md) | Populated once status is &#x60;completed&#x60; | 

## Example

```python
from aiand.models.upload_object import UploadObject

# TODO update the JSON string below
json = "{}"
# create an instance of UploadObject from a JSON string
upload_object_instance = UploadObject.from_json(json)
# print the JSON string representation of the object
print(UploadObject.to_json())

# convert the object into a dict
upload_object_dict = upload_object_instance.to_dict()
# create an instance of UploadObject from a dict
upload_object_from_dict = UploadObject.from_dict(upload_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


