---
title: 'FlowCPO: A Unified Divergence View of Preference Alignment for Flow Models'
title_zh: FlowCPO：面向流模型偏好对齐的统一散度视角方法
authors:
- Yansen Han
- Shengyi Liao
- Peng Sun
- Deyuan Liu
- Yuanxing Zhang
- Pengfei Wan
- Tao Lin
affiliations:
- Westlake University
- Zhejiang University
- Kuaishou Technology
arxiv_id: '2609.09905'
url: https://arxiv.org/abs/2609.09905
pdf_url: https://arxiv.org/pdf/2609.09905
published: '2026-09-09'
collected: '2026-09-10'
category: Training
direction: 生成模型训练 · 偏好对齐优化
tags:
- Preference Alignment
- Flow Matching
- Diffusion Model
- Offline Training
- KL Divergence
one_liner: 提出无需在线采样的流对比偏好优化方法，统一流模型偏好对齐散度框架，域内效果优于FlowDPO
practical_value: '- 电商多模态生成场景（如商品图、营销文案/短视频生成）做偏好对齐时，可复用FlowCPO双分支架构，无需在线采样就能同时利用偏好/非偏好样本，降低训练成本的同时提升域内生成效果

  - 可直接复用论文给出的最优超参组合：β取0.5~1.0、负样本权重λ=1、EMA动量η=0.99，避免负正则强度过高导致训练崩溃

  - 若你的偏好数据来自其他模型（跨域/OOD场景），不建议使用FlowCPO，此时仅用正样本的RFT在 reward 类指标上表现更优

  - 做离散序列（如推荐query、营销文案）的偏好对齐时，可迁移其散度统一框架，对比不同KL方向+采样模式的组合，快速找到适配业务的最优对齐范式'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有流模型/扩散模型的偏好对齐方法分为两类：在线RL类需要实时从当前模型采样，训练成本极高；离线类要么仅用正样本微调，要么采用DPO类似然比代理目标，不同方法间的理论关联不清晰，且简化版FlowDPO的损失存在无下界问题，训练稳定性差，亟需统一理论框架指导离线偏好对齐方法设计。
### 方法关键点
- 构建基于散度的统一分类框架，将现有流对齐方法按「采样模式（在线/离线）」+「KL散度方向（正向/反向）」两个维度划分，填补了离线正向KL范式的空白
- 提出双分支FlowCPO目标：用冻结参考生成器产出固定的偏好/非偏好样本对，正分支拟合偏好样本的流场，镜像分支拟合非偏好样本的流场，全程无需在线采样
- 理论证明线性插值场景下正向KL目标可由对比流匹配损失上界约束，损失始终非负，从根源避免了简化版FlowDPO损失无下界的不稳定问题
### 关键实验
基于Stable Diffusion 3.5开展实验，对比RFT、FlowDPO两大基线：域内场景下CFG=3.0时，FlowCPO的GenEval得分达0.84、OCR得分达0.87，分别比FlowDPO高0.03、0.12，通用偏好指标也整体最优；跨域场景下FlowCPO的GenEval仍最优，但reward类指标劣于RFT。
### 核心结论
离线偏好对齐时，域内数据用同时利用正负样本的正向KL双分支方法收益最高，跨域数据优先选用仅正样本的RFT避免分布偏移带来的效果下降。
