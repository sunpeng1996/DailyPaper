---
title: 'PixCon: Clean-Positive Contrastive Learning for Foundation-Model Semi-Supervised
  Segmentation'
title_zh: PixCon：面向基础模型半监督分割的干净正例对比学习
authors:
- Ebenezer Tarubinga
affiliations:
- Ebenworks Systems, Seoul, Korea
arxiv_id: '2607.03068'
url: https://arxiv.org/abs/2607.03068
pdf_url: https://arxiv.org/pdf/2607.03068
published: '2026-07-02'
collected: '2026-07-08'
category: Other
direction: 半监督语义分割 · 对比学习优化
tags:
- Contrastive Learning
- Semi-Supervised Learning
- Semantic Segmentation
- Foundation Model
- Memory Bank
one_liner: 仅用学生模型正确分类标注样本构建零污染记忆库的像素对比分割优化框架
practical_value: '- 做对比学习召回/排序时，可借鉴仅用模型已正确分类的标注样本构建类别正例记忆库，避免伪标签噪声，提升对比损失效果

  - 可复用InfoNCE损失梯度分析方法，量化对比学习中正例集污染对模型效果的影响，指导样本筛选策略设计

  - 参考无推理额外开销的优化思路，新增模块仅训练阶段生效，不影响线上推理延迟，适配业务落地要求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
半监督语义分割传统优化思路聚焦伪标签置信度过滤，但基于DINOv2等基础模型作为teacher时，严格过滤后伪标签纯净度已达98%，剩余性能瓶颈来源于类别嵌入空间的结构设计而非标签过滤。
### 方法关键点
1. PixCon干净正例像素对比框架，仅将学生模型已正确分类的标注像素加入对应类别记忆库，从构造上保证正例集零污染，无需额外阈值
2. 单分支结构基于一致性主干实现，不增加推理参数
3. 对监督InfoNCE梯度做一阶分析，证明正例污染带来的误差项与ρ_F/(1-ρ_F)成正比，从理论上解释污染的负面影响
### 关键结果
在Pascal VOC、Cityscapes、ADE20K数据集上匹配或超越DINOv2基线UniMatch V2，Pascal-1/8分卷下每种子提升约+0.2mIoU，三种子平均mIoU达87.90，追平公开SOTA结果。
