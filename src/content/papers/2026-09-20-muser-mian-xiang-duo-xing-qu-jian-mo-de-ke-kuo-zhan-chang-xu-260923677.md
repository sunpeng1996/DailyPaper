---
title: 'MuSeR: Scalable Long-sequence Recommendation with Multi-interest Modeling'
title_zh: MuSeR：面向多兴趣建模的可扩展长序列推荐框架
authors:
- Yongkang Fu
- Beining Bao
- Yu Jiang
- Xiangyu Zhao
- Hongyang Wei
- Guangxing Chen
- Zuodong Yang
- Shantao Li
- Zonggang Wu
- Yuqi Lu
affiliations:
- Baidu
- City University of Hong Kong
- Chinese University of Hong Kong
arxiv_id: '2609.23677'
url: https://arxiv.org/abs/2609.23677
pdf_url: https://arxiv.org/pdf/2609.23677
published: '2026-09-20'
collected: '2026-09-23'
category: RecSys
direction: 长序列推荐 · 多兴趣用户建模
tags:
- Long-sequence Recommendation
- Multi-interest Modeling
- Multimodal Alignment
- Industrial Recommendation
- Retrieval
one_liner: 融合分层压缩、多兴趣提取、多模态对齐的工业级可落地长序列推荐检索框架
practical_value: '- 可直接复用用户行为序列分层压缩策略：近期行为保全量精度、中期16倍池化、早期64倍池化，将1e4~1e5长度行为压缩到千级以内，平衡精度和时延

  - 多兴趣建模可复用正交正则化约束避免兴趣向量冗余，线上服务时异步更新长期兴趣向量缓存，实时计算短期兴趣动态加权融合，降低60%冗余计算

  - 物品侧可复用「大模型生成语义摘要+轻量Embedding模型蒸馏+ID/语义Embedding融合」方案，大幅提升冷启动/短视频场景召回效果，实测相对提升30%+

  - 向量检索可复用分层波束搜索策略，上层用HNSW粗召、下层用多目标DNN重排，相比纯HNSW降低27%端到端时延、降低35%部署成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐系统受限于时延和内存预算，通常仅保留数百条近期用户行为，长期稳定兴趣信号被丢弃；同时用户跨模态、多异质兴趣难以通过稀疏ID表征充分建模，现有长序列、多兴趣方案大多无法同时满足精度、时延、成本的工业落地要求。

### 方法关键点
- 分层时序压缩：将用户行为按时间分为近期、中期、早期三段，分别保留全量、16倍池化、64倍池化，将1e4~1e5长度行为压缩到千级左右，用轻量Transformer编码
- 多查询兴趣提取：用M个可学习query向量从压缩序列中提取多个独立兴趣向量，训练时加正交正则化保证兴趣解耦，线上服务时动态加权匹配候选物品
- 多模态语义对齐：用ERNIE-4.0-Turbo生成物品语义摘要，蒸馏到轻量模型后用BGE映射为语义向量，和ID Embedding融合得到统一物品表征，缩小语义鸿沟
- 工程部署：异步更新长期兴趣向量缓存，实时计算短期兴趣动态融合，检索采用分层波束搜索，适配CPU/GPU/NPU异构硬件

### 关键结果
公开数据集上Amazon三个品类的Recall@K、NDCG@K均优于SOTA基线NANN，最高相对提升2.4%；百度工业数据集上首页Feed场景Recall@100达0.087、Recall@500达0.2232，发现页/短视频场景Recall@100达0.1377、Recall@500达0.2534，均显著优于基线；线上A/B测试全场景落地后，Feed DAU提升0.26%，总会话时长提升0.89%。

### 核心结论
工业级推荐系统的核心突破往往不是单一模型创新，而是模型、工程、业务约束的系统级整合，在精度、时延、成本三者间找到最优平衡。
