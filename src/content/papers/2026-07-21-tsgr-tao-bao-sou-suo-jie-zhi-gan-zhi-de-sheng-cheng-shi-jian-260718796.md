---
title: 'TSGR: Taobao Search Generative Retrieval'
title_zh: TSGR：淘宝搜索价值感知的生成式检索与预排统一框架
authors:
- Tianyu Zhan
- Gui Ling
- Tong Xiong
- Kunhai Lin
- Yang Wang
- Kaixuan Zhang
- Zhihong Chen
- Yuliang Yan
- Dan Ou
- Shengyu Zhang
affiliations:
- Zhejiang University
- Taobao & Tmall Group of Alibaba
arxiv_id: '2607.18796'
url: https://arxiv.org/abs/2607.18796
pdf_url: https://arxiv.org/pdf/2607.18796
published: '2026-07-21'
collected: '2026-07-22'
category: GenRec
direction: 生成式搜索 · 价值感知Semantic ID
tags:
- Generative Retrieval
- Semantic ID
- E-commerce Search
- Value-aware Ranking
- Multi-task Training
one_liner: 面向电商搜索的价值感知生成式检索框架，统一召回与预排，线上GMV提升1.64%
practical_value: '- SID构造可复用QP-SID思路，在聚类维度内置多套并行价值排序（全局+query维度的点击/转化排序），将高价值商品的token分配到训练更充分的靠前索引位，天然提升高价值商品的生成优先级，无需修改模型结构即可拿到业务收益

  - 可复用VRM模块设计，复用生成骨干的用户隐藏态，仅增加轻量交叉注意力层融合商品侧特征，实现召回+预排一体化，减少跨阶段目标错位，几乎无额外推理延迟，还可省掉独立预排链路的维护成本

  - 训练可参考渐进式多任务Pre-SFT+加权多正样本SFT pipeline，Pre-SFT阶段先让LLM学会语义到SID的映射、用户意图理解等基础能力，大幅降低SFT阶段的学习难度与数据量要求，加权多正样本直接按业务价值设置权重（付款>点击>曝光），对齐业务目标更高效

  - 线上部署可参考前缀约束的分层beam search方案，前两层SID用前缀树剪枝无效路径，结合动态beam size设置，可将推理延迟控制在工业级搜索可接受的80ms以内'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式检索仅优化语义匹配，对商品业务价值感知薄弱：一是SID构造仅关注语义相似度，相同语义下不同转化价值的商品无区分度，且全局固定的SID忽略不同query场景下的商品价值差异；二是生成候选排序仅依赖beam search生成概率，无法融合商品侧业务特征，导致高价值商品被漏召，限制下游业务收益，在强业务目标导向的电商搜索场景问题尤为突出。

### 方法关键点
- 语义ID层设计QP-SID：构造三层并行码本，前两层基于类目、聚类先验做语义编码，第三层效率码本为每个聚类内置1套全局价值排序（基于30天点击量）+3套query感知的价值排序（基于query关键词与聚类的共现点击统计），高价值、query相关商品分配更早的token索引，天然对齐生成概率与业务价值
- 新增Value-aware Ranking Module（VRM）：复用生成骨干的用户隐藏态，融合商品侧统计特征、预训练商品embedding、SID embedding，通过交叉注意力建模用户-商品交互，输出PV、CTR、CVR多目标分数，与生成目标联合训练，实现召回+预排一体化，无需独立预排阶段
- 训练采用渐进式pipeline：先做Pre-SFT多任务预训练，覆盖语义编码、个性化、检索、协同、推荐5类任务，激活基础能力；SFT阶段采用会话级加权多正样本损失，权重按付款>点击>曝光设置，直接对齐业务目标

### 关键实验
基于淘宝2亿+真实用户交互数据训练，对比FORGE等工业基线，离线HR@1000提升9.16%；线上38天A/B测试，IPV+0.43%，交易笔数+1.12%，GMV+1.64%，推理延迟控制在80ms内，已上线生产。

### 核心结论
生成式检索落地工业电商场景，需将业务价值信号从底层ID构造到上层排序全链路注入，而非仅优化语义匹配。
