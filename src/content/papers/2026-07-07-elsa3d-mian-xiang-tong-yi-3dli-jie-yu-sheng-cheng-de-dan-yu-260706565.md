---
title: 'ELSA3D: Elastic Semantic Anchoring for Unified 3D Understanding and Generation'
title_zh: ELSA3D：面向统一3D理解与生成的弹性语义锚定方法
authors:
- Tianjiao Yu
- Xinzhuo Li
- Yifan Shen
- Onkar Susladkar
- Yuanzhe Liu
- Xiaona Zhou
- Ismini Lourentzou
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2607.06565'
url: https://arxiv.org/abs/2607.06565
pdf_url: https://arxiv.org/pdf/2607.06565
published: '2026-07-07'
collected: '2026-07-08'
category: Multimodal
direction: 多模态大模型 · 3D统一理解与生成
tags:
- 3D_Foundation_Model
- Cross_Modal_Alignment
- Token_Routing
- Multimodal_Generation
- Efficient_Inference
one_liner: 提出基于弹性语义锚的统一3D多模态模型，实现多任务SOTA同时减半计算量与推理延迟
practical_value: '- 电商3D商品素材生产场景可复用稀疏Anchor Token跨模态路由逻辑，降低文生3D/图生3D推理延迟，适配大批量商品3D建模需求

  - 层级语义-尺度匹配思路可迁移至多模态推荐召回/排序，将不同粒度语义特征路由到对应尺度特征处理层，提升匹配精度同时降本

  - 轻量per-block动态路由机制可复用给大模型推荐系统，将算力集中在高价值特征交互节点，降低整体推理开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
统一3D基础模型需在同一骨干下同时实现3D生成与语言驱动推理，但现有方案文本-3D交互为隐式，直接拼接两类token做自注意力会丢失粗结构线索与细几何细节，还存在大量计算冗余。
### 方法关键点
1. 采用尺度感知八叉树分词器编码3D几何信息，匹配不同抽象层级的语义特征；
2. 引入Anchor Token作为稀疏跨模态单元，完成语义选择、尺度路由、对应尺度几何证据检索、融合信号回写全流程，保证交互稀疏精准；
3. 每层配置轻量路由器，动态决定文本token对应的锚点实例化几何尺度，算力集中在对齐需求最高的区域。
### 关键结果
在图生3D、文生3D、3D字幕任务上均达SOTA，性能优于现有最强统一基线，对比同架构非弹性版本，FLOPs与推理延迟均减半。
