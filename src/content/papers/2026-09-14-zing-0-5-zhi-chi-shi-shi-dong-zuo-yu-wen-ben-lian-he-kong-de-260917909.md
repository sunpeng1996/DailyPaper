---
title: 'Zing-0.5: Toward Playable Worlds with Real-Time Joint Action and Text Control'
title_zh: Zing-0.5：支持实时动作与文本联合控制的可交互生成世界
authors:
- Mingyang Chen
- Shengdong Chen
- Xiaoxiao Fu
- Bosheng Gong
- Haoyuan Guo
- Bowen Li
- Jiawen Li
- Kejun Li
- Tianpeng Li
- Yin Liu
affiliations:
- Zing Team, SeedLeap.ai
arxiv_id: '2609.17909'
url: https://arxiv.org/abs/2609.17909
pdf_url: https://arxiv.org/pdf/2609.17909
published: '2026-09-14'
collected: '2026-09-17'
category: Other
direction: 交互式生成世界 · 多模态联合控制
tags:
- World Model
- Multi-modal Control
- Knowledge Distillation
- Real-time Inference
- Generative Content
one_liner: 5B参数自回归世界模型，支持键盘与文本联合控制实现低延迟高一致性可交互生成世界
practical_value: '- 多模态控制对齐思路可迁移到导购Agent：将用户文本指令+鼠标/触屏交互动作联合作为输入条件，实现更精准的虚拟导购、3D卖场导航控制逻辑

  - 分阶段蒸馏的增量生成方法可复用在长序列生成场景：比如直播流生成、商品短视频连贯生成，用段级教师模型监督块级学生模型，平衡生成一致性和速度

  - 低延迟推理优化方案可直接复用：4步生成+上下文保留流处理的组合，能大幅降低实时交互场景（比如AR试穿、虚拟逛街）的服务器算力成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有交互式世界模型仅支持单一动作或文本控制，无法同时满足用户自由探索+主动干预生成内容的需求，且普遍存在推理延迟高、长序列生成一致性差、部署成本高的问题。
### 方法关键点
1. 统一动作与文本条件建模：融合幅度感知键盘输入、时序对齐文本指令、联合标注视频，在同序列中学习导航与事件控制逻辑
2. 事件级增量生成监督：基于多提示连贯视频训练段级教师模型，通过分布匹配蒸馏监督块级因果学生模型，保障生成一致性
3. 低延迟推理优化：结合4步生成+上下文保留流处理，压缩推理开销
### 关键结果
832×480分辨率下推理帧率达24FPS，单流分钟服务器成本仅0.009美元；158个WBench导航用例上整体得分81.0、一致性得分88.5，支持导航过程中无需重启即可通过文本修改生成事件
