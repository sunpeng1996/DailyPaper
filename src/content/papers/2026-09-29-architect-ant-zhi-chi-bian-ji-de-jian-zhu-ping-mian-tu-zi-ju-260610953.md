---
title: 'Architect-Ant: Editable Automatic Furnishing of Architectural Floor Plans'
title_zh: Architect-Ant：支持编辑的建筑平面图自动家具布置框架
authors:
- Fedor Rodionov
- Aleksandar Cvejic
- Michael Birsak
- John Femiani
- Peter Wonka
affiliations:
- King Abdullah University of Science and Technology (KAUST)
- Miami University
arxiv_id: '2606.10953'
url: https://arxiv.org/abs/2606.10953
pdf_url: https://arxiv.org/pdf/2606.10953
published: '2026-09-29'
collected: '2026-10-04'
category: Other
direction: 建筑平面布局生成 · 约束感知生成
tags:
- Layout Generation
- DSL
- GRPO
- Constraint-aware Generation
- Dataset
one_liner: 提出AntPlan专业家具标注数据集与约束感知可编辑建筑平面家具布置生成框架，性能优于现有SOTA
practical_value: '- 电商虚拟家装、直播间商品陈列等布局生成场景，可复用「预训练模型微调+GRPO+自定义结果约束打分」的范式，无需预设推理路径即可低成本对齐业务规则，规避迭代式Agent推理的高时延问题

  - 生成式场景中若需输出可二次编辑的结构化结果（如可调整的商品组合陈列方案、套餐搭配），可借鉴坐标类DSL的设计思路，平衡生成可控性与下游编辑灵活性

  - 专业领域小样本生成任务可参考「小批量有监督微调对齐领域模式 + RL类方法对齐业务约束」的两阶段训练路径，降低高成本专业标注的需求量'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
自动建筑平面家具布置面临真实专业标注数据稀缺、需同时满足几何与功能多重交互约束的痛点，现有迭代式Agent推理方案计算成本高，亟需高效的约束感知生成方案。
### 方法关键点
1. 开源AntPlan数据集，包含505份专业建筑平面图，覆盖92类家具、10类住宅房间的密集标注；
2. 设计Architect-Ant框架，用可编辑的坐标类DSL表示布局，先通过有监督微调学习专业软装模式，再用GRPO算法结合自定义Layout Rule Score（LRS）聚合专业规则约束，仅用结果级监督优化模型，无需预设推理路径。
### 关键结果
对比各类SOTA基线，几何约束违规率更低、功能完整性更高，生成结果更符合真实住宅软装模式，支持对象级编辑，可直接转换为3D场景。
