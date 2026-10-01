---
title: When LLM-Inferred User Context Adds Value in Production Streaming Recommendation
title_zh: 生产环境流式推荐中LLM推断用户上下文的适用场景研究
authors:
- Milad Sabouri
- Neeraj Sharma
- Sardar Hamidian
- Shaghayegh Agah
affiliations:
- DePaul University
- Comcast Technology AI
arxiv_id: '2609.38999'
url: https://arxiv.org/abs/2609.38999
pdf_url: https://arxiv.org/pdf/2609.38999
published: '2026-09-30'
collected: '2026-10-01'
category: RecSys
direction: 推荐系统 · LLM用户画像场景适配
tags:
- LLM User Profiling
- Context-Aware Recommendation
- Streaming Recommendation
- User Modeling
- Production RecSys
one_liner: 揭示LLM生成用户画像仅对探索型用户更优，多数习惯型用户适配传统聚合画像
practical_value: '- 可直接复用分群策略：通过历史长度、历史内容多样性提前判定用户为习惯型/探索型，习惯型用户用传统embedding聚合画像，探索型用户用LLM生成画像，平衡效果与成本

  - 若业务追求推荐列表多样性且可接受热门度上升、长尾覆盖下降，可对特定用户群启用LLM生成画像，无需全量替换基线

  - LLM生成用户画像时，仅对探索型用户用全历史生成摘要即可，无需拆分长短时序做注意力融合，可降低推理成本；对习惯型用户若用LLM画像，可拆分长短时序减少效果损失

  - 上线前注意LLM画像的流行度偏倚问题：会导致整体长尾内容曝光下降80%左右，需配套偏置矫正策略避免生态问题'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统上下文推荐依赖人工预定义特征，近年基于LLM将用户行为历史生成自然语言摘要作为用户画像的方案逐渐兴起，但现有研究仅观测到域级效果差异，未明确用户粒度的适用条件，也缺乏生产级大catalog场景下的验证。
### 方法关键点
- 搭建2×2对照实验框架，交叉两大维度：表示类型（传统item embedding聚合/LLM生成摘要+SBERT编码）、上下文范围（全历史/长短时序拆分注意力融合），共4种用户画像策略，其余模型组件完全固定，仅对比画像差异的影响。
- 自定义用户分群规则：测试集交互全不在训练历史的划为探索型用户，其余为习惯型用户，分群评估效果。
- 同时覆盖精度类（Recall/NDCG/HitRate）与非精度类（多样性/覆盖率/新颖度）指标，全面评估不同画像的业务影响。
### 关键实验结果
- 实验数据来自生产流媒体平台，覆盖1万用户、24万+item的全量catalog，基线为全历史item embedding均值聚合的Centroid方案。
- 精度结果：占比82%的习惯型用户上，LLM全历史摘要方案Recall@10比基线低30.7%；占比18%的探索型用户上，该方案Recall@10比基线高18.7%、NDCG@10高31.5%。
- 非精度结果：LLM画像使单用户推荐列表多样性提升4%左右，但全量用户的catalog覆盖率下降约80%，新颖度下降18-22%，存在显著的热门内容吸引效应。
### 核心结论
不存在通用最优的用户画像方案，可根据用户消费模式自适应选择画像策略，多数场景下默认使用传统聚合画像更稳妥
