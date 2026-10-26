---
title: Generalized CycleGRPO for Fine-Grained Multimodal Understanding and Grounding
title_zh: 通用CycleGRPO：面向细粒度多模态理解与定位
authors:
- Xin Zhang
- Haochen Wang
- Beibei Lin
- Zhaoxiang Zhang
- Robby T. Tan
- Jason Li
- Dacheng Tao
affiliations:
- NUS
- UCAS
- NTU
arxiv_id: '2610.29552'
url: https://arxiv.org/abs/2610.29552
pdf_url: https://arxiv.org/pdf/2610.29552
published: '2026-10-20'
collected: '2026-10-26'
category: Multimodal
direction: 多模态大模型 · 细粒度区域文本对齐
tags:
- CycleGRPO
- Multimodal LLM
- Reinforcement Learning
- Region Grounding
- Video Understanding
one_liner: 提出通用CycleGRPO框架，跨三类域统一多模态区域描述与定位，无需额外标注或外部判分
practical_value: '- 电商多模态商品表征优化：可复用CycleGRPO的「区域→描述→区域」循环自监督思路，无需大量人工标注商品描述，用区域重建IoU作为奖励优化多模态商品特征，降低标注成本

  - 短视频电商商品定位优化：针对短视频中重复出现的相似商品片段，可借鉴DOVE基准的差异性评估逻辑，引导生成带唯一区分特征的商品描述，避免相似片段误召回

  - 多模态导购Agent优化：Agent处理用户「定位视频中某款商品」类需求时，可复用本文的循环一致性奖励机制，同时优化描述生成和区域定位准确率，无需额外训练reward模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态大模型的区域理解（区域生成描述）和定位（描述匹配区域）两个互补任务通常分开优化，分别依赖昂贵的文本标注和几何标注，两类标注无互相约束，导致细粒度场景下生成的描述无法唯一区分相似区域/片段，尤其视频中存在重复事件时，描述泛化性差、定位准确率低，依赖外部LLM判分或奖励模型的RL方案成本高、可迁移性差。
### 方法关键点
1. 提出通用CycleGRPO强化学习框架，统一支持空间（图像掩码/bounding box）、时间（视频时间区间）、时空（带时间戳的空间框）三类区域的优化，无需额外适配
2. 构建「输入区域→生成描述→根据描述重建区域」的闭环，用输入区域和重建区域的几何重叠度作为可验证奖励，RL训练阶段无需参考caption、外部LLM判分或独立奖励模型
3. 嵌套GRPO优化策略：描述生成和定位任务共享同一模型参数，分别做组相对优势计算，联合梯度更新
4. 开源DOVE视频描述评估基准，通过目标区间与同视频相似重复区间的对比组，量化描述的细粒度区分度，提出TEC指标衡量时序证据覆盖率
### 关键结果
- 空间域：基于SAMTok基线，GroundingSuite整体gIoU从57.5%提升至68.2%，GRES平均gIoU从71.2%提升至78.7%
- 时间域：基于Qwen3-VL基线，Charades的tIoU从45.6%提升至51.9%，DOVE基准TEC从14.8%提升至33.3%
- 时空域：基于Open-o3-Video基线，V-STaR的mAM从34.6%提升至36.2%，mLGM从47.2%提升至49.8%
### 核心结论
区域-文本的循环一致性是无需外部标注即可同时提升多模态理解和定位能力的通用自监督原则
