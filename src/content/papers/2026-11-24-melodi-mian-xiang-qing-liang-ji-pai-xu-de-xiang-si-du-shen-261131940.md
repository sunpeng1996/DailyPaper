---
title: 'MELODI: Similarity-Identity Decoupling for Lightweight Ranking'
title_zh: MELODI：面向轻量级排序的相似度-身份特征解耦框架
authors:
- Quoc Phong Nguyen
- Vuong Le
- Volodymyr Vaskovych
- Julien Monteil
affiliations:
- Amazon International Machine Learning
arxiv_id: '2611.31940'
url: https://arxiv.org/abs/2611.31940
pdf_url: https://arxiv.org/pdf/2611.31940
published: '2026-11-24'
collected: '2026-11-25'
category: RecSys
direction: 推荐系统 · 轻量级候选排序优化
tags:
- Lightweight Ranking
- User Behavior Modeling
- Cross Attention
- Feature Decoupling
- CTR Prediction
one_liner: 提出相似度-身份解耦的轻量级排序框架，大候选集下精度优于基线且延迟更低
practical_value: '- 架构借鉴：排序阶段可拆分相似度分支（用户历史+候选交互）和身份分支（候选独立特征），两路独立优化避免交互信号与静态信号混淆

  - 工程优化：跨注意力的历史K/V缓存可在单请求多候选场景下复用，1000候选场景下延迟最高可降14倍，适合召回后候选量大的精排/粗排场景

  - 选型参考：候选数<500时DIN延迟更优，候选数>500时MELODI的精度+延迟性价比更高，可根据业务候选集规模选型

  - 调优trick：用户历史和候选的嵌入共享LayerNorm可大幅提升基线SASRec的MRR（最高+41.6%），小成本实现提效'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有目标感知排序模型（如DIN、BST）普遍存在两个问题：一是将用户-候选交互信号与候选独立静态特征混合建模，易损失有效信号；二是大候选集下需为每个候选重复计算历史编码，延迟过高，无法满足 latency 约束。同时传统低计算量的 pool-then-similarity 计算顺序无法等价复现 similarity-then-pool 的高精度效果，亟需兼顾精度与推理效率的轻量级排序方案。
### 方法关键点
- 理论证明：当相似度算子对历史输入线性时，低计算量的 pool-then-similarity 模式可完全等价复现 similarity-then-pool 的精度，为架构优化提供理论依据
- 双分支架构：相似度分支采用多头跨注意力做候选感知的历史池化，接无残差的 DCN-v2 风格门控交叉层（仅对候选做非线性变换，对历史保持线性）；独立身份分支单独建模候选静态特征（如基础转化率、品类属性），两路特征拼接后输入 MLP 打分
- 工程优化：历史的嵌入、LayerNorm、K/V 投影结果可在单请求内多候选间复用，避免重复计算
### 关键结果
- 公开数据集（Steam、MovieLens-25M）：MELODI 较 DIN MRR 提升 3.5%~4.4%；1000 候选场景下延迟较 DIN 低 5 倍，较 BST 低 7~8 倍；为 SASRec 加入历史-候选共享 LayerNorm 可使 MRR 最高提升 41.6%
- 亚马逊工业数据集：较基线 AUPRC 提升 7.8%~25%，NDCG@20 提升 3.2%~11.3%；请求级历史复用后延迟较 DIN 低 5~11 倍

**最值得记住的结论**：当排序候选数超过 500 时，相似度-身份解耦+历史缓存的 MELODI 架构可同时实现精度提升与延迟下降，性价比显著优于 DIN、BST 等传统基线
