---
title: 'Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End
  Autonomous Driving'
title_zh: 离散推理到连续动作：端到端自动驾驶的隐空间对齐规划框架
authors:
- Ruoyu Yao
- Yusen Xie
- Qingzhao Liu
- Pei Liu
- Zewei Yang
- Yipeng Zhu
- Xiaolong Wang
- Jun Ma
arxiv_id: '2609.04070'
url: https://arxiv.org/abs/2609.04070
pdf_url: https://arxiv.org/pdf/2609.04070
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 多模态VLA · 隐空间对齐动作生成
tags:
- VLA
- VQ-VAE
- latent alignment
- motion planning
- multimodal reasoning
one_liner: 提出隐空间对齐的VLA框架LaPla，解决VLM离散推理与自动驾驶连续动作的模态鸿沟，实现性能与延迟双重提升
practical_value: '- 预训练VQ-VAE隐空间对齐、跳过离散codebook查表的思路，可迁移到GenRec场景，将离散Semantic ID映射为连续隐空间特征，消除ID检索量化误差，提升生成推荐准确率

  - 并行动作查询单步前向推理替代自回归生成的设计，可复用在实时推荐、广告排序的大模型推理链路，大幅降低推理延迟、提升吞吐

  - 冻结预训练解码器实现语义隐态到可执行动作的映射范式，可用于Agent执行器开发，对齐LLM语义输出与业务动作空间，减少语义到动作的落地gap'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VLM的离散推理能力难以适配自动驾驶等需要输出连续、物理约束动作的场景，传统VLA方案采用离散codebook映射易引入量化误差，自回归生成也存在推理延迟高的问题。
### 方法关键点
1. 基于残差VQ-VAE构建动作tokenizer，将车辆轨迹特征编码到结构化隐空间，作为物理先验桥接高维语义与原始动作空间的模态gap
2. 提出LaPla统一VLA框架，输入多视角图像、历史动作、文本指令等多模态数据，通过并行动作查询单步前向注意力建模上下文，直接将隐态投影到预训练VQ-VAE的连续隐空间
3. 采用冻结的VQ-VAE解码器将连续隐态转换为可执行动作，跳过离散查表与自回归生成流程，消除量化误差的同时降低延迟
### 关键结果
- nuScenes基准开环测试：长时序L2误差较SOTA VLA方法降低15.52%
- NVIDIA AlpaSim闭环测试：驾驶成功率提升33.34个百分点，推理延迟显著降低
