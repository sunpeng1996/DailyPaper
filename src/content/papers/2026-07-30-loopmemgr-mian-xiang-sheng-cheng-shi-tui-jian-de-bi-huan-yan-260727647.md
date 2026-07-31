---
title: 'LoopMemGR: From Behavior Logs to Evolving Memory for Generative Recommendation'
title_zh: LoopMemGR：面向生成式推荐的闭环经验记忆框架
authors:
- Hui Qian
- Changfa Wu
- Chang Liu
- Binbin Cao
- Jian Wu
- Yuliang Yan
- Han Zhu
- Bo Zheng
affiliations:
- Alibaba Group
arxiv_id: '2607.27647'
url: https://arxiv.org/abs/2607.27647
pdf_url: https://arxiv.org/pdf/2607.27647
published: '2026-07-30'
collected: '2026-07-31'
category: GenRec
direction: 生成式推荐 · 闭环记忆增强
tags:
- Generative Recommendation
- Semantic ID
- Memory Augmentation
- Sequential Recommendation
- Closed-loop System
one_liner: 为生成式推荐构建闭环经验记忆，通过三视角压缩在固定token预算下复用跨请求决策信号
practical_value: '- 业务侧可新增「推荐经验日志」，除用户行为外额外存储系统过往曝光+反馈轨迹，复用负向反馈、历史探索信号，避免重复推送无效内容

  - 可直接复用三视角经验压缩trick：近邻去重保留短期上下文，频次统计长期品类偏好，全局共享Query补冷启动经验，压缩到10~20个固定token几乎不增加LLM推理负担

  - 给全局记忆Query增加多样性正则损失，避免不同token学到冗余特征，可大幅提升有限记忆槽位的信息密度

  - 工程上可与现有基于Semantic ID的生成式推荐底座（如RankGR、FORGE）无缝对接，无需修改核心生成逻辑，仅需在Prompt中额外插入少量经验token即可落地'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐普遍采用「历史行为当上下文」的范式，每次请求都重新从用户行为序列重构偏好，但系统过往的推荐决策、曝光后的用户反馈（尤其是未点击负信号、已探索品类信息）全部被丢弃，形成不对称记忆：仅记录用户行为，不保留系统侧决策轨迹，易出现重复推送、无效探索等问题；若直接将全量历史曝光塞进上下文则会导致输入长度爆炸，推理成本陡增。

### 方法关键点
1. 新增与用户行为日志并行的**推荐经验日志**，存储每轮推荐-反馈轨迹，形成「读经验→生成推荐→写回经验」的闭环，严格保证因果顺序，避免未来信息泄露
2. 三视角记忆阅读器（TVMR）分层提取经验：近邻视角去重保留最新M个推荐，捕捉短期交互动态；频次视角统计高频推送品类，总结长期探索规律；全局视角采用跨用户共享的可学习Query，补充冷启动场景下的稀疏经验
3. 以近期经验为锚点的门控融合，将3M个候选token压缩到固定M个（实验中M=16），同时给全局Query增加多样性正则，避免特征冗余

### 关键结果
在阿里淘宝工业数据集（2100万用户、2.7亿商品、260亿交互）上对比传统推荐、生成式推荐共11个基线：
- 相比最强基线RankGR，K≥100时Click HR提升11.57~15.30个百分点，PV HR提升11.87~17.65个百分点
- 仅用16个经验token即可保留全量原始经验log 74%以上的性能增益

生成式推荐不是单次孤立预测任务，将系统侧的临时决策转化为可复用的持久化经验，可在极低额外成本下带来显著效果提升
