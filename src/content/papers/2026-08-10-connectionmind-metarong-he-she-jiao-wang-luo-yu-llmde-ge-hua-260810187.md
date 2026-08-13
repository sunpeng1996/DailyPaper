---
title: 'ConnectionMind: Leveraging Social Networks and Large Language Models for Personalized
  Recommendation at Meta'
title_zh: ConnectionMind：Meta融合社交网络与LLM的个性化推荐框架
authors:
- Haoyu Han
- Yuming Liu
- Lei Huang
- Lizhu Zhang
- Jiliang Tang
- Xiangjun Fan
affiliations:
- Meta Platforms, Inc.
- Michigan State University
arxiv_id: '2608.10187'
url: https://arxiv.org/abs/2608.10187
pdf_url: https://arxiv.org/pdf/2608.10187
published: '2026-08-10'
collected: '2026-08-12'
category: RecSys
direction: 社交推荐 · LLM图推理落地
tags:
- Social Recommendation
- LLM4Rec
- Graph Reasoning
- Reinforcement Learning
- Production Deployment
one_liner: 将社交推荐转化为异构图路径探索任务，采用SFT+RL两阶段训练LLM策略，落地Meta生产获正向收益
practical_value: '- 社交/内容/电商推荐场景可复用多关系异构图建模思路，将用户关系、关注关系、社群、商品/内容关联等信号纳入统一图结构，为LLM推理提供结构化先验

  - 大模型落地低延迟推荐场景可采用分层混合推理架构：仅给高ARPU/高活用户调用LLM做精准推理，其余流量用LLM推理轨迹蒸馏的轻量GNN/MLP承接，平衡效果与算力成本

  - LLM执行结构化决策任务（如图探索、路径规划）可采用SFT暖启动+RL调优的训练范式，奖励可拆解为格式合规、最终效果、中间步骤合理性三个维度，降低训练收敛难度'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统社交推荐要么无差别聚合所有社交信号引入大量噪声，要么将社交上下文压缩为隐向量，缺乏可解释性与信号选择能力，无法匹配社交场景下用户消费决策高度依赖高价值社交关系（好友、关注创作者、社群）的特性；而纯LLM推荐忽略结构化社交信号，效果甚至弱于传统社交推荐模型，亟需兼顾社交信号选择性利用、可解释性与规模化落地能力的推荐框架。

### 方法关键点
- 构建异质社交-内容交互图，包含用户、创作者、内容三类节点，覆盖好友、关注、群组归属、内容发布、协同消费、语义相似等多类型带权时序边
- 将推荐任务转化为从用户节点到候选内容节点的路径探索问题，LLM作为探索策略，根据当前路径、节点语义、邻接边信息输出下一步扩展动作，同时返回带证据路径的推荐结果
- 两阶段训练：第一阶段用历史用户交互的最短路径数据做SFT，让LLM掌握合法图遍历逻辑与用户偏好规律；第二阶段用GRPO做RL优化，奖励由格式合法性、推荐F1值、中间路径有效性三个加权维度组成
- 生产端采用分层推理架构：Top 5~10%高活用户直接调用LLM推理，其余用户用LLM生成的有效路径蒸馏出的轻量GNN承接，满足毫秒级延迟要求

### 关键结果
离线公开数据集测试中，8B参数版本ConnectionMind在Foursquare数据集Recall@10达0.0966，相对无社交信息的LLM推荐基线BIGRec提升174%；Meta生产环境离线Recall@10相对原生GNN基线提升88%，相对70B Llama纯排序基线提升35%；线上千万级用户A/B测试，视频观看时长提升0.43%，内容曝光提升0.33%，视频会话数提升0.22%。

> 在成熟大规模推荐系统中，将LLM的语义推理能力与结构化业务先验（如社交图）结合，再通过分层推理架构落地，可在可控成本下获得可衡量的业务收益。
