# aiand.OpenaiApi

All URIs are relative to *https://api.aiand.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chat_completion**](OpenaiApi.md#create_chat_completion) | **POST** /v1/chat/completions | Create a chat completion
[**create_completion**](OpenaiApi.md#create_completion) | **POST** /v1/completions | Create a completion
[**create_response**](OpenaiApi.md#create_response) | **POST** /v1/responses | Create a response
[**list_models**](OpenaiApi.md#list_models) | **GET** /v1/models | List models


# **create_chat_completion**
> CreateChatCompletionResponse create_chat_completion(create_chat_completion_request=create_chat_completion_request)

Create a chat completion

Creates a chat completion for the provided messages and parameters.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.create_chat_completion_request import CreateChatCompletionRequest
from aiand.models.create_chat_completion_response import CreateChatCompletionResponse
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
    api_instance = aiand.OpenaiApi(api_client)
    create_chat_completion_request = aiand.CreateChatCompletionRequest() # CreateChatCompletionRequest | The request body for the chat completion (optional)

    try:
        # Create a chat completion
        api_response = api_instance.create_chat_completion(create_chat_completion_request=create_chat_completion_request)
        print("The response of OpenaiApi->create_chat_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->create_chat_completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_chat_completion_request** | [**CreateChatCompletionRequest**](CreateChatCompletionRequest.md)| The request body for the chat completion | [optional] 

### Return type

[**CreateChatCompletionResponse**](CreateChatCompletionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Insufficient Credits |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limited |  -  |
**500** | Internal Server Error |  -  |
**502** | Bad Gateway |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_completion**
> CreateCompletionResponse create_completion(create_completion_request=create_completion_request)

Create a completion

Creates a completion for the provided prompt and parameters. This is a legacy endpoint — use /v1/chat/completions for new integrations.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.create_completion_request import CreateCompletionRequest
from aiand.models.create_completion_response import CreateCompletionResponse
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
    api_instance = aiand.OpenaiApi(api_client)
    create_completion_request = aiand.CreateCompletionRequest() # CreateCompletionRequest | The request body for the completion (optional)

    try:
        # Create a completion
        api_response = api_instance.create_completion(create_completion_request=create_completion_request)
        print("The response of OpenaiApi->create_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->create_completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_completion_request** | [**CreateCompletionRequest**](CreateCompletionRequest.md)| The request body for the completion | [optional] 

### Return type

[**CreateCompletionResponse**](CreateCompletionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Insufficient Credits |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limited |  -  |
**500** | Internal Server Error |  -  |
**502** | Bad Gateway |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response**
> CreateResponseResponse create_response(create_response_request=create_response_request)

Create a response

Creates a response for the provided input and parameters.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.create_response_request import CreateResponseRequest
from aiand.models.create_response_response import CreateResponseResponse
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
    api_instance = aiand.OpenaiApi(api_client)
    create_response_request = aiand.CreateResponseRequest() # CreateResponseRequest | The request body for the response. (optional)

    try:
        # Create a response
        api_response = api_instance.create_response(create_response_request=create_response_request)
        print("The response of OpenaiApi->create_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->create_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_response_request** | [**CreateResponseRequest**](CreateResponseRequest.md)| The request body for the response. | [optional] 

### Return type

[**CreateResponseResponse**](CreateResponseResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Insufficient Credits |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limited |  -  |
**500** | Internal Server Error |  -  |
**502** | Bad Gateway |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_models**
> ListModels200Response list_models()

List models

Lists all active models with pricing.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import aiand
from aiand.models.list_models200_response import ListModels200Response
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
    api_instance = aiand.OpenaiApi(api_client)

    try:
        # List models
        api_response = api_instance.list_models()
        print("The response of OpenaiApi->list_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->list_models: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListModels200Response**](ListModels200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

