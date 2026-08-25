---
title: Towards a Densing Law for User Representation Learning at Billion-Scale Capacity
title_zh: 面向十亿级规模用户表征学习的行为致密化定律
authors:
- Bin Dou
- Junru Zhang
- Zhaoyi Yuan
- Wuliang Huang
- Letian Gong
- Baokun Wang
- Huan Li
- Yu Cheng
- Weiqiang Wang
affiliations:
- Ant Group
- Zhejiang University
arxiv_id: '2608.23392'
url: https://arxiv.org/abs/2608.23392
pdf_url: https://arxiv.org/pdf/2608.23392
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: 十亿级用户表征 行为tokenization缩放定律
tags:
- User Representation
- Tokenization
- Scaling Law
- RQ-VAE
- CTR Prediction
one_liner: 提出用户行为致密化定律与自适应tokenization方法，突破十亿级用户表征的原始数据缩放瓶颈
practical_value: '- 业务侧用户量超过3000万、行为序列长度超过60天后，原始行为数据训练的边际收益会骤降，可优先引入RQ-VAE类行为tokenization压缩输入，性价比远高于盲目堆模型参数、拉长行为窗口

  - 可复用致密化定律的量化公式，根据自身业务的用户规模、行为序列长度、数据多样性，快速估算最小够用的token配置（codebook大小、残差层数），避免无效的超参数遍历

  - 可借鉴ALGN的自适应分配思路，对高行为熵、低重复度的用户分配更多token容量，对常规消费、高重复行为的用户减少token分配，进一步提升输入信息密度

  - 用户表征预训练无需盲目追大模型，0.2B参数已经是原始数据训练的效果天花板，优先优化输入信息密度的ROI更高'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界用户表征学习通常通过提升用户量、拉长行为序列、增大模型规模实现效果增长，但十亿级规模下存在两大痛点：一是原始行为数据缩放瓶颈，冗余行为占比提升导致边际收益骤降，甚至出现预训练loss下降但下游效果不升的「损失-质量解离」现象；二是缺乏量化方法指导tokenization配置随数据规模的缩放规则，易造成资源浪费或效果不足。
### 方法关键点
- 先导实验验证原始行为缩放墙：在十亿级支付宝数据集上证实，用户量超3000万、行为序列超60天、模型参数超0.2B后，下游任务收益基本停滞
- 提出行为致密化定律，量化数据规模与最小充足tokenization容量的幂律关系：对数坐标下容量与数据规模呈线性关系，系数由数据多样性、tokenization方法共同决定
- 提出自适应长度门控网络ALGN，根据量化残差与表达不确定性，给不同用户自适应分配残差量化深度，优化token容量的分配效率
### 关键实验结果
基于支付宝1亿~20亿用户、30~270天行为数据，覆盖分类、文本召回、U2U召回三类下游任务，对比VQ-VAE、RQ-VAE等baseline：行为序列长270天时，tokenized表征AUC比原始输入高0.82个百分点；用户量达1亿时，tokenized表征AUC比原始输入高0.71个百分点；ALGN在同等计算成本下效果优于所有基线tokenization方法。
### 核心结论
十亿级用户表征的核心瓶颈不是模型容量或数据总量，而是输入行为的信息密度，通过致密化提升单位输入的有效信息，收益远高于盲目堆数据、堆模型。
