---
title: 'Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov
  Jump Processes'
title_zh: 并行图像理解与生成：自校正耦合马尔可夫跳变过程
authors:
- Minh-Quan Le
- Armand Comas
- Alexandros Lattas
- Stylianos Moschoglou
- Pedro Vélez
- Amit Raj
- Aaron Germuth
- Thabo Beeler
- Dimitris Samaras
- Di Qiu
affiliations:
- Google
- Google DeepMind
- Stony Brook University
arxiv_id: '2607.13188'
url: https://arxiv.org/abs/2607.13188
pdf_url: https://arxiv.org/pdf/2607.13188
published: '2026-07-13'
collected: '2026-07-17'
category: Multimodal
direction: 多模态联合生成 · 自校正采样框架
tags:
- Multimodal Generation
- Diffusion Model
- Sampler
- Cross-modal Alignment
- Self-correction
one_liner: 提出无需训练的多模态联合生成采样器CO₂Jump，解决掩码扩散模型跨模态矛盾无法修正问题
practical_value: '- 跨模态生成场景可复用跨模态置信度加权的耦合更新逻辑，解决图文生成/理解不同步、矛盾的问题，适配电商商品图文一体化生成、卖点配图自动生成场景

  - 无需训练的单通采样器设计思路可直接迁移到现有多模态扩散模型落地，无需额外finetune成本，适合快速迭代的运营素材生成需求

  - 跨模态矛盾触发的重掩码自校正机制可用于多模态Agent推理链路纠错，比如图文导购Agent回答用户商品问题时的矛盾信息自动修正'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
人类认知中理解与生成过程天然耦合，现有掩码扩散模型（MDM）采样器仅支持图文交错解码或独立并行更新，无法同步同一步内另一模态的最新决策，且无重掩码能力，跨模态矛盾既无法检测也无法修复。
### 方法关键点
1. 提出自校正耦合马尔可夫跳变过程（SC-CMJP）框架，单模态转移率由另一模态经跨模态注意力加权的置信度得分计算得到；
2. 新增重掩码跳变机制，跨模态证据冲突时立即撤回已生成内容；
3. 配套推出训练-free单通采样器CO₂Jump，开源JEdit-1M、JMaze-200K、JNono-200K共3个大规模多模态生成数据集及对应分布内/外基准。
### 关键结果
CO₂Jump在图像理解编辑、视觉推理（迷宫、数织求解）任务上取得最优联合性能，采样性能随去噪步数单调提升，跨模态耦合收益随推理轨迹逐步累加。
