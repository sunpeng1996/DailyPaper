---
title: 'La-JEPA: Compact Robot Policies with Latent World Modeling'
title_zh: La-JEPA：基于隐空间世界建模的紧凑机器人策略
authors:
- Mateo Clémente
- George Z. Xue
- Amin Abyaneh
- Liheng Ma
- Rui Heng Yang
- Tongtong Cao
- Zhanguang Zhang
- Yingxue Zhang
affiliations:
- Huawei Technologies Ltd.
- University of Toronto
- McGill University
- Mila – Quebec Artificial Intelligence Institute
arxiv_id: '2611.08156'
url: https://arxiv.org/abs/2611.08156
pdf_url: https://arxiv.org/pdf/2611.08156
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: 世界模型 · 紧凑控制策略设计
tags:
- JEPA
- World Model
- Robot Policy
- Latent Modeling
- Efficient Inference
one_liner: 提出无生成类预训练主干的轻量La-JEPA机器人策略，性能超同类大参数量方案
practical_value: '- 训练时新增未来特征预测辅助任务、推理时仅输出目标结果的架构设计，可复用在搜索推荐多任务训练场景，大幅降低推理延迟

  - 基于预训练大模型的特征空间从零训练小模型，可在参数量远低于大模型的前提下获得可比效果，适合电商端侧/低延迟推荐的轻量化模型设计

  - JEPA特征在OOD场景效果显著优于VAE隐特征的结论，可参考用于RAG、生成式推荐的召回向量选型'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有世界动作模型、视觉语言动作模型均基于生成类预训练Transformer主干，推理成本高，生成导向的架构设计是否适配控制任务的最优权衡尚不明确。
### 方法关键点
提出La-JEPA轻量世界动作模型，在预训练V-JEPA 2.1编码器的特征空间中从零训练策略Transformer，架构专门针对控制任务优化；训练时联合学习未来特征预测与动作预测，推理时跳过未来生成步骤仅输出动作。
### 关键结果数字
无具身预训练的策略中，在RoboTwin 2.0、修正指令的LIBERO-Plus数据集上达到SOTA，参数量远低于竞品；同等性能下推理速度远超Fast-WAM；4个真实机器人任务上平均成功率与pi0.5相当，优于所有非具身预训练基线；OOD场景下JEPA特征效果显著优于视频VAE隐特征。
