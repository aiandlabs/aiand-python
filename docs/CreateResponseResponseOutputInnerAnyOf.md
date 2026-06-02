# CreateResponseResponseOutputInnerAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**role** | **str** |  | 
**status** | **str** |  | 
**content** | [**List[CreateResponseResponseOutputInnerAnyOfContentInner]**](CreateResponseResponseOutputInnerAnyOfContentInner.md) |  | 

## Example

```python
from aiand.models.create_response_response_output_inner_any_of import CreateResponseResponseOutputInnerAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseResponseOutputInnerAnyOf from a JSON string
create_response_response_output_inner_any_of_instance = CreateResponseResponseOutputInnerAnyOf.from_json(json)
# print the JSON string representation of the object
print(CreateResponseResponseOutputInnerAnyOf.to_json())

# convert the object into a dict
create_response_response_output_inner_any_of_dict = create_response_response_output_inner_any_of_instance.to_dict()
# create an instance of CreateResponseResponseOutputInnerAnyOf from a dict
create_response_response_output_inner_any_of_from_dict = CreateResponseResponseOutputInnerAnyOf.from_dict(create_response_response_output_inner_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


