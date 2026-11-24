---
title: 'DKnown-Jev-2: Article-Level Answer-Evidence Classification and Efficient Inference
  with a Pre-trained Language Model'
title_zh: DKnown-Jev-2：基于预训练语言模型的篇章级答案证据分类与高效推理
authors:
- Qi Li
- Jianjun Xu
- Jiu Li
- Pingtao Wei
affiliations:
- 北京财智科技
arxiv_id: '2611.31056'
url: https://arxiv.org/abs/2611.31056
pdf_url: https://arxiv.org/pdf/2611.31056
published: '2026-11-23'
collected: '2026-11-24'
category: RAG
direction: RAG · 证据筛选低延迟优化
tags:
- RAG
- Evidence Selection
- Pointer Network
- Efficient Inference
- Long-Context Processing
one_liner: 提出篇章级答案证据分类模型DKnown-Jev-2，准确率91.77%，单4090推理延迟仅118ms
practical_value: '- RAG证据筛选环节可复用指针式分类头设计，用自然语言定义标签语义，减少标注成本，适配电商售后、合规政策等垂直领域规则类知识检索场景

  - 多段落长文本证据分类可采用共享篇章编码+非自回归推理架构，单4090单请求延迟仅118ms，满足线上服务低延迟要求

  - 电商/政务合规类知识库检索可借鉴「适用性条件+内容匹配」双重判断逻辑，降低无关/不适用内容召回假阳性，提升RAG回答准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG证据筛选多基于语义相似度，未覆盖规范性知识的适用条件（如地域、时效、适用主体），且多针对单段落设计，无法处理多段落跨片段证据整合，易出现证据遗漏、不适用内容误判，无法满足政策、售后等垂直领域问答需求。
### 方法关键点
- 输入融合用户问题、适用条件、篇章元数据、全段落序列，加入Answer Evidence(AE)/Non-answer Evidence(NE)标签的自然语言定义与特殊标记位
- 基于Qwen3.5-9B底座，采用指针式分类头，匹配候选标签标记表示与决策标记表示输出分类概率，无需自回归解码
- 混合注意力机制：决策上下文区双向可见，其余层用因果线性注意力，支持跨段落证据交互
- 训练采用交叉熵损失+RLCD辅助损失，快速适配垂直领域数据
### 关键实验
测试集含972条人工标注篇章级实例，32.6%为多段落样本，最长篇章达9322字符；对比Jev、OpenAI Decision两个基线：
- 整体准确率91.77%、Macro-F1 91.28%，较Jev分别提升2.16、2.37个百分点，假阴性减少17、假阳性减少4
- 多段落场景表现稳定：2-3段落准确率92.67%、4+段落准确率92.06%，均为最优
- 单NVIDIA RTX 4090单并发推理延迟约118ms
### 核心结论
RAG证据筛选不能仅依赖语义相似度，需结合适用条件与多段落信息联合判断，非自回归指针分类头架构可同时兼顾高准确率与线上低延迟要求。
