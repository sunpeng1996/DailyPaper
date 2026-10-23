---
title: 'PAIR: Preference-Aligned Intent Retrieval for Premium People Recommendation
  at LinkedIn'
title_zh: 'PAIR: 领英高端会员人脉推荐的偏好对齐意图检索框架'
authors:
- Zhongkai Shangguan
- Yanbin Kang
- Yihan Cao
- Ruijie Jiang
- Qiannan Yin
- Chang Yue
- Zijian Zhou
- Girish Kathalagiri
- Changshuai Wei
- Zhengming Xing
affiliations:
- LinkedIn
arxiv_id: '2610.30941'
url: https://arxiv.org/abs/2610.30941
pdf_url: https://arxiv.org/pdf/2610.30941
published: '2026-10-22'
collected: '2026-10-23'
category: RecSys
direction: 推荐系统·大模型检索·用户意图建模
tags:
- Embedding-based Retrieval
- Preference Learning
- User Intent Modeling
- LLM4Rec
- Production RecSys
one_liner: 针对职业社交非对称匹配需求，提出低成本更新的偏好对齐检索框架提升高端人脉推荐效果
practical_value: '- 非对称匹配场景（电商供需匹配、招聘、B2B推荐等）可直接复用偏好对齐训练范式，用曝光日志的点击/未点击对构造对比学习样本，无需参考模型，训练成本远低于DPO类方法

  - 动态用户意图建模可复用三塔+预计算embedding融合方案，历史行为仅需O(Kd)向量运算即可更新，无需在线LLM推理，延迟无明显上涨，适配亿级用户规模

  - 多业务线延迟/存储要求不同的场景，可加入Matryoshka loss训练一套embedding，按需截断维度，减少多模型维护成本

  - 业务优化优先级上，召回层的偏好对齐优化ROI远高于加大模型规模，该方案中偏好微调贡献了90%以上的离线效果提升'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
职业社交场景的匹配本质是非对称互补的，例如求职者更倾向点击招聘方而非同背景求职者，但传统人脉推荐依赖profile相似度或社交关系，完全无法适配这种目标驱动的跨角色交互需求；同时工业级部署需解决三大约束：训练信号需对齐用户偏好而非相似度、用户动态意图更新不能每次重跑LLM、不同业务线的latency/存储要求不同无法支撑多套模型。
### 方法关键点
- 训练目标：受DPO偏好学习启发，用生产曝光日志构造偏好对，点击样本为正，同曝光未点击（硬负例）+随机采样（易负例）按1:3配比构造负例，做多负例对比学习，无需显式参考模型，训练效率高
- 三塔架构：静态profile塔与候选塔共享0.6B LLM encoder参数，预计算所有用户的profile embedding；历史塔用用户最近10次点击的预存profile embedding，通过带位置编码的无查询注意力做轻量聚合，最终用户表示为静态embedding与历史embedding的归一化加权融合
- 加入Matryoshka loss，同时在200/256/512/1024四个维度优化，推理时按需截断embedding适配不同业务的效率要求
### 关键实验
数据集为领英Premium业务的209K训练样本、11.8K测试样本；对比基线为领英生产的Holistic-171 embedding、0.6B通用embedding；离线MAR@100达0.45，较生产基线相对提升56%，较通用0.6B embedding提升134%；线上A/B测试CTR提升7.5%，Premium会员留存提升2.1%，页面加载latency仅上涨0.1%，无业务感知的性能退化。
### 核心结论
垂直业务场景下，针对业务偏好做定制化微调的收益远高于提升通用模型的参数规模。
