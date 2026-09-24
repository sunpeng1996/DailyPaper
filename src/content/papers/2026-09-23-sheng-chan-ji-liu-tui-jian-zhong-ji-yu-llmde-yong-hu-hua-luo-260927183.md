---
title: When LLM-Based User Profiling Adds Value in Production Streaming Recommendation
title_zh: 生产级流推荐中基于LLM的用户画像落地价值分析
authors:
- Milad Sabouri
- Neeraj Sharma
- Sardar Hamidian
- Shaghayegh Agah
affiliations:
- DePaul University
- Comcast Technology AI
arxiv_id: '2609.27183'
url: https://arxiv.org/abs/2609.27183
pdf_url: https://arxiv.org/pdf/2609.27183
published: '2026-09-23'
collected: '2026-09-24'
category: RecSys
direction: 推荐系统 · LLM用户画像价值评估
tags:
- LLM
- User Profiling
- Content-based Recommendation
- Production Evaluation
- Streaming Recommendation
one_liner: 通过2×2对照实验明确LLM用户画像仅对探索型用户有精度增益，多数场景传统聚合方法更优
practical_value: '- 可复用用户分层策略：先将用户分为习惯型/探索型，探索型用户（历史行为少、历史内容多样性高）优先用LLM用户画像，其余用户用低成本的SBERT
  embedding均值聚合方案，降本提效

  - LLM画像副作用预警：LLM生成的用户画像会让推荐结果向热门内容集中，全局覆盖率下降80%左右，若业务看重长尾分发需搭配消偏策略

  - 时序拆分参数参考：短期行为窗口比例建议设置在15%-25%区间，超过30%会导致时序融合的精度明显下降

  - 落地范式参考：不需要全量用户上LLM画像，做路由层根据用户特征分流，仅对15%-20%的探索型用户调用LLM，大幅控制算力成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM用户画像虽在公开电商/推荐数据集上表现优于传统聚合方法，但生产环境算力成本高、用户行为异质性强，其落地价值尚未被系统验证，需要明确何时值得投入额外成本引入LLM用户画像。

### 方法关键点
- 2×2对照实验设计，两个变量维度：画像类型（SBERT embedding聚合 / LLM生成自然语言偏好摘要后SBERT编码）、时序处理（全历史聚合 / 长短时序拆分后注意力融合），共4种方案，其余组件（item编码器、MLP打分头、训练目标）完全对齐，唯一变量为用户画像生成逻辑
- 用户分层：将用户分为探索型（测试集交互物品均未出现在训练历史中）、习惯型两类，分群评估效果
- 评估维度覆盖精度（Recall@K、NDCG@K、HitRate@K）和非精度指标（单列表多样性、全局覆盖率、内容新颖度）

### 关键实验
- 数据集：Comcast生产流媒体平台1万用户、24万条内容的真实交互数据
- 对比基准：全历史SBERT embedding均值聚合方案
- 核心结果：①习惯型用户：LLM画像Recall@10下降32%左右，全面劣于聚合方案；②探索型用户：LLM画像Recall@10提升19%、NDCG@10提升31.5%，显著优于聚合方案；③LLM画像非精度表现：单用户推荐列表多样性提升4%，但全局覆盖率下降80%、新颖度下降18%-20%，推荐向头部热门内容集中

### 核心结论
LLM用户画像不是全场景银弹，仅在用户偏好需要跨物品泛化的探索场景下值得投入，其余场景传统聚合方案是更优的鲁棒性默认选择
