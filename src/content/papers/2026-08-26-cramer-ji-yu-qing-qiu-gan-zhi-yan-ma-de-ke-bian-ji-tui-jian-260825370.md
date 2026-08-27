---
title: 'CRAMER: Control via Request-Aware Masking for Editing Recommenders'
title_zh: CRAMER：基于请求感知掩码的可编辑推荐系统框架
authors:
- Zhiyuan Julian Su
- Naihe Feng
- Zhen Luther Qin
- Ga Wu
affiliations:
- Renmin University of China
- Dalhousie University
arxiv_id: '2608.25370'
url: https://arxiv.org/abs/2608.25370
pdf_url: https://arxiv.org/pdf/2608.25370
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 序列推荐·用户意图实时适配
tags:
- Sequential Recommendation
- Parameter Efficient Tuning
- Model Control
- Request-aware Recommendation
- Mask Tuning
one_liner: 通过请求感知参数掩码调控冻结序列推荐主干，无需重训即可适配用户自然语言即时意图
practical_value: '- 可复用请求感知掩码思路对线上冻结的推荐主干做轻量适配，无需重训即可响应用户即时自然语言意图，适配电商场景下用户临时属性筛选、偏好调整等需求，成本远低于全量重训

  - 掩码位置优先选择Transformer的FFN层和注意力输出投影矩阵WO，这两个位置调控性价比最高，无需全参数掩码即可实现不错的适配效果，有效控制推理 overhead

  - 训练侧可直接复用带KL稀疏正则的损失+Gumbel-Top-k+STE的组合，解决离散掩码的梯度回传问题，无需大幅改动现有训练流程即可快速落地

  - 对话/会话推荐场景下可替代LLM重排方案，在精度持平甚至更优的情况下将推理延迟降低两个数量级，适合对延迟要求高的C端推荐业务'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐模型依赖历史行为建模，无法快速响应用户即时自然语言请求（如「要防水的户外鞋」「不要甜口的零食」），现存适配方案要么需重训主干计算成本过高，要么用LLM推理/重排延迟太大，要么输入侧语义增强的方式捕捉不到否定、细粒度属性约束等复杂意图，无法在冻结已部署主干的前提下实现低延迟实时适配，满足不了大流量线上场景的需求。

### 方法关键点
- 主干完全冻结，仅训练轻量请求转掩码模块：用PLM编码用户自然语言请求，mean pooling得到语义向量，经线性层投影为门控logits
- 采用Gumbel-Top-k采样得到k-hot行列门控向量，分解后对主干的FFN层、注意力输出投影矩阵WO做元素级掩码，无需修改主干结构
- 训练目标为预测损失加KL稀疏正则，用直传估计器（STE）解决离散掩码的梯度回传问题，平衡掩码稀疏性和适配效果

### 关键实验
在ReDial、KuaiSAR、Amazon Beauty/CDs&Vinyl四个数据集上测试，对比Query-SeqRec、BLaIR、LLM-ESR、REARANK四个SOTA基线，基于SASRec和BERT4Rec两个主流序列推荐主干，CRAMER在85.4%的实验设置下显著优于最强基线，NDCG@10最高提升7.8%；推理仅增加0.018s延迟，比LLM重排的REARANK快两个数量级，GPU内存开销仅增加1355MiB，远低于重排方案。

对已部署的冻结推荐主干做请求感知的结构化参数掩码，是平衡适配效果、推理延迟、落地成本的最优路径之一
