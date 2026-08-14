---
title: 'DTAMLP: Denoise Time-aware MLP for Session-based Recommendation'
title_zh: DTAMLP：面向会话推荐的去噪时间感知多层感知机模型
authors:
- Jiamu Zheng
- Xiaojun Shan
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2608.12975'
url: https://arxiv.org/abs/2608.12975
pdf_url: https://arxiv.org/pdf/2608.12975
published: '2026-08-13'
collected: '2026-08-14'
category: RecSys
direction: 会话推荐 · 时间感知噪声过滤
tags:
- Session-based Recommendation
- MLP
- Time-aware
- Denoise
- Frequency Domain Filtering
one_liner: 提出即插即用时间权重融合方案与频域去噪的全MLP会话推荐架构
practical_value: '- 可直接复用即插即用的权重融合模块：无需修改TiSASRec、SR-GNN等现有模型主干，仅将原生注意力权重与阈值截断的点击间隔权重做线性融合，β可设为固定值或可学习参数，即可稳定提升排序指标

  - 电商会话场景处理短停留误点击时，无需直接丢弃短停留交互，对相邻点击间隔做阈值截断后按权重衰减处理，更贴合真实用户行为（误点击仍携带部分偏好信号）

  - 高并发实时推荐场景可参考FFT-Transformer设计：用1D FFT频域滤波替代部分Transformer多头注意力或GNN聚合模块，在保证效果的同时降低计算复杂度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有时间感知、GNN类会话推荐模型默认所有点击间隔的信息量等价，忽略了短停留误点击带来的偶发噪声，易导致会话表示偏差；同时FMLP-Rec提出的频域滤波优化效果缺乏可解释性，两类噪声都会显著拉低推荐准确率，而电商场景匿名用户会话占比极高，该问题的优化空间大。

### 方法关键点
- 权重融合模块：将模型原生注意力权重与阈值η截断的点击间隔权重做线性融合，β为融合系数，可直接插入现有模型无需修改主干结构
- FFT-Transformer模块：用1D FFT将物品embedding转换到频域，经可学习滤波矩阵过滤纠缠的偏好噪声后逆变换回时域，替代传统多头注意力降低计算复杂度
- 空间一致表示设计：会话embedding由物品embedding加权求和得到，保证与物品embedding在同一表示空间，后续相似度计算的理论一致性更强

### 关键结果
在Diginetica、RetailRocket两个公开电商数据集上对比11个主流基线：Diginetica上相比最优基线GCARM，MRR@10提升5.72%、NDCG@10提升4.92%、Recall@10提升4.82%；RetailRocket上相比最优基线各指标提升1.17%~4.46%；权重融合模块插入原生TiSASRec，在MovieLens-1m上NDCG@10最高提升0.68个百分点。

### 核心结论
短停留误点击的偶发噪声是会话推荐中极易被忽略的优化点，仅需几行代码实现的即插即用权重融合模块，就能带来稳定的指标收益。
