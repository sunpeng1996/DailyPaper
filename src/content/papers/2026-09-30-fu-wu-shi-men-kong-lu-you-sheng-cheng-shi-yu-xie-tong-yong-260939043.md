---
title: 'Routing Between Generative and Collaborative User Profiles: A Serving-Time
  Gate for Controllable Novelty'
title_zh: 服务时门控路由生成式与协同用户画像实现推荐新颖性可控
authors:
- Milad Sabouri
- Neeraj Sharma
- Sardar Hamidian
- Shaghayegh Agah
affiliations:
- DePaul University
- Comcast Technology AI
arxiv_id: '2609.39043'
url: https://arxiv.org/abs/2609.39043
pdf_url: https://arxiv.org/pdf/2609.39043
published: '2026-09-30'
collected: '2026-10-01'
category: RecSys
direction: 生成式推荐 · 模型路由优化
tags:
- LLM4Rec
- User Profiling
- Routing Gate
- Recommendation Novelty
- Controllable RecSys
one_liner: 通过服务时轻量路由门控选择推荐模型，在可控NDCG损失下显著提升推荐新颖性
practical_value: '- 可复用「默认协同模型+小流量触发LLM生成式推荐」的架构，不用全量上线生成式推荐，平衡效果与LLM推理成本

  - 路由门特征可直接复用：用户历史长度、消费内容流行度分布、两类模型的用户表征norm，都是服务时易获取的特征，训练用GBDT即可，工程成本极低

  - 可复用路由阈值可调设计，业务侧可根据场景灵活调整NDCG损失预算，匹配不同时期的新颖性需求（比如大促新品期可放宽预算提升新品曝光）

  - 结论可复用：无需盲目迷信LLM生成式用户画像，非生成式语义质心画像在选择性路由下也能拿到相当的新颖性收益，成本更低'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
协同序列推荐依赖用户历史交互，易倾向热门内容，新颖性不足；全量上线基于LLM生成用户画像的推荐会带来明显的NDCG损失，还会增加LLM推理与画像更新成本，无法灵活平衡相关性与新颖性的业务需求。
### 方法关键点
- 预设两类推荐模型：默认采用协同序列推荐，候选为基于用户语义画像的推荐，包含LLM生成的Narrative、TemporalNarrative，及非生成式Centroid语义质心画像三类
- 服务时路由门采用GBDT二分类器，输入仅为服务时可获取的特征：用户历史长度、消费内容流行度统计、两类模型的用户表征norm
- 训练标签构造：对每个用户，若路由到候选模型后Novelty提升且NDCG不下降则为正样本，否则为负
- 推理时通过调整路由阈值控制被分到候选模型的用户比例，实现新颖性-相关性的可控trade-off
### 关键实验结果
基于真实流媒体平台1万用户的行为数据测试，对比基线为随机路由、niche用户优先路由、短历史用户优先路由三类简单策略：在5%的NDCG损失预算下，学习到的门控仅路由12.5%的用户，就能带来6.5%的Novelty@10提升，比最强启发式基线高1.8个百分点；非生成式Centroid画像在路由下也能拿到和LLM生成画像相当的效果。
### 核心结论
生成式用户画像的价值不在于替代协同推荐，而在于通过选择性路由，用可控的相关性损失换取全系统的新颖性提升，更简单的非生成式语义画像也能通过路由拿到可观收益。
