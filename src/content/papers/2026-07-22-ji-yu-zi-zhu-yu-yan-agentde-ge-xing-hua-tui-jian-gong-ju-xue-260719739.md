---
title: Personalized Recommendation Tool Learning via Autonomous Language Agents
title_zh: 基于自主语言Agent的个性化推荐工具学习框架
authors:
- Mingdai Yang
- Zhiwei Liu
- Weizhi Zhang
- Yibo Wang
- Hao Peng
- Philip Yu
affiliations:
- University of Illinois Chicago
- Microsoft
- Beihang University
- Hangzhou Innovation Institute of BUAA
arxiv_id: '2607.19739'
url: https://arxiv.org/abs/2607.19739
pdf_url: https://arxiv.org/pdf/2607.19739
published: '2026-07-22'
collected: '2026-07-23'
category: Agent
direction: Agent 驱动多推荐工具融合优化
tags:
- LLM Agent
- Recommender System
- Tool Learning
- Ranking Aggregation
- Personalization
one_liner: 提出PRTA框架，由LLM Agent自主融合多传统推荐工具结果，规避LLM推荐的幻觉与上下文长度限制
practical_value: '- 架构可直接复用「LLM做调度决策+传统推荐模型做全排序」的思路，无需修改LLM本身，从架构层面规避幻觉和上下文长度问题，适配现有推荐管线改造，落地成本低

  - 三层反射机制（本地工具评估、全局工具对比、排名对比）可迁移至多模型融合场景，给每个用户动态分配不同召回/排序模型权重，效果优于固定权重融合

  - 轻量化上下文重排序设计实用性强：仅对多工具聚合后的Top K结果做LLM重排，既利用LLM语义能力，又控制计算成本，适合电商二级/三级排序场景

  - 小参数本地量化LLM（如Phi-4）即可支撑Agent调度和重排任务，无需调用大模型API，隐私性好延迟低，适配离线/近线推荐场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM做推荐的方案存在两个核心痛点：一是幻觉问题易生成不存在的item，二是上下文长度限制无法支撑全库item排序，过往方案要么依赖复杂prompt调教效果不稳定，要么仅能在小候选集上验证，不符合工业界全排序真实需求。同时传统推荐模型虽擅长行为建模和全排序，但缺乏语义推理能力，无法适配用户动态个性化需求。

### 方法关键点
- PRTA架构解耦行为建模与语义推理：传统推荐模型（LightGCN、SASRec、SimpleX等）作为工具负责全库排序输出打分，LLM Agent仅负责个性化工具权重分配和Top结果重排，从架构层面规避LLM的核心缺陷
- 设计三层反射机制更新用户级工具权重向量：1）本地工具评估：LLM判断单个工具的Top K结果与用户近期行为的相关性，更新对应权重；2）全局工具对比：LLM从所有工具中选出最匹配用户需求的一个，加权更新；3）排名对比：基于历史交互item在各工具中的排名，用规则更新权重，补充LLM语义判断的偏差
- 推理阶段：先用学到的用户级工具权重加权聚合所有工具的排序结果，再对Top K结果做LLM上下文重排，输出最终推荐列表

### 关键实验
在Amazon、Yelp、Goodreads三个公开数据集上测试，对比LightGCN、SASRec、SimpleX、DiffRec等传统推荐模型，以及LLMRank、单工具+RAG重排等基线。相比最优基线，Amazon数据集R@10提升60%、N@10提升66.15%，Goodreads数据集R@10提升68.8%、N@10提升50.09%，所有数据集指标均显著领先。单用户推理延迟<0.5s（V100-32GB），可落地性强。

最值得记住的一句话：解决LLM在推荐场景的缺陷无需仅聚焦模型本身优化，通过架构设计将合适任务分配给对应模块，可低成本实现更高落地价值。
