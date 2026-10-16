---
title: 'TransX Technical Report: Scaling Sequence Transduction for Recommendation'
title_zh: TransX技术报告：面向工业推荐的可扩展序列转换框架
authors:
- Da Xu
- Liyan Fang
- Divya Venugopalan
- Sunny Hsu
- Xukai Wang
- Rishav Roy Chowdhury
- Cindy Liang
- Nishant Satya Lakshmikanth
affiliations:
- LinkedIn
arxiv_id: '2610.20913'
url: https://arxiv.org/abs/2610.20913
pdf_url: https://arxiv.org/pdf/2610.20913
published: '2026-10-14'
collected: '2026-10-16'
category: RecSys
direction: 工业推荐 · 模型与基建协同设计
tags:
- Recommendation System
- Sequence Transduction
- KV Cache
- Model-Infrastructure Co-design
- Disaggregated Serving
one_liner: 提出序列编码、行为记忆、候选融合解耦的工业推荐框架，实现指标提升与服务成本大幅下降
practical_value: '- 架构分层可直接复用：将用户行为编码、行为记忆存储、候选交叉融合拆为独立可扩展模块，把行为编码计算从在线路径剥离，用离线/近线预计算的行为记忆KV复用跨请求公共计算，大幅降低在线推理成本

  - 训练优化trick落地：采用打包用户全行为轨迹的训练单元，多请求前缀共享同一份行为编码结果，配合序列-扇出并行策略避免重复计算行为前缀，可提升长行为序列推荐模型的训练吞吐量

  - 服务成本优化方案：采用KV量化+分级存储（GPU/host/持久层）+ 离线预填充+近线刷新的分阶段服务架构，同等SLO下可降低80%服务成本，适配大流量高并发的工业推荐场景

  - 算力分配经验复用：编码器深度达到一定阈值后收益饱和，同等模型容量下优先提升候选交叉融合模块容量，行为记忆分辨率随模型扩容基本保持稳定，可指导算力分配避免无效投入'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前工业推荐模型扩容时，长行为序列的重复计算导致在线服务成本随模型容量线性增长，同时缺乏明确的算力分配规则，难以在效果和成本间找到最优平衡。
### 方法关键点
- 架构解耦为三个独立模块：因果序列编码器负责用户行为序列上下文编码，与候选无关可跨请求复用；全局-局部混合行为记忆模块将长历史压缩为固定长度KV，控制内存占用与下游计算量；候选条件融合模块用GQA实现多候选共享行为KV的交叉计算
- 训练基建协同设计：采用打包用户全轨迹的训练单元，多请求前缀共享同一份行为编码结果，配合序列-扇出并行策略降低重复计算，训练吞吐量提升84%
- 服务架构拆分：离线批量预填充全量用户行为KV，近线增量刷新用户最新行为状态，在线仅执行候选融合与打分逻辑，行为KV采用量化+分级存储降低存储与传输开销
### 关键实验结果
在LinkedIn社交推荐场景（2万QPS，单请求0.5k-1.2k候选）开展生产A/B测试：核心模型较基线CTR提升6.02%、转化率提升4.45%；检索与排序后训练变体分别较对应基线CTR提升2.96%、转化率提升1.33%；同等SLO下服务成本降低80%，相同成本下可支撑5倍于HSTU基线的单请求FLOPs，同等FLOPs下H200单卡吞吐量提升4倍。
### 核心结论
推荐系统扩容无需在线成本同比增长，优先将算力分配给候选融合模块比盲目加深编码器收益更高，行为记忆分辨率无需随模型容量同步扩容。
