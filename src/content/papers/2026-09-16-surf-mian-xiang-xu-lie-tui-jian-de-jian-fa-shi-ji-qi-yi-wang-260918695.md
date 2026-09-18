---
title: 'SURF: Subtractive Updates for Recommender Forgetting'
title_zh: SURF：面向序列推荐的减法式机器遗忘框架
authors:
- Filippo Betello
- Antonio Purificato
- Nicola Tonellotto
- Fabrizio Silvestri
affiliations:
- Sapienza University of Rome
- University of Pisa
arxiv_id: '2609.18695'
url: https://arxiv.org/abs/2609.18695
pdf_url: https://arxiv.org/pdf/2609.18695
published: '2026-09-16'
collected: '2026-09-18'
category: RecSys
direction: 序列推荐 · 隐私合规机器遗忘
tags:
- Sequential Recommendation
- Machine Unlearning
- Recommender System
- GDPR Compliance
- Model Forgetting
one_liner: 面向序列推荐的轻量机器遗忘框架，效果接近全量重训，仅需2%的重训时间预算
practical_value: '- 电商推荐应对GDPR等合规的「被遗忘权」请求时，可直接复用SURF逻辑，无需全量重训，仅针对待遗忘item的近邻训练小辅助模型，推理时做分数减法即可，落地成本极低

  - 完全不修改原模型权重，支持可逆恢复，遇到误删或遗忘请求撤回场景，直接关闭减法逻辑即可，无需额外训练，适配生产环境的动态需求

  - 超参数可直接复用论文最优配置：近邻数k设为1、缩放系数α设为0.7，即可达到遗忘效果与推荐精度的最优平衡，仅需根据场景需求调整α即可快速切换trade-off

  - 可替代商品/内容下架场景的后置过滤方案，从表征层面消除下架item的影响，避免关联违规内容仍被透出，同时不会引入后置过滤的排序偏差'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
GDPR等全球隐私法规要求推荐系统必须支持「被遗忘权」，而现有序列推荐遗忘方案存在明显缺陷：全量重训计算成本极高，分块重训精度损失大，基于影响函数的方案稳定性差、内存开销高，均无法满足生产级落地需求。
### 方法关键点
- 三步轻量流程：1）在原模型embedding空间检索待遗忘item的k近邻，构造仅包含关联交互的小型遗忘数据集；2）复用原模型架构在小数据集上训练辅助模型，专门拟合待遗忘item的影响；3）推理时原模型打分减去α倍辅助模型打分即可，全程不修改原模型权重
- 理论证明三大核心特性：非目标item排名稳定、仅对待遗忘item的局部邻域产生可控扰动、目标item的影响被有效移除，保障全局推荐效果不受损
### 关键实验
在7个公开数据集（MovieLens、Amazon Beauty、Steam等）上，与全量重训、RecEraser、UltraRE等5个SOTA基线对比，适配GRU4Rec、SASRec、BERT4Rec三类主流序列推荐 backbone：
- NDCG@20较最优基线最高提升32%，遗忘效果接近甚至超过全量重训，FRBO指标与全量重训相当，推荐排名稳定性几乎无损失
- 训练时间仅为全量重训的2%，推理额外开销低于10%，效率远高于其他基线
### 核心结论
不修改原模型权重的推理端减法式遗忘，是兼顾合规要求、推荐效果、落地成本的最优生产级方案
