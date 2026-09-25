---
title: 'Hyperbolic Multimodal Continual Learning: A Closest-Admissible Solution'
title_zh: 双曲多模态持续学习：最近可采纳解方法
authors:
- Jiahong Liu
- Ming Shen
- Xiaohao Liu
- Rex Ying
- Menglin Yang
- Tat-Seng Chua
- Irwin King
affiliations:
- The Chinese University of Hong Kong
- National University of Singapore
- Yale University
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2609.29329'
url: https://arxiv.org/abs/2609.29329
pdf_url: https://arxiv.org/pdf/2609.29329
published: '2026-09-24'
collected: '2026-09-25'
category: Training
direction: 双曲多模态 · 持续学习训练优化
tags:
- Continual Learning
- Hyperbolic Geometry
- Multimodal Learning
- Representation Learning
- Optimization
one_liner: 提出基于双曲等距约束的双曲多模态持续学习框架，降低旧任务表征漂移、提升跨任务性能
practical_value: '- 电商多模态召回/检索场景的持续迭代可复用双曲等距约束方法，避免新增任务后旧类目/商品的跨模态匹配关系漂移，无需全量重训

  - 语义层级建模场景（如类目树、知识图谱关联的商品推荐）可借鉴该方法的双曲几何保护机制，保留层级结构的同时迭代模型

  - 持续训练场景中可直接复用CA/MR校正逻辑优化AdamW更新步，在不损失新任务学习效果的前提下降低灾难性遗忘'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有持续学习方法针对欧氏空间设计，应用到双曲多模态模型时无法保留洛伦兹几何结构，会导致旧任务学到的模态内相似性、跨模态对应关系、语义层级发生扭曲，即使任务得分不变，核心表征关系仍被破坏。
### 方法关键点
HMCL框架将旧多模态几何结构保留转化为约束所有模态遵循共享双曲等距变换，推导可采纳的一阶参数更新族；设计最近可采纳（CA）校正模块，保留与候选模态更新最匹配的共享旋转，极简版本MR固定旋转为0；两者对AdamW的更新位移做校正，搭配任务锚定机制限制任务内参数更新累积量，同时保留学习自由度。
### 关键结果
在16任务分类-检索流、3种双曲骨干上，HMCL相比序列微调和4个基线，最终性能和反向迁移均有提升，HMCL-CA在所有骨干上取得最高总分；表征漂移降低81.2%~95.5%，ImageNet-WordNet实验语义层级保留更优。
