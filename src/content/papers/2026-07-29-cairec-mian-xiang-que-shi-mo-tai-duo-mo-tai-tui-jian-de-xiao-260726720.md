---
title: 'CaIRec: Calibrated Modality Imputation for Incomplete Multimodal Recommendation'
title_zh: CaIRec：面向缺失模态多模态推荐的校准式模态补全框架
authors:
- Ruiyu Liu
- Xiaohao Liu
- Miaomiao Cai
- Yunshan Ma
- See-Kiong Ng
affiliations:
- Southern University of Science and Technology
- National University of Singapore
- Singapore Management University
arxiv_id: '2607.26720'
url: https://arxiv.org/abs/2607.26720
pdf_url: https://arxiv.org/pdf/2607.26720
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 多模态推荐 · 缺失模态补全
tags:
- Multimodal Recommendation
- Missing Modality Imputation
- Cross-modal Calibration
- Graph Recommendation
- Preference Adaptation
one_liner: 提出两阶段校准式模态补全框架，解决缺失模态多模态推荐的结构扭曲与偏好适配差距问题
practical_value: '- 电商场景大量商品缺图/缺描述，可直接复用两阶段补全思路：先做跨模态结构校准保证补全表征一致性，再做推荐任务适配，比直接补全表征效果更好

  - 伪缺失实例构造技巧可迁移：用已有完整模态的商品构造mask-补全对，对齐补全表征和真实观测表征的分布，减少补全通路和真实通路的偏差

  - 补全感知物品图的构造方法可复用：融合补全后的模态相似性与协同过滤相似度，重建模态缺失导致断裂的物品邻接关系，提升偏好传播效果

  - 现有多模态推荐系统遇到冷启动/模态缺失问题时，无需重新训练整个模型，可叠加该补全模块适配缺失场景，改造成本低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现实电商、内容推荐场景中大量商品/内容缺失图片、文本描述等模态信息，现有模态补全方法存在两个核心问题：一是仅优化补全表征本身，忽略同一物品跨模态关系的一致性，导致跨模态结构扭曲；二是补全表征未针对个性化排序任务做适配，补全通路与真实观测通路存在分布偏差，同时模态缺失破坏了偏好传播所需的物品邻域关系，存在偏好适配gap，严重降低多模态推荐效果。

### 方法关键点
- 采用两阶段独立训练框架，第一阶段**Structural Imputation Calibration (SIC)** 负责结构校准的模态补全，第二阶段**Preference-oriented Representation Calibration (PRC)** 负责推荐任务适配，避免多任务冲突
- SIC阶段：基于共享潜变量模型从已有观测模态推断缺失模态表征，新增结构正则约束同一物品跨模态相似性的分布一致性，用真实观测的跨模态对做对齐监督，锚定补全空间的跨模态对应关系
- PRC阶段：构造伪缺失样本，用独立Adapter对齐补全表征与真实观测表征在推荐空间的分布；融合补全后模态相似性与协同过滤相似度，构造补全感知物品图，修复模态缺失导致断裂的偏好传播路径，结合BPR损失优化排序效果

### 关键实验
在Amazon的Clothing、Sports、Beauty三个电商公开数据集上，50%模态缺失率下相比最优基线平均提升3.77%，缺失率越高优势越明显，90%高缺失率下仍保持稳定性能，增益主要集中在存在模态缺失的商品组。

### 核心结论
模态补全不能仅追求表征还原度，必须同时保证跨模态结构一致性和推荐任务适配性，才能真正转化为推荐效果的提升。
