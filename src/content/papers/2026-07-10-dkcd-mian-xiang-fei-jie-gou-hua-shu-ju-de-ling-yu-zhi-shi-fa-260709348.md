---
title: 'DKCD: Domain Knowledge-Enhanced Causal Discovery from Unstructured Data'
title_zh: DKCD：面向非结构化数据的领域知识增强因果发现
authors:
- Xin Li
- Jin Li
- Shoujin Wang
- Kun Yu
- Fang Chen
affiliations:
- University of Technology Sydney
arxiv_id: '2607.09348'
url: https://arxiv.org/abs/2607.09348
pdf_url: https://arxiv.org/pdf/2607.09348
published: '2026-07-10'
collected: '2026-07-13'
category: Reasoning
direction: 领域知识增强 · 非结构化数据因果发现
tags:
- Causal Discovery
- Domain Knowledge
- LLM
- Unstructured Data
- Knowledge Retrieval
one_liner: 提出领域知识增强的DKCD框架，解决非结构化数据因果发现中隐因子识别不全、标注不可靠问题
practical_value: '- 电商推荐场景可复用「显式特征关联领域知识挖掘隐因子」的思路，补充用户消费意愿、商品潜在属性等未被显式记录的因果因子，提升归因准确率

  - Agent决策链路中可引入知识引导的因果推理模块，基于领域知识库校准决策因子标注，减少错误传导导致的策略偏差

  - 广告归因场景可直接复用DKCD的三段式架构，从用户评论、客服对话等非结构化数据中构建更精准的转化因果图'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有基于通用LLM的非结构化数据因果发现方法存在两大核心缺陷：一是缺乏领域专属知识，导致对因果推理至关重要的隐含因子识别覆盖率低；二是缺少领域 grounded 推理逻辑，因子标注误差大，会传导至下游因果图构建环节，在高专业度场景表现不佳
### 方法关键点
DKCD采用三段式联动架构：1）知识挖掘：基于观测到的显式因果因子，检索匹配的领域知识库内容，为后续推理提供支撑；2）知识引导因果推理：依托召回的领域知识挖掘隐含因果因子，同时生成因果线索校准因子标注，分别解决上述两个痛点；3）因果结构发现：基于更完整的因子集合与高精度标注输出最终因果图
### 关键结果
在两个领域专属测试数据集上，DKCD在因果因子识别、因果图构建两项核心任务上均实现显著性能提升
