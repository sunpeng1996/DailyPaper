---
title: 'RetrievalFormer: A Dual-Encoder Transformer for Efficient Approximate Nearest
  Neighbor Retrieval and Cold-Item Recommendation'
title_zh: 开放索引：共享搜索推荐架构在推荐侧的性能损耗量化
authors:
- Theodore Rogers
- Joe Standerfer
- Dmitrii Timoshenko
- Haoxue Li
- Zuhaib Akhtar
- Soyoung Yang
affiliations:
- Amazon Web Services
arxiv_id: '2608.24079'
url: https://arxiv.org/abs/2608.24079
pdf_url: https://arxiv.org/pdf/2608.24079
published: '2026-08-25'
collected: '2026-08-26'
category: RecSys
direction: 共享搜索推荐 · 双编码器召回冷启动
tags:
- Two-Tower
- Cold-Start
- Sequential Recommendation
- ANN Retrieval
- Unified Search Recommendation
one_liner: 量化双编码器共享搜索推荐索引的推荐侧精度损失、冷启动增益与训练目标规模瓶颈
practical_value: '- 上新频繁的电商/内容场景可优先选双编码器架构做共享索引，冷启Recall@20比专用冷启方法高40%，无需额外冷启训练阶段即可支持新物品零样本召回。

  - 训练目标按需选型：小 catalog 用full-softmax cross-entropy可提6.9%~54%的Recall@20；超过240K item的大
  catalog 需用优化后的采样InfoNCE避免OOM。

  - 基准对比需提前校准时序标签：RecBole等工具默认将timestamp转float32会导致19.7%的用户时序目标排序错误，直接用会导致基线对比完全失准。

  - 冷启/暖启性能可通过分数融合兼得：直接加权融合内容塔冷启分数与ID类CF暖启分数，无需额外训练即可同时保持两类场景的最优性能。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界越来越多采用共享搜索推荐item索引的架构，用一套双编码器embedding同时服务两类请求，但共享索引在推荐侧的精度损耗一直没有严格量化；同时ID-softmax类推荐模型无法支持新物品零冷启，无法满足搜索侧新物品即时可召回的强要求，亟需明确这套架构的性能trade-off。

### 方法关键点
- 设计RetrievalFormer非对称双编码器：用户侧用Transformer建模交互序列，物品侧用AttentionFusion模块编码异构特征，跨塔共享特征embedding表，既减少参数量又保证语义一致性。
- 对比两类训练范式：采样InfoNCE（训练成本与catalog规模无关，适合大库）、full-softmax交叉熵（直接优化全库排序，精度更高但训练内存随catalog线性增长）。
- 严格控制评估协议：用整数timestamp校准时序目标，解决float32精度导致的19.7%用户目标排序错误问题；所有基线均经过5轮调优，冷启实验严格零泄露保证对比公平。

### 关键结果
- 暖启动场景：MovieLens-1M上RetrievalFormer达到最强ID类基线Recall@20的94.8%（相对损失5.2%），NDCG@20的88.6%（相对损失11.4%）；MIND短序列数据集上差距缩小到0.8%~3.6%。
- 冷启动场景：严格零泄露的物品冷启下，内容塔Recall@20达0.172，是最强专用冷启基线的1.4倍，无训练内容相似性基线的3倍。
- 训练目标瓶颈：切换为full-softmax目标在MIND-small上提54%Recall@20，MovieLens-1M提6.9%，但catalog规模到240K时单44G GPU即OOM。

最值得记住的一句话：双编码器共享索引的暖启精度损失可接受，其零冷启能力刚好适配搜索推荐共构的即时上新需求，训练目标的规模墙是当前最大落地瓶颈。
