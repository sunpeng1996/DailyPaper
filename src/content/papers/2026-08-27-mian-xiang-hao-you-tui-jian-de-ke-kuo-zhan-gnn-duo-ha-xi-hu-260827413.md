---
title: 'Scaling Graph Neural Networks for Friend Recommendation: Multi-Hash User Embeddings
  and Temporal Neighbor Sampling'
title_zh: 面向好友推荐的可扩展GNN：多哈希用户嵌入与时序邻居采样
authors:
- Maksim Utushkin
- Andrei Ovsiannikov
- Alexander D'yakonov
affiliations:
- AI VK
arxiv_id: '2608.27413'
url: https://arxiv.org/abs/2608.27413
pdf_url: https://arxiv.org/pdf/2608.27413
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 大规模图推荐 · GNN可扩展性优化
tags:
- GNN
- Friend Recommendation
- Multi-Hash Embedding
- Temporal Graph Sampling
- Large-scale Recommendation
one_liner: 提出多哈希ID嵌入与时序邻居采样结合的超大规模GNN好友推荐系统，线上获16%好友添加量提升
practical_value: '- 高基数ID场景可直接复用多哈希嵌入方案，亿级用户下仅用<1%的内存开销即可达到与全量ID嵌入表相当的效果，规避超大嵌入表的分布式存储复杂度

  - 动态图训练避免未来信息泄露时，可采用邻接表按时戳排序+二分查找的采样方案，将时序采样耗时从O(deg(v)+k)降至O(log deg(v)+k)，训练速度提升约2.5倍

  - 大规模GNN部署可采用CPU采样与GPU训练解耦的pipeline，单台8A100主机即可支撑200亿边级别的图训练，降低分布式部署门槛

  - 慢变化关系（好友、关注等）推荐场景，可采用定期离线刷新GNN嵌入、在线仅做内积打分的方案，完全不增加排序链路延迟'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
超大规模社交场景下的好友推荐核心依赖多跳图结构信息，GNN是天然适配方案，但落地面临三大痛点：194M用户、28B边的规模带来极高存储压力；用户属性信号弱，但全量ID嵌入表超过200GB无法落地；动态图训练时防止未来信息泄露的时序邻居采样，对高degree用户存在O(deg(v))的性能瓶颈，主流GNN库原生实现无法满足生产要求。
### 方法关键点
- 输入层采用多哈希ID嵌入：通过3个独立哈希函数将用户ID映射到远小于用户量的共享嵌入表，拼接后投影得到ID表征，结合少量属性特征作为GNN输入
- 时序邻居采样优化：邻接表采用按时戳排序的CSR存储，采样时通过二分查找快速定位当前时刻之前的合法邻居前缀，再从中均匀采样k个邻居，避免全量扫描邻接表
- 训练架构采用CPU采样与GPU训练解耦：CPU侧负责子图采样构造批量，GPU侧专注模型训练，多进程并行平衡算力瓶颈
### 关键实验
实验基于VK生产社交图，含194M用户、28B边，对比Top-pop、MF、生产基线WalkGNN：离线ROC-AUC达0.6278，较基线WalkGNN提升0.0706；线上A/B测试较生产基线，好友添加量提升16%，新增好友用户数提升11.5%，排序latency无回归；多哈希方案仅用2GB内存就达到203GB全量ID嵌入表相当甚至更优的效果，二分采样比naive时序采样快2.5倍。
### 核心结论
工业级大规模GNN落地的核心瓶颈往往不是模型架构选择，而是ID表征压缩、采样效率等工程设计决策的优化。
