---
title: 'CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation'
title_zh: CoMet：基于上下文与多样性分解的多模态不确定性估计方法
authors:
- Sanghyuk Chun
- William Yang
- Amaya Dharmasiri
- Olga Russakovsky
affiliations:
- Princeton University
arxiv_id: '2606.32012'
url: https://arxiv.org/abs/2606.32012
pdf_url: https://arxiv.org/pdf/2606.32012
published: '2026-06-30'
collected: '2026-07-01'
category: Multimodal
direction: 多模态大模型 · 不确定性估计
tags:
- Multimodal LLM
- Uncertainty Estimation
- Hallucination Detection
- Post-hoc Module
- Efficient Inference
one_liner: 将多模态大模型不确定性拆分为两类独立项，通过轻量后验模块实现无需采样的高效不确定性估计
practical_value: '- 多模态生成式推荐、电商图文问答Agent场景可复用不确定性拆分思路，分别评估prompt歧义度与候选答案合理数量，替代高成本的多次采样熵计算方案

  - 轻量后接不确定性模块的架构适配成本极低，可基于现有MLLM基座增量训练，无需改动基座权重，适合快速上线商品问答幻觉筛查能力

  - 输出的不确定性分数可直接作为推荐/Agent回答的兜底阈值，低于置信度要求时触发RAG校验或转人工审核，降低多模态推荐的错误率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
多模态大模型（MLLM）在开放场景下不确定性来源复杂，既可能来自上下文/prompt本身的歧义，也可能来自输入对应的多候选答案多样性，现有主流方案依赖多次采样或自回归生成完整答案，计算成本高，无法满足业务实时性要求。
### 方法关键点
提出CoMet不确定性估计框架，将整体不确定性拆解为两类独立可量化项：上下文相关项捕捉prompt/任务本身的固有歧义性，多样性相关项统计当前输入下符合上下文约束的合理答案数量；仅训练一个轻量后验模块直接拟合两类不确定性，无需生成完整答案或重复采样，推理 overhead 极低。
### 关键结果
在开放多模态基准、幻觉检测、视觉问答多选基准上，不确定性估计效果全面优于现有基线方法，同时推理效率较采样类方案提升1个数量级以上。
