---
title: 'Beyond Maintenance Manual Multimodal RAG: Suggesting What Tool'
title_zh: 支持工具推荐的航空维修多模态RAG扩展框架
authors:
- Seongjun Ha
- Md Rashedul Islam
affiliations:
- Purdue University
- Clemson University
arxiv_id: '2609.05116'
url: https://arxiv.org/abs/2609.05116
pdf_url: https://arxiv.org/pdf/2609.05116
published: '2026-09-04'
collected: '2026-09-07'
category: RAG
direction: 多模态RAG · 垂直场景功能扩展
tags:
- Multimodal RAG
- Tool Recommendation
- Vertical Domain Application
- Information Retrieval
- Document QA
one_liner: 面向航空维修场景扩展多模态RAG pipeline，同步返回维修流程与所需专用/手动工具
practical_value: '- 垂直领域RAG落地可基于业务痛点扩展功能，不局限于原始文档召回，可联动多数据源输出结构化增值信息，例如电商场景下给商品返回配套耗材、安装工具推荐

  - 当主文档未覆盖目标信息时，可引入关联异构数据源做信息补全和推理，例如电商场景可引入商品规格参数库推理适配配件/工具

  - 多模态RAG pipeline可做模块化扩展，无需重构原有检索生成链路即可新增业务属性输出，大幅降低迭代成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
航空维修场景现有多模态RAG仅支持返回维修流程与配套图片，无法提供任务所需工具信息：维修手册仅在执行步骤处标注专用工具，完全未提及手动工具，技师需额外查询零件目录（IPC）获取硬件尺寸后自行推断，耗时且易出现工具选择错误，引发设备损坏。
### 方法关键点
提出MRAG-SWAT框架，对原有MRAG pipeline做模块化扩展：1. 从召回的维修流程中提取专用工具信息；2. 联动IPC零件目录检索对应硬件尺寸，推理生成所需手动工具列表，最终同步返回维修流程、专用工具、手动工具三类结果。
### 关键结果
在Lycoming IO-360-N1A发动机场景下完成8个测试query验证，可有效减少技师往返工具房次数，避免工具选择不当导致的航空设备损坏。
