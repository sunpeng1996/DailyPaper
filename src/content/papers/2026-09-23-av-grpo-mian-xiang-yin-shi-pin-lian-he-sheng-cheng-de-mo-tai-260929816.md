---
title: 'AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for
  Joint Audio-Video Generation'
title_zh: AV-GRPO：面向音视频联合生成的模态锚定解耦扩散强化学习框架
authors:
- Zhiyu Xu
- Weilong Yan
- Yufei Shi
- Shiyang Li
- Yihao Liu
- Kin-Man Lam
- Yuewen Cao
affiliations:
- Shanghai AI Laboratory
- The Hong Kong Polytechnic University
- National University of Singapore
- Nanyang Technological University
- Zhejiang University
arxiv_id: '2609.29816'
url: https://arxiv.org/abs/2609.29816
pdf_url: https://arxiv.org/pdf/2609.29816
published: '2026-09-23'
collected: '2026-09-26'
category: Multimodal
direction: 多模态生成 · 扩散强化学习优化
tags:
- Diffusion Model
- Reinforcement Learning
- Multimodal Generation
- LoRA
- Fine-tuning
one_liner: 提出模态锚定解耦扩散RL框架AV-GRPO与5DAV数据集，提升音视频联合生成效果
practical_value: '- 多模态任务解耦优化思路可迁移到电商短视频/直播带货内容生成场景，将音画同步、内容保真、语义对齐的联合优化拆分为单模态子任务降低训练成本

  - 模态锚定+冻结塔优化trick可复用到多模态推荐大模型LoRA微调流程，减少显存占用同时提升奖励信用分配准确率

  - 分维度难度可控数据集构建方法可参考用于生成式推荐的多模态评测集建设，提升benchmark的公平性和鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有音视频联合生成模型存在单模态保真度低、文本-模态对齐差、跨模态同步弱问题，直接引入RL后训练存在多模态奖励信号纠缠、双模态塔联合优化算力成本高、同步评估难度随样本波动导致奖励对比不公平的痛点。

### 方法关键点
1. 模态锚定在线扩散RL框架AV-GRPO包含三个核心模块：模态锚定rollout解耦学习信号、轨迹锁定冻结塔优化降本并重分配奖励、适配单模态动态的自适应目标与扰动强度，将耦合多模态偏好学习转化为条件单模态子任务；2. 构建5维度解耦、难度可控的训练数据集5DAV支撑系统化训练。

### 关键结果数字
在JavisBench、VABench上，LoRA微调和全量微调场景下，AV-GRPO的生成质量、语义对齐、跨模态同步指标均优于基线LTX-2.3
