---
title: 'X-Embedding: Two-Stage Training for Multilingual Patent Prior-Art Retrieval'
title_zh: X-Embedding：面向多语言专利现有技术检索的两阶段训练方法
authors:
- Wentao Wu
- Xu Wang
- Linqing Chen
- Fenhong Zhu
- Hanmeng Zhong
- Yuanxiang Huangfu
affiliations:
- Patsnap
arxiv_id: '2610.29521'
url: https://arxiv.org/abs/2610.29521
pdf_url: https://arxiv.org/pdf/2610.29521
published: '2026-10-21'
collected: '2026-10-24'
category: RecSys
direction: 垂类多语言检索 · 两阶段向量表征训练
tags:
- Embedding
- Cross-lingual Retrieval
- Two-stage Training
- Matryoshka Representation Learning
- Domain Adaptation
one_liner: 提出两阶段训练的X-Embedding框架，大幅提升多语言专利高相关X类文献的检索性能
practical_value: '- 两阶段训练范式可迁移到垂类搜索/推荐场景：先做领域预训练对齐内容结构、跨语言/模态信息，再做任务级相关性微调，效果优于直接监督微调

  - 可直接复用Matryoshka表征学习技巧：单个模型同时输出多维度embedding，低维适配召回效率要求、高维适配精排精度要求，降低向量链路维护成本

  - 负例采样策略可借鉴：除检索候选难负例外，引入低相关标注样本作为负例，提升模型对相关性等级的判别能力'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
多语言专利现有技术检索需识别与发明新颖性/创造性强相关的X类文献，现有语义匹配模型仅能捕捉主题相似性，无法满足高相关度检索要求，跨语言、多文档视图适配性不足。
### 方法关键点
1. 两阶段训练框架：第一阶段对齐专利内部互补章节、同族专利跨语言对应章节，融合专利结构与多语言表达学习领域通用表征；第二阶段以审查报告X类引用为正例，检索候选、A类引用为负例优化X类相关性。
2. 嵌入Matryoshka表征学习（MRL），单个模型可同时输出64/1024维embedding。
### 关键结果
中、英、日多语言数据集上，64维embedding整体macro Hit@100达89.09%，较Qwen3-Embedding-0.6B、RoBERTa分别提升21.25、3.68个百分点；两阶段训练较直接监督微调整体Hit@100高3.19个百分点，英、日语场景分别提升5.34、4.72个百分点，Hit@10、Hit@20分别提升3.71、3.79个百分点。
