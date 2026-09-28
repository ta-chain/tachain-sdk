# @ta-chain/tachain-sdk@0.1.0

A TypeScript SDK client for the api.example.com API.

## Usage

First, install the SDK from npm.

```bash
npm install @ta-chain/tachain-sdk --save
```

Next, try it out.


```ts
import {
  Configuration,
  ApiDeclarationApi,
} from '@ta-chain/tachain-sdk';
import type { DeleteV1DeclarationDeleteRequest } from '@ta-chain/tachain-sdk';

async function example() {
  console.log("🚀 Testing @ta-chain/tachain-sdk SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKey
    apiKey: "YOUR API KEY",
    // To configure API key authorization: Signature
    apiKey: "YOUR API KEY",
    // Configure HTTP bearer authorization: BearerToken
    accessToken: "YOUR BEARER TOKEN",
    // To configure API key authorization: Timestamp
    apiKey: "YOUR API KEY",
  });
  const api = new ApiDeclarationApi(config);

  const body = {
    // 'Token' | 'API Key' | Use \'Token\' with bearer authorization, or \'API Key\' with signed API key headers. This header is mandatory in the deployed API.
    xCredentialType: xCredentialType_example,
    // string | query 方式传入的单个附件申报 ID。 (optional)
    attachmentId: attachmentId_example,
    // string | query 方式传入的单个表单申报 ID。 (optional)
    formDataId: formDataId_example,
    // TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest (optional)
    tacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest: ...,
  } satisfies DeleteV1DeclarationDeleteRequest;

  try {
    const data = await api.deleteV1DeclarationDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```


## Documentation

### API Endpoints

All URIs are relative to *https://api.example.com*

| Class | Method | HTTP request | Description
| ----- | ------ | ------------ | -------------
*ApiDeclarationApi* | [**deleteV1DeclarationDelete**](docs/ApiDeclarationApi.md#deletev1declarationdelete) | **DELETE** /v1/declaration/Delete | 申报信息删除接口。
*ApiDeclarationApi* | [**getV1DeclarationListPaging**](docs/ApiDeclarationApi.md#getv1declarationlistpaging) | **GET** /v1/declaration/ListPaging | 申报信息查询接口。
*ApiDeclarationApi* | [**getV1DeclarationRequiredDocuments**](docs/ApiDeclarationApi.md#getv1declarationrequireddocuments) | **GET** /v1/declaration/RequiredDocuments | 单据所需申报信息查询接口。
*ApiDeclarationApi* | [**postV1DeclarationSubmit**](docs/ApiDeclarationApi.md#postv1declarationsubmit) | **POST** /v1/declaration/Submit | 申报文件/表单提交接口。
*ApiDeliveryApi* | [**deleteV1DeliveryDelete**](docs/ApiDeliveryApi.md#deletev1deliverydelete) | **DELETE** /v1/delivery/Delete | 删除发货单。
*ApiDeliveryApi* | [**getV1DeliveryListPaging**](docs/ApiDeliveryApi.md#getv1deliverylistpaging) | **GET** /v1/delivery/ListPaging | 查询发货单信息及明细信息。
*ApiDeliveryApi* | [**getV1DeliveryReceiptListPaging**](docs/ApiDeliveryApi.md#getv1deliveryreceiptlistpaging) | **GET** /v1/delivery/ReceiptListPaging | 查询收货单集合，核对收货信息。
*ApiDeliveryApi* | [**postV1DeliveryCreate**](docs/ApiDeliveryApi.md#postv1deliverycreate) | **POST** /v1/delivery/Create | 创建发货单。
*ApiDeliveryApi* | [**putV1DeliveryConfirmReceipt**](docs/ApiDeliveryApi.md#putv1deliveryconfirmreceipt) | **PUT** /v1/delivery/ConfirmReceipt | 确认收货。
*ApiDeliveryApi* | [**putV1DeliveryReturnReceipt**](docs/ApiDeliveryApi.md#putv1deliveryreturnreceipt) | **PUT** /v1/delivery/ReturnReceipt | 收货退回。
*ApiDeliveryApi* | [**putV1DeliveryUpdate**](docs/ApiDeliveryApi.md#putv1deliveryupdate) | **PUT** /v1/delivery/Update | 修改发货单。
*ApiEnumApi* | [**getV1EnumGetList**](docs/ApiEnumApi.md#getv1enumgetlist) | **GET** /v1/enum/GetList | 第三方-获取统一枚举列表（支持批量查询/查询所有）
*ApiOrderApi* | [**deleteV1OrderDelete**](docs/ApiOrderApi.md#deletev1orderdelete) | **DELETE** /v1/order/Delete | 第三方-更新订单状态（通过匹配条件获取订单ID）
*ApiOrderApi* | [**deleteV1OrderDeleteLine**](docs/ApiOrderApi.md#deletev1orderdeleteline) | **DELETE** /v1/order/DeleteLine | 第三方-更新订单明细状态（通过匹配条件获取明细ID）
*ApiOrderApi* | [**getV1OrderPOListPaging**](docs/ApiOrderApi.md#getv1orderpolistpaging) | **GET** /v1/order/POListPaging | 第三方-获取采购订单分页列表（含明细）
*ApiOrderApi* | [**getV1OrderSOListPaging**](docs/ApiOrderApi.md#getv1ordersolistpaging) | **GET** /v1/order/SOListPaging | 第三方-获取销售订单分页列表（含明细）
*ApiOrderApi* | [**postV1OrderCreate**](docs/ApiOrderApi.md#postv1ordercreate) | **POST** /v1/order/Create | 第三方-创建订单（含明细）
*ApiOrderApi* | [**postV1OrderSoAccept**](docs/ApiOrderApi.md#postv1ordersoaccept) | **POST** /v1/order/SoAccept | 第三方-销售订单接单（支持绑定成品/自动创建成品）
*ApiOrderApi* | [**putV1OrderUpdate**](docs/ApiOrderApi.md#putv1orderupdate) | **PUT** /v1/order/Update | 第三方-更新订单（部分字段）
*ApiOrderWorkflowApi* | [**postV1OrderSubmitAudit**](docs/ApiOrderWorkflowApi.md#postv1ordersubmitaudit) | **POST** /v1/order/SubmitAudit | 销售方根据已入库的订单、生产、发货及申报资料提交审核。
*ApiOrderWorkflowApi* | [**putV1OrderConfirmReceipt**](docs/ApiOrderWorkflowApi.md#putv1orderconfirmreceipt) | **PUT** /v1/order/ConfirmReceipt | 采购方按整单或单条订单明细确认收货。
*ApiProductionApi* | [**deleteV1ProductionDelete**](docs/ApiProductionApi.md#deletev1productiondelete) | **DELETE** /v1/production/Delete | 删除生产记录单。
*ApiProductionApi* | [**getV1ProductionListPaging**](docs/ApiProductionApi.md#getv1productionlistpaging) | **GET** /v1/production/ListPaging | 查询生产记录单及详细领料信息。
*ApiProductionApi* | [**postV1ProductionCreate**](docs/ApiProductionApi.md#postv1productioncreate) | **POST** /v1/production/Create | 创建生产记录单。
*ApiProductionApi* | [**putV1ProductionUpdate**](docs/ApiProductionApi.md#putv1productionupdate) | **PUT** /v1/production/Update | 修改生产记录单。


### Models

- [GetV1EnumGetList200Response](docs/GetV1EnumGetList200Response.md)
- [MicrosoftAspNetCoreMvcProblemDetails](docs/MicrosoftAspNetCoreMvcProblemDetails.md)
- [Model1](docs/Model1.md)
- [Model3](docs/Model3.md)
- [Model4](docs/Model4.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDocumentRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDocumentRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListDto](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListDto.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResultDto](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResultDto.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiIntegrationDeleteRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiIntegrationDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderConfirmReceiptRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderConfirmReceiptRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditRequest.md)
- [TacticChainApiServiceDataEntitiesCompany](docs/TacticChainApiServiceDataEntitiesCompany.md)
- [TacticChainApiServiceDataEntitiesCompanyComplianceProfile](docs/TacticChainApiServiceDataEntitiesCompanyComplianceProfile.md)
- [TacticChainApiServiceDataEntitiesCompanyUtilityDeclaration](docs/TacticChainApiServiceDataEntitiesCompanyUtilityDeclaration.md)
- [TacticChainApiServiceDataEntitiesCustomer](docs/TacticChainApiServiceDataEntitiesCustomer.md)
- [TacticChainApiServiceDataEntitiesFactory](docs/TacticChainApiServiceDataEntitiesFactory.md)
- [TacticChainApiServiceDataEntitiesOrder](docs/TacticChainApiServiceDataEntitiesOrder.md)
- [TacticChainApiServiceDataEntitiesOrderLine](docs/TacticChainApiServiceDataEntitiesOrderLine.md)
- [TacticChainApiServiceDataEntitiesSupplier](docs/TacticChainApiServiceDataEntitiesSupplier.md)
- [TacticChainApiServiceDataEntitiesSupplierOnboardingExt](docs/TacticChainApiServiceDataEntitiesSupplierOnboardingExt.md)
- [TacticChainApiServiceDataEntitiesTrader](docs/TacticChainApiServiceDataEntitiesTrader.md)
- [TacticChainApiServiceHelperResultApiEnum](docs/TacticChainApiServiceHelperResultApiEnum.md)
- [TacticChainApiServiceHelperResultBrandReportAllocatedDeliveryKpiDetail](docs/TacticChainApiServiceHelperResultBrandReportAllocatedDeliveryKpiDetail.md)
- [TacticChainApiServiceHelperResultBrandReportUnlinkedOrderDetail](docs/TacticChainApiServiceHelperResultBrandReportUnlinkedOrderDetail.md)
- [TacticChainApiServiceHelperResultKpiArchivedDataChangeDetail](docs/TacticChainApiServiceHelperResultKpiArchivedDataChangeDetail.md)
- [TacticChainApiServiceHelperResultMappingOrderSelect](docs/TacticChainApiServiceHelperResultMappingOrderSelect.md)
- [TacticChainApiServiceHelperResultOrderTraceReport](docs/TacticChainApiServiceHelperResultOrderTraceReport.md)
- [TacticChainApiServiceHelperTemplateDtoBusinessRiskWarnInfoDto](docs/TacticChainApiServiceHelperTemplateDtoBusinessRiskWarnInfoDto.md)
- [TacticChainApiServiceHelperTemplateDtoMultiSoLineCompleteStatus](docs/TacticChainApiServiceHelperTemplateDtoMultiSoLineCompleteStatus.md)
- [TacticChainApiServiceModelsBrandKpiPolicyResult](docs/TacticChainApiServiceModelsBrandKpiPolicyResult.md)
- [TacticChainApiServiceModelsBrandOrderKpiSnapshotDto](docs/TacticChainApiServiceModelsBrandOrderKpiSnapshotDto.md)
- [TacticChainApiServiceModelsBrandOrderSupplierOrderSnapshotDto](docs/TacticChainApiServiceModelsBrandOrderSupplierOrderSnapshotDto.md)
- [TacticChainApiServiceModelsBrandOrderUncompletedDeclareSnapshotDto](docs/TacticChainApiServiceModelsBrandOrderUncompletedDeclareSnapshotDto.md)
- [TacticChainApiServiceModelsOrderStageFormDto](docs/TacticChainApiServiceModelsOrderStageFormDto.md)
- [TacticChainApiServiceModelsProductBomGroupingDto](docs/TacticChainApiServiceModelsProductBomGroupingDto.md)
- [TacticChainApiServiceModelsProductionRawMaterialDto](docs/TacticChainApiServiceModelsProductionRawMaterialDto.md)
- [TacticChainApiServiceViewModelsAttachmentInApiCreateDto](docs/TacticChainApiServiceViewModelsAttachmentInApiCreateDto.md)
- [TacticChainApiServiceViewModelsAttachmentInApiDto](docs/TacticChainApiServiceViewModelsAttachmentInApiDto.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1SystemStringSystemPrivateCoreLibVersion9000CultureNeutralPublicKeyToken7cec85d7bea7798e](docs/TacticChainApiServiceViewModelsCommonApiResponse1SystemStringSystemPrivateCoreLibVersion9000CultureNeutralPublicKeyToken7cec85d7bea7798e.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResultDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResultDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsDeliveryNoteApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsDeliveryNoteApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsOrderApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsOrderApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsProductionApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceViewModelsCommonApiResponse1TacticChainApiServiceViewModelsProductionApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsDeliveryNoteApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsDeliveryNoteApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsOrderApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsOrderApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsProductionApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceViewModelsCommonPagedResponse1TacticChainApiServiceViewModelsProductionApiDtoTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceViewModelsDeliveryNoteApiDto](docs/TacticChainApiServiceViewModelsDeliveryNoteApiDto.md)
- [TacticChainApiServiceViewModelsDeliveryNoteDetailApiDto](docs/TacticChainApiServiceViewModelsDeliveryNoteDetailApiDto.md)
- [TacticChainApiServiceViewModelsDocumentTypeApiDto](docs/TacticChainApiServiceViewModelsDocumentTypeApiDto.md)
- [TacticChainApiServiceViewModelsOrderApiDto](docs/TacticChainApiServiceViewModelsOrderApiDto.md)
- [TacticChainApiServiceViewModelsOrderLineApiDto](docs/TacticChainApiServiceViewModelsOrderLineApiDto.md)
- [TacticChainApiServiceViewModelsOrderStageFormApiDto](docs/TacticChainApiServiceViewModelsOrderStageFormApiDto.md)
- [TacticChainApiServiceViewModelsOrderStageFormDatumApiDto](docs/TacticChainApiServiceViewModelsOrderStageFormDatumApiDto.md)
- [TacticChainApiServiceViewModelsProductionApiDto](docs/TacticChainApiServiceViewModelsProductionApiDto.md)
- [TacticChainApiServiceViewModelsProductionRawMaterialApiDto](docs/TacticChainApiServiceViewModelsProductionRawMaterialApiDto.md)
- [TacticChainApiServiceViewModelsProductionSalesOrderApiDto](docs/TacticChainApiServiceViewModelsProductionSalesOrderApiDto.md)
- [TacticChainApiServiceViewModelsStageAttachmentApiDto](docs/TacticChainApiServiceViewModelsStageAttachmentApiDto.md)

### Authorization


Authentication schemes defined for the API:
<a id="BearerToken"></a>
#### BearerToken


- **Type**: HTTP Bearer Token authentication
<a id="ApiKey"></a>
#### ApiKey


- **Type**: API key
- **API key parameter name**: `X-API-Key`
- **Location**: HTTP header
<a id="Timestamp"></a>
#### Timestamp


- **Type**: API key
- **API key parameter name**: `X-Timestamp`
- **Location**: HTTP header
<a id="Signature"></a>
#### Signature


- **Type**: API key
- **API key parameter name**: `X-Signature`
- **Location**: HTTP header

## About

This TypeScript SDK client supports the [Fetch API](https://fetch.spec.whatwg.org/)
and is automatically generated by the
[OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `1.0.0`
- Package version: `0.1.0`
- Generator version: `7.25.0`
- Build package: `org.openapitools.codegen.languages.TypeScriptFetchClientCodegen`

The generated npm module supports the following:

- Environments
  * Node.js
  * Webpack
  * Browserify
- Language levels
  * ES5 - you must have a Promises/A+ library installed
  * ES6
- Module systems
  * CommonJS
  * ES6 module system


## Development

### Building

To build the TypeScript source code, you need to have Node.js and npm installed.
After cloning the repository, navigate to the project directory and run:

```bash
npm install
npm run build
```

### Publishing

Once you've built the package, you can publish it to npm:

```bash
npm publish
```

## License

[]()
