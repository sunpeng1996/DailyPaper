---
title: 'MMOE: Modernizing Diffusion Transformers with Efficient Expert Design'
title_zh: MMOE：基于高效专家设计的扩散Transformer优化架构
authors:
- Yanhao Jia
- Jiepeng Wang
- Haibin Huang
- Chi Zhang
- Erik Cambria
- Xuelong Li
affiliations:
- Nanyang Technological University
- China Telecom TeleAI
arxiv_id: '2607.24665'
url: https://arxiv.org/abs/2607.24665
pdf_url: https://arxiv.org/pdf/2607.24665
published: '2026-07-27'
collected: '2026-07-28'
category: Training
direction: 生成式模型 · MoE效率优化
tags:
- MoE
- Diffusion Transformer
- Efficient Training
- Expert Routing
- AIGC
one_liner: 将LLM成熟MoE效率机制迁移到扩散Transformer，单8卡H100下实现更优质效比
practical_value: '- 做生成式推荐、电商AIGC素材模型的MoE优化时，可直接复用轻量零计算专家（copy/zero/constant）设计，减少无效MLP计算，降显存提推理速度，适配低算力部署场景

  - 门控残差路由+跨层注意力残差复用的组合设计，可直接迁移到大模型精调、多模态生成模型训练场景，加速收敛，降低训练成本

  - 无需盲目扩大MoE总参数量和稀疏度，将LLM领域已验证的效率机制适配到业务生成类模型，可在可控预算下拿到更好的质效比'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前扩散Transformer的MoE优化普遍走堆总参数量、提高稀疏度的路线，没有引入LLM领域已经验证的效率机制，导致训练部署成本高、质效比失衡，中小算力预算下很难落地，需要探索更平衡的AIGC模型缩放路径。
### 方法关键点
- 基于SiT结构的扩散Transformer进行模块化升级，不改变原有扩散目标、采样器和对外接口，可无缝兼容现有扩散模型训练流程
- 引入MoE++的轻量零计算专家（copy、zero、constant），搭配门控残差路由，允许token选择低成本变换路径，减少无效MLP计算
- 新增跨层注意力残差聚合机制，允许后续层复用前面完成层的特征，优化信息流动，提升收敛速度
### 关键实验结果
所有实验均在单8卡H100节点训练，batch size 256，训练400k步，在ImageNet-256分类生成任务上，对比dense SiT、标准MoE、SMOE、MoE++、AMOE基线：400k步时MMOE的FID达到3.75，比dense SiT低27.9%；比性能接近的AMOE训练时间从120h压缩到67h，单块前向显存降低20%，反向显存降低32%，在所有稀疏变体中取得最优质效比。

最值得记住的一句话：AIGC模型的MoE升级不需要盲目堆叠参数量，将LLM领域经过验证的效率机制适配过来，就能在可控预算下实现更好的质效平衡。
