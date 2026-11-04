---
title: 'Length Is Cheap, Competition Is Not: Attention Predicts Context Rot in Retrieval'
title_zh: 检索任务中上下文衰减核心是注意力竞争而非长度
authors:
- Yinuo Liu
affiliations:
- University of California San Diego
arxiv_id: '2611.04169'
url: https://arxiv.org/abs/2611.04169
pdf_url: https://arxiv.org/pdf/2611.04169
published: '2026-11-03'
collected: '2026-11-04'
category: RAG
direction: RAG长上下文 · 上下文衰减机制
tags:
- Long-Context
- Context-Rot
- RAG
- Attention
- Retrieval
one_liner: 证明LLM检索任务的上下文衰减由语义竞争而非长度导致，注意力占比可直接预测损失
practical_value: '- 做电商RAG导购、Agent记忆模块优化时，不用盲目截断上下文压token数，优先去重、消解语义冲突的召回内容，ROI更高

  - 可复用证据注意力占比a*作为RAG系统的轻量诊断指标，无需每次做端到端评估即可快速判断上下文质量

  - 做长上下文LLM评测时需加可见中性填充对照组，避免把masked填充带来的位置偏差误判为长度本身的影响'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
之前行业普遍将LLM长上下文性能衰减（context rot）归因于长度本身，优化方向集中在架构扩容，但实际场景中上下文增长往往伴随语义相似的竞争内容，两者混淆既无法定位根因，也会误导RAG、Agent记忆模块的优化策略。
### 方法关键点
- 固定上下文长度和证据位置，仅修改填充内容，设置4组对照：短上下文、中性填充、同格式竞争内容填充、masked填充
- 测试5款0.5B-3B开源模型（Qwen2.5、SmolLM2、OLMo-2、Llama-3.2），上下文长度覆盖512到32K token
- 统计检索相关头分配给证据的注意力占比a*，验证其与检索损失的相关性
### 关键结果数字
- 中性填充下，Qwen2.5-1.5B在32K token时检索精度仍保持0.98，几乎无损失；同长度替换为竞争内容填充时精度骤降到0.11-0.21
- 12.6万次试验中，log(1/a*)可解释35%-58%的损失方差，而log长度仅能解释2%-8%；1个同key冲突内容会让损失放大9-110倍
- 重复之前masked填充实验，32K token时masked填充比可见中性填充精度低46个点，证明masked带来的位置偏差而非长度本身导致精度下降
### 最值得记住的一句话
检索任务中上下文的有效预算不是token数，而是和查询竞争注意力的语义冲突内容数量。
