---
title: A phase diagram for training and inference in language models
title_zh: 大语言模型训练与推理的表示几何相图
authors:
- Zhuo-Yang Song
- Zeyu Li
- Qing-Hong Cao
- Ming-xing Luo
- Hua Xing Zhu
affiliations:
- 北京大学物理学院
- LightRay AI Lab
- 北京大学高能物理研究中心
- 郑州大学物理学院
- 北京计算科学研究中心
arxiv_id: '2611.19848'
url: https://arxiv.org/abs/2611.19848
pdf_url: https://arxiv.org/pdf/2611.19848
published: '2026-11-15'
collected: '2026-11-17'
category: LLM
direction: 大语言模型 · 表示几何与训练相变
tags:
- LLM
- representation_geometry
- phase_transition
- training_dynamics
- inference_flow
one_liner: 用两个几何集体坐标构建LLM相图，区分训练前后的推理流行为与相变
practical_value: '- 可复用u（文档区分度）、dC（文档维度）两个无偏几何指标，快速评测垂直领域微调LLM、推荐场景用LLM的训练成熟度，无需执行全量下游任务评测

  - 针对长用户行为序列、长商品描述建模的Transformer，可通过监控各层u、dC值优化层裁剪策略，降低推理延迟

  - 微调Agent用LLM时，可将推理流进入工作相的比例作为早停指标，减少无效训练步数，降低训练成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM行为研究多聚焦输出层指标，内部表示几何与模型实际行为的关联缺乏统一分析框架，不同架构、训练策略的模型表现难以横向对比，无法从表示层面判断训练完成度。

### 方法关键点
- 定义两个旋转、缩放不变的集体坐标：文档区分度u（文档均值偏移与文档内token方差的归一化比值）、文档维度dC（文档内表示协方差的参与比，表征有效变化方向数）
- 以u、dC为轴构建相图，将Transformer前向传播的层间表示变化映射为推理流轨迹，用离散Langevin方程描述流的动力学特性
- 划分工作相（训练完成模型推理流停留的中心区域）与漂移相（未训练模型推理流趋向的外围区域），通过流在工作相代表点P*的收缩率区分两类相位

### 关键结果
- 测试5个架构家族的8个训练完成模型，推理流全部在相对深度0.11前进入工作相，深层位置离散度仅0.085 dex，远低于156组未训练模型的0.3~1.4 dex
- Pythia-1.4B训练过程中，256~512步发生突变相变：工作相占比从接近0跃升至接近1，惯性系数从0.28+降至接近0，收缩率由负转正

所有训练合格的LLM的内部表示都会收敛到相同的几何相区，无需解码仅通过前向传播的表示几何即可判断模型训练成熟度。
