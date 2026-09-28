---
title: 'KuaFu: Compressing Long User Behavior into Understanding at Billion Scale'
title_zh: KuaFu：十亿级规模下超长用户行为压缩理解框架
authors:
- Jiahao Hui
- Lin Zhu
- Yishen Hu
- Jingdong Shu
- Zetai Jiang
- Xining Ran
- Ben Tan
- Yeshou Cai
- Gong Chen
- Haijie Gu
affiliations:
- Tencent Inc.
arxiv_id: '2609.31045'
url: https://arxiv.org/abs/2609.31045
pdf_url: https://arxiv.org/pdf/2609.31045
published: '2026-09-25'
collected: '2026-09-28'
category: RecSys
direction: 用户建模 · 长行为序列压缩
tags:
- User Modeling
- Long Behavior Sequence
- Context Compression
- LLM4Rec
- Industrial Deployment
one_liner: 提出双轴可缓存的用户行为压缩层，兼顾理解保真度与推理效率，已落地腾讯十亿级推荐场景
practical_value: '- 复用单行为item级独立压缩设计，压缩后embedding按物料ID缓存，缓存规模随物料库而非用户数×任务数增长，大幅降低十亿级场景的存储与重复计算成本

  - 训练可参考四阶段保真范式：重建预训练→压缩QA后训练→压缩生成联合训练→幻觉感知RL优化，搭配序列长度递增的课程学习，解决长序列压缩训练不收敛问题

  - 幻觉优化可采用按业务危害加权的RL奖励，比如将虚构用户兴趣设为最高惩罚，同时增加回答完整度奖励，平衡幻觉抑制与回答覆盖度，避免模型拒答

  - 工程部署可将离线item压缩集群与在线用户画像解码集群拆分，分别扩缩容，兼顾离线批量计算效率与周更十亿级用户画像的吞吐要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界LLM驱动的对话Agent、生成式推荐、个性化广告系统均依赖超长用户行为理解，现有单任务方案先过滤任务相关行为子序列再单独建模，面临两大核心瓶颈：一是过滤后单用户平均仍有数百到上千行为，序列化后token规模达数万，远超LLM上下文窗口；二是十亿级用户画像每周更新需要100K QPM算力，固定GPU预算下吞吐压力极大。直接截断或粗粒度压缩会引入虚构兴趣、信号遗漏、时间错配、逻辑断裂四类幻觉，且错误只能通过下游业务指标感知，迭代周期长达数月。
### 方法关键点
- 以单行为item为最小压缩单元，每个item独立编码，压缩后embedding可跨用户、跨任务复用缓存，新行为只需增量编码追加，无需全序列重压缩
- 双轴投影器沿两个维度压缩：token轴将8个memory token压缩到2-4个（压缩比10×），维度轴将2560维压缩到128-256维（压缩比20×），单item缓存从10KB降至0.5KB
- 四阶段保真导向训练：重建预训练→压缩QA后训练→压缩生成联合训练→幻觉感知RL训练，搭配序列长度递增的课程学习保证收敛；RL阶段针对四类幻觉按业务危害加权惩罚，增加完整度奖励避免模型拒答
- 分层中间评估协议直接评估压缩表示保真度，将压缩错误反馈周期从数月缩短至数天
### 关键实验
在腾讯4个生产用户画像任务上，压缩后模型效果持平甚至优于未压缩单任务模型，单GPU吞吐提升37%~350%，合计节省190张GPU；全量部署10个月后整体GMV提升1.37%。公共基准上，同等压缩比下MRQA域外EM最高提升17.7%，RecBench上4B模型效果超过同系列8B baseline1.9个百分点。

**最值得记住的一句话：长序列压缩的系统经济性核心是表示的可缓存性，而非单纯的压缩比。**
