---
title: Token-Efficient Data Reasoning Agents via Adaptive Structuring of Unstructured
  Data
title_zh: 基于非结构化数据自适应结构化的Token高效数据推理Agent
authors:
- Milad Rezaei Hajidehi
- Qitong Wang
- Stratos Idreos
affiliations:
- Harvard University
arxiv_id: '2608.31082'
url: https://arxiv.org/abs/2608.31082
pdf_url: https://arxiv.org/pdf/2608.31082
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: Agent 非结构化数据推理成本优化
tags:
- Agentic Reasoning
- KV Cache
- Unstructured Data
- Cost Optimization
- Structured Extraction
one_liner: 提出Agentic数据裂解机制，复用已加载文档KV cache抽取可复用结构化知识，大幅降低推理成本
practical_value: '- 搭建电商商品问答/企业知识库Agent时，可复用用户查询触发加载的文档KV cache，低边际成本抽取商品/文档的实体、属性、关系存入结构化库，后续同类查询直接读取避免重复加载大文档，降低token成本

  - 搜索推荐侧的用户query意图理解场景，可复用自适应结构化思路，对高频查询涉及的商品、品类属性做增量抽取，无需全量预构建知识图谱，节省预处理与推理成本

  - KV cache复用+非阻塞子Agent并行抽取的工程架构可直接落地，抽取逻辑放在请求响应路径外，不影响当前用户查询的延迟'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多跳数据推理Agent需要反复加载大段非结构化文档提取零散证据，token成本极高（单条查询可达百万token，近1美元）；全量预结构化所有文档不可行，因为大部分结构永远不会被查询用到；而真实业务中相关查询存在语义局部性，会重复访问同一文档的同类属性，存在大幅降本空间。

### 方法关键点
- 提出Agentic数据裂解（Adc）机制，仅当推理Agent为响应用户查询加载文档时，才fork裂解子Agent，复用文档已生成的KV cache做增量结构化抽取，无额外预填充成本，且子Agent运行在响应路径外不增加当前查询延迟
- 设计扩展RDF格式的裂解对象数据模型，存储实体-关系-属性三元组，附带源文档证据、基数、单位信息，支持结构化查询
- 推理时先查询已裂解的结构化存储，命中则直接返回结果，未命中再fallback加载原始文档，保证精度不损失

### 关键实验
在FanOutQA基准（每查询平均跨7篇文档）新增1条相关查询模拟真实语义局部性，对比原生Agentic推理baseline：成本下降53%，LLM裁判评估的准确率仅降1个百分点（无统计显著性），10分位查询成本降低9倍，中位数成本降低3.4倍；在电影多跳查询案例中成本下降67%。

**最值得记住的一句话**：无需全量预构建非结构化数据的知识图谱，利用查询的语义局部性和KV cache复用做自适应增量结构化，能在保精度的前提下实现数量级的推理成本下降。
