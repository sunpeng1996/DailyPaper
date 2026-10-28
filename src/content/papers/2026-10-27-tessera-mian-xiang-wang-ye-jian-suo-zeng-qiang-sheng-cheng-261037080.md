---
title: 'Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation'
title_zh: Tessera：面向网页检索增强生成的结构完整证据单元
authors:
- Peichun Hua
- He Sun
- Zirui Zhuang
- Qi Qi
- Yiming Qiu
- Shinan Liu
- Yunming Xiao
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- The University of Hong Kong
- Beijing University of Posts and Telecommunications
arxiv_id: '2610.37080'
url: https://arxiv.org/abs/2610.37080
pdf_url: https://arxiv.org/pdf/2610.37080
published: '2026-10-27'
collected: '2026-10-28'
category: RAG
direction: 检索增强生成 · 网页结构化证据提取
tags:
- RAG
- Web_Search
- Structured_Evidence
- Agentic_RAG
- HTML_Parsing
one_liner: 提出训练无关的Web RAG证据递送层，解耦检索与阅读单元，无需改动现有组件即可提升准确率
practical_value: '- 电商商品/攻略类RAG系统可直接复用该结构化提取逻辑，将商品详情页HTML解析为带页头、分类路径、属性表头的细粒度单元，解决固定分块丢失商品规格、参数表上下文的痛点，无需改动现有召回排序链路

  - Agent多步搜索场景下，可将该层作为搜索工具后置处理模块，把返回网页重组成自包含证据块，实测可减少Agent无效搜索次数，3K token带Tessera的效果优于12K
  token原始分块，同时降低上下文成本

  - 现有RAG系统无需重训模型、无需重建索引，仅需在召回后新增轻量处理层，替换最后1个召回结果的token预算为结构化单元块，即可拿到显著效果提升，工程落地成本极低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Web RAG管线固定用索引阶段的分块/截图tile作为检索、排序、阅读的统一单元，结构化内容（表格、信息框、列表）常被拆分丢失上下文，甚至在抽取阶段就被丢弃，即便增加上下文预算、优化抽取逻辑也难以解决这类证据损失，导致召回了正确页面却送不到正确证据的问题。

### 方法关键点
- 训练无关的查询时递送层，完全兼容现有文本、多模态、Agent RAG管线，无需改动索引、召回器、阅读器，不增加token预算
- 从Top-10召回结果对应的锚点页面HTML出发，解析为细粒度证据单元：段落/列表项为块单元，表格/信息框优先构建忠实网格，自动补全页标题、章节路径、表头等上下文，每个单元自包含可独立解读
- 经词汇预过滤、交叉编码器筛选与查询相关的单元，按上下文分组打包进原有最后1个召回项的token预算，避免重复冗余

### 关键实验结果
- 在NQ、NQ-Tables、SimpleQA共7851个问答样本上，文本、截图RAG管线准确率提升5~6个点，多步搜索Agent在FRAMES数据集提升5.2个点，效果优于14个现有基线（包括RM3、HyDE、RAPTOR、HtmlRAG等）
- 3K token带Tessera的效果优于12K token的原始分块/截图，同时降低推理成本
- 对7.6%原始索引丢失证据的问题，Tessera的证据恢复率达81%

最值得记住的一句话：Web RAG的核心瓶颈不是召回不到正确页面，而是检索单元与阅读单元的耦合导致证据递送失效，解耦二者的收益远高于单纯扩大上下文预算
