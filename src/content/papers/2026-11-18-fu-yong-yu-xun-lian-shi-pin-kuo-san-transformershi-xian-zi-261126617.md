---
title: 'One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised
  Latent Action Learning'
title_zh: 复用预训练视频扩散Transformer实现自监督隐式动作学习
authors:
- Yuxin Jiang
- Wenqiang Sun
- Jiaqi Li
- Yuchao Gu
- Lvmin Zhang
- Ivor Tsang
- Mike Zheng Shou
affiliations:
- National University of Singapore
- A*STAR Singapore
- Tencent
- Stanford University
arxiv_id: '2611.26617'
url: https://arxiv.org/abs/2611.26617
pdf_url: https://arxiv.org/pdf/2611.26617
published: '2026-11-18'
collected: '2026-11-21'
category: Agent
direction: Agent 自监督隐式动作学习
tags:
- Video DiT
- Self-supervised Learning
- Latent Action
- Dynamics Modeling
- Transfer Learning
one_liner: 基于同一预训练视频DiT初始化正反动力学模型，实现跨域可迁移的自监督隐式动作学习
practical_value: '- 可复用「同一预训练基座初始化两个互补任务模型」的架构思路，比如用同一LLM同时做用户兴趣理解和推荐结果生成，减少基座部署成本

  - 正反动力学约束+信息瓶颈的训练范式可迁移到多模态语义对齐任务，比如电商短视频-商品Semantic ID的统一空间学习，提升跨域召回效果

  - 少样本/零样本跨域迁移的训练思路可复用在Agent多场景动作泛化任务，比如电商导购Agent跨不同直播间/商品品类的交互动作适配'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有隐式动作学习多从零开始训练动力学模型，数据效率低、跨域迁移能力差，未充分利用预训练视频模型已有的时序与物理世界先验知识

### 方法关键点
O²LaF框架遵循「同一先验、双动力学」核心原则：
1. 用同一预训练视频DiT同时初始化两个任务模型：带可学习action queries的前馈过渡编码器负责逆动力学（从视觉变化预测隐式动作）、动作条件因果视频生成器负责前动力学（从动作预测后续视觉变化）
2. 通过紧凑信息瓶颈约束隐式动作空间，端到端联合优化两个动力学模型

### 关键结果数字
在导航、机器人操纵任务上，少样本动作探测性能达到新SOTA，跨视觉上下文、跨实体的零样本动作迁移能力显著优于基线；适配V-JEPA2等预测表征预训练模型也可获得有竞争力的性能
