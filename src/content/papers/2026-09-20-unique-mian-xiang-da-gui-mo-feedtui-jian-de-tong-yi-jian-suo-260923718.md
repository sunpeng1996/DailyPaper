---
title: 'UNIQUE: A Unified Retrieval and Ranking System for Large-Scale Feed Recommendation'
title_zh: UNIQUE：面向大规模Feed推荐的统一检索与排序系统
authors:
- Zhuang Liu
- Yongkang Fu
- Zuodong Yang
- Guangxing Chen
- Zonggang Wu
- Yuqi Lu
- Shouke Qin
- Shantao Li
- Maolin Wang
affiliations:
- Beihang University
- Baidu Inc.
- Hong Kong Institute of AI for Science, City University of Hong Kong
arxiv_id: '2609.23718'
url: https://arxiv.org/abs/2609.23718
pdf_url: https://arxiv.org/pdf/2609.23718
published: '2026-09-20'
collected: '2026-09-23'
category: RecSys
direction: 工业级推荐 · 统一检索排序优化
tags:
- Recommender-Systems
- Retrieval-Ranking-Unification
- Flat-Quantization
- Generative-Retrieval
- Industrial-Deployment
one_liner: 提出融合反馈感知平量化与早期融合的统一检索排序框架，落地百度Feed场景实现指标效率双提升
practical_value: '- 架构层面可复用检索排序早期融合设计，共享底层用户表征减少跨阶段信息损失，同时降低多模型维护成本

  - 量化模块可替换传统层级RQ-VAE为单层平量化+使用频率加权的码分配规则，缓解码本马太效应，提升长尾/冷启物品召回效果

  - 工程落地可参考其TensorRT FP16推理+动态窗口缓存的优化方案，大流量场景下P99 latency可控制在100ms以内，满足工业级实时性要求

  - 多场景复用同一架构仅替换输入特征和训练数据的做法，可大幅降低多业务线推荐系统的迭代维护成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业Feed推荐普遍采用级联检索-排序架构，存在两大核心痛点：一是层级量化召回的误差逐层累积，且头部物品易占用过多码本资源，长尾、冷启物品表征效果差；二是两阶段独立训练存在信息损失，召回无法复用排序的细粒度监督信号，排序效果受限于上游召回候选池质量，同时多模型维护成本高。

### 方法关键点
- 三层耦合架构：①EQN层用DSSM多任务监督学习物品语义表征，替换层级量化为单层平量化，加入码本使用频率加权分配规则缓解马太效应；②UIGN层编码用户多粒度行为序列，采用早期融合架构拼接用户表征、候选物品、候选语义码，实现底层表征共享；③TDN层基于融合表征做多目标（CTR、观看时长、完播率等）排序。
- 端到端训练融合码预测生成损失、多任务排序判别损失、码本学习损失，让排序监督反向优化召回表征。
- 推理时先预测Top语义码召回候选，再用同一模型完成多目标排序，无需独立排序模型。

### 关键结果
离线在KuaiRand-Pure数据集上，相比最优基线UniGRF-HSTU，HR@10提升12.52%，CTR-AUC提升0.84‰；在线在百度移动首页Feed、发现页、短视频场景A/B测试，总观看时长提升0.96%，总分发量提升1.08%，新用户观看时长提升1.44%，P99 latency仅89ms，推理MFU达44.23%。

最值得记住的一句话：统一检索排序的核心不是简单的参数共享，而是通过早期融合实现跨阶段监督信号复用，同时用平量化兼顾召回效率与长尾覆盖。
