# CompleteUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_ids** | **List[str]** | Ordered list of part ids returned by /parts | 
**md5** | **str** | Optional MD5 of the assembled file | [optional] 

## Example

```python
from aiand.models.complete_upload_request import CompleteUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteUploadRequest from a JSON string
complete_upload_request_instance = CompleteUploadRequest.from_json(json)
# print the JSON string representation of the object
print(CompleteUploadRequest.to_json())

# convert the object into a dict
complete_upload_request_dict = complete_upload_request_instance.to_dict()
# create an instance of CompleteUploadRequest from a dict
complete_upload_request_from_dict = CompleteUploadRequest.from_dict(complete_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


