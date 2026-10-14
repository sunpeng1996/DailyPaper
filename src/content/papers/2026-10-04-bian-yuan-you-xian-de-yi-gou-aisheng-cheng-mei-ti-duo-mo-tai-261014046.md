---
title: An Edge-First Multimodal Asset Management Studio and Retrieval Engine for Heterogeneous
  AI-Generated Media
title_zh: 边缘优先的异构AI生成媒体多模态资产管理工作台与检索引擎
authors:
- Chaoyu Lin
affiliations:
- Independent Researcher
arxiv_id: '2610.14046'
url: https://arxiv.org/abs/2610.14046
pdf_url: https://arxiv.org/pdf/2610.14046
published: '2026-10-04'
collected: '2026-10-14'
category: Multimodal
direction: 多模态AIGC 端侧资产管理与检索
tags:
- AI-generated media
- digital asset management
- local inference
- keyset pagination
- multimodal retrieval
one_liner: 实现边缘优先的异构AIGC多模态资产管理系统，支持低延迟检索与高效浏览
practical_value: '- 电商海量商品图文资产端侧管理可复用 Tauri + Rust + ONNX Runtime 技术栈，实现无远程依赖的低延迟检索，降低带宽成本

  - 高偏移量分页场景可直接采用 keyset 分页方案，对比传统 offset 分页延迟从数十ms降至亚ms级，大幅提升列表浏览体验

  - 端侧任务调度可引入生成感知的队列取消机制，过滤无效 stale 解码请求，降低CPU、内存等端侧资源占用'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
AIGC图像附带prompt、模型参数、工作流等异构元数据，本地管理需要兼顾元数据提取、流畅浏览、无远程依赖的检索能力，现有工具未完整覆盖该场景需求。
### 方法关键点
搭建Berry AI Studio边缘优先系统，采用Vue+Tauri+Rust+SQLite+ONNX Runtime技术栈，核心特性包括：格式专属元数据解析与原始payload留存、生成感知的队列缩略图任务取消机制、持久化多层缩略图清单、cursor分页、本地图文检索。
### 关键结果
5万条目录记录下，热启首页数据库调用中位数285.3ms；偏移4万时，keyset分页将原始查询延迟中位数从57.9ms降至0.46ms；虚拟化滚动P95更新时间中位数0.3ms；取消机制拦截全部1200个无效投机解码请求；10个测试用例的53个元数据字段匹配准确率100%。
