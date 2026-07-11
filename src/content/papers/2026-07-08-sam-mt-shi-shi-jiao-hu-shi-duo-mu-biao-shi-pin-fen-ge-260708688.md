---
title: 'SAM-MT: Real-Time Interactive Multi-Target Video Segmentation'
title_zh: SAM-MT：实时交互式多目标视频分割
authors:
- Ruiqi Shen
- Chang Liu
- Henghui Ding
affiliations:
- Fudan University
- Shanghai University of Finance and Economics
arxiv_id: '2607.08688'
url: https://arxiv.org/abs/2607.08688
pdf_url: https://arxiv.org/pdf/2607.08688
published: '2026-07-08'
collected: '2026-07-11'
category: Other
direction: 多目标视频分割 · SAM2推理优化
tags:
- SAM2
- Video Segmentation
- Attention Optimization
- Sparse Memory
- Real-time Inference
one_liner: 基于SAM2构建多目标视频分割框架，解耦延迟与目标数量，实现与单目标基线相当的实时性能
practical_value: '- 多目标处理与延迟解耦的思路可迁移至多兴趣用户建模、多候选物料并行打分场景，避免候选量上升带来的线性延迟增长

  - 解耦掩码注意力机制可借鉴用于多语义特征交叉场景，减少不同用户兴趣、不同候选物料间的信号干扰

  - 稀疏时序记忆策略可复用至用户长短期行为建模，在降低存储与计算开销的同时维持行为时序演化的稳定性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多目标视频分割方案多为单目标处理逻辑的重复复用，推理延迟随目标数量增加线性上升，无法满足实时交互要求。
### 方法关键点
1. 基于SAM2改造为多目标交互框架，采用显式query表征独立目标，并行引入全局上下文共享表征降低重复计算
2. 用解耦掩码注意力消除跨目标干扰，维持目标身份独立性
3. 搭配稀疏时序记忆机制保障演化稳定性，配套遮挡处理、重叠预防专项策略
### 关键结果
成功解耦推理延迟与目标数量，10个目标场景下FPS>36，速度与单目标基线持平，同时保留SAM2的视频分割精度。
