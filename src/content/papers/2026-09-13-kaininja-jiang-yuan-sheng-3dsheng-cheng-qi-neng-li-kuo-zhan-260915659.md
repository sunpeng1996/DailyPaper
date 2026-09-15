---
title: 'Kaininja: Extending Native 3D Generators to the Part Level'
title_zh: KaiNinja：将原生3D生成器能力扩展至零件层级
authors:
- Ruihan Yu
- Lian Fu
- Muyao Niu
- Zheng-hui Huang
- Yu-Ju Tsai
- Sho Kuno
- Fengbo Lan
- Yonghao Yu
- Erwin Wu
- Ming-Hsuan Yang
affiliations:
- Alaya Lab
- The University of Tokyo
- University of California, Merced
- Institute of Science Tokyo
arxiv_id: '2609.15659'
url: https://arxiv.org/abs/2609.15659
pdf_url: https://arxiv.org/pdf/2609.15659
published: '2026-09-13'
collected: '2026-09-15'
category: Other
direction: 原生3D生成 · 零件级能力扩展
tags:
- 3D Generation
- Part-level Generation
- Dual-volume Representation
- LLM-driven Agent
- O-Voxel
one_liner: 提出双体积表示，无需分割器即可将TRELLIS.2扩展到零件级，同时提升整体生成精度
practical_value: '- 电商3D商品自动建模业务可复用双体积表示方案，省去后续人工拆分商品部件的成本

  - 训练3D生成模型时可引入LLM-driven Agent生成的标注数据，降低零件级3D资产的人工标注成本

  - 现有原生3D生成管线升级零件级能力时，可参考无分割器的端到端设计，降低推理延迟'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有原生3D生成器仅能输出融合的整体网格，下游编辑、绑定、仿真等任务需要零件级资产，后置3D分割方案速度慢、精度上限低，且原生O-Voxel网格单个体素仅存一张表面，无法表达零件接触界面。

### 方法关键点
1. 提出双体积O-Voxel表示，解决单体积无法表达零件接触面的核心问题
2. 基于双体积表示构建KaiNinja，是TRELLIS.2的零件级扩展，管线无需掩码或分割器
3. 训练数据覆盖CAD模型、LLM驱动Agent生成的零件资产，是首个采用Agent生成零件数据训练的3D生成模型

### 关键结果
相较不同范式的零件生成管线，整体物体Chamfer距离降低40%，严格零件F-score提升16%；保留原TRELLIS.2的生成速度与质量，同时整体物体保真度优于同骨干网同数据集微调的基线
