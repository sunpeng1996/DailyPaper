---
title: 'PhysOPSD: Code as Privilege for Physically Plausible Video Generation'
title_zh: PhysOPSD：以可执行代码为特权上下文的物理可信视频生成
authors:
- Harold Haodong Chen
- Rui Peng
- Lingteng Qiu
- Kejie Qiu
- Chao Xu
- Zilong Dong
affiliations:
- HKUST
- Alibaba Group
arxiv_id: '2611.12411'
url: https://arxiv.org/abs/2611.12411
pdf_url: https://arxiv.org/pdf/2611.12411
published: '2026-11-08'
collected: '2026-11-11'
category: Multimodal
direction: 多模态视频生成 · 物理约束对齐优化
tags:
- Video Generation
- On-Policy Self-Distillation
- Privileged Context
- Physical Plausibility
- Executable Code
one_liner: 提出以可执行代码为特权上下文的OPSD训练框架，提升视频生成物理合理性同时保留通用生成质量
practical_value: '- 电商商品短视频/3D动态展示场景可复用该思路，注入物理仿真代码约束生成内容的合理性，避免穿模、运动不符合常识的劣质素材

  - 可迁移「可执行代码作为特权上下文」的范式到Agent仿真训练中，解决传统RL奖励稀疏、SFT分布偏移的问题

  - 仅需3K样本即可对齐物理约束的蒸馏方法可复用在生成式内容的后调优化中，大幅降低训练成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成模型视觉保真度优异，但生成符合物理规律的动态交互场景效果差；SFT存在离线状态不匹配问题，RL面临物理奖励稀疏、定义模糊的痛点，常规OPSD框架缺少有效特权上下文设计，文本声明性不足、参考视频无法参数化控制物理规则。
### 方法关键点
1. 提出PhysOPSD框架，引入可执行代码作为特权物理上下文，通过PhysOPSD-Engine将真实物理场景转化为可验证的仿真程序
2. 设计双层物理特权机制通过中间瓶颈弥合信息差，在相同rollout噪声下引入可控物理变量暴露因果动态偏移
### 关键结果
仅用3K样本训练即可在各类骨干模型上显著提升物理合理性，效果优于SFT、RL基线，同时不损失通用视频生成质量
