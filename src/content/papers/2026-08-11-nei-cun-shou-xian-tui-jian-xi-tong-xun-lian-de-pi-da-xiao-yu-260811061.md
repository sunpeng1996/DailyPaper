---
title: Batch Size or Negatives? A Selection Rule for Memory-Constrained Recommender
  Training
title_zh: 内存受限推荐系统训练的批大小与负样本数量选择规则
authors:
- Artyom Sabitov
- Daniil Volkov
- Alexey Zaytsev
affiliations:
- Moscow Independent Research Institute of Artificial Intelligence
- Intellectual data analysis and predictive modeling institute
- Applied AI Institute
- Risk department
arxiv_id: '2608.11061'
url: https://arxiv.org/abs/2608.11061
pdf_url: https://arxiv.org/pdf/2608.11061
published: '2026-08-11'
collected: '2026-08-12'
category: RecSys
direction: 推荐系统·训练内存优化
tags:
- Sequential Recommendation
- Negative Sampling
- Sampled Softmax
- Training Efficiency
- Memory Optimization
one_liner: 推导内存受限场景下推荐训练批大小与负样本数的最优分配规则，收敛更快效果更优
practical_value: '- 固定训练内存预算B时，优先最大化批大小n，最小化负样本数k，工程上可直接取n=k=√B，无需额外网格搜索调参，大幅节省调优成本

  - 大品类电商/内容推荐用sampled softmax训练时，无需为负样本数量牺牲批大小，增大批带来的收敛加速和效果提升远多于增加负样本的收益

  - 理论推导的无偏梯度校正方案对SASRec这类主流序列推荐模型无实际收益，业务训练时无需额外实现该校正逻辑，减少冗余开发'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大规模推荐系统采用sampled softmax训练时，内存占用近似为O(nk)（n为批大小，k为负样本数）。固定内存预算B=nk下，优先扩大批还是增加负样本长期缺乏理论指导，多依赖经验调参，浪费算力与调优成本。
### 方法关键点
- 将sampled softmax训练的梯度噪声拆解为批采样噪声（由n控制）和类别采样噪声（由k控制），在标准平滑性与方差假设下推导梯度方差的上界
- 理论证明梯度方差随n增大、k减小而降低，最优分配为n接近B、k接近1；考虑工程约束（负样本需包含批内所有正样本），实际采用n=k=√B的配置
- 推导理论上的无偏梯度校正公式，验证其在实际推荐场景下的效果
### 关键结果
- 覆盖Synthetic、MovieLens-1M、Gowalla、Netflix、MovieLens-20M数据集，模型采用SASRec，优化器兼容SGD与Adam
- 同内存预算下对比3组(n,k)配置：(32,512)、(64,256)、(128,128)
- n=k=√B的配置相比极端不平衡配置，收敛速度指标AUL最高降低72%（Gowalla数据集Adam优化器下，AUL从158降至43.7），NDCG@10最高提升37%（同场景下NDCG@10从0.0649升至0.0889）
- 理论上的无偏梯度校正对SASRec等序列推荐模型无实际效果增益

**最值得记住的结论**：内存受限的sampled softmax训练场景下，增大批大小的收益远高于增加负样本数量
