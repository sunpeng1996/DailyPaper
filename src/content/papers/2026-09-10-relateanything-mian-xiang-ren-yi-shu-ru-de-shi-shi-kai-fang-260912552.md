---
title: 'RelateAnything: Real-Time Open-Vocabulary Relation Prediction From Any Inputs'
title_zh: RelateAnything：面向任意输入的实时开放词汇关系预测
authors:
- Maëlic Neau
affiliations:
- Independent Researcher
arxiv_id: '2609.12552'
url: https://arxiv.org/abs/2609.12552
pdf_url: https://arxiv.org/pdf/2609.12552
published: '2026-09-10'
collected: '2026-09-17'
category: Multimodal
direction: 多模态开放词汇关系预测
tags:
- Open-Vocabulary
- Relation Prediction
- Scene Graph Generation
- Lightweight Model
- Multimodal
one_liner: 推出53M参数轻量开放词汇关系预测模型，配套大规模标注数据集与多维度评估基准
practical_value: '- 电商商品图场景理解、搭配推荐可复用其无对象标签输入、推理时自定义关系谓词的架构，无需重训即可适配服饰、家居等不同品类的关系识别需求

  - 小参数多模态模型训练可参考其positive-unlabeled监督策略、反义词语义纠偏的text encoder优化技巧，提升小模型跨域泛化性

  - 多模态召回、场景理解的效果评估可复用OV-SGG-Bench的跨数据集、零样本评估思路，避免域内评估过高估计业务落地效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有场景图关系预测模型依赖固定预定义谓词集合、绑定特定目标检测器，缺乏开放词汇适配能力，在训练数据、模型架构、评估指标三大层面存在落地瓶颈。
### 方法关键点
1. 仅53M参数的轻量模型RelateAnything，无需输入对象标签，推理时可自定义文本形式的关系谓词词表，替换区域输入源无需重训；
2. 构建RA-4M数据集，含474k张图像、4.3M条标注、10102个自由文本谓词，采用几何校验过滤噪声；
3. 训练采用positive-unlabeled监督，优化text encoder解决对比学习编码器中反义词语义相似度高达0.95的问题；
4. 提出OV-SGG-Bench多维度评估基准，解决传统召回指标偏向训练集分布的问题。
### 关键结果数字
推理速度达20ms/帧，跨数据集/零样本benchmark上平均召回率是同量级SOTA的2.3~3.5倍，参数仅为3B VLM场景图模型的2%且性能更优，域内评估会高估迁移收益约5倍。
