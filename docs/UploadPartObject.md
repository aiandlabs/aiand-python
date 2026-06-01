# UploadPartObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Stable part id with &#x60;part-&#x60; prefix | 
**object** | **str** |  | 
**upload_id** | **str** |  | 
**created_at** | **int** | Unix timestamp | 

## Example

```python
from aiand.models.upload_part_object import UploadPartObject

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPartObject from a JSON string
upload_part_object_instance = UploadPartObject.from_json(json)
# print the JSON string representation of the object
print(UploadPartObject.to_json())

# convert the object into a dict
upload_part_object_dict = upload_part_object_instance.to_dict()
# create an instance of UploadPartObject from a dict
upload_part_object_from_dict = UploadPartObject.from_dict(upload_part_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


