---
title: 'SPADE: Spatiotemporal Preference Alignment and Diversity Enhancement for Local
  Search'
title_zh: SPADE：面向本地搜索的时空偏好对齐与多样性增强生成式Query推荐框架
authors:
- Chenxu Wang
- Wenxuan Yang
- Yueqi Mou
- Shuxian Bi
- Biao Tang
- Peng Yan
affiliations:
- Meituan
- Independent
arxiv_id: '2611.04662'
url: https://arxiv.org/abs/2611.04662
pdf_url: https://arxiv.org/pdf/2611.04662
published: '2026-11-03'
collected: '2026-11-04'
category: QueryRec
direction: 生成式Query推荐 · 本地时空建模
tags:
- QueryRecommendation
- GenerativeRec
- SpatiotemporalModeling
- DPO
- BeamSearch
- LocalSearch
one_liner: 美团提出生成式本地搜索Query推荐框架，四大组件联合优化，离线在线效果均超工业SOTA
practical_value: '- 分词器优化：可复用OA-BPE思路，将业务价值（CTR/CVR/GMV等）加权到BPE合并规则，无需额外训练即可提升高价值长尾query/商品的生成概率

  - 时空特征注入：本地生活/到店/外卖业务的推荐/Query推荐场景，可复用STAR模块，用多尺度正弦编码+零初始化软门注入连续时空特征，避免破坏预训练LM表示，提升细粒度时空匹配效果

  - DPO落地优化：工业场景偏好对齐可复用MARS-DPO，直接用线上召回列表构造正负样本，采用多维度复合reward+自适应难负采样+SFT锚定损失，避免纯DPO的效果漂移，适配真实业务反馈分布

  - 解码多样性优化：生成式推荐解码阶段可替换标准beam search为SDBS，仅给低秩beam加位置感知sigmoid奖励，不损失top相关性的前提下提升输出多样性，复杂度仅O(B)适配低延迟要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
本地生活平台首页主动Query推荐是核心流量入口，现有方案存在四大痛点：标准BPE按词频合并，长尾高价值query被过度切分导致生成概率低；粗粒度位置编码无法匹配细粒度地理需求；通用偏好优化和线上真实曝光点击分布不匹配；标准beam search输出高度重复，浪费展示位，亟需端到端框架同时解决长尾覆盖、时空对齐、偏好匹配、输出多样性四个核心要求。

### 方法关键点
- 词汇层：OA-BPE将业务价值（CTR/CVR/曝光量权重）融入BPE合并规则，给高价值长尾query更短的分词结果，提升其生成先验，复杂度和标准BPE一致
- 输入层：STAR模块用多尺度六角正弦编码对GPS和时间做连续表征，通过零初始化软门逐步注入模型，不破坏预训练LM基础表示，实现细粒度时空对齐
- 训练层：MARS-DPO分两阶段训练，先跨域预训练学习通用意图，再用线上曝光点击数据做偏好对齐，采用多维度复合reward（排名+检索质量+地理距离）、自适应难负采样、SFT锚定损失，适配真实业务分布
- 解码层：SDBS给低秩beam加位置感知sigmoid多样性奖励，top beam不受干扰，仅O(B)复杂度，不损失召回的前提下提升输出slate多样性

### 关键实验
在美团10万用户、148万唯一query的生产数据上实验，对比最强生成式基线AIGQ，离线HR@5+5.6%、GeoC@5-40.3%、Exec@5+1.9%，长尾意图下HR@5+13.5%，地理稀疏区域GeoC@5-48.3%；一周线上A/B测试实现模块CTR+1.88%、搜索量+0.177%、搜索DAU+0.105%，P95延迟65.4ms满足线上要求。

最值得记住的一句话：生成式推荐的优化要从词汇、编码、训练、解码全链路联合设计，各环节的小改进会叠加产生远超单点优化的业务收益。
