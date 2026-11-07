---
title: 'StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Diffusion Models'
title_zh: StepX-OPD：扩散模型多教师在线策略蒸馏的重新思考
authors:
- Chenru Wang
- Xuanyang Zhang
- Yucheng Han
- Wenbo Nie
- Wei Cheng
- Xianfang Zeng
- Gang YU
- Chi Zhang
affiliations:
- StepFun
- Westlake University
arxiv_id: '2611.04386'
url: https://arxiv.org/abs/2611.04386
pdf_url: https://arxiv.org/pdf/2611.04386
published: '2026-11-02'
collected: '2026-11-07'
category: Training
direction: 扩散模型蒸馏 · 多教师训练优化
tags:
- Diffusion Model
- Knowledge Distillation
- On-Policy Distillation
- Text-to-Image
- Training Efficiency
one_liner: 融合扩散模型能力整合与少步蒸馏两阶段，4步采样效果超40步基线，训练成本降37%
practical_value: '- 多能力蒸馏可采用阶段融合方案，替代传统先整合能力再压缩的串行流程，降低训练等待周期与资源消耗

  - 低噪声区域单独回归速度项的trick可迁移到生成式推荐的扩散模型压缩场景，提升少步采样生成质量

  - 多教师蒸馏时需排查能力溢出问题（如生成冗余内容），可针对性加入正则项降低无关输出概率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文生图扩散模型落地需先通过多教师on-policy蒸馏整合指令跟随、文本渲染等能力，再做少步采样蒸馏，两阶段串行存在能力损失、训练周期长的缺陷。
### 方法关键点
1. StepX-OPD融合两阶段流程，学生模型同时学习多能力与少步采样，用冻结专家教师监督自身采样轨迹的状态而非未使用的长轨迹
2. 针对KL权重分解发现的低噪声区速度不匹配问题，单独对轨迹低噪声部分做速度回归
3. 给出优化变体解决多能力整合导致的无提示生成冗余文本问题
### 关键结果
在SD3.5-Medium、FLUX.1-dev两个底座上，4步采样归一化平均分高于所有对比4步方法，且超过40步Flow-OPD基线；SD3.5场景下训练GPU时耗比串行蒸馏方案低37%
