---
title: Fast Multi-dimensional Refusal Subspaces via RFM-AGOP
title_zh: 基于RFM-AGOP的大模型多维拒绝子空间快速提取方法
authors:
- Thomas Winninger
affiliations:
- Télécom SudParis
- ENS Paris-Saclay
arxiv_id: '2607.02396'
url: https://arxiv.org/abs/2607.02396
pdf_url: https://arxiv.org/pdf/2607.02396
published: '2026-07-02'
collected: '2026-07-03'
category: LLM
direction: 大模型可解释性 · 拒绝子空间提取
tags:
- Mechanistic Interpretability
- Refusal Subspace
- RFM
- AGOP
- LLM Safety
- Activation Steering
one_liner: 带探针初始化的RFM-AGOP秒级提取LLM多维拒绝子空间，效果优于现有方法
practical_value: '- 做Agent/生成式推荐的合规管控时，可复用该方法快速提取违规内容生成、敏感请求拒绝的特征子空间，通过激活投影实现低开销的实时内容拦截，无需重训练对齐

  - 复用探针初始化+EMA平滑的trick优化RFM类特征提取方法的收敛稳定性，降低调参成本，适配业务侧自定义行为（如拒绝推荐低质量内容）的子空间提取需求

  - 针对大参数LLM做行为干预时，优先考虑多维子空间建模而非单向量控制，避免因模型规模上升导致的干预效果失效'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有单维拒绝方向无法覆盖大模型复杂的拒绝行为，而主流多维拒绝子空间提取方法（如RCO）依赖大量梯度迭代，计算成本极高，在生成长推理链的大模型上几乎不可落地，亟需低成本、高效的子空间提取方案。

### 方法关键点
- 适配RFM-AGOP框架，引入线性探针初始化+AGOP更新的EMA平滑策略，解决原生RFM收敛对噪声敏感、易卡在单维子空间的问题
- 用多语种有害/无害对比数据集提取对应层最后token的残差流激活，训练后取特征矩阵Top-k特征向量构建拒绝子空间
- 消融/干预时按特征值加权投影，最小化对模型通用推理能力的 collateral damage

### 关键实验结果
在Qwen 2.5 7B、Qwen 3全系列（1.7B~14B）上测试，对比DIM、RCO、Clusters三类基线：
1. 速度上，单RTX4090笔记本秒级完成子空间提取，比RCO的小时级耗时快3个数量级以上
2. 效果上，Qwen 3 8B消融前3个拒绝方向后攻击成功率（ASR）达62%，远超RCO基线的28%，同时MMLU评分基本无下降
3. 大参数模型（≥8B）的拒绝行为必须用多维子空间建模，单维干预的ASR不足10%，完全无法生效

### 核心结论
大模型的复杂行为随参数规模提升呈现更高的子空间维度，单维特征干预的有效性会随模型增大快速下降
