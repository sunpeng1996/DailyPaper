---
title: 'CONCORD-Rec: Catalog-Conditioned Modality Utility for Semantic-ID Diffusion
  Recommendation'
title_zh: CONCORD-Rec：面向语义ID扩散推荐的目录条件模态效用框架
authors:
- Haopeng Jin
- Bingkang Shi
- Tao Yu
- Yifei Ma
- Hao Liu
- Hongzhu Yi
- Jinwen Luo
affiliations:
- Tencent
- University of Chinese Academy of Sciences
- Beijing University of Posts and Telecommunications
arxiv_id: '2611.23710'
url: https://arxiv.org/abs/2611.23710
pdf_url: https://arxiv.org/pdf/2611.23710
published: '2026-11-18'
collected: '2026-11-19'
category: GenRec
direction: 生成式推荐 · 多模态Semantic ID扩散
tags:
- Semantic ID
- Diffusion Recommendation
- Multimodal Fusion
- Generative Recommendation
- Counterfactual Learning
one_liner: 用反事实目录分区效用监督模态门控，提升多模态语义ID扩散推荐的鲁棒性与推理效率
practical_value: '- 多模态融合可直接复用反事实效用评估逻辑，针对商品标题/主图/详情页/视频等模态动态分配权重，适配电商场景普遍存在的模态冲突、缺失问题

  - B*tanh模态残差限幅设计可直接落地，既能保证模态信息不会覆盖行为主信号，极端场景还能完全回退到纯行为推荐，规避多模态引入的bad case

  - 扩散推荐推理优化可参考4步解码方案，对比常规16步解码延迟降低近70%，同时效果不降反升，适配电商推荐低延迟的线上要求

  - 离线跨折教师标注模态效用的方案可复用，无需上线AB实验就能提前量化不同模态对不同推荐场景的真实增益，降低试错成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多模态Semantic ID扩散推荐默认所有输入模态均有效，当商品的文本、图像、音视频模态出现缺失、质量退化或语义冲突时，全局均匀融合策略会在迭代去噪过程中传播错误信息，大幅降低推荐效果。

### 方法关键点
- 离线用跨折冻结教师模型做反事实效用标注：对相同候选集与掩码SID状态，对比加入/移除某模态时目标code分区的损失差，作为该模态的效用监督信号，不直接蒸馏token概率
- 设计位置级动态门控：每个未解码的SID位置结合模态可用性输出权重，对模态残差用B*tanh做幅值限制，保留纯行为特征的base槽位，极端场景可完全回退到纯行为推荐
- 解码阶段绑定可行目录约束：仅在匹配已解码code的在库商品中生成候选，避免输出无效SID

### 关键结果
在MicroLens-100K等20个兼容协议的数据集上对比均匀融合基线：干净场景NDCG@20平均提升4.0%；30%模态缺失时提升7.95%；30%模态语义冲突时提升14.63%；4步解码对比16步均匀解码，p95延迟降低68.14%同时NDCG@20提升2.68%。

> 最值得记住：多模态信息的可用性不等于有用性，针对预测任务的反事实效用评估才是动态分配模态权重的可靠依据
