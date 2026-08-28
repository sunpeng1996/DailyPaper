---
title: 'Sidecar: Training-Free Semantic Reuse for Character-Consistent Free-form Visual
  Storytelling'
title_zh: Sidecar：免训练语义复用实现自由形式视觉叙事的角色一致性
authors:
- Sibo Dong
- Sarah Adel Bargal
affiliations:
- Georgetown University
arxiv_id: '2608.27280'
url: https://arxiv.org/abs/2608.27280
pdf_url: https://arxiv.org/pdf/2608.27280
published: '2026-08-27'
collected: '2026-08-28'
category: Multimodal
direction: 多模态生成 · 跨帧一致性优化
tags:
- Text-to-Image
- Training-free
- Semantic Augmentation
- Character Consistency
- Visual Storytelling
one_liner: 提出免训练即插即用语义增强模块Sidecar，提升视觉叙事跨帧角色一致性且几乎无计算开销
practical_value: '- 电商商品短视频/种草内容生成场景可复用该即插即用语义注入逻辑，无需微调扩散模型即可保证多帧生成的商品/模特外观一致性，降低落地成本

  - Agent多轮生成多模态内容时，可借鉴核心实体语义缓存复用思路，避免后续指代类prompt遗漏关键属性导致生成内容偏差

  - 低资源多模态生成任务可参考免训练、不修改基座模型的插件设计思路，快速对齐业务需求且几乎无额外计算开销'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
自由形式视觉叙事中角色仅首次出现时有完整属性描述，后续prompt多以指代/类型表述省略身份语义，预训练文生图模型独立生成每帧时极易出现跨帧角色不一致问题，现有方案要么需额外训练、要么改动基座模型，落地成本高。

### 方法关键点
1. 设计即插即用的Sidecar语义增强模块，缓存角色首次出现时的完整实体级语义信息；
2. 推理阶段自动识别后续prompt中的指代表述，将缺失的身份语义补入对应prompt embedding，无需额外训练、不修改扩散模型基座架构。

### 关键结果
在FreeStoryBench测试集上，基于SDXL、FLUX的多个基线模型接入Sidecar后，prompt-图像对齐效果、跨帧角色一致性均获得稳定提升，额外计算开销可忽略。
