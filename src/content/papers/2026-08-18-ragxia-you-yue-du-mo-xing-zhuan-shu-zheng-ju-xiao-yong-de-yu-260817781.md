---
title: 'Preference Is Not Intervention: The Structure and Stability Boundaries of
  Reader-Specific Evidence Utility'
title_zh: RAG下游阅读模型专属证据效用的结构与稳定性边界研究
authors:
- Shi Zhou
affiliations:
- College of Software, Jilin University
arxiv_id: '2608.17781'
url: https://arxiv.org/abs/2608.17781
pdf_url: https://arxiv.org/pdf/2608.17781
published: '2026-08-18'
collected: '2026-08-19'
category: RAG
direction: RAG 下游模型个性化证据选择
tags:
- RAG
- Evidence Utility
- Reader Personalization
- Stability Boundary
- Preference Decomposition
one_liner: 控变量证实RAG证据效用的下游模型特异性，拆解序数偏好稳定、干预方向跨任务有界的核心规律
practical_value: '- 做多LLM路由的RAG系统时，优先落地证据序数偏好级的下游模型个性化排序，该模块跨query稳定性达ρ=0.6~0.83，投入产出比远高于帮助/伤害判定级的个性化

  - 二分类事实核验类RAG场景（如商品真伪校验、投诉内容真实性判定）可复用跨query的证据符号判定，该类任务下符号稳定性达0.75；但开放域QA场景（如商品咨询答疑）不要跨query复用符号判定，尤其是误导、无关证据的符号基本为query局部属性

  - RAG效果评估不能仅依赖NDCG、Spearman相关等排序类指标，这类指标仅能反映序数偏好稳定性，上线后的证据留存/剔除决策（依赖符号方向）可能完全不达预期，需额外增加稀疏校准后的符号效用跨query稳定性校验

  - 跨LLM迁移RAG证据选择策略时，不要依赖模型间的序数偏好相似度，实验验证该相似度与迁移效果无相关性（ρ=-0.27，不显著），直接做目标模型的轻量效用微调投入产出比更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前RAG系统普遍探索下游LLM专属的证据优化策略，但现有研究混淆了任务、模型结构等干扰变量，无法明确下游模型本身的证据效用差异是可跨query复用的稳定属性，还是仅为query绑定的局部交互，直接影响个性化RAG的落地可行性。
### 方法关键点
- 严格控制变量：固定query、证据、任务、评分规则、干预逻辑，仅改变下游reader（LLM部署实例）身份测度证据效用
- 效用三维度拆解：将reader特异性效用拆分为activity（证据是否产生影响）、ordinal preference（证据效用相对排序）、conditional signed direction（证据帮助/损害的符号方向，仅统计对双reader都有效的样本）
- 稳定性校准机制：用split-half可靠性度量跨query稳定性，引入稀疏匹配的permutation空基线，排除稀疏性、解码噪声、度量偏差对结果的干扰
### 关键结果
基于9个不同规模、部署方式的reader，在NQ/HotpotQA、RAMDocs、RAGuard、PRISM四个独立场景测试：
- 33%的双有效样本中，不同reader对证据的效果符号判定完全相反；reader×query交互解释29.8%的效用方差，远高于8.4%的permutation空基线
- ordinal preference跨所有场景稳定性达ρ=0.60~0.83，稳定可复用；开放域QA下符号方向稳定性仅0.14~0.35，远低于稀疏匹配的空基线，二分类事实核验下符号稳定性高达0.75，与序数偏好无显著差距
- 开放域QA中误导性、无关证据的符号稳定性仅0.1左右，无跨query复用价值
### 核心结论
Preference is not intervention：稳定的序数偏好相似度既不能支撑跨reader的干预决策迁移，也不能证明帮助/损害方向的稳定性。
