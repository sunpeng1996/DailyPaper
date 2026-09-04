---
title: 'UniCon: A Unified Context-Centric Modeling Paradigm for CTR Prediction'
title_zh: UniCon：面向CTR预测的统一上下文中心建模范式
authors:
- Jiajun Cui
- Zhengqi Xu
- Fan Zhang
- Zhangteng
- Gu Tang
- Honghong Zhu
- Mengxi Wu
- Yulin Liang
- Xingxing Wang
affiliations:
- Meituan
arxiv_id: '2609.03290'
url: https://arxiv.org/abs/2609.03290
pdf_url: https://arxiv.org/pdf/2609.03290
published: '2026-09-03'
collected: '2026-09-04'
category: RecSys
direction: CTR预测 · 统一上下文建模
tags:
- CTR-Prediction
- Context-Modeling
- Unified-Modeling
- Ranking
- Industrial-RecSys
one_liner: 将历史曝光与当前候选统一为上下文单元，分层建模局部交互与跨上下文演化，大幅提升CTR预测效果
practical_value: '- 建模层面：可将同一次曝光的item、上下文、用户特征打包为上下文单元，替代传统的序列+非序列特征拆分范式，显式建模同屏item的竞争/互补关系

  - 工程优化：可复用无padding变长attention、上下文粒度TopK压缩、PyTorch AOT编译的部署方案，在提升长序列建模效果的同时控制推理延时

  - 多任务设计：可在CTR主任务外增加曝光预测、位置预测辅助任务，优化候选侧的上下文表征，无需依赖实际曝光的结构信息

  - 候选分块：当候选集过大时，可采用300左右的分块大小进行hash分片，在效果损失可接受的前提下大幅降低计算开销'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有工业CTR统一建模按传统特征工程习惯拆分为序列（历史行为）与非序列（当前候选、请求特征）两类信号，人为割裂用户决策的上下文结构：用户每次行为都发生在同一次曝光的上下文内，历史曝光和当前请求仅区别于结果是否被观测，拆分后会混淆同屏item共现与跨屏时序接近的关系，尤其在电商货架、瀑布流等强上下文场景下限制模型效果与缩放效率。
### 方法关键点
- 上下文单元定义：将单次曝光的item集合、对应意图/环境信号、用户特征统一打包为上下文单元，历史单元标注点击反馈，当前候选单元用可学习占位符填充反馈位，实现历史与候选结构对齐
- 分层交互架构：交替堆叠intra-context层（单元内attention，建模同屏item的竞争、互补等局部关系）与inter-context层（跨单元attention，建模用户兴趣、环境的时序演化），共享参数处理历史与候选单元
- 效率优化：上下文粒度的目标感知压缩（按与当前候选的相似度保留TopK历史单元）、无padding变长attention、PyTorch AOT编译部署，大幅降低推理开销
- 多任务监督：新增曝光预测、位置预测辅助任务，在无最终曝光结构的前提下优化候选上下文单元表征
### 关键结果
基于美团搜索广告1年生产数据验证，离线AUC比生产基线高0.0139，比最强基线RankMixer+DSIN+CIM高0.0036；在线A/B测试实现3.09% RPM、2.07% CTR、2.95% 收入的显著提升，上下文压缩后推理GFLOPs仅为未压缩版本的24.6%，满足生产延时SLA。

最值得记住的一句话：将上下文单元作为CTR建模的基础抽象，而非仅将上下文作为补充特征，能同时提升模型效果与缩放效率，适配强上下文的工业推荐场景。
