---
title: 'RuleMem: Active Rule Memory for Long-Term Conversational Agents'
title_zh: 面向长期对话Agent的主动规则记忆框架RuleMem
authors:
- Xingyuan Zeng
- Zuohan Wu
- Quanming Yao
- Yue Wang
- Wei Liu
- Libin Zheng
- Jiuke Wang
- Jian Yin
affiliations:
- Sun Yat-sen University
- The Hong Kong University of Science and Technology (Guangzhou)
- Shenzhen Institute of Computing Sciences
- The Hong Kong Polytechnic University
- Tsinghua University
arxiv_id: '2609.03915'
url: https://arxiv.org/abs/2609.03915
pdf_url: https://arxiv.org/pdf/2609.03915
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: Agent长时记忆 · 规则归纳推理
tags:
- LLM Agent
- Long-term Memory
- Rule Induction
- Conversational QA
- RAG
one_liner: 从对话历史归纳可复用自然语言规则，主动引导证据检索与逻辑推理，提升长期对话QA效果
practical_value: '- 电商客服/用户运营对话Agent场景可复用规则归纳逻辑，从历史对话提炼可复用应答/用户偏好规则，替代纯向量相似检索，解决语义鸿沟导致的召回失效问题，例如用户咨询「收货时间能否调整」时，可触发「用户有特殊收货需求→可走售后申请调整」规则召回对应证据，不需要依赖关键词完全匹配

  - RPC规则校验机制可直接复用在规则类知识库自动构建场景，通过LLM内部困惑度+外部事实一致性双维度打分过滤低质量/幻觉规则，适合电商售后规则、优惠活动规则的自动校验入库，降低人工审核成本

  - 长周期用户兴趣建模场景可借鉴事实到规则的抽象思路，从用户历史行为（点击、下单、咨询）提炼高阶关联规则（如「用户购买露营帐篷→大概率需要露营灯/天幕」），用于跨语义的召回拓展，提升推荐召回的覆盖率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有长对话Agent的记忆机制均为被动存储模式，纯事实记忆依赖表面相似性检索，存在语义鸿沟导致的召回失败问题；结构化事实记忆仅在实例层面构建关联，推理时缺乏明确逻辑骨架，易出现逻辑断链、幻觉等推理失效问题，无法支撑长上下文下的多跳复杂推理需求。

### 方法关键点
- 双层记忆架构：分事实库（存储对话提取的<主体,关系,客体,时间>时序四元组）和规则库（存储自然语言Horn clause格式的抽象规则，用类型占位符替换具体实体）
- 规则生成链路：从事实库构建时序知识图谱，采样多跳推理路径，聚类相似路径后用LLM提炼通用规则，覆盖因果、关联等逻辑模式
- RPC规则校验：结合LLM内部先验一致性（规则前件到后件的困惑度下降幅度）和外部事实一致性（补充事实证据后后件困惑度的进一步下降幅度）计算置信度，过滤过拟合、幻觉规则
- 推理链路：查询先匹配规则库的规则后件激活相关规则，再用规则前件作为检索cue召回对应事实，经变量绑定校验后，基于「规则+事实」结构化prompt生成答案

### 关键结果
在LoCoMo长对话QA基准上对比14个主流基线（含Mem0、GraphRAG、Zep等），平均准确率达78.05%，超出基线平均27.47个点，相对提升54.3%；引导召回将平均召回率从0.56提升至0.79（+41.1%），显式推理将推理失败率平均降低12.0%。

### 核心结论
Agent的记忆不应该是被动的检索对象，而要主动提炼抽象规则，同时作为检索引导和推理骨架，从根本上解决长上下文下的召回与推理失效问题。
