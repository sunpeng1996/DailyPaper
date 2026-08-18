---
title: 'When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse'
title_zh: 基于文档级注意力崩塌的RAG投毒攻击检测方法
authors:
- Yingtao Ren
- Ziyi Zhao
- Yiwei Fu
- Xiao Luo
- Yu-Cheng Chang
- Chin-Teng Lin
affiliations:
- University of Technology Sydney
- Peking University
- University of Wisconsin–Madison
arxiv_id: '2608.06947'
url: https://arxiv.org/abs/2608.06947
pdf_url: https://arxiv.org/pdf/2608.06947
published: '2026-08-06'
collected: '2026-08-18'
category: RAG
direction: RAG安全 · 投毒攻击检测
tags:
- RAG Poisoning
- Attention Mechanism
- Attack Detection
- Mechanistic Interpretability
- LLM Security
one_liner: 发现RAG投毒引发的文档级注意力崩塌现象，提出轻量实时检测框架D-SCAN
practical_value: '- 电商/广告场景用RAG做问答、商品推荐文案生成时，可复用D-SCAN检测外部召回的商品信息、用户评论等是否被投毒，避免生成虚假推荐内容

  - 无需完全依赖输出侧的困惑度、一致性等做异常检测，可监控LLM推理时的文档级注意力熵、密度等内部信号，更早识别投毒尝试，甚至攻击未生效时就能检测

  - 工程实现上无过多计算开销，单轮推理下D-SCAN的AUC也能达0.8以上，适合线上实时场景部署，线性分类器的结构也便于快速迭代

  - 做RAG系统安全优化时，可优先关注跨文档的注意力分配特征，文档级信号比token级特征对投毒检测的贡献更高，能减少特征冗余'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有RAG投毒检测依赖输出侧的困惑度、一致性等信号，但攻击者会刻意构造高置信度的投毒内容，导致中毒输出的困惑度比正常输出更低，传统不确定性检测完全失效，且现有方法缺乏可解释性，无法定位投毒文档，亟需更鲁棒的检测方案。

### 方法关键点
- 发现RAG投毒下的两大现象：一是盲自信，中毒生成的token平均概率更高、多轮采样一致性更强，传统输出侧指标失效；二是注意力崩塌，模型注意力会异常集中在投毒文档上，文档级注意力熵显著降低
- 提出文档级注意力密度指标，聚合每个生成token对单篇文档的注意力权重，再归一化文档长度消除长度偏差
- 设计轻量检测框架D-SCAN，抽取token级+文档级的注意力熵、方差、密度等特征，训练线性分类器实现投毒检测，同时可定位具体投毒文档

### 关键实验
在2Wiki、HotpotQA、Musique三个多跳QA基准上对比HaloScope、ReDeep、RevPRAG等SOTA基线，D-SCAN在三个数据集的AUC分别达0.9337、0.8330、0.9060，F1分别达0.8578、0.7783、0.8358，全面领先基线；即使攻击未生效（未改变最终输出），D-SCAN仍能保持高检测准确率；单轮推理下所有数据集AUC均超0.8，满足实时要求。

### 核心结论
RAG投毒的核心特征是注意力被恶意文档劫持，监控内部注意力动态比检查输出语义更能提前、准确识别攻击。
