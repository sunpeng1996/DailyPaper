---
title: 'CodeHID: Learning an Addressable Hierarchical Code Index for Generative Code
  Retrieval'
title_zh: 'CodeHID: 面向生成式代码检索的可寻址层次化编码索引学习'
authors:
- Zhen Li
- Yuhong Chen
- Wenhao Xu
- Xiaodong Li
- Hui Li
affiliations:
- 厦门大学
arxiv_id: '2608.24089'
url: https://arxiv.org/abs/2608.24089
pdf_url: https://arxiv.org/pdf/2608.24089
published: '2026-08-25'
collected: '2026-08-26'
category: GenRec
direction: 生成式检索 · 层次化语义ID构造
tags:
- Generative Retrieval
- Semantic ID
- Hierarchical Index
- DocID Learning
- Code Retrieval
one_liner: 提出层次化语义DocID+双阶段生成引导的生成式代码检索框架，大幅提升首召准确率
practical_value: '- 构造层次化Semantic ID时可复用伪邻居引导方案：基于k-NN语义邻接+分层相似度阈值做前缀对齐监督，保证语义相似的商品/内容共享ID前缀，提升生成式召回的粗筛效率

  - 训练生成式ID预测模型时可叠加双阶段优化技巧：训练侧加入hard negative排序蒸馏，推理侧加前缀约束+查询相关前缀加权，大幅提升首召准确率，适配电商搜索/推荐topN优先场景

  - 可直接复用多级残差量化(RQ-VAE)方案生成ID，无需人工定义类目体系，自动构建全局静态可寻址的ID空间，适配百万级以上商品/内容语料规模'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式检索直接构造的DocID前缀无对应语义区域，而代码、电商商品、内容本身存在天然层次语义结构，传统平匹配检索无法有效区分高相似候选，首召准确率低，亟需更合理的可寻址层次化索引支撑生成式检索。

### 方法关键点
- 伪邻居引导的DocID学习：基于RQ-VAE做多级残差量化生成分层ID，用预训练编码器得到的语义k-NN邻接关系+分层相似度阈值做伪标签，监督语义相似样本共享对应深度的ID前缀，同时保证不同样本的可区分性
- 双阶段DocID生成引导：训练侧加入hard negative排序蒸馏，对齐预训练编码器的相关性排序分布，增强相似ID的区分度；推理侧构建查询相关的ID前缀树做约束解码，叠加查询相关的前缀加权修正生成概率，减少前缀错误

### 关键实验
在CoSQA、ProCQA代码检索数据集上，对比BM25、CodeBERT、UniXcoder、DSI等12个基线，CoSQA上Hit@1达0.744，较最优基线UniXcoder的0.518提升43.6%；ProCQA Python数据集上Hit@1达0.597，较最优基线NCI的0.406提升47%，各数据集MRR@20均有20%以上相对提升。

### 核心结论
生成式检索的效果上限首先由DocID空间的语义组织结构决定，其次才是生成模型的优化，合理的层次化ID设计能大幅降低生成难度、提升首召准确率
