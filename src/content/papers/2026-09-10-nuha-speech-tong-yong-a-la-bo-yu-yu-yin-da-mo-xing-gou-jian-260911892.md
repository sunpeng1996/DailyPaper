---
title: 'Nuha-Speech: Building General-Purpose Arabic Speech-LLMs'
title_zh: Nuha-Speech：通用阿拉伯语语音大模型构建方案
authors:
- Yingzhi Wang
- Reem Alhazzani
- Muhammad Alqurishi
affiliations:
- Elm Company, KSA
arxiv_id: '2609.11892'
url: https://arxiv.org/abs/2609.11892
pdf_url: https://arxiv.org/pdf/2609.11892
published: '2026-09-10'
collected: '2026-09-12'
category: LLM
direction: 小语种语音大模型全链路研发
tags:
- Speech-LLM
- Arabic NLP
- Instruction Tuning
- SQA Corpus
- Multilingual LLM
one_liner: 打造覆盖数据集、训练、评估全链路的阿拉伯语通用语音大模型方案，含150万+语音问答语料
practical_value: '- 跨境电商/多语种语音交互业务落地小语种语音能力时，可复用「开源基座+垂直指令微调+定制评估」的全链路框架，降低从零研发成本

  - 低资源语种垂直大模型研发可参考大规模领域SQA语料构建思路，快速对齐基座的场景适配能力

  - 多语种语音客服、语音搜索等Agent类场景，可直接基于该方案迭代阿拉伯语语音理解与交互能力'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前多语种Speech-LLM对阿拉伯语支持严重不足，现有阿拉伯语语音大模型任务覆盖窄、依赖私有数据集、零样本泛化能力弱，缺乏完整的训练与评估基础设施。
### 方法关键点
1. 构建超150万样本的大规模阿拉伯语语音问答（SQA）语料，覆盖多类核心语音任务的instruction tuning需求；
2. 基于不同参数规模的Qwen-Omni基座开展监督微调，适配阿拉伯语语音交互场景；
3. 设计包含多类型任务、定制化评估指标的统一评测框架。
### 关键结果
在阿拉伯语语音资源受限的条件下，搭建了从数据到训练、评估的完整阿拉伯语通用Speech-LLM研发基础设施，填补了领域相关空白。
