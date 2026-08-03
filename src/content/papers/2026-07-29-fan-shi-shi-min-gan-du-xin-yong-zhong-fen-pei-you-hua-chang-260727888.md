---
title: 'Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit Reallocation
  for Long-CoT Reasoning'
title_zh: 反事实敏感度信用重分配：优化长CoT推理的token级奖励分配
authors:
- Qiangqiang He
- Zhongheng Wu
- ZiJian Wang
affiliations:
- 南京大学
- 上海交通大学
arxiv_id: '2607.27888'
url: https://arxiv.org/abs/2607.27888
pdf_url: https://arxiv.org/pdf/2607.27888
published: '2026-07-29'
collected: '2026-08-03'
category: Reasoning
direction: 长CoT推理 · GRPO信用分配优化
tags:
- CoT
- GRPO
- RLVR
- Credit Assignment
- Reinforcement Learning
one_liner: 基于反事实敏感度对GRPO做token级奖励重分配，稳定提升长CoT数学推理性能
practical_value: '- 生成式推荐/Agent推理的RL训练可复用CSCR思路，对语义关键token（如商品属性、推理步骤）和表面token（如连接词、语气词）做差异化加权，避免平均分配奖励浪费优化效率

  - RLHF类训练不要直接用OPSD的likelihood shift做监督信号，其极性和结果一致性仅58%左右，优先保留验证器给出的全局方向，仅用likelihood
  shift做权重调制

  - 长序列生成RL优化中，可采用相同的反事实敏感度分析方法，快速定位对条件反馈敏感但对最终结果无实质贡献的噪声token做降权处理

  - 电商导购Agent长CoT训练可直接复用CSCR的权重计算逻辑，仅需调整阈值λ适配业务场景的token敏感分布，无需额外标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前基于可验证奖励的强化学习（RLVR）做长CoT训练时，GRPO把序列级奖励均匀分配给所有token，忽略不同token对最终结果的贡献差异；OPSD类自蒸馏方法默认特权条件下的似然偏移是可靠的答案对齐信号，但该假设从未被验证，实际训练中经常出现优化不稳定甚至性能下降的问题。

### 方法关键点
- 构造正负两极的反事实特权提示，对同一采样轨迹分别重打分，计算每个token的反事实敏感度（两个条件下似然偏移的最大值）
- 对高敏感度token做指数级降权，低敏感度token保留全权重，加权后做序列内归一化，保证全局奖励预算和验证器给出的优化方向不变
- 仅对GRPO做最小修改，无需额外标注、价值模型或教师模型，训练成本几乎无增加

### 关键结果
在DAPO-17K数据集上训练，对比GRPO、OPSD、SDPO等6个基线，在AMC23、AIME24-26、SMT25共5个长CoT数学推理基准上，Qwen3-1.7B版本平均比GRPO高6.06分，Qwen3-4B版本平均比GRPO高3.74分，所有模型-基准组合均取得最优结果。

### 核心结论
91.4%-95.8%的token在正负反事实条件下的似然偏移方向一致，特权条件下的似然偏移更多反映token对条件的敏感度而非对结果的贡献，无法作为可靠的方向监督信号。
