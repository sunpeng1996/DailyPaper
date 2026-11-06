---
title: 'OptST: Optimizing Semantic Tokenization for LLM-Enhanced Recommendation'
title_zh: OptST：面向LLM增强推荐的语义分词优化
authors:
- Hanchong Chen
- Jie Liu
- Fuyuan Lyu
- Dugang Liu
- Lingjie Li
- Xiuqiang He
- Xing Tang
affiliations:
- 深圳技术大学
- 香港理工大学
- 麦吉尔大学
- 深圳大学
arxiv_id: '2611.07523'
url: https://arxiv.org/abs/2611.07523
pdf_url: https://arxiv.org/pdf/2611.07523
published: '2026-11-05'
collected: '2026-11-06'
category: GenRec
direction: LLM增强推荐 · 语义分词优化
tags:
- Semantic ID
- RQ-VAE
- LoRA
- LLM4Rec
- CTR Prediction
one_liner: 通过低秩码本适配和交互感知前缀选择优化语义分词，提升LLM增强推荐性能
practical_value: '- 语义分词适配技巧：预训练RQ-VAE无需重训，仅通过层共享LoRA+anchor正则适配下游推荐任务，参数量仅2dr/层，远低于全量码本更新，工程落地成本低

  - 前缀动态选择方案：引入交互感知深度门控，根据用户/物品冷热度、残差量化状态动态选择token前缀长度，可在效果和存储/计算开销间做自适应平衡

  - 梯度回传Trick：离散token赋值采用直通估计(STE)，前向硬赋值保证推理效率，后向软加权传递推荐损失，解决离散操作无梯度问题

  - 架构兼容设计：生成的离散token完全兼容现有推荐的类别特征Embedding lookup范式，无需修改原有推荐主干架构即可快速接入'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM增强推荐的语义分词普遍采用两阶段流水线：分词器预训练后固定，下游推荐任务无法调整语义分区规则，无法区分对推荐有价值的细粒度语义差异；同时固定的token深度无法适配不同交互的语义粒度需求，全量使用所有层会带来不必要的存储和计算开销。连续语义向量存储成本高，现有离散token方案又存在任务不匹配问题，亟需面向下游推荐任务适配的高效语义分词方案。
### 方法关键点
- 冻结预训练RQ-VAE的编码器和基础码本，每层码本采用共享低秩变换做任务适配，搭配anchor正则限制与预训练语义结构的偏差，避免语义漂移
- 采用直通估计(STE)实现离散token赋值的梯度回传：前向硬近邻赋值保证推理时的离散性，后向软加权传递推荐损失，解决离散操作无梯度问题
- 新增交互感知的前缀选择门控，输入残差量化状态、用户/物品频率、层位置特征，动态选择当前交互所需的token深度，搭配深度正则避免默认使用全量层
### 关键结果
在4个公开推荐数据集（Movies、Yelp、Games、Clothing）上对比13个基线：
- 相比SOTA LLM增强推荐基线UserIP，AUC分别提升0.21%、0.21%、0.44%、0.56%，均达统计显著性
- 适配AutoInt、DeepFM、DCNv2等5种不同推荐主干，均获得稳定AUC提升，无需修改原有主干架构
- 层共享低秩适配相比全量码本更新，参数量减少90%以上，效果反而更优
### 核心结论
任务感知的语义分词是LLM生成的用户/物品语义与下游推荐模型之间的高效接口，无需重训上游大模型即可显著提升推荐效果
