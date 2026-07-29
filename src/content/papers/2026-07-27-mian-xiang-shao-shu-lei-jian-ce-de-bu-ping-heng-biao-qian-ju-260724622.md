---
title: 'A Model for Imbalanced Label Aggregation: A Focus on Minority-Class Detection'
title_zh: 面向少数类检测的不平衡标签聚合模型
authors:
- Gabriel Singer
- Samuel Gruffaz
- Olivier Vo Van
- Nicolas Vayatis
- Argyris Kalogeratos
affiliations:
- SNCF
- Tampere University
- Université Paris-Saclay
- ENS Paris-Saclay
arxiv_id: '2607.24622'
url: https://arxiv.org/abs/2607.24622
pdf_url: https://arxiv.org/pdf/2607.24622
published: '2026-07-27'
collected: '2026-07-29'
category: Other
direction: 众包标注 · 不平衡数据标签聚合
tags:
- Crowdsourcing
- Label Aggregation
- Imbalanced Data
- Minority Class Detection
- Generative Model
one_liner: 提出结合样本难度与类别相关标注者能力的生成式标签聚合模型，显著提升少数类样本召回
practical_value: '- 电商推荐/广告场景的稀有样本（如高转化负样本、违规内容、小众偏好样本）标注聚合可直接复用该模型，兼顾标注者类别偏好与样本难度，提升稀有样本召回

  - 众包标注流程可基于该模型对标注者按类别能力分层，给少数类样本分配对应专精的标注者，降低高价值样本的标注成本

  - 业务中处理不平衡数据集的标签融合时，可参考其对Condorcet陪审团定理的不平衡场景修正结论，避免多数投票带来的少数类漏判'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有众包标签聚合方案要么只建模类别依赖的标注误差忽略样本难度，要么只建模样本难度不考虑类别相关的标注能力差异，无法适配工业场景中少数类标签（如违规内容、高价值转化样本）价值高但占比极低的需求。
### 方法关键点
生成式标签聚合模型同时建模跨类别的样本难度、标注者的类别专属标注能力，适配不平衡标注场景；修正了不平衡场景下的Condorcet陪审团定理，证明多数投票会渐进保持原始类别比例，无法解决少数类识别偏差。
### 关键结果
在33个真实众包数据集（覆盖图像、文本多分类，大标注量/大样本量两类大规模场景）测试，minority recall为同类方法最高，同时balanced accuracy保持竞争力。
