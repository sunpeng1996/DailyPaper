---
title: Optimization Dynamics Imprint Semantic Specificity in Contrastive Embedding
  Norms
title_zh: 对比学习嵌入范数编码语义特异性的优化动力学机制
authors:
- Ziwei Su
- Junyu Ren
- Victor Veitch
affiliations:
- University of Chicago
arxiv_id: '2606.30625'
url: https://arxiv.org/abs/2606.30625
pdf_url: https://arxiv.org/pdf/2606.30625
published: '2026-06-29'
collected: '2026-06-30'
category: Training
direction: 对比学习 · 嵌入语义校准
tags:
- Contrastive Learning
- Embedding Norm
- Semantic Specificity
- Retrieval Calibration
- Optimization Dynamics
one_liner: 从优化动力学角度解释对比学习嵌入范数的语义关联机制，给出解析公式与无成本校准方案
practical_value: '- 电商搜索/召回场景可直接复用预训练对比嵌入的范数作为免费校准信号，修正高频query、大类商品的cosine相似度低估问题，无需额外训练即可提升召回准确率

  - 排序链路可新增嵌入范数特征，其编码的概念粒度、用户查询不确定性信息可辅助区分泛搜/精搜意图，无需额外标注成本

  - 语义索引构建阶段，可基于范数阈值对商品/query embedding做分桶，适配不同粒度的召回策略，提升异构query的匹配效率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
对比学习通常采用尺度不变损失+cosine相似度完成检索/匹配推理，训练和推理阶段均会忽略嵌入范数，但工业实践中反复观测到范数与概念粒度、token频率、不确定性等语义属性强相关，相关应用长期依赖启发式规则，缺乏底层机制解释。
### 方法关键点
从优化动力学视角建立理论分析框架，推导得到嵌入范数的解析表达式，证明范数编码语义信息是对比训练过程的自然副产品，无需额外标注或模型修改，同时明确了范数作为校准信号的适用场景边界。
### 关键结果
范数可作为无成本校准工具修正cosine打分偏差，可解释过往检索场景中高频词cosine相似度被低估的现象，适配大部分主流对比嵌入模型（如Sentence-BERT、E5、CLIP等）。
