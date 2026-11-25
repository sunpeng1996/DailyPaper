---
title: 'Distill to Loop: Turning Pretrained Diffusion Transformers into Looped Models
  with Adjustable Depth'
title_zh: Dooop：将预训练扩散Transformer转换为深度可调的循环模型
authors:
- Chenru Wang
- Shengwei An
affiliations:
- Virginia Tech
arxiv_id: '2611.31977'
url: https://arxiv.org/abs/2611.31977
pdf_url: https://arxiv.org/pdf/2611.31977
published: '2026-11-23'
collected: '2026-11-25'
category: Training
direction: 扩散Transformer · 知识蒸馏 · 循环模型优化
tags:
- Looped Transformer
- Knowledge Distillation
- Diffusion Transformer
- Parameter Efficiency
- Inference Optimization
one_liner: 基于知识蒸馏将预训练非循环扩散Transformer转为深度可调的循环模型，大幅降参降计算量且效果追平原模型
practical_value: '- 生成式推荐/广告素材生成场景可复用该蒸馏思路，将大参数量生成模型转为循环轻量模型，在保持效果的前提下降低推理成本，适配高QPS业务需求

  - 可复用「测试时灵活调整循环深度」的设计，根据业务 latency 要求动态调整计算量，兼顾峰值流量下的可用性与低峰期的生成效果

  - 跨步数循环指导的trick可迁移到多轮生成类任务（如文案迭代、多步推荐推理），用极小额外计算成本提升最终输出质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有循环扩散Transformer需从头训练，成本极高，而已有大量成熟预训练非循环扩散模型无法直接复用为循环结构，同时扩散模型推理成本高的问题也限制了业务落地。

### 方法关键点
提出Dooop蒸馏框架，将预训练非循环扩散Transformer的权重作为循环学生模型的初始化，将蒸馏过程建模为向教师模型收敛的不动点迭代，每轮循环对应深度维度的常微分方程（ODE）一步，测试时无需重训练即可调整循环次数，还可复用扩散采样的高阶ODE求解器提升效果；额外设计不同循环步数输出间的循环指导机制，几乎不增加计算即可优化生成效果。

### 关键结果数字
在SD3-medium上，参数量仅为教师37%的循环学生模型，跑2-4轮循环即可在GenEval、ImageReward等4个指标上平均效果追平教师，2轮循环时仅消耗教师58%的计算量；加入循环指导后，4步SD3-medium的4项指标平均分从88.2提升至99.2。
