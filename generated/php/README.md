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

Install version 0.1.0 from Packagist:

~~~sh
composer require ta-chain/tachain-sdk:0.1.0
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
$attachment_id = 'attachment_id_example'; // string | query 方式传入的单个附件申报 ID。
$form_data_id = 'form_data_id_example'; // string | query 方式传入的单个表单申报 ID。
$tactic_chain_api_service_controllers_api_integration_v1_api_declaration_delete_request = new \TachainSdk\Model\TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest(); // \TachainSdk\Model\TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest

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
*ApiDeliveryApi* | [**deleteV1DeliveryDelete**](docs/Api/ApiDeliveryApi.md#deletev1deliverydelete) | **DELETE** /v1/delivery/Delete | 删除发货单。
*ApiDeliveryApi* | [**getV1DeliveryListPaging**](docs/Api/ApiDeliveryApi.md#getv1deliverylistpaging) | **GET** /v1/delivery/ListPaging | 查询发货单信息及明细信息。
*ApiDeliveryApi* | [**getV1DeliveryReceiptListPaging**](docs/Api/ApiDeliveryApi.md#getv1deliveryreceiptlistpaging) | **GET** /v1/delivery/ReceiptListPaging | 查询收货单集合，核对收货信息。
*ApiDeliveryApi* | [**postV1DeliveryCreate**](docs/Api/ApiDeliveryApi.md#postv1deliverycreate) | **POST** /v1/delivery/Create | 创建发货单。
*ApiDeliveryApi* | [**putV1DeliveryConfirmReceipt**](docs/Api/ApiDeliveryApi.md#putv1deliveryconfirmreceipt) | **PUT** /v1/delivery/ConfirmReceipt | 确认收货。
*ApiDeliveryApi* | [**putV1DeliveryReturnReceipt**](docs/Api/ApiDeliveryApi.md#putv1deliveryreturnreceipt) | **PUT** /v1/delivery/ReturnReceipt | 收货退回。
*ApiDeliveryApi* | [**putV1DeliveryUpdate**](docs/Api/ApiDeliveryApi.md#putv1deliveryupdate) | **PUT** /v1/delivery/Update | 修改发货单。
*ApiEnumApi* | [**getV1EnumGetList**](docs/Api/ApiEnumApi.md#getv1enumgetlist) | **GET** /v1/enum/GetList | 第三方-获取统一枚举列表（支持批量查询/查询所有）
*ApiOrderApi* | [**deleteV1OrderDelete**](docs/Api/ApiOrderApi.md#deletev1orderdelete) | **DELETE** /v1/order/Delete | 第三方-更新订单状态（通过匹配条件获取订单ID）
*ApiOrderApi* | [**deleteV1OrderDeleteLine**](docs/Api/ApiOrderApi.md#deletev1orderdeleteline) | **DELETE** /v1/order/DeleteLine | 第三方-更新订单明细状态（通过匹配条件获取明细ID）
*ApiOrderApi* | [**getV1OrderPOListPaging**](docs/Api/ApiOrderApi.md#getv1orderpolistpaging) | **GET** /v1/order/POListPaging | 第三方-获取采购订单分页列表（含明细）
*ApiOrderApi* | [**getV1OrderSOListPaging**](docs/Api/ApiOrderApi.md#getv1ordersolistpaging) | **GET** /v1/order/SOListPaging | 第三方-获取销售订单分页列表（含明细）
*ApiOrderApi* | [**postV1OrderCreate**](docs/Api/ApiOrderApi.md#postv1ordercreate) | **POST** /v1/order/Create | 第三方-创建订单（含明细）
*ApiOrderApi* | [**postV1OrderSoAccept**](docs/Api/ApiOrderApi.md#postv1ordersoaccept) | **POST** /v1/order/SoAccept | 第三方-销售订单接单（支持绑定成品/自动创建成品）
*ApiOrderApi* | [**putV1OrderUpdate**](docs/Api/ApiOrderApi.md#putv1orderupdate) | **PUT** /v1/order/Update | 第三方-更新订单（部分字段）
*ApiOrderWorkflowApi* | [**postV1OrderSubmitAudit**](docs/Api/ApiOrderWorkflowApi.md#postv1ordersubmitaudit) | **POST** /v1/order/SubmitAudit | 销售方根据已入库的订单、生产、发货及申报资料提交审核。
*ApiOrderWorkflowApi* | [**putV1OrderConfirmReceipt**](docs/Api/ApiOrderWorkflowApi.md#putv1orderconfirmreceipt) | **PUT** /v1/order/ConfirmReceipt | 采购方按整单或单条订单明细确认收货。
*ApiProductionApi* | [**deleteV1ProductionDelete**](docs/Api/ApiProductionApi.md#deletev1productiondelete) | **DELETE** /v1/production/Delete | 删除生产记录单。
*ApiProductionApi* | [**getV1ProductionListPaging**](docs/Api/ApiProductionApi.md#getv1productionlistpaging) | **GET** /v1/production/ListPaging | 查询生产记录单及详细领料信息。
*ApiProductionApi* | [**postV1ProductionCreate**](docs/Api/ApiProductionApi.md#postv1productioncreate) | **POST** /v1/production/Create | 创建生产记录单。
*ApiProductionApi* | [**putV1ProductionUpdate**](docs/Api/ApiProductionApi.md#putv1productionupdate) | **PUT** /v1/production/Update | 修改生产记录单。

## Models

- [GetV1EnumGetList200Response](docs/Model/GetV1EnumGetList200Response.md)
- [MicrosoftAspNetCoreMvcProblemDetails](docs/Model/MicrosoftAspNetCoreMvcProblemDetails.md)
- [Model1](docs/Model/Model1.md)
- [Model3](docs/Model/Model3.md)
- [Model4](docs/Model/Model4.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDocumentRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDocumentRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListDto](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListDto.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResultDto](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResultDto.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiIntegrationDeleteRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiIntegrationDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderConfirmReceiptRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderConfirmReceiptRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditRequest](docs/Model/TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditRequest.md)
- [TacticChainApiServiceDataEntitiesCompany](docs/Model/TacticChainApiServiceDataEntitiesCompany.md)
- [TacticChainApiServiceDataEntitiesCompanyComplianceProfile](docs/Model/TacticChainApiServiceDataEntitiesCompanyComplianceProfile.md)
- [TacticChainApiServiceDataEntitiesCompanyUtilityDeclaration](docs/Model/TacticChainApiServiceDataEntitiesCompanyUtilityDeclaration.md)
- [TacticChainApiServiceDataEntitiesCustomer](docs/Model/TacticChainApiServiceDataEntitiesCustomer.md)
- [TacticChainApiServiceDataEntitiesFactory](docs/Model/TacticChainApiServiceDataEntitiesFactory.md)
- [TacticChainApiServiceDataEntitiesOrder](docs/Model/TacticChainApiServiceDataEntitiesOrder.md)
- [TacticChainApiServiceDataEntitiesOrderLine](docs/Model/TacticChainApiServiceDataEntitiesOrderLine.md)
- [TacticChainApiServiceDataEntitiesSupplier](docs/Model/TacticChainApiServiceDataEntitiesSupplier.md)
- [TacticChainApiServiceDataEntitiesSupplierOnboardingExt](docs/Model/TacticChainApiServiceDataEntitiesSupplierOnboardingExt.md)
- [TacticChainApiServiceDataEntitiesTrader](docs/Model/TacticChainApiServiceDataEntitiesTrader.md)
- [TacticChainApiServiceHelperResultApiEnum](docs/Model/TacticChainApiServiceHelperResultApiEnum.md)
- [TacticChainApiServiceHelperResultBrandReportAllocatedDeliveryKpiDetail](docs/Model/TacticChainApiServiceHelperResultBrandReportAllocatedDeliveryKpiDetail.md)
- [TacticChainApiServiceHelperResultBrandReportUnlinkedOrderDetail](docs/Model/TacticChainApiServiceHelperResultBrandReportUnlinkedOrderDetail.md)
- [TacticChainApiServiceHelperResultKpiArchivedDataChangeDetail](docs/Model/TacticChainApiServiceHelperResultKpiArchivedDataChangeDetail.md)
- [TacticChainApiServiceHelperResultMappingOrderSelect](docs/Model/TacticChainApiServiceHelperResultMappingOrderSelect.md)
- [TacticChainApiServiceHelperResultOrderTraceReport](docs/Model/TacticChainApiServiceHelperResultOrderTraceReport.md)
- [TacticChainApiServiceHelperTemplateDtoBusinessRiskWarnInfoDto](docs/Model/TacticChainApiServiceHelperTemplateDtoBusinessRiskWarnInfoDto.md)
- [TacticChainApiServiceHelperTemplateDtoMultiSoLineCompleteStatus](docs/Model/TacticChainApiServiceHelperTemplateDtoMultiSoLineCompleteStatus.md)
- [TacticChainApiServiceModelsBrandKpiPolicyResult](docs/Model/TacticChainApiServiceModelsBrandKpiPolicyResult.md)
- [TacticChainApiServiceModelsBrandOrderKpiSnapshotDto](docs/Model/TacticChainApiServiceModelsBrandOrderKpiSnapshotDto.md)
- [TacticChainApiServiceModelsBrandOrderSupplierOrderSnapshotDto](docs/Model/TacticChainApiServiceModelsBrandOrderSupplierOrderSnapshotDto.md)
- [TacticChainApiServiceModelsBrandOrderUncompletedDeclareSnapshotDto](docs/Model/TacticChainApiServiceModelsBrandOrderUncompletedDeclareSnapshotDto.md)
- [TacticChainApiServiceModelsOrderStageFormDto](docs/Model/TacticChainApiServiceModelsOrderStageFormDto.md)
- [TacticChainApiServiceModelsProductBomGroupingDto](docs/Model/TacticChainApiServiceModelsProductBomGroupingDto.md)
- [TacticChainApiServiceModelsProductionRawMaterialDto](docs/Model/TacticChainApiServiceModelsProductionRawMaterialDto.md)
- [TacticChainApiServiceViewModelsAttachmentInApiCreateDto](docs/Model/TacticChainApiServiceViewModelsAttachmentInApiCreateDto.md)
- [TacticChainApiServiceViewModelsAttachmentInApiDto](docs/Model/TacticChainApiServiceViewModelsAttachmentInApiDto.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1SystemStringSystemPrivateCoreLibVersion9000CultureNeutralPublicKeyToken7cec85d7bea7798e](docs/Model/TacticChainApiServiceViewModelsCommonApiResponse1SystemStringSystemPrivateCoreLibVersion9000CultureNeutralPublicKeyToken7cec85d7bea7798e.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResultDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResultDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsDeliveryNoteApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsDeliveryNoteApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsOrderApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsOrderApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsProductionApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsProductionApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsDeliveryNoteApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsDeliveryNoteApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsOrderApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsOrderApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsProductionApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/Model/TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsProductionApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsDeliveryNoteApiDto](docs/Model/TacticChainApiServiceViewModelsDeliveryNoteApiDto.md)
- [TacticChainApiServiceViewModelsDeliveryNoteDetailApiDto](docs/Model/TacticChainApiServiceViewModelsDeliveryNoteDetailApiDto.md)
- [TacticChainApiServiceViewModelsDocumentTypeApiDto](docs/Model/TacticChainApiServiceViewModelsDocumentTypeApiDto.md)
- [TacticChainApiServiceViewModelsOrderApiDto](docs/Model/TacticChainApiServiceViewModelsOrderApiDto.md)
- [TacticChainApiServiceViewModelsOrderLineApiDto](docs/Model/TacticChainApiServiceViewModelsOrderLineApiDto.md)
- [TacticChainApiServiceViewModelsOrderStageFormApiDto](docs/Model/TacticChainApiServiceViewModelsOrderStageFormApiDto.md)
- [TacticChainApiServiceViewModelsOrderStageFormDatumApiDto](docs/Model/TacticChainApiServiceViewModelsOrderStageFormDatumApiDto.md)
- [TacticChainApiServiceViewModelsProductionApiDto](docs/Model/TacticChainApiServiceViewModelsProductionApiDto.md)
- [TacticChainApiServiceViewModelsProductionRawMaterialApiDto](docs/Model/TacticChainApiServiceViewModelsProductionRawMaterialApiDto.md)
- [TacticChainApiServiceViewModelsProductionSalesOrderApiDto](docs/Model/TacticChainApiServiceViewModelsProductionSalesOrderApiDto.md)
- [TacticChainApiServiceViewModelsStageAttachmentApiDto](docs/Model/TacticChainApiServiceViewModelsStageAttachmentApiDto.md)

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
    - Package version: `0.1.0`
    - Generator version: `7.25.0`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`
