---
title: 'Solv3R: 3D Looped Transformer as a Multi-view Solver'
title_zh: Solv3R：作为多视图求解器的三维循环Transformer
authors:
- Jeong-gi Kwak
- Andrea Tagliasacchi
- Sho Kagami
- Yuki Ono
- Kwang Moo Yi
affiliations:
- University of British Columbia
- Wayve Labs
- Simon Fraser University
- University of Toronto
- Sony Semiconductor Solutions Corporation
arxiv_id: '2611.02857'
url: https://arxiv.org/abs/2611.02857
pdf_url: https://arxiv.org/pdf/2611.02857
published: '2026-11-02'
collected: '2026-11-05'
category: Other
direction: 多视图三维重建 · 循环Transformer架构
tags:
- Looped Transformer
- 3D Reconstruction
- KV Cache
- Foundation Model
- Multi-view Geometry
one_liner: 提出无需任务定制训练即可适配多场景三维重建的循环Transformer求解器
practical_value: '- 迭代无关的统一状态更新算子设计思路，可迁移至流式推荐场景的增量用户/物品表征更新，无需区分历史数据与新数据的迭代阶段

  - 已完成计算的状态KV缓存复用机制，可借鉴到生成式推荐/RAG问答系统的上下文缓存，大幅降低重复计算开销

  - 单底座无需任务定制训练即可适配多场景的设计范式，可参考用于搭建跨电商搜索/推荐/广告多场景的统一LLM底座'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统运动恢复结构（SfM）可迭代优化相机位姿与场景几何，支持地图增量扩展而无需重计算已处理视图，但现有几何基础模型多为单步前向推理或按帧串行更新，难以实现高效的重建扩展与效果迭代优化。
### 方法关键点
1. 设计循环Transformer架构Solv3R，采用与迭代次数无关的统一更新算子，支持已优化视图和新增视图联合更新，无需区分状态完成度
2. 训练目标保证迭代过程中保留准确重建结果同时修正误差状态，同时支持固定图像集合优化与新观测融合
3. 已求解视图表征可通过KV cache复用为几何上下文，大幅降低跨迭代计算开销
### 关键结果
单模型无需任务定制训练或新增模块，即可同时支持离线重建、增量重建、重定位、流式推理等多场景任务，性能匹配当前SOTA水平。
