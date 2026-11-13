---
title: 'eDMD: Endpoint Distribution Matching for Few-Step Diffusion Distillation'
title_zh: 《eDMD：面向少步扩散蒸馏的端点分布匹配方法》
authors:
- Tong Zhao
- Xianfang Zeng
- Yucheng Han
- Ruoyu Wang
- Mingkun Lei
- Gang Yu
- Chi Zhang
affiliations:
- 浙江大学
- 西湖大学AGI实验室
- StepFun
arxiv_id: '2611.17194'
url: https://arxiv.org/abs/2611.17194
pdf_url: https://arxiv.org/pdf/2611.17194
published: '2026-11-12'
collected: '2026-11-13'
category: Training
direction: 扩散模型 · 少步蒸馏效率优化
tags:
- Diffusion Distillation
- Distribution Matching
- Few-step Generation
- Training Efficiency
- Score Distillation
one_liner: 提出仅基于学生最终输出训练fake模型的少步扩散蒸馏方法，4步生成效果全面超越现有SOTA
practical_value: '- 做电商生成式物料（商品图、营销海报、虚拟人素材）的少步扩散蒸馏时，可直接复用eDMD的端点训练逻辑，fake模型仅用最终输出训练，避免中间态干扰，大幅提升少步生成质量

  - 教师监督优化可借鉴Precise Teacher思路，低噪声区间用教师短多步轨迹替代单步预测，不增加学生推理成本的前提下提升训练阶段的监督精度

  - 多步蒸馏的中间步查询采样可参考校准查询密度方案，优先选择教师预测一致性高的噪声区间采样，减少不可靠监督对训练的干扰'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有多步DMD扩散蒸馏方法将中间态纳入fake模型训练，导致学生更新信号与中间分布纠缠，即使最终输出分布已匹配教师，仍会收到非零梯度推离最优解，少步生成的细节还原能力和结构准确性受限，难以满足业务低时延生成需求。

### 方法关键点
- 端点分布匹配：仅用学生最终生成输出来训练共享fake模型，消除参考残差，理论证明仅当最终输出分布匹配教师时分布匹配项才会消失，不受中间态分布影响
- 精准教师（PT）：低噪声区间用教师的短多步生成轨迹替代单步预测，提供更精准的监督信号，不增加学生推理成本
- 校准查询密度：预计算教师不同噪声层级的预测一致性，中间步查询优先采样一致性高的区间，减少不可靠监督干扰

### 关键实验
在SD3-Medium、FLUX.2-klein 4B/9B、Qwen-Image-2.1四个主流扩散骨干上做4步蒸馏，对比DMD2、TDM、D-DMD、CDM等SOTA基线：FLUX.2-klein 4B上HPSv3++达12.699，比基线最高提升1.909；FLUX.2-klein 9B上HPSv3++达12.431，比基线最高提升1.106，所有骨干上的人类偏好、细节还原、结构准确性均全面领先。

最值得记住的一句话：多步蒸馏的监督目标必须严格对齐最终交付的输出分布，对中间态的额外约束反而会限制少步生成的效果上限
