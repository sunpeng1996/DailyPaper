---
title: Mitigating Popularity Bias in Sequential Recommendations with Sparse Prior-Regularized
  Objective
title_zh: 基于稀疏先验正则化目标的序列推荐流行度偏差缓解方法
authors:
- Anton Pembek
- Anton Klenitskiy
- Alexander Savchenko
- Alexey Vasilev
affiliations:
- Sber AI Lab
- Lomonosov Moscow State University (MSU)
- HSE University
arxiv_id: '2610.17823'
url: https://arxiv.org/abs/2610.17823
pdf_url: https://arxiv.org/pdf/2610.17823
published: '2026-10-13'
collected: '2026-10-14'
category: RecSys
direction: 序列推荐 · 流行度偏差缓解
tags:
- Sequential Recommendation
- Popularity Bias
- Entmax
- Loss Function
- Debiasing
one_liner: 提出无需修改模型架构的PR-entmax训练目标，同时提升序列推荐相关性与去流行度偏差效果
practical_value: '- 现有序列推荐pipeline可直接替换交叉熵损失为PR-entmax，无需修改模型架构，仅调整训练侧逻辑，推理侧去掉先验项即可，落地成本极低

  - 可复用「训练阶段加入流行度先验调整logit、推理侧用纯上下文得分」的范式，平衡训练阶段负样本竞争合理性与推理阶段相关性纯净度

  - 稀疏度参数α推荐取1.2~1.6区间，可在几乎无损NDCG的前提下大幅提升长尾商品曝光，覆盖度最高可相对提升44%，适配电商长尾提效需求

  - 可借鉴动态负样本选择逻辑：仅让同时满足上下文相关+有一定流行度的负样本参与梯度更新，减少无用负样本的训练算力浪费'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐模型普遍基于交叉熵损失优化，易放大流行度偏差，导致头部商品过度曝光、长尾商品曝光不足，用户体验受限且平台生态失衡；现有去偏差方案普遍存在去偏效果提升但推荐相关性下降的 trade-off，落地性价比低。

### 方法关键点
- 基于entmax稀疏概率映射设计PR-entmax损失，将商品流行度先验`log q_i`直接加在模型输出的上下文logit上，共同决定参与梯度更新的活跃样本集
- 训练阶段用先验调整后的得分计算稀疏概率，仅得分高于阈值的样本参与梯度更新，自动筛选同时满足上下文相关、有一定流行度的硬负样本，减少无效训练
- 推理阶段完全移除流行度先验项，直接用模型输出的纯上下文相关性得分排序，避免先验干扰最终推荐的相关性

### 关键实验结果
在ML-1M、天猫、Yoochoose等5个涵盖电商、影视、音乐的公开数据集上，基于SASRec、GRU4Rec两种主流序列模型，对比交叉熵、IPW、logit调整等6种基线方法：PR-entmax在多数数据集上NDCG@10相对提升2%~18%，Coverage@10相对提升14%~44%，Novelty@100最高相对提升33%，整体上移了相关性-去偏差的帕累托前沿。

> 最值得记住：仅修改训练损失、推理无额外开销的PR-entmax，是平衡序列推荐相关性与长尾曝光的高性价比落地方案
