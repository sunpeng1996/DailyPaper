---
title: 'POEM: Partial-Order Enhanced Real-Time Sequential Modeling for Recommendation'
title_zh: POEM：面向推荐的偏序增强实时序列建模框架
authors:
- Linxiao Che
- Yijia Sun
- Siyuan Lou
- Shanshan Huang
- Qiang Luo
- Ruiming Tang
- Han Li
- Kun Gai
affiliations:
- Kuaishou Technology
- Unaffiliated
arxiv_id: '2606.29946'
url: https://arxiv.org/abs/2606.29946
pdf_url: https://arxiv.org/pdf/2606.29946
published: '2026-06-29'
collected: '2026-06-30'
category: RecSys
direction: 实时推荐 · 偏序学习 · 多阶段对齐
tags:
- Sequential Recommendation
- Partial-Order Learning
- Real-Time Recommendation
- Multi-Stage Recommendation
- Cascade Alignment
one_liner: 利用前序请求的多目标排序信号构建偏序序列，实现请求级实时用户兴趣建模
practical_value: '- 多阶段推荐系统可借鉴将下游实时排序信号结构化融入上游召回输入的思路，提升级联一致性和候选通过率，改善整体 pipeline
  效果

  - 多目标排序信号融合可复用逆秩加权融合方案，天然解决不同目标分数尺度不一致问题，无需额外归一化，工程实现简单

  - 训练正样本可采用「用户真实反馈+系统偏好Top项」的双正样本策略，兼顾用户真实兴趣和级联对齐，缓解用户反馈稀疏和选择偏差问题

  - 工业级实时serving可复用基于低延迟缓存存储前序请求排序结果的流水线，实现请求级兴趣更新，延迟可控'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统顺序推荐仅依赖静态的用户历史点击序列，仅在用户产生新交互后才更新兴趣表示，无法捕捉请求级的实时兴趣偏移；同时多阶段推荐 pipeline 中，上游召回未利用下游排序阶段产生的实时多目标偏序信息，存在阶段目标不一致、候选通过率低的问题。

### 方法关键点
- 动态偏序序列构造：每次用户请求，从缓存读取前一次请求的Top排序候选，对CTR/CVR/watch time等多目标排序分数，采用逆秩加权融合得到统一得分，按得分分组后组内随机采样，构造保留偏序结构的动态序列；
- 双序列编码：用户历史交互序列和动态偏序序列分别用独立Transformer编码，融合得到最终用户兴趣表示；
- 分层学习策略：正样本同时包含用户真实反馈正例和系统偏好Top正例，基于 Swing 算法构建的商品图挖掘上下文感知hard negative，损失结合交叉熵和带间隔的pairwise损失。

### 关键实验结果
基于快手108M用户、42M商品的大规模工业数据验证，离线对比DSSM/SASRec/CAIN，在1小时实时测试集上，POEM的HR@50相对次优基线提升15.9%，NDCG@50提升29.9%；在线A/B测试，在两个主场景分别获得人均观看时长+0.249%、+0.213%的显著增益。

最值得记住的一句话：排序信号不仅可以做监督信号，还可以作为结构先验构造输入序列，实现请求级实时兴趣建模和多阶段对齐。
