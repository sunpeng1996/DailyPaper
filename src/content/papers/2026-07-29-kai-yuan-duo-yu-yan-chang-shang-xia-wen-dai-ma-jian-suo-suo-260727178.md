---
title: 'DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for
  Multilingual, Long-Context, and Code Search'
title_zh: 开源多语言长上下文代码检索：DenseOn与LateOn检索模型
authors:
- Raphaël Sourty
- Antoine Chaffin
- Paulo Roberto Moura Junior
- Amélie Chatelain
affiliations:
- LightOn
arxiv_id: '2607.27178'
url: https://arxiv.org/abs/2607.27178
pdf_url: https://arxiv.org/pdf/2607.27178
published: '2026-07-29'
collected: '2026-07-30'
category: RAG
direction: 检索模型 · 多语言跨场景迁移
tags:
- Retrieval
- Dense Retrieval
- Late Interaction
- Multilingual
- Long Context
- Open Source
one_liner: 开源全流程检索训练配方及4款跨多语言长上下文代码场景的小体量SOTA检索模型
practical_value: '- 多语言跨境电商搜索可复用translate-train+晚交互模型的组合，仅翻译少量主流语言的训练语料，即可覆盖大量小语种搜索场景，大幅降低语料标注成本

  - 站内长文本（商品详情页、用户评价、帮助文档）检索可优先选择ColBERT式晚交互模型，相比单向量稠密检索，在长上下文和跨域泛化场景下有10%-20%的性能增益

  - 小体量检索模型训练可复用论文的非破坏性数据过滤+硬负样本挖掘+跨编码器蒸馏的流水线，在150M参数级就能达到接近大模型的检索效果，推理成本降低50%以上

  - 跨境场景下如果仅服务已覆盖的主流语言，选择单向量稠密模型即可满足需求，推理速度更快；若需要覆盖未标注的小语种，优先选择晚交互模型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前SOTA检索模型普遍依赖闭源训练数据与训练流程，可复现性差，性能增益来源难以追溯；同时多语言检索标注语料高度集中于英语，小语种标注成本极高，单向量稠密检索的跨语言泛化能力弱，晚交互模型的多语言迁移规律尚未被系统验证。
### 方法关键点
- 数据层：重构34个公开源的14亿英文query-document对，经非破坏性标注过滤得到6.65亿高质量预训练对，搭配188万带挖掘硬负样本的微调对；将英文语料翻译为8种语言生成28亿多语言预训练对，补充1630万包含长上下文、代码的微调对
- 模型层：基于ModernBERT训练149M参数的单向量稠密模型DENSEON和ColBERT式晚交互模型LATEON；基于mmBERT训练307M参数的多语言版本MDENSEON和MLATEON
- 训练层：预训练采用InfoNCE损失+16k大批次+GradCache降内存，微调加入硬负样本采样、Matryoshka训练（稠密模型）、跨编码器KL蒸馏
### 关键实验
在BEIR基准上，149M的DENSEON和LATEON分别达到56.20、57.22平均nDCG@10，为同体量SOTA；多语言版MLATEON在MIRACL全语言集上nDCG@10达67.04，比同体量MDENSEON高9个点，在长上下文MLDR基准上比MDENSEON高26个点，代码检索MTEB Code得分达73.48。
### 核心结论
晚交互模型的token级匹配能力可将translate-train从目标语言扩量策略升级为多语言泛化方案，仅需翻译少量语言即可覆盖大量未见过的语种和脚本。
