# FileDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**deleted** | **bool** |  | 

## Example

```python
from aiand.models.file_deleted import FileDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of FileDeleted from a JSON string
file_deleted_instance = FileDeleted.from_json(json)
# print the JSON string representation of the object
print(FileDeleted.to_json())

# convert the object into a dict
file_deleted_dict = file_deleted_instance.to_dict()
# create an instance of FileDeleted from a dict
file_deleted_from_dict = FileDeleted.from_dict(file_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


