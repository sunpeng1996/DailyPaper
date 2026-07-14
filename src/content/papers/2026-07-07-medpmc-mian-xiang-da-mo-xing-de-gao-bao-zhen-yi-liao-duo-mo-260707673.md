---
title: 'MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal
  Data for Foundation Models'
title_zh: MedPMC：面向大模型的高保真医疗多模态数据规模化构建系统框架
authors:
- Hyunjae Kim
- Dain Kim
- Pan Xiao
- Serina S. Applebaum
- Younjoon Chung
- Xuguang Ai
- Yu Yin
- Roy Jiang
- Yuexi Du
- Yawen Wei
affiliations:
- Yale University
- Korea University
- Washington University in St. Louis
- The University of Queensland
- Microsoft Research
arxiv_id: '2607.07673'
url: https://arxiv.org/abs/2607.07673
pdf_url: https://arxiv.org/pdf/2607.07673
published: '2026-07-07'
collected: '2026-07-14'
category: Multimodal
direction: 多模态大模型 · 垂直领域数据构建
tags:
- Multimodal LLM
- Data Curation
- CLIP
- Medical AI
- Visual Retrieval
one_liner: 提出自动化可更新医疗多模态数据构建框架MedPMC，生成千万级高质量图文对提升模型性能
practical_value: '- 可复用公开文献/商品详情页的多模态数据清洗流水线设计，包括初筛、多图拆分、图文对齐的模块配置，适配电商/广告场景的商品图文对自动化构建

  - 小体量高保真图文对训练的CLIP模型效果优于低质大训练集的结论，可指导推荐/搜索场景多模态召回模型的训练数据优先级判断

  - 多模态大模型视觉编码器的预训练数据优化路径，可迁移到电商多模态生成式推荐的基座微调任务中'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
医疗多模态大模型发展受限于高质量标注数据稀缺，现有PubMed Central（PMC）衍生数据集保真度、可复现性、临床有效性不足。

### 方法关键点
MedPMC为自动化可迭代更新的全链路数据处理框架，覆盖初筛过滤无效内容、多面板图检测拆分、图文对齐、医疗图像分类环节，可规模化生成高保真医疗多模态图文对。

### 关键结果
- 处理610万篇PMC文献，生成1100万医疗图文对，人工审核医学相关性达95.3%，远超此前同类数据集的19.7%
- 基于该数据训练的CLIP模型，在26个医疗基准上零样本AUC比同类基线高7.1个百分点，仅用基线不到一半的训练数据
- 作为多模态大模型视觉编码器，医疗VQA性能最高提升16.9个百分点，皮肤病图像检索Recall@5提升11.7个百分点
