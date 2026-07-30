---
title: 'CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization'
title_zh: CoRT：面向评分规则引导策略优化的Token级反事实回放方法
authors:
- Bo-Wen Zhang
- Junwei He
- Wen Wang
- Song-Lin Lv
- Wentao Ma
- Rongyi Lin
- Shuhan Zhong
- Lan-Zhe Guo
affiliations:
- 南京大学
- 字节跳动
- 中国科学院大学
arxiv_id: '2607.25659'
url: https://arxiv.org/abs/2607.25659
pdf_url: https://arxiv.org/pdf/2607.25659
published: '2026-07-27'
collected: '2026-07-30'
category: Training
direction: LLM训练 · GRPO信用分配优化
tags:
- GRPO
- Policy Optimization
- Credit Assignment
- Counterfactual Reasoning
- RLHF
one_liner: 通过反事实回放实现Token级信用分配，无额外模块提升GRPO训练效果
practical_value: '- 做生成式推荐/电商文案/Query改写的GRPO对齐时，可直接接入CoRT，仅新增一次无rubric的前向打分，无需额外标注或辅助模型，即可提升约束满足率

  - 业务中有明确生成rubric（如必须包含促销词、字数限制、格式要求）的RL训练场景，均可复用CoRT的反事实对比思路，把响应级奖励精准分配到关联token

  - CoRT的SmoothStep权重调度+响应级归一化trick可直接复用在所有token级加权的RL流程中，避免训练梯度不稳定、权重漂移问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有rubric引导的GRPO类RL训练流程会将结构化的多维度评分压缩为单响应级标量奖励，均匀广播到所有生成token，完全浪费了rubric中隐含的token级归因信息；而现有token级信用分配方案需要额外训练辅助打分模型，增加了流程复杂度和标注成本，不适用于大规模落地。

### 方法关键点
1. 反事实打分：对同一条采样响应，分别在带rubric的原prompt、移除rubric的反事实prompt下做前向推理，得到每个token的两个对数似然值，差值即为该token对rubric的依赖度
2. 权重映射与归一化：将似然差值映射到有界区间后做响应级归一化，保证单条响应内token平均权重为1，不改变原响应级奖励的整体规模与更新方向
3. 平滑调度：用SmoothStep函数逐步启用token加权，避免训练初期奖励统计不稳定导致的梯度爆炸
4. 优势重分配：将原GRPO的响应级advantage乘以对应token的权重后更新策略，全程无需额外标注、辅助模型或额外生成步骤

### 关键结果
基于HIR-16k数据集训练，在4B/7B/14B参数量模型、CSR/AON两种奖励模式下，平均比基线GRPO提升4.4个百分点，在MultiDimIF约束满足任务上最高提升11.85个百分点，效果优于需要额外训练token级判别器的RTT方法，同时兼容DAPO、GSPO等其他策略优化算法。

**最值得记住的结论**：无需额外标注或辅助模块，仅利用模型自身对输入上下文的敏感性差异，就能实现高效的token级信用分配，大幅降低rubric引导RL的落地成本。
