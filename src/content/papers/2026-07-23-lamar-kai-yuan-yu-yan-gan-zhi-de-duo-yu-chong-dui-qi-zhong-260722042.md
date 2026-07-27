---
title: 'LAMAR: An Open Language-Aware Multilingual Alignment Reranker'
title_zh: LAMAR：开源语言感知的多语种对齐重排序器
authors:
- Seongtae Hong
- Youngjoon Jang
- Jungseob Lee
- Seungyoon Lee
- Heuiseok Lim
affiliations:
- Korea University
arxiv_id: '2607.22042'
url: https://arxiv.org/abs/2607.22042
pdf_url: https://arxiv.org/pdf/2607.22042
published: '2026-07-23'
collected: '2026-07-27'
category: RAG
direction: 多语种RAG · 重排序模型优化
tags:
- Multilingual RAG
- Reranker
- Cross-Encoder
- Knowledge Distillation
- Preference Alignment
one_liner: 提出两阶段训练的语言感知多语种重排序器，兼顾语义相关性与跨语言一致性
practical_value: '- 跨境电商/多语种搜索推荐场景的RAG系统可直接接入开源LAMAR重排器，优先排序与用户query同语种的召回结果，实测可提升下游LLM回答准确率10%以上

  - 小参数多语种重排器训练可复用两阶段范式：先通过英语锚定蒸馏校准跨语种语义评分，再加入轻量语言一致性偏好损失，无需海量标注数据即可兼顾语义与语种匹配

  - 多语种系统评测可复用论文的语言一致性诊断方法：构造平行语义多语种候选集，量化重排器优先选择同语种文档的能力，规避现有模型对英语等语种的偏置问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多语种RAG场景中，现有多语种重排器仅以语义相关性为排序目标，不会优先选择与查询同语种的语义等价文档，但实验验证同语种上下文可让Qwen2.5-32B、Llama-3.3-70B的生成答案F1最高提升0.3，该问题直接降低跨境搜索、多语种客服Agent、国际化推荐内容解释的生成质量。

### 方法关键点
- 两阶段训练范式：第一阶段采用英语锚定相关性蒸馏，以英语教师重排器的输出作为跨语种query-文档对的训练目标，校准多语种输入的语义相关性评分尺度，避免不同语种的语义评分偏差
- 第二阶段偏好对齐：联合ADR-MSE组排序损失保证语义正负样本的排序正确性，新增语言一致性损失，让同语种的语义等价文档排名高于其他语种的同语义文档，兼顾语义与语种匹配
- 训练数据基于MMARCO、MIRACL等公开多语种检索数据集构造，覆盖50+语种，兼顾低资源语种的适配效果

### 关键实验结果
- 语言一致性评测：在XQuAD（12语种）、BELEBELE（14语种）平行Oracle候选集上，仅0.6B参数的LAMAR nDCG@1分别达96.89、94.66，超过所有基线，包括1B参数的llama-nemotron-rerank
- 通用多语种重排评测：在MIRACL、XGLUE等5个MMTEB基准上平均nDCG@10达86.84，性能与1B+大参数重排器相当
- 实际检索场景：在bge-m3召回的Top20候选集上重排，所有指标均为最优

### 核心结论
多语种重排不能仅优化语义相关性，同语种一致性是提升多语种RAG系统效果的核心低成本优化点之一。
