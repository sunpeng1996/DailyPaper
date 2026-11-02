---
title: 'BrowseFlow: Sparse Event Flow Matching for Generative User Simulation'
title_zh: BrowseFlow：面向生成式用户模拟的稀疏事件流匹配方法
authors:
- Yitian Pang
- Jiayi Zhang
- Zhenjia Ma
- Xiaowei Yue
- Dagui Chen
- Jian Xu
affiliations:
- 清华大学
- 阿里巴巴淘宝天猫集团
arxiv_id: '2610.41374'
url: https://arxiv.org/abs/2610.41374
pdf_url: https://arxiv.org/pdf/2610.41374
published: '2026-10-30'
collected: '2026-11-02'
category: RecSys
direction: 生成式用户模拟 · 流匹配
tags:
- User Simulation
- Flow Matching
- Sparse Event Modeling
- Recommender Systems
- Generative Model
one_liner: 提出基于条件离散流匹配的生成式用户模拟方法，开源淘宝浏览基准，解决稀疏事件与随机响应痛点
practical_value: '- 做用户模拟时可采用「浏览范围+稀疏关键事件」的拆分表示，无需逐帧生成滚动等高频动作，既减少计算量，又能缓解关键事件样本稀疏带来的训练不平衡问题

  - 评估生成式用户行为时，可引入Energy Score（ES）和关键事件计数的Wasserstein距离，代替传统单点匹配指标，更准确衡量生成分布与真实分布的一致性

  - 离散流匹配的插入式生成范式可迁移到其他稀疏交互序列生成任务（如点击序列、交易序列生成），无需严格左到右自回归，生成灵活度更高

  - 开源TaobaoBrowse基准可直接用于用户模拟器的预训练或效果评估，减少业务侧细粒度行为数据集的构建成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
用户模拟是电商推荐系统迭代、强化学习训练、反事实效果评估的核心基础，现有方案存在两个核心痛点：一是用户浏览行为具有天然随机性，同一用户面对相同推荐feed可能产生完全不同的轨迹，传统单点匹配指标仅能验证单条轨迹的匹配度，无法评估生成分布的合理性；二是点击、点赞等关键反馈事件占比极低（仅1.52%~5.96%），逐帧生成滚动、滑动等高频动作的范式会让关键事件的监督信号被淹没，模型无法有效学习交互规律。
### 方法关键点
- 稀疏响应表示：将用户浏览行为拆分为「浏览范围D」+「有序关键事件序列E」，浏览范围直接压缩所有滚动动作，将生成重点放在稀疏关键事件上，避免冗余计算
- 两阶段生成：先基于用户特征、历史交互、feed内容预测浏览范围的概率分布，采样得到D后，用条件离散Flow Matching在D范围内生成关键事件的位置和类型，通过随机保留事件的方式构造训练路径，学习插入动力学
- 分布级评估：引入Energy Score（ES）同时衡量生成响应的保真度和多样性，用关键事件计数的W1距离衡量分布对齐度
- 开源TaobaoBrowse基准，包含淘宝真实推荐上下文和细粒度浏览轨迹
### 关键实验
在TaobaoBrowse、KuaiRand-Like、AdSERP三个数据集上对比KuaiSim、UserSim、DBN等6个主流基线：TaobaoBrowse数据集上ES降低33%，Count W1降低73%，SeqHit@1提升20%；AdSERP数据集上Count W1降低74%，SeqHit@1提升60%。
### 核心结论
忠实用户模拟的核心原则是：建模真正有价值的关键事件，同时捕捉用户浏览行为的所有可能性。
