---
title: Importance Scoring of Transformer Attention Heads in Learning Tabular Data
title_zh: 面向表格数据学习的Transformer注意力头重要性打分方法
authors:
- Ahmad Jad Allah
- Kazi F. Akhter
- Md. Kamrozzaman Bhuiyan
- Manar D. Samad
affiliations:
- Tennessee State University
- Enosis Solutions
- North Carolina Agricultural and Technical University
arxiv_id: '2608.27241'
url: https://arxiv.org/abs/2608.27241
pdf_url: https://arxiv.org/pdf/2608.27241
published: '2026-08-27'
collected: '2026-08-28'
category: Training
direction: Transformer优化 · 注意力头剪枝与轻量化
tags:
- Transformer
- Multi-head Attention
- Pruning
- Tabular Data
- Model Efficiency
one_liner: 提出适配表格数据的Transformer注意力头重要度量化方法，可剪枝冗余头提升模型效率
practical_value: '- 做电商/广告推荐场景的Tabular Transformer优化时，可复用该开源重要度打分方法剪枝低价值注意力头，降低推理时延、节省部署资源

  - 针对业务私域表格特征场景（如用户行为、商品属性表），可参考结论优先跨层筛选剪枝头，不用固定按层裁剪，避免误删重要头

  - 可直接将该打分方法集成到现有Transformer模型迭代流水线中，快速完成模型轻量化适配上线'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Transformer在CV、NLP领域已被广泛研究，但在表格数据场景下的应用与优化探索较少，大参数量Transformer推理成本高、可解释性差的问题在表格场景下缺乏针对性解决方案。
### 方法关键点
提出专门适配表格数据的Transformer注意力头重要度量化指标，通过单头对模型输出的贡献度打分，支持按分值梯度剪枝低价值头，降低模型冗余。
### 关键结果
- 基于40个异构表格数据集验证，72.5%的实验中按重要度从低到高剪枝时，模型性能抗跌性最强；
- 优先删除最高重要度头会带来最大的分类性能跌幅；
- 重要头跨层分散无统一层分布规律，且不同schema的表格数据集的头重要度分布差异远大于CV、NLP场景。
