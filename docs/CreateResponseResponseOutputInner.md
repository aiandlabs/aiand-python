# CreateResponseResponseOutputInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**role** | **str** |  | 
**status** | **str** |  | 
**content** | [**List[CreateResponseResponseOutputInnerAnyOfContentInner]**](CreateResponseResponseOutputInnerAnyOfContentInner.md) |  | 
**call_id** | **str** |  | 
**name** | **str** |  | 
**arguments** | **str** |  | 
**summary** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from aiand.models.create_response_response_output_inner import CreateResponseResponseOutputInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseResponseOutputInner from a JSON string
create_response_response_output_inner_instance = CreateResponseResponseOutputInner.from_json(json)
# print the JSON string representation of the object
print(CreateResponseResponseOutputInner.to_json())

# convert the object into a dict
create_response_response_output_inner_dict = create_response_response_output_inner_instance.to_dict()
# create an instance of CreateResponseResponseOutputInner from a dict
create_response_response_output_inner_from_dict = CreateResponseResponseOutputInner.from_dict(create_response_response_output_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


