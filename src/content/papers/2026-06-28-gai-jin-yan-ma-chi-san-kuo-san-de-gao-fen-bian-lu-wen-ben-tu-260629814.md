---
title: 'Nemotron-Labs-Diffusion-Image: Advancing Masked Discrete Diffusion for High-Resolution
  Image Synthesis'
title_zh: 改进掩码离散扩散的高分辨率文本到图像合成
authors:
- Shufan Li
- Greg Heinrich
- Hanrong Ye
- Yonggan Fu
- Aditya Grover
- Jan Kautz
- Pavlo Molchanov
affiliations:
- NVIDIA
arxiv_id: '2606.29814'
url: https://arxiv.org/abs/2606.29814
pdf_url: https://arxiv.org/pdf/2606.29814
published: '2026-06-28'
collected: '2026-06-30'
category: Multimodal
direction: 多模态文生图 · 离散扩散模型
tags:
- Discrete Diffusion
- Text-to-Image
- High-Resolution Generation
- Training Optimization
one_liner: 针对掩码离散文生图扩散的两大痛点，提出新机制与损失，实现最优高分辨率文生图效果
practical_value: '- 做大词表离散建模（如推荐中Semantic ID大词表）时，可复用GCE损失，给embedding空间近邻token分配正信号，缓解训练信号稀疏问题

  - 大词表场景可复用自定义融合算子优化思路，能显著降低训练时VRAM占用，提升训练吞吐效率

  - 离散生成任务可借鉴动态自校正思路：推理时允许修改已生成的离散token，通过迭代精修提升生成质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有掩码离散扩散模型（MDM）用于高分辨率文生图存在两大核心痛点：一是和连续扩散可全程逐步精修全图表征不同，标准MDM的离散token一旦解掩码就无法修改，缺乏自校正能力；二是离散图像tokenizer增大词表虽能提升重建保真度，但会导致单token训练信号愈发稀疏，给生成建模带来优化难题。

### 方法关键点
针对第一个痛点，新增token-editing机制，允许模型推理时动态修正已经解掩码的token，实现迭代精修；针对第二个痛点，提出Grouped Cross-Entropy（GCE）目标，给GT embedding空间内的近邻token分配正学习信号，缓解信号稀疏；额外实现了GCE的自定义融合算子，大幅降低大词表场景下的VRAM占用。

### 关键结果
两项创新同时提升了训练效率和图像保真度，在公开评测上取得SOTA：GenEval 0.90、DPG 86.9、HPSv3 10.76，1024px分辨率性能超越过往掩码生成模型。
