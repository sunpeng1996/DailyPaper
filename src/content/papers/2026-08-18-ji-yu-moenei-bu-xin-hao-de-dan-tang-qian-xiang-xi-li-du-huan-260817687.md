---
title: Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals
title_zh: 基于MoE内部信号的单趟前向细粒度幻觉检测方法
authors:
- Joao Fonseca
- Rodrigo Rodrigues
- Paolo Romano
affiliations:
- INESC-ID
- Instituto Superior Técnico
arxiv_id: '2608.17687'
url: https://arxiv.org/abs/2608.17687
pdf_url: https://arxiv.org/pdf/2608.17687
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: 大模型幻觉检测 · MoE内部信号挖掘
tags:
- MoE
- Hallucination Detection
- Per-token Detection
- Single Forward Pass
- LLM Internal Signal
one_liner: 提取MoE特有路由、专家激活等信号，实现单趟前向token级幻觉检测，性能超现有方案
practical_value: '- 业务侧用MoE LLM做生成式导购、商品文案、智能客服的团队，可直接复用MoE信号提取逻辑，加轻量分类器实现实时幻觉检测，3倍左右的latency
  overhead符合在线场景要求

  - 基于RAG的电商问答Agent可搭配token级检测，精准定位幻觉片段触发定向召回，比整句检测干预粒度更细，提升准确率的同时减少不必要的召回开销

  - 标注资源不足的场景可复用LLM-as-judge的token级标注流水线，自动生成幻觉标签迭代检测器，无需人工标注即可持续优化

  - MoE推理引擎开发团队可将这套信号集成到推理输出中，作为模型内置的可靠性指标，无需上层业务额外改造即可提供幻觉检测能力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM幻觉检测方案存在两大痛点：采样类方法需要多轮生成推理成本高，无法适配在线场景；内部信号类方法仅能做回答/句子级检测，无法定位细粒度幻觉片段，难以实现精准干预。MoE架构已成为大模型落地的主流选择，其路由机制产生的特有内部信号天然与token粒度对齐，且与认知不确定性高度相关，但此前未被用于幻觉检测。
### 方法关键点
- 特征体系：融合通用Transformer信号（隐藏层得分、注意力得分）与6种MoE特有信号（router entropy、专家隐藏层得分、专家相似度、专家使用分布、Gini impurity、逆Herfindahl指数），拼接为紧凑的token级特征向量
- 训练范式：采用LLM-as-judge自动标注流水线，对比生成回答与参考证据输出幻觉片段，自动映射为token级标签，无需人工标注即可训练LR、XGBoost、MLP等轻量分类器
- 推理逻辑：仅需单趟前向传播即可输出token级幻觉得分，无需修改原MoE模型结构，也无需额外采样
### 关键结果
在5个公开QA数据集、2个开源MoE模型（OLMoE-1B-7B、Gemma-4-26B）上对比全类别baseline，最高实现0.91回答级AUROC、0.76 token级AUROC，优于现有所有方案；推理开销仅为原生生成的3倍，远低于采样类方法。
> 最值得记住：MoE的路由激活信号天然携带认知不确定性信息，零改造即可实现低成本细粒度幻觉检测，性价比远超现有方案。
