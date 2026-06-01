# aiand.FilesApi

All URIs are relative to *https://api.aiand.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /v1/files/{id} | Delete a file
[**get_file**](FilesApi.md#get_file) | **GET** /v1/files/{id} | Retrieve a file
[**get_file_content**](FilesApi.md#get_file_content) | **GET** /v1/files/{id}/content | Download file content
[**list_files**](FilesApi.md#list_files) | **GET** /v1/files | List files
[**upload_file**](FilesApi.md#upload_file) | **POST** /v1/files | Upload a file


# **delete_file**
> FileDeleted delete_file(id)

Delete a file

Soft-deletes the file row and best-effort removes the underlying R2 object.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.file_deleted import FileDeleted
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
    api_instance = aiand.FilesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a file
        api_response = api_instance.delete_file(id)
        print("The response of FilesApi->delete_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FileDeleted**](FileDeleted.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted file marker |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> FileObject get_file(id)

Retrieve a file

Returns metadata for a single file.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.file_object import FileObject
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
    api_instance = aiand.FilesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Retrieve a file
        api_response = api_instance.get_file(id)
        print("The response of FilesApi->get_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FileObject**](FileObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file&#39;s metadata |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_content**
> bytes get_file_content(id)

Download file content

Returns the raw bytes with `Content-Type` and `Content-Disposition` headers set from the upload metadata.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
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
    api_instance = aiand.FilesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Download file content
        api_response = api_instance.get_file_content(id)
        print("The response of FilesApi->get_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bytes**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file bytes |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> FileList list_files()

List files

Returns files in reverse-chronological order (newest first).

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.file_list import FileList
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
    api_instance = aiand.FilesApi(api_client)

    try:
        # List files
        api_response = api_instance.list_files()
        print("The response of FilesApi->list_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->list_files: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FileList**](FileList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of files |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FileObject upload_file(file, purpose=purpose)

Upload a file

Multipart form upload.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.file_object import FileObject
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
    api_instance = aiand.FilesApi(api_client)
    file = None # bytes | The asset bytes (multipart/form-data field)
    purpose = 'purpose_example' # str | One of `vision`, `video`, `audio`, or `document`. Determines size, MIME limits, and which models can reference the file. Optional for single-shot file uploads when the API can infer it from MIME type. (optional)

    try:
        # Upload a file
        api_response = api_instance.upload_file(file, purpose=purpose)
        print("The response of FilesApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**| The asset bytes (multipart/form-data field) | 
 **purpose** | **str**| One of &#x60;vision&#x60;, &#x60;video&#x60;, &#x60;audio&#x60;, or &#x60;document&#x60;. Determines size, MIME limits, and which models can reference the file. Optional for single-shot file uploads when the API can infer it from MIME type. | [optional] 

### Return type

[**FileObject**](FileObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The uploaded file&#39;s metadata |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

