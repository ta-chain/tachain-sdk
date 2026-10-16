# @ta-chain/tachain-sdk@0.1.1

A TypeScript SDK client for the api.example.com API.

## Source repository and local build

This SDK is in the [generated/typescript directory](https://github.com/ta-chain/tachain-sdk/tree/main/generated/typescript) of the [open-source SDK repository](https://github.com/ta-chain/tachain-sdk).

~~~sh
git clone https://github.com/ta-chain/tachain-sdk.git
cd tachain-sdk/generated/typescript
npm install --no-audit --no-fund
npm run build
~~~

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
    // string | 查询返回的附件申报记录标识；也可在 Body 按单据和资料类型删除。 (optional)
    attachmentId: attachmentId_example,
    // string | 查询返回的表单记录标识；也可在 Body 按业务键删除。 (optional)
    formDataId: formDataId_example,
    // TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest (optional)
    tacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest: {"stageId":"Order","orderSide":"SO","supplierExtNo":"ERP-SO-001-10","customerName":"客户名称","documentTypeCode":"INVOICE","deleteAttachments":true,"deleteForms":false},
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
*ApiDeclarationUploadApi* | [**postV1DeclarationUploadFile**](docs/ApiDeclarationUploadApi.md#postv1declarationuploadfile) | **POST** /v1/declaration/UploadFile | 上传申报文件，返回 FileId；文件内容最多 30 MiB。
*ApiDeliveryApi* | [**deleteV1DeliveryDelete**](docs/ApiDeliveryApi.md#deletev1deliverydelete) | **DELETE** /v1/delivery/Delete | 删除发货单。
*ApiDeliveryApi* | [**getV1DeliveryListPaging**](docs/ApiDeliveryApi.md#getv1deliverylistpaging) | **GET** /v1/delivery/ListPaging | 查询发货单信息及明细信息。
*ApiDeliveryApi* | [**getV1DeliveryReceiptListPaging**](docs/ApiDeliveryApi.md#getv1deliveryreceiptlistpaging) | **GET** /v1/delivery/ReceiptListPaging | 查询收货单集合，核对收货信息。
*ApiDeliveryApi* | [**postV1DeliveryCreate**](docs/ApiDeliveryApi.md#postv1deliverycreate) | **POST** /v1/delivery/Create | 创建发货单。
*ApiDeliveryApi* | [**putV1DeliveryConfirmReceipt**](docs/ApiDeliveryApi.md#putv1deliveryconfirmreceipt) | **PUT** /v1/delivery/ConfirmReceipt | 确认收货。
*ApiDeliveryApi* | [**putV1DeliveryReturnReceipt**](docs/ApiDeliveryApi.md#putv1deliveryreturnreceipt) | **PUT** /v1/delivery/ReturnReceipt | 收货退回。
*ApiDeliveryApi* | [**putV1DeliveryUpdate**](docs/ApiDeliveryApi.md#putv1deliveryupdate) | **PUT** /v1/delivery/Update | 修改发货单。
*ApiEnumApi* | [**getV1EnumGetList**](docs/ApiEnumApi.md#getv1enumgetlist) | **GET** /v1/enum/GetList | 第三方-获取统一枚举列表（支持批量查询/查询所有）
*ApiMaterialApi* | [**deleteV1MaterialDelete**](docs/ApiMaterialApi.md#deletev1materialdelete) | **DELETE** /v1/material/Delete | 删除未被使用的资料；软删除，已被订单等业务使用时返回业务错误。
*ApiMaterialApi* | [**getV1MaterialGet**](docs/ApiMaterialApi.md#getv1materialget) | **GET** /v1/material/Get | 按编码或 ID 精确查询。
*ApiMaterialApi* | [**getV1MaterialListPaging**](docs/ApiMaterialApi.md#getv1materiallistpaging) | **GET** /v1/material/ListPaging | 分页查询；searchText 搜索编码或名称，scopeCode 按加工阶段筛选。
*ApiMaterialApi* | [**postV1MaterialCreate**](docs/ApiMaterialApi.md#postv1materialcreate) | **POST** /v1/material/Create | 创建原料资料。
*ApiMaterialApi* | [**putV1MaterialUpdate**](docs/ApiMaterialApi.md#putv1materialupdate) | **PUT** /v1/material/Update | 完整修改原料资料。
*ApiOrderApi* | [**deleteV1OrderDelete**](docs/ApiOrderApi.md#deletev1orderdelete) | **DELETE** /v1/order/Delete | 第三方-更新订单状态（通过匹配条件获取订单ID）
*ApiOrderApi* | [**deleteV1OrderDeleteLine**](docs/ApiOrderApi.md#deletev1orderdeleteline) | **DELETE** /v1/order/DeleteLine | 第三方-更新订单明细状态（通过匹配条件获取明细ID）
*ApiOrderApi* | [**getV1OrderPOListPaging**](docs/ApiOrderApi.md#getv1orderpolistpaging) | **GET** /v1/order/POListPaging | 第三方-获取采购订单分页列表（含明细）
*ApiOrderApi* | [**getV1OrderSOListPaging**](docs/ApiOrderApi.md#getv1ordersolistpaging) | **GET** /v1/order/SOListPaging | 第三方-获取销售订单分页列表（含明细）
*ApiOrderApi* | [**postV1OrderCreate**](docs/ApiOrderApi.md#postv1ordercreate) | **POST** /v1/order/Create | 第三方-创建订单（含明细）
*ApiOrderApi* | [**postV1OrderSoAccept**](docs/ApiOrderApi.md#postv1ordersoaccept) | **POST** /v1/order/SoAccept | 第三方-销售订单接单（支持绑定成品/自动创建成品）
*ApiOrderApi* | [**putV1OrderUpdate**](docs/ApiOrderApi.md#putv1orderupdate) | **PUT** /v1/order/Update | 第三方-更新订单（部分字段）
*ApiOrderWorkflowApi* | [**getV1OrderReceiptPending**](docs/ApiOrderWorkflowApi.md#getv1orderreceiptpending) | **GET** /v1/order/ReceiptPending | 采购订单确认收货待办项查询。
*ApiOrderWorkflowApi* | [**postV1OrderDeclarationVerification**](docs/ApiOrderWorkflowApi.md#postv1orderdeclarationverification) | **POST** /v1/order/DeclarationVerification | 销售订单提交审核前一键校验。
*ApiOrderWorkflowApi* | [**postV1OrderSubmitAudit**](docs/ApiOrderWorkflowApi.md#postv1ordersubmitaudit) | **POST** /v1/order/SubmitAudit | 销售方根据已入库的订单、生产、发货及申报资料提交审核。
*ApiOrderWorkflowApi* | [**putV1OrderConfirmReceipt**](docs/ApiOrderWorkflowApi.md#putv1orderconfirmreceipt) | **PUT** /v1/order/ConfirmReceipt | 采购方按整单或单条订单明细确认收货。
*ApiProcessRouteApi* | [**deleteV1ProcessRouteDelete**](docs/ApiProcessRouteApi.md#deletev1processroutedelete) | **DELETE** /v1/processRoute/Delete | 软删除加工路线；历史单据保持其已有引用，新建业务不可再选择该路线。
*ApiProcessRouteApi* | [**getV1ProcessRouteGet**](docs/ApiProcessRouteApi.md#getv1processrouteget) | **GET** /v1/processRoute/Get | 按路线编码或查询返回的 ID 精确查询，两者同时传入须一致。
*ApiProcessRouteApi* | [**getV1ProcessRouteListPaging**](docs/ApiProcessRouteApi.md#getv1processroutelistpaging) | **GET** /v1/processRoute/ListPaging | 分页查询正常路线；searchText 匹配编码或名称，scopeCode 筛选加工阶段。
*ApiProcessRouteApi* | [**postV1ProcessRouteCreate**](docs/ApiProcessRouteApi.md#postv1processroutecreate) | **POST** /v1/processRoute/Create | 创建加工路线及有序工序。
*ApiProcessRouteApi* | [**putV1ProcessRouteUpdate**](docs/ApiProcessRouteApi.md#putv1processrouteupdate) | **PUT** /v1/processRoute/Update | 完整修改路线；steps 省略保留原工序，数组则替换全部工序，空数组清空。
*ApiProductApi* | [**deleteV1ProductDelete**](docs/ApiProductApi.md#deletev1productdelete) | **DELETE** /v1/product/Delete | 删除未被使用的资料；软删除，已被订单等业务使用时返回业务错误。
*ApiProductApi* | [**getV1ProductGet**](docs/ApiProductApi.md#getv1productget) | **GET** /v1/product/Get | 按编码或 ID 精确查询。
*ApiProductApi* | [**getV1ProductListPaging**](docs/ApiProductApi.md#getv1productlistpaging) | **GET** /v1/product/ListPaging | 分页查询；searchText 搜索编码或名称，scopeCode 按加工阶段筛选。
*ApiProductApi* | [**postV1ProductCreate**](docs/ApiProductApi.md#postv1productcreate) | **POST** /v1/product/Create | 创建成品资料。
*ApiProductApi* | [**putV1ProductUpdate**](docs/ApiProductApi.md#putv1productupdate) | **PUT** /v1/product/Update | 完整修改成品资料。
*ApiProductionApi* | [**deleteV1ProductionDelete**](docs/ApiProductionApi.md#deletev1productiondelete) | **DELETE** /v1/production/Delete | 删除生产记录单。
*ApiProductionApi* | [**getV1ProductionListPaging**](docs/ApiProductionApi.md#getv1productionlistpaging) | **GET** /v1/production/ListPaging | 查询生产记录单及详细领料信息。
*ApiProductionApi* | [**postV1ProductionCreate**](docs/ApiProductionApi.md#postv1productioncreate) | **POST** /v1/production/Create | 创建生产记录单。
*ApiProductionApi* | [**putV1ProductionUpdate**](docs/ApiProductionApi.md#putv1productionupdate) | **PUT** /v1/production/Update | 修改生产记录单。
*ApiReferenceApi* | [**getV1ReferenceEnumValues**](docs/ApiReferenceApi.md#getv1referenceenumvalues) | **GET** /v1/reference/EnumValues | 查询 enum_value；EnumTypeId 必填，Value 可选精确匹配。
*ApiReferenceApi* | [**getV1ReferenceMappings**](docs/ApiReferenceApi.md#getv1referencemappings) | **GET** /v1/reference/Mappings | 查询 external_mapping；MappedTable 必填，ExternalValue 可选精确匹配。


### Models

- [DeleteV1DeclarationDelete200Response](docs/DeleteV1DeclarationDelete200Response.md)
- [GetV1DeclarationListPaging200Response](docs/GetV1DeclarationListPaging200Response.md)
- [GetV1DeclarationRequiredDocuments200Response](docs/GetV1DeclarationRequiredDocuments200Response.md)
- [GetV1DeliveryListPaging200Response](docs/GetV1DeliveryListPaging200Response.md)
- [GetV1EnumGetList200Response](docs/GetV1EnumGetList200Response.md)
- [GetV1MaterialListPaging200Response](docs/GetV1MaterialListPaging200Response.md)
- [GetV1OrderPOListPaging200Response](docs/GetV1OrderPOListPaging200Response.md)
- [GetV1OrderReceiptPending200Response](docs/GetV1OrderReceiptPending200Response.md)
- [GetV1ProcessRouteListPaging200Response](docs/GetV1ProcessRouteListPaging200Response.md)
- [GetV1ProductListPaging200Response](docs/GetV1ProductListPaging200Response.md)
- [GetV1ProductionListPaging200Response](docs/GetV1ProductionListPaging200Response.md)
- [GetV1ReferenceEnumValues200Response](docs/GetV1ReferenceEnumValues200Response.md)
- [GetV1ReferenceMappings200Response](docs/GetV1ReferenceMappings200Response.md)
- [Model1](docs/Model1.md)
- [Model2](docs/Model2.md)
- [Model3](docs/Model3.md)
- [Model4](docs/Model4.md)
- [PostV1DeclarationSubmit200Response](docs/PostV1DeclarationSubmit200Response.md)
- [PostV1DeclarationUploadFile200Response](docs/PostV1DeclarationUploadFile200Response.md)
- [PostV1MaterialCreate200Response](docs/PostV1MaterialCreate200Response.md)
- [PostV1OrderCreate200Response](docs/PostV1OrderCreate200Response.md)
- [PostV1OrderDeclarationVerification200Response](docs/PostV1OrderDeclarationVerification200Response.md)
- [PostV1OrderSubmitAudit200Response](docs/PostV1OrderSubmitAudit200Response.md)
- [PostV1ProcessRouteCreate200Response](docs/PostV1ProcessRouteCreate200Response.md)
- [PostV1ProductCreate200Response](docs/PostV1ProductCreate200Response.md)
- [PostV1ProductionCreate200Response](docs/PostV1ProductionCreate200Response.md)
- [PutV1DeliveryConfirmReceipt200Response](docs/PutV1DeliveryConfirmReceipt200Response.md)
- [PutV1DeliveryReturnReceipt200Response](docs/PutV1DeliveryReturnReceipt200Response.md)
- [PutV1OrderConfirmReceipt200Response](docs/PutV1OrderConfirmReceipt200Response.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiBomLineRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiBomLineRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiBomLineResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiBomLineResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiCatalogDeleteRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiCatalogDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationAttachmentResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationAttachmentResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDocumentRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationDocumentRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFileRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFileRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFormRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFormRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFormResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFormResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryCreateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDeleteRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailCreateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailUpdateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryDetailUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryUpdateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDocumentFormResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDocumentFormResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiDocumentTypeResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiDocumentTypeResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiEnumValueResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiEnumValueResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiErrorResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiErrorResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiFiberCompositionRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiFiberCompositionRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiFiberCompositionResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiFiberCompositionResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiFileResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiFileResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiFileUploadResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiFileUploadResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiMappingResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiMappingResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiMaterialCreateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiMaterialCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiMaterialUpdateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiMaterialUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderAcceptRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderAcceptRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderConfirmReceiptRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderConfirmReceiptRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderCreateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeleteLineRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeleteLineRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeleteRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineCreateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineUpdateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderLineUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingLineResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingLineResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptResult](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptResult.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiOrderUpdateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiOrderUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiPageResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteCreateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteUpdateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProcessStepRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProcessStepRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProcessStepResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProcessStepResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductCreateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductUpdateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionCreateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductionCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionDeleteRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductionDeleteRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialCreateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialUpdateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductionRawMaterialUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderCreateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderCreateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderUpdateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductionSalesOrderUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiProductionUpdateRequest](docs/TacticChainApiServiceControllersApiIntegrationV1ApiProductionUpdateRequest.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiReceiptPendingItemResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiReceiptPendingItemResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiReferencePageResponse1TacticChainApiServiceControllersApiIntegrationV1ApiEnumValueResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiReferencePageResponse1TacticChainApiServiceControllersApiIntegrationV1ApiEnumValueResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiReferencePageResponse1TacticChainApiServiceControllersApiIntegrationV1ApiMappingResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiReferencePageResponse1TacticChainApiServiceControllersApiIntegrationV1ApiMappingResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1SystemStringSystemPrivateCoreLibVersion9000CultureNeutralPublicKeyToken7cec85d7bea7798e](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1SystemStringSystemPrivateCoreLibVersion9000CultureNeutralPublicKeyToken7cec85d7bea7798e.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationListResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiDeliveryResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiFileUploadResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiFileUploadResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiMaterialResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderDeclarationVerificationResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptPendingResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptResultTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderReceiptResultTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiOrderSubmitAuditResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProcessRouteResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull](docs/TacticChainApiServiceControllersApiIntegrationV1ApiResult1TacticChainApiServiceControllersApiIntegrationV1ApiProductionResponseTacticChainApiServiceVersion1000CultureNeutralPublicKeyTokenNull.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiVerificationFileResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiVerificationFileResponse.md)
- [TacticChainApiServiceControllersApiIntegrationV1ApiVerificationResponse](docs/TacticChainApiServiceControllersApiIntegrationV1ApiVerificationResponse.md)

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
- Package version: `0.1.1`
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
