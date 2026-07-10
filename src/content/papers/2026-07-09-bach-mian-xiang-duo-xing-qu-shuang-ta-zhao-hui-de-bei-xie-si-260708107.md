---
title: 'BACH: A Bayesian Admixture of Contrastive Heads for Multi-Interest Two-Tower
  Retrieval'
title_zh: BACH：面向多兴趣双塔召回的贝叶斯对比头混合模型
authors:
- Quoc Phong Nguyen
- Paul Albert
- Long Vuong
- Vuong Le
- Julien Monteil
affiliations:
- Amazon
arxiv_id: '2607.08107'
url: https://arxiv.org/abs/2607.08107
pdf_url: https://arxiv.org/pdf/2607.08107
published: '2026-07-09'
collected: '2026-07-10'
category: RecSys
direction: 多兴趣双塔召回 · 贝叶斯软路由
tags:
- Two-Tower Retrieval
- Multi-Interest Recommendation
- Variational Inference
- Candidate Generation
- Bayesian Model
one_liner: 用变分推断实现多兴趣双塔软路由，缓解头塌陷同时输出用户级兴趣权重
practical_value: '- 训练多兴趣双塔时可直接替换传统正样本选头的硬路由，改为给所有候选计算max内积的serving-consistent训练，实验显示可比目标路由提升9%~29%
  R@100，是零额外成本的效果提升trick

  - 可在现有多兴趣双塔基础上新增轻量门控塔，输出用户级兴趣权重πu，既缓解头塌陷，还能直接用于serving阶段对各头召回结果加权，无额外推理开销

  - 低延迟/冷启动场景可采用全局共享兴趣头+个性化权重方案，各头的召回列表提前离线预计算，serving仅需完成加权排序，同时支持运营手动调控兴趣曝光占比

  - 多兴趣头的浓度可通过球形后验软路由自正则，无需额外添加头使用正则项，减少调参成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
双塔召回单用户embedding无法覆盖用户多元兴趣，现有多兴趣硬路由机制易出现赢者通吃的头塌陷问题，且无法输出用户级兴趣重要性权重，serving时只能假设头权重均匀，导致头部兴趣过度曝光、小众兴趣被压制。

### 方法关键点
- 将多兴趣双塔建模为用户级softmax混合模型，通过变分推断拟合，采用power-spherical/von Mises-Fisher球形识别后验替代硬argmax路由，给所有头分配梯度从根源缓解头塌陷
- 新增独立门控塔输出用户级兴趣权重πu，直接复用在serving阶段对各头召回结果加权，训练与serving逻辑完全一致
- 支持全个性化头到全局共享兴趣头的平滑过渡：全局头方案可提前预计算各头的召回列表，serving仅需加权排序，大幅降低延迟
- 头的浓度通过ELBO的KL项自正则，无需额外先验或正则约束

### 关键结果
在MovieLens-20M、Taobao、Netflix三个大规模基准数据集上，对比单向量双塔、硬路由多兴趣基线（MIND、ComiRec等）：
1. 32头p-BACH在MovieLens上AUPRC达0.069，较最优硬路由基线高3.6%；v-BACH在Netflix上AUPRC达0.091，较硬路由基线高12.7%
2. serving-consistent的全候选max训练比传统正样本选头路由，R@100提升9%~29%，AUPRC提升13%~41%
3. 全局共享头方案性能接近单向量双塔，serving延迟降低90%以上，冷启动友好

### 核心结论
多兴趣双塔的训练规则必须与serving的打分规则对齐，用软路由替代硬argmax既能缓解头塌陷，还能得到可解释、可调控的用户兴趣权重
