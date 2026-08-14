---
title: 'Context-Matched Distillation: Teacher Causality for Autoregressive Video Distillation'
title_zh: 上下文匹配蒸馏：面向自回归视频生成的教师因果约束方法
authors:
- Hmrishav Bandyopadhyay
- Xuanchi Ren
- Zijian Huang
- Jay Zhangjie Wu
- Tianshi Cao
- Ruilong Li
- Bryan Chu
- Sanja Fidler
- Yi-Zhe Song
- Zian Wang
affiliations:
- NVIDIA
- SketchX, CVSSP, University of Surrey
arxiv_id: '2608.13391'
url: https://arxiv.org/abs/2608.13391
pdf_url: https://arxiv.org/pdf/2608.13391
published: '2026-08-12'
collected: '2026-08-14'
category: Training
direction: 自回归视频生成 · 因果蒸馏训练
tags:
- Knowledge Distillation
- Autoregressive Generation
- Causal Alignment
- Video Generation
- Low-latency Inference
one_liner: 提出上下文匹配因果蒸馏框架，解决自回归视频生成蒸馏中师生因果信息不匹配问题
practical_value: '- 因果对齐蒸馏思路可迁移到生成式推荐、Agent多步序列生成场景，避免用未来信息做监督导致的训练/推理分布偏移

  - Prefix Scoring技巧可复用在自回归类任务（如搜索Query补全、推荐序列生成）的少步蒸馏，对齐学生真实生成上下文提升蒸馏效果

  - Prefix Corruption方法可直接用到生成类任务蒸馏的早期训练阶段，扰动不可靠前缀提升训练稳定性，减少调参成本

  - 统一因果约束的师生初始化方案，适合低延迟实时生成场景（如实时广告文案/短视频生成）的推理加速'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
交互式自回归视频生成要求同时满足低延迟生成与精准在线控制，现有少步蒸馏方案采用双向教师监督因果学生，教师评分会用到学生生成时无法获取的未来帧、控制信息，导致监督信号与学生因果信息集错位，效果受限。
### 方法关键点
1. 提出上下文匹配蒸馏（CMD）因果DMD框架，用无未来信息访问权限的因果教师替换双向全片段评分教师，且用同一因果教师初始化少步学生，保证教师训练、学生蒸馏、推理全链路因果约束一致；
2. 新增Prefix Scoring机制，基于学生生成的缓存前缀评估对应目标，对齐监督信号与学生真实生成上下文；
3. 新增Prefix Corruption策略，训练早期扰动不可靠前缀，在保持目标-上下文对齐的同时稳定训练过程。
### 关键结果
在长短视频基准上达到自回归方法SOTA的综合性能，时变相机控制的遵循度实现大幅提升。
