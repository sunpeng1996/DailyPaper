---
title: 'VDOT++: Unified Few-Step Video Generation via Unbalanced Optimal Transport
  Distillation'
title_zh: VDOT++：基于非平衡最优传输蒸馏的统一少步视频生成
authors:
- Yutong Wang
- Xingtong Ge
- Enhuai Liu
- Yunke Wang
- Tianfan Xue
- Yu Qiao
- Yaohui Wang
- Xinyuan Chen
- Chang Xu
arxiv_id: '2610.03221'
url: https://arxiv.org/abs/2610.03221
pdf_url: https://arxiv.org/pdf/2610.03221
published: '2026-10-02'
collected: '2026-10-05'
category: Other
direction: 扩散模型蒸馏 · 少步视频生成
tags:
- Video Diffusion
- Optimal Transport
- Distillation
- Few-step Sampling
- Generative Model
one_liner: 提出非平衡最优传输蒸馏框架，实现三类任务下的4步高性能视频生成
practical_value: '- 非平衡OT蒸馏思路可迁移到生成式推荐扩散模型的少步采样加速，解决师生分布重叠度低时的蒸馏不稳定问题

  - L1 ground cost + 加权中位数聚合的trick可复用在多模态生成任务的蒸馏Loss优化，降低离群点对训练的干扰

  - 跨尺度蒸馏（大打分网络赋能小生成器）方案可直接借鉴到端侧生成类业务的小模型迭代，大幅降低推理成本

  - 统一蒸馏范式的设计思路可参考用于构建覆盖文案/海报/视频的多模态营销内容生成流水线'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频扩散模型采样需多次调用大骨干，推理成本高；传统DMD蒸馏的反向KL目标在师生分布重叠低时指导不稳定；平衡OT蒸馏要求逐帧空间token全匹配，不符合T2V/I2V单条件多输出的特性。
### 方法关键点
1. 采用非对称非平衡OT蒸馏，允许不可靠学生token分配更低权重，同时保证教师token覆盖度，适配多输出场景；
2. 替换均值聚合为L1 ground cost驱动的坐标级加权中位数，抑制远距传输目标干扰；
3. 融合分布匹配与对抗优化，引入跨尺度蒸馏用大打分网络提升小生成器效果，统一支持T2V/I2V/条件生成三类任务。
### 关键结果
4步采样生成器在UVCBench、VBench等4个基准上效果媲美多步教师模型，性能超过现有少步SOTA基线。
