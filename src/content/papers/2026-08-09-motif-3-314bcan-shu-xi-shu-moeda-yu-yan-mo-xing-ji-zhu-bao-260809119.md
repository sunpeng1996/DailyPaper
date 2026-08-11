---
title: 'Motif 3: Technical Report'
title_zh: Motif 3：314B参数稀疏MoE大语言模型技术报告
authors:
- Junghwan Lim
- Joon Son Chung
- Sungmin Lee
- Wai Ting Cheung
- Gihun Cho
- Minsu Ha
- Sangho Kang
- Beomgyu Kim
- Dongseok Kim
- Jangwoong Kim
affiliations:
- Motif Technologies
arxiv_id: '2608.09119'
url: https://arxiv.org/abs/2608.09119
pdf_url: https://arxiv.org/pdf/2608.09119
published: '2026-08-09'
collected: '2026-08-11'
category: LLM
direction: 大语言模型 · 稀疏MoE架构优化
tags:
- MoE
- LLM
- Attention Optimization
- Long Context
- Training Efficiency
- KV Cache
one_liner: 推出总参314B、单token激活13.2B的稀疏MoE大模型，在Agent、推理等任务达开源领先水平
practical_value: '- GDLA注意力结构可直接复用：结合差分注意力降噪能力与latent KV压缩优势，降低KV cache占用同时提升注意力准确性，适配长上下文用户行为序列建模的推荐/Agent场景

  - 专家专属PolyNorm激活可替换SwiGLU：做MoE结构的LLM4Rec/多场景Agent时，每个专家可自适应路由到的token分布，大幅降低专家坍缩概率

  - 长上下文训练的窗口感知并行策略可迁移：滑动窗口层用Ring Attention、全注意力层用Ulysses，256K上下文下训练效率提升显著，适合长会话推荐大模型微调工程

  - 多教师On-Policy蒸馏方案可复用：将多个垂直领域专家能力合并到统一模型，适配电商搜/推/广多场景统一大模型的能力融合需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前开源大模型与闭源模型仍存在明显能力差距，MoE架构可在不显著提升单token算力的前提下扩展模型容量，但大规模MoE训练普遍存在稳定性差、专家坍缩、长上下文支持难、KV cache占用高等痛点，亟需更高效的架构设计与工程训练方案。

### 方法关键点
- 架构：总参314B、单token激活13.2B的decoder-only MoE，每层配置384个路由专家，仅选择8个激活；核心采用GDLA注意力，融合分组差分注意力的降噪能力与MLA的低KV cache优势，同时搭配改良的流形约束超连接、专家专属PolyNorm激活、多token预测辅助目标，原生支持256K上下文。
- 训练：基于12.5万亿token多域语料预训练，采用分层专家负载均衡、MXFP8选择性量化、Muon优化器、窗口感知上下文并行等工程方案，解决大规模MoE训练不稳定问题；后训练阶段引入6个RL训练的专项教师+1个SFT软件工程教师，通过多教师On-Policy蒸馏将多领域能力整合到统一模型。

### 关键结果
GDLA相比MLA少用9.2%的训练token即可达到loss 3.2；模型在长周期Agent任务、数学推理、科学知识、低幻觉评估上达到开源领先水平，最大上下文窗口支持256K。

### 核心结论
MoE架构的性能上限不仅来自参数量与数据规模，更依赖细粒度的架构设计、稳定的大规模训练工程方案，以及多教师蒸馏的能力整合策略。
