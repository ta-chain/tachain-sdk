# TachainSdk

Public integration endpoints. Set your own base URL and credential before calling.


## Source repository and local build

This package is distributed from its [standalone source repository](https://github.com/ta-chain/tachain-sdk-php). Its generated code is also maintained in the [SDK monorepo](https://github.com/ta-chain/tachain-sdk/tree/main/generated/php).

~~~sh
git clone https://github.com/ta-chain/tachain-sdk-php.git
cd tachain-sdk-php
composer install --no-interaction --prefer-dist
~~~

## Installation & Usage

### Requirements

PHP 8.1 and later.

### Composer

After version 0.1.1 is released on Packagist, install it with:

~~~sh
composer require ta-chain/tachain-sdk:0.1.1
~~~

Composer obtains the source from the [standalone PHP repository](https://github.com/ta-chain/tachain-sdk-php).

### Manual Installation

Download the files and include `autoload.php`:

```php
<?php
require_once('/path/to/TachainSdk/vendor/autoload.php');
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



// Configure API key authorization: ApiKey
$config = TachainSdk\Configuration::getDefaultConfiguration()->setApiKey('X-API-Key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = TachainSdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-Key', 'Bearer');

// Configure API key authorization: Signature
$config = TachainSdk\Configuration::getDefaultConfiguration()->setApiKey('X-Signature', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = TachainSdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-Signature', 'Bearer');

// Configure Bearer authorization: BearerToken
$config = TachainSdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure API key authorization: Timestamp
$config = TachainSdk\Configuration::getDefaultConfiguration()->setApiKey('X-Timestamp', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = TachainSdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-Timestamp', 'Bearer');


$apiInstance = new TachainSdk\Api\ApiDeclarationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$x_credential_type = 'x_credential_type_example'; // string | Use 'Token' with bearer authorization, or 'API Key' with signed API key headers. This header is mandatory in the deployed API.
$attachment_id = 'attachment_id_example'; // string | 查询返回的附件申报记录标识；也可在 Body 按单据和资料类型删除。
$form_data_id = 'form_data_id_example'; // string | 查询返回的表单记录标识；也可在 Body 按业务键删除。
$tactic_chain_api_service_controllers_api_integration_v1_api_declaration_delete_request = {"stageId":"Order","orderSide":"SO","supplierExtNo":"ERP-SO-001-10","customerName":"客户名称","documentTypeCode":"INVOICE","deleteAttachments":true,"deleteForms":false}; // \TachainSdk\Model\TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest

try {
    $result = $apiInstance->deleteV1DeclarationDelete($x_credential_type, $attachment_id, $form_data_id, $tactic_chain_api_service_controllers_api_integration_v1_api_declaration_delete_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ApiDeclarationApi->deleteV1DeclarationDelete: ', $e->getMessage(), PHP_EOL;
}

```

## API Endpoints

All URIs are relative to *https://api.example.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiDeclarationApi* | [**deleteV1DeclarationDelete**](docs/Api/ApiDeclarationApi.md#deletev1declarationdelete) | **DELETE** /v1/declaration/Delete | 申报信息删除接口。
*ApiDeclarationApi* | [**getV1DeclarationListPaging**](docs/Api/ApiDeclarationApi.md#getv1declarationlistpaging) | **GET** /v1/declaration/ListPaging | 申报信息查询接口。
*ApiDeclarationApi* | [**getV1DeclarationRequiredDocuments**](docs/Api/ApiDeclarationApi.md#getv1declarationrequireddocuments) | **GET** /v1/declaration/RequiredDocuments | 单据所需申报信息查询接口。
*ApiDeclarationApi* | [**postV1DeclarationSubmit**](docs/Api/ApiDeclarationApi.md#postv1declarationsubmit) | **POST** /v1/declaration/Submit | 申报文件/表单提交接口。
*ApiDeclarationUploadApi* | [**postV1DeclarationUploadFile**](docs/Api/ApiDeclarationUploadApi.md#postv1declarationuploadfile) | **POST** /v1/declaration/UploadFile | 上传申报文件，返回 FileId；文件内容最多 30 MiB。
*ApiDeliveryApi* | [**deleteV1DeliveryDelete**](docs/Api/ApiDeliveryApi.md#deletev1deliverydelete) | **DELETE** /v1/delivery/Delete | 删除发货单。
*ApiDeliveryApi* | [**getV1DeliveryListPaging**](docs/Api/ApiDeliveryApi.md#getv1deliverylistpaging) | **GET** /v1/delivery/ListPaging | 查询发货单信息及明细信息。
*ApiDeliveryApi* | [**getV1DeliveryReceiptListPaging**](docs/Api/ApiDeliveryApi.md#getv1deliveryreceiptlistpaging) | **GET** /v1/delivery/ReceiptListPaging | 查询收货单集合，核对收货信息。
*ApiDeliveryApi* | [**postV1DeliveryCreate**](docs/Api/ApiDeliveryApi.md#postv1deliverycreate) | **POST** /v1/delivery/Create | 创建发货单。
*ApiDeliveryApi* | [**putV1DeliveryConfirmReceipt**](docs/Api/ApiDeliveryApi.md#putv1deliveryconfirmreceipt) | **PUT** /v1/delivery/ConfirmReceipt | 确认收货。
*ApiDeliveryApi* | [**putV1DeliveryReturnReceipt**](docs/Api/ApiDeliveryApi.md#putv1deliveryreturnreceipt) | **PUT** /v1/delivery/ReturnReceipt | 收货退回。
*ApiDeliveryApi* | [**putV1DeliveryUpdate**](docs/Api/ApiDeliveryApi.md#putv1deliveryupdate) | **PUT** /v1/delivery/Update | 修改发货单。
*ApiEnumApi* | [**getV1EnumGetList**](docs/Api/ApiEnumApi.md#getv1enumgetlist) | **GET** /v1/enum/GetList | 第三方-获取统一枚举列表（支持批量查询/查询所有）
*ApiMaterialApi* | [**deleteV1MaterialDelete**](docs/Api/ApiMaterialApi.md#deletev1materialdelete) | **DELETE** /v1/material/Delete | 删除未被使用的资料；软删除，已被订单等业务使用时返回业务错误。
*ApiMaterialApi* | [**getV1MaterialGet**](docs/Api/ApiMaterialApi.md#getv1materialget) | **GET** /v1/material/Get | 按编码或 ID 精确查询。
*ApiMaterialApi* | [**getV1MaterialListPaging**](docs/Api/ApiMaterialApi.md#getv1materiallistpaging) | **GET** /v1/material/ListPaging | 分页查询；searchText 搜索编码或名称，scopeCode 按加工阶段筛选。
*ApiMaterialApi* | [**postV1MaterialCreate**](docs/Api/ApiMaterialApi.md#postv1materialcreate) | **POST** /v1/material/Create | 创建原料资料。
*ApiMaterialApi* | [**putV1MaterialUpdate**](docs/Api/ApiMaterialApi.md#putv1materialupdate) | **PUT** /v1/material/Update | 完整修改原料资料。
*ApiOrderApi* | [**deleteV1OrderDelete**](docs/Api/ApiOrderApi.md#deletev1orderdelete) | **DELETE** /v1/order/Delete | 第三方-更新订单状态（通过匹配条件获取订单ID）
*ApiOrderApi* | [**deleteV1OrderDeleteLine**](docs/Api/ApiOrderApi.md#deletev1orderdeleteline) | **DELETE** /v1/order/DeleteLine | 第三方-更新订单明细状态（通过匹配条件获取明细ID）
*ApiOrderApi* | [**getV1OrderPOListPaging**](docs/Api/ApiOrderApi.md#getv1orderpolistpaging) | **GET** /v1/order/POListPaging | 第三方-获取采购订单分页列表（含明细）
*ApiOrderApi* | [**getV1OrderSOListPaging**](docs/Api/ApiOrderApi.md#getv1ordersolistpaging) | **GET** /v1/order/SOListPaging | 第三方-获取销售订单分页列表（含明细）
*ApiOrderApi* | [**postV1OrderCreate**](docs/Api/ApiOrderApi.md#postv1ordercreate) | **POST** /v1/order/Create | 第三方-创建订单（含明细）
*ApiOrderApi* | [**postV1OrderSoAccept**](docs/Api/ApiOrderApi.md#postv1ordersoaccept) | **POST** /v1/order/SoAccept | 第三方-销售订单接单（支持绑定成品/自动创建成品）
*ApiOrderApi* | [**putV1OrderUpdate**](docs/Api/ApiOrderApi.md#putv1orderupdate) | **PUT** /v1/order/Update | 第三方-更新订单（部分字段）
*ApiOrderWorkflowApi* | [**getV1OrderReceiptPending**](docs/Api/ApiOrderWorkflowApi.md#getv1orderreceiptpending) | **GET** /v1/order/ReceiptPending | 采购订单确认收货待办项查询。
*ApiOrderWorkflowApi* | [**postV1OrderDeclarationVerification**](docs/Api/ApiOrderWorkflowApi.md#postv1orderdeclarationverification) | **POST** /v1/order/DeclarationVerification | 销售订单提交审核前一键校验。
*ApiOrderWorkflowApi* | [**postV1OrderSubmitAudit**](docs/Api/ApiOrderWorkflowApi.md#postv1ordersubmitaudit) | **POST** /v1/order/SubmitAudit | 销售方根据已入库的订单、生产、发货及申报资料提交审核。
*ApiOrderWorkflowApi* | [**putV1OrderConfirmReceipt**](docs/Api/ApiOrderWorkflowApi.md#putv1orderconfirmreceipt) | **PUT** /v1/order/ConfirmReceipt | 采购方按整单或单条订单明细确认收货。
*ApiProcessRouteApi* | [**deleteV1ProcessRouteDelete**](docs/Api/ApiProcessRouteApi.md#deletev1processroutedelete) | **DELETE** /v1/processRoute/Delete | 软删除加工路线；历史单据保持其已有引用，新建业务不可再选择该路线。
*ApiProcessRouteApi* | [**getV1ProcessRouteGet**](docs/Api/ApiProcessRouteApi.md#getv1processrouteget) | **GET** /v1/processRoute/Get | 按路线编码或查询返回的 ID 精确查询，两者同时传入须一致。
*ApiProcessRouteApi* | [**getV1ProcessRouteListPaging**](docs/Api/ApiProcessRouteApi.md#getv1processroutelistpaging) | **GET** /v1/processRoute/ListPaging | 分页查询正常路线；searchText 匹配编码或名称，scopeCode 筛选加工阶段。
*ApiProcessRouteApi* | [**postV1ProcessRouteCreate**](docs/Api/ApiProcessRouteApi.md#postv1processroutecreate) | **POST** /v1/processRoute/Create | 创建加工路线及有序工序。
*ApiProcessRouteApi* | [**putV1ProcessRouteUpdate**](docs/Api/ApiProcessRouteApi.md#putv1processrouteupdate) | **PUT** /v1/processRoute/Update | 完整修改路线；steps 省略保留原工序，数组则替换全部工序，空数组清空。
*ApiProductApi* | [**deleteV1ProductDelete**](docs/Api/ApiProductApi.md#deletev1productdelete) | **DELETE** /v1/product/Delete | 删除未被使用的资料；软删除，已被订单等业务使用时返回业务错误。
*ApiProductApi* | [**getV1ProductGet**](docs/Api/ApiProductApi.md#getv1productget) | **GET** /v1/product/Get | 按编码或 ID 精确查询。
*ApiProductApi* | [**getV1ProductListPaging**](docs/Api/ApiProductApi.md#getv1productlistpaging) | **GET** /v1/product/ListPaging | 分页查询；searchText 搜索编码或名称，scopeCode 按加工阶段筛选。
*ApiProductApi* | [**postV1ProductCreate**](docs/Api/ApiProductApi.md#postv1productcreate) | **POST** /v1/product/Create | 创建成品资料。
*ApiProductApi* | [**putV1ProductUpdate**](docs/Api/ApiProductApi.md#putv1productupdate) | **PUT** /v1/product/Update | 完整修改成品资料。
*ApiProductionApi* | [**deleteV1ProductionDelete**](docs/Api/ApiProductionApi.md#deletev1productiondelete) | **DELETE** /v1/production/Delete | 删除生产记录单。
*ApiProductionApi* | [**getV1ProductionListPaging**](docs/Api/ApiProductionApi.md#getv1productionlistpaging) | **GET** /v1/production/ListPaging | 查询生产记录单及详细领料信息。
*ApiProductionApi* | [**postV1ProductionCreate**](docs/Api/ApiProductionApi.md#postv1productioncreate) | **POST** /v1/production/Create | 创建生产记录单。
*ApiProductionApi* | [**putV1ProductionUpdate**](docs/Api/ApiProductionApi.md#putv1productionupdate) | **PUT** /v1/production/Update | 修改生产记录单。
*ApiReferenceApi* | [**getV1ReferenceEnumValues**](docs/Api/ApiReferenceApi.md#getv1referenceenumvalues) | **GET** /v1/reference/EnumValues | 查询 enum_value；EnumTypeId 必填，Value 可选精确匹配。
*ApiReferenceApi* | [**getV1ReferenceMappings**](docs/Api/ApiReferenceApi.md#getv1referencemappings) | **GET** /v1/reference/Mappings | 查询 external_mapping；MappedTable 必填，ExternalValue 可选精确匹配。

## Models

- [DeleteV1DeclarationDelete200Response](docs/Model/DeleteV1DeclarationDelete200Response.md)
- [GetV1DeclarationListPaging200Response](docs/Model/GetV1DeclarationListPaging200Response.md)
- [GetV1DeclarationRequiredDocuments200Response](docs/Model/GetV1DeclarationRequiredDocuments200Response.md)
- [GetV1DeliveryListPaging200Response](docs/Model/GetV1DeliveryListPaging200Response.md)
- [GetV1EnumGetList200Response](docs/Model/GetV1EnumGetList200Response.md)
- [GetV1MaterialListPaging200Response](docs/Model/GetV1MaterialListPaging200Response.md)
- [GetV1OrderPOListPaging200Response](docs/Model/GetV1OrderPOListPaging200Response.md)
- [GetV1OrderReceiptPending200Response](docs/Model/GetV1OrderReceiptPending200Response.md)
- [GetV1ProcessRouteListPaging200Response](docs/Model/GetV1ProcessRouteListPaging200Response.md)
- [GetV1ProductListPaging200Response](docs/Model/GetV1ProductListPaging200Response.md)
- [GetV1ProductionListPaging200Response](docs/Model/GetV1ProductionListPaging200Response.md)
- [GetV1ReferenceEnumValues200Response](docs/Model/GetV1ReferenceEnumValues200Response.md)
- [GetV1ReferenceMappings200Response](docs/Model/GetV1ReferenceMappings200Response.md)
- [Model1](docs/Model/Model1.md)
- [Model2](docs/Model/Model2.md)
- [Model3](docs/Model/Model3.md)
- [Model4](docs/Model/Model4.md)
- [PostV1DeclarationSubmit200Response](docs/Model/PostV1DeclarationSubmit200Response.md)
- [PostV1DeclarationUploadFile200Response](docs/Model/PostV1DeclarationUploadFile200Response.md)
- [PostV1MaterialCreate200Response](docs/Model/PostV1MaterialCreate200Response.md)
- [PostV1OrderCreate200Response](docs/Model/PostV1OrderCreate200Response.md)
- [PostV1OrderDeclarationVerification200Response](docs/Model/PostV1OrderDeclarationVerification200Response.md)
- [PostV1OrderSubmitAudit200Response](docs/Model/PostV1OrderSubmitAudit200Response.md)
- [PostV1ProcessRouteCreate200Response](docs/Model/PostV1ProcessRouteCreate200Response.md)
- [PostV1ProductCreate200Response](docs/Model/PostV1ProductCreate200Response.md)
- [PostV1ProductionCreate200Response](docs/Model/PostV1ProductionCreate200Response.md)
- [PutV1DeliveryConfirmReceipt200Response](docs/Model/PutV1DeliveryConfirmReceipt200Response.md)
- [PutV1DeliveryReturnReceipt200Response](docs/Model/PutV1DeliveryReturnReceipt200Response.md)
- [PutV1OrderConfirmReceipt200Response](docs/Model/PutV1OrderConfirmReceipt200Response.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiBomLineRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiBomLineRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiBomLineResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiBomLineResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiCatalogDeleteRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiCatalogDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationAttachmentResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationAttachmentResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDocumentRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDocumentRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFileRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFileRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFormRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFormRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFormResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFormResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryCreateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDeleteRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailCreateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailUpdateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryUpdateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDocumentFormResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDocumentFormResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDocumentTypeResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDocumentTypeResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiEnumValueResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiEnumValueResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiErrorResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiErrorResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiFiberCompositionRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiFiberCompositionRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiFiberCompositionResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiFiberCompositionResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiFileResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiFileResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiFileUploadResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiFileUploadResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiMappingResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiMappingResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiMaterialCreateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiMaterialCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiMaterialUpdateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiMaterialUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderAcceptRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderAcceptRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderConfirmReceiptRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderConfirmReceiptRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderCreateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeleteLineRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeleteLineRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeleteRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineCreateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineUpdateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingLineResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingLineResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptResult](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptResult.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderUpdateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteCreateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteUpdateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProcessStepRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProcessStepRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProcessStepResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProcessStepResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductCreateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductUpdateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionCreateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductionCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionDeleteRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductionDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialCreateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialUpdateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderCreateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderUpdateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionUpdateRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiProductionUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiReceiptPendingItemResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiReceiptPendingItemResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiReferencePageResponse1TacticChainApiServiceControllersApiIntegrationV1ApiEnumValueResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiReferencePageResponse1TacticChainApiServiceControllersApiIntegrationV1ApiEnumValueResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiReferencePageResponse1TacticChainApiServiceControllersApiIntegrationV1ApiMappingResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiReferencePageResponse1TacticChainApiServiceControllersApiIntegrationV1ApiMappingResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1SystemStringSystemPrivateCoreLibVersion9000CultureNeutralPublicKeyToken7cec85d7bea7798e](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1SystemStringSystemPrivateCoreLibVersion9000CultureNeutralPublicKeyToken7cec85d7bea7798e.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiFileUploadResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiFileUploadResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptResultTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptResultTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiVerificationFileResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiVerificationFileResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiVerificationResponse](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiVerificationResponse.md)

## Authorization

Authentication schemes defined for the API:
### BearerToken

- **Type**: Bearer authentication

### ApiKey

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


### Timestamp

- **Type**: API key
- **API key parameter name**: X-Timestamp
- **Location**: HTTP header


### Signature

- **Type**: API key
- **API key parameter name**: X-Signature
- **Location**: HTTP header


## Tests

To run the tests, use:

```bash
composer install
vendor/bin/phpunit
```

## Author



## About this package

This PHP package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `1.0.0`
    - Package version: `0.1.1`
    - Generator version: `7.25.0`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`
