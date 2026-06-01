# aiand.UploadsApi

All URIs are relative to *https://api.aiand.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_upload_part**](UploadsApi.md#add_upload_part) | **POST** /v1/uploads/{id}/parts | Add a part to an upload
[**cancel_upload**](UploadsApi.md#cancel_upload) | **POST** /v1/uploads/{id}/cancel | Cancel an upload
[**complete_upload**](UploadsApi.md#complete_upload) | **POST** /v1/uploads/{id}/complete | Complete an upload
[**create_upload**](UploadsApi.md#create_upload) | **POST** /v1/uploads | Create an upload session


# **add_upload_part**
> UploadPartObject add_upload_part(id, data)

Add a part to an upload

Uploads up to 64 MB of bytes as one part of a pending session. Parts must be added in order — completing the upload submits them in the order returned to the client.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.upload_part_object import UploadPartObject
from aiand.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aiand.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aiand.Configuration(
    host = "https://api.aiand.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = aiand.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aiand.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiand.UploadsApi(api_client)
    id = 'id_example' # str | 
    data = None # bytes | Bytes for this part (multipart/form-data field), max 64 MB

    try:
        # Add a part to an upload
        api_response = api_instance.add_upload_part(id, data)
        print("The response of UploadsApi->add_upload_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->add_upload_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | **bytes**| Bytes for this part (multipart/form-data field), max 64 MB | 

### Return type

[**UploadPartObject**](UploadPartObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The part record |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_upload**
> UploadObject cancel_upload(id)

Cancel an upload

Aborts the underlying R2 multipart upload and marks the session `cancelled`. Idempotent — already-completed or already-cancelled sessions return 404.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.upload_object import UploadObject
from aiand.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aiand.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aiand.Configuration(
    host = "https://api.aiand.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = aiand.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aiand.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiand.UploadsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Cancel an upload
        api_response = api_instance.cancel_upload(id)
        print("The response of UploadsApi->cancel_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->cancel_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UploadObject**](UploadObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cancelled upload |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_upload**
> UploadObject complete_upload(id, complete_upload_request=complete_upload_request)

Complete an upload

Assembles the listed parts in order and materializes the upload as a regular `file-...` object referenced via the returned `file` field.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.complete_upload_request import CompleteUploadRequest
from aiand.models.upload_object import UploadObject
from aiand.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aiand.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aiand.Configuration(
    host = "https://api.aiand.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = aiand.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aiand.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiand.UploadsApi(api_client)
    id = 'id_example' # str | 
    complete_upload_request = aiand.CompleteUploadRequest() # CompleteUploadRequest | Ordered part_ids to assemble (optional)

    try:
        # Complete an upload
        api_response = api_instance.complete_upload(id, complete_upload_request=complete_upload_request)
        print("The response of UploadsApi->complete_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->complete_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **complete_upload_request** | [**CompleteUploadRequest**](CompleteUploadRequest.md)| Ordered part_ids to assemble | [optional] 

### Return type

[**UploadObject**](UploadObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The completed upload, with &#x60;file&#x60; populated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload**
> UploadObject create_upload(create_upload_request=create_upload_request)

Create an upload session

Creates a chunked upload session for files larger than the single-shot `/v1/files` cap. Sessions expire 1 hour after creation.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.create_upload_request import CreateUploadRequest
from aiand.models.upload_object import UploadObject
from aiand.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aiand.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aiand.Configuration(
    host = "https://api.aiand.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = aiand.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aiand.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiand.UploadsApi(api_client)
    create_upload_request = aiand.CreateUploadRequest() # CreateUploadRequest | Upload metadata declared up front (optional)

    try:
        # Create an upload session
        api_response = api_instance.create_upload(create_upload_request=create_upload_request)
        print("The response of UploadsApi->create_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->create_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_upload_request** | [**CreateUploadRequest**](CreateUploadRequest.md)| Upload metadata declared up front | [optional] 

### Return type

[**UploadObject**](UploadObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upload session in &#x60;pending&#x60; status |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

