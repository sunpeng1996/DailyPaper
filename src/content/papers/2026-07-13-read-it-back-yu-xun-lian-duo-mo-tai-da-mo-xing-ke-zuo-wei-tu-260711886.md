---
title: 'Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image
  Generation'
title_zh: 《Read It Back：预训练多模态大模型可作为文生图零样本奖励模型》
authors:
- Runhui Huang
- Qihui Zhang
- Zhe Liu
- Yu Gao
- Jie Wu
- Hengshuang Zhao
affiliations:
- The University of Hong Kong
- ByteDance Seed
- Peking University
arxiv_id: '2607.11886'
url: https://arxiv.org/abs/2607.11886
pdf_url: https://arxiv.org/pdf/2607.11886
published: '2026-07-13'
collected: '2026-07-15'
category: Multimodal
direction: 多模态大模型 · 零样本奖励模型构建
tags:
- MLLM
- Reward Model
- Zero-Shot
- Text-to-Image
- Reinforcement Learning
one_liner: 提出无训练SpectraReward，通过生成图反向恢复prompt的对数似然作为文生图RL的奖励信号
practical_value: '- 电商商品图/营销文案等生成类任务做RL对齐时，可直接复用预训练MLLM/LLM，通过生成结果反向恢复原始prompt的对数似然作为零样本奖励，省去偏好标注和奖励模型微调成本

  - 自研统一多模态/大模型架构可复用自身理解分支作为生成分支的奖励模型，形成闭环自优化，无需引入外部大模型，降低部署与推理开销

  - 做RLHF类优化时不要盲目堆奖励模型参数量，优先保障奖励模型与生成策略的对齐度，可获得更高投入产出比'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：文生图RL优化高度依赖高质量奖励模型，现有基于MLLM的奖励方案需要人工偏好标注、单独微调奖励模型，成本高且推理效率低。
**方法关键点**：1. 提出训练无关的SpectraReward，仅通过单步图像条件teacher-forced前向传播，计算生成图像恢复原始prompt的平均对数似然作为奖励，直接复用MLLM预训练图文对齐能力，无额外数据与训练开销；2. 衍生Self-SpectraReward，统一多模态模型可复用自身理解分支作为生成分支的奖励，形成无外部依赖的自优化闭环。
**关键结果**：在2个扩散模型、3种RL算法、9款4B~235B参数量MLLM backbone、5个分布外文生图基准上验证，性能显著优于现有MLLM衍生奖励方案；更大的奖励MLLM不一定效果更好，Self-SpectraReward可匹配甚至超越参数量远大于自身的外部奖励模型，奖励与策略对齐度是文生图RL的核心影响因素。
