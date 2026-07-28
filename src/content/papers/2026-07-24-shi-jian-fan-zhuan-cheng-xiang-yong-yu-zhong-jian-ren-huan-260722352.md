---
title: 'Time-Reversed Imaging: A Multimodal Benchmark and Framework for Reconstructing
  Past Human-Environment Interactions'
title_zh: 时间反转成像：用于重建人-环境过往交互的多模态基准与框架
authors:
- Jorge Bacca
- Kebin Contreras
- Luis Toscano-Palomino
- Mauro Dalla Mura
arxiv_id: '2607.22352'
url: https://arxiv.org/abs/2607.22352
pdf_url: https://arxiv.org/pdf/2607.22352
published: '2026-07-24'
collected: '2026-07-28'
category: Multimodal
direction: 多模态场景理解 · 历史交互反演
tags:
- Multimodal Learning
- Diffusion Model
- Benchmark Dataset
- Scene Understanding
- Generative Reasoning
one_liner: 提出时间反转成像新范式，配套多模态数据集TRACE-HEI与基准推理方法
practical_value: '- 多模态互补消歧的思路可迁移至多模态用户兴趣建模，融合文本、图像、行为信号降低兴趣预估不确定性

  - 结构化语义约束扩散模型的范式可复用在生成式推荐可控生成环节，提升推荐结果匹配度

  - 从残差痕迹反推历史行为的逻辑可参考用于电商异常交易检测，基于事后数据轨迹回溯违规操作'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
单帧RGB反推历史人-环境交互存在无限解，歧义极高，现有视频插/外推方法无法基于场景残留痕迹还原过往事件。
### 方法关键点
1. 提出时间反转成像新范式，基于热、紫外、可见光三模态残留物理印记反推近期发生的交互事件
2. 发布首个该方向基准数据集TRACE-HEI，覆盖坐、触摸、移动物体、液体泼洒等动作，包含不同材质下接触后最长3分钟的同步三模态视频序列
3. 基准方法先提取痕迹的结构化文本描述，再用其约束视觉-语言引导的扩散模型，生成合理的历史帧
### 关键结果
多模态互补可有效降低解的歧义，从衰减痕迹反推近期事件具备可行性，为该领域奠定首个计算与实验基础。
