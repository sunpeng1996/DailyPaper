---
title: Toward a Compositional Knowledge Architecture for a Shared Organizational Cortex
title_zh: 面向共享组织皮层的组合式知识架构
authors:
- Andrew Miracle
- Phyl Georgiou
- Christine Okoth
- Ese Monday
affiliations:
- Robin Inc.
- Nosen
arxiv_id: '2611.05753'
url: https://arxiv.org/abs/2611.05753
pdf_url: https://arxiv.org/pdf/2611.05753
published: '2026-11-03'
collected: '2026-11-05'
category: Agent
direction: Agent 共享知识记忆架构设计
tags:
- Agent Memory
- Knowledge Architecture
- Truth Maintenance
- RAG
- Information Retrieval
one_liner: 提出信号-领域-论断-维度四层架构，实现可动态维护的组织级共享判断能力
practical_value: '- 可直接复用四层知识分层逻辑：将电商业务的用户行为、商品信息等原始数据映射为Signals，按行业、品类等划分Domains，沉淀选品、投放、推荐理由等业务判断为Claims，定义性价比、上新度等可量化维度为Dimensions，避免重复推导业务规则

  - 真值维护机制适配动态业务场景：商品上下架、优惠变更、政策调整时，自动遍历所有依赖该知识的Claims（如推荐理由、投放策略），批量更新有效状态，避免过期知识错误出现在推荐结果或Agent回复中

  - 维度感知检索可优化生成式推荐排序：在传统混合检索得分基础上，叠加业务维度匹配分+低可信度内容惩罚，实测可提升nDCG@10约0.08，显著提升推荐结果的业务合理性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG、知识图谱、Agent记忆系统仅存储原始数据和事实，不保留多源信息聚合推导的判断逻辑及前提假设，当原始证据变更时，无法自动溯源更新已生成的判断，跨场景复用需要重新推导，还存在结论传播时丢失证据和不确定性的问题，组织级知识复用效率极低，错误率高。

### 方法关键点
- 四层组合架构设计：Signals层存储从原始数据（对话、文档、报表等）提取的原子可验证命题，保留来源；Domains层定义语义边界，负责检索路由和范围过滤；Claims层存储多源Signals/已有Claims推导的判断结论，保留推导路径、前提假设、来源、状态；Dimensions层定义可解释的有序度量轴，给Claims标注可比较的位置分。
- 真值维护机制：通过依赖网络动态标记Claim的5种状态（提议/接受/争议/撤回/取代），证据变更时按拓扑序遍历更新所有依赖的Claim状态，冲突仅在冲突双方标记不向下游传播，避免误判扩散。
- 维度感知检索框架：基础混合检索得分叠加维度匹配分+低可信度（提议/争议状态）Claim惩罚，提升检索结果的相关性和可靠性。

### 关键实验结果
在3个工作空间共272条 held-out 查询上测试：仅加入维度项即可提升nDCG@10 0.028（p=0.002）；全架构检索对比纯Signals检索nDCG@10提升0.081（p<0.001）；对比GraphRAG风格的图增强Signals检索，nDCG@10提升0.053（p<0.001）。

### 核心结论
知识复用的核心不是存储原始证据，而是存储推导得到的判断、其依赖的所有前提、动态的有效性状态，以及可解释的量化度量维度。
