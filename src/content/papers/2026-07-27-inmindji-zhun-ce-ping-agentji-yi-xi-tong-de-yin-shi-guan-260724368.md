---
title: 'Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent
  Memory'
title_zh: InMind基准：测评Agent记忆系统的隐式关联盲点
authors:
- Ruizhe Li
- Mingxuan Du
- Benfeng Xu
- Zhendong Mao
affiliations:
- University of Science and Technology of China
- Metastone Technology
arxiv_id: '2607.24368'
url: https://arxiv.org/abs/2607.24368
pdf_url: https://arxiv.org/pdf/2607.24368
published: '2026-07-27'
collected: '2026-07-28'
category: Agent
direction: Agent 长时记忆性能测评
tags:
- Agent Memory
- Benchmark
- RAG
- Implicit Association
- Long-term Memory
one_liner: 发布125任务专家验证的InMind基准，定位Agent记忆系统的隐式关联盲区
practical_value: '- 电商导购、用户服务类Agent建设中，不能仅将用户禁忌、强偏好（如食品过敏、商品使用禁忌）存入向量库，需将高风险特征纳入always-in-state常驻上下文，避免检索漏召导致的安全/合规问题，如用户坚果过敏时搜马卡龙要主动提示风险

  - 现有RAG/记忆系统的测评不能只考核直接召回率，需补充隐式关联场景测试case，如用户提过家中有3岁以下幼儿，搜小颗粒积木时要主动提示choking hazard，这类场景是业务风险高发区

  - 设计用户画像特征的路由规则时，不能仅靠频次、热度筛选常驻上下文的特征，需结合领域规则给高风险、高影响特征加权，优先常驻，平衡上下文成本和业务风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
主流检索式Agent长时记忆默认待召回记忆与查询语义相似，但大量真实关联依赖外部知识（如坚果过敏与马卡龙的关联来自杏仁粉原料的常识），现有系统常出现「能直接召回记忆、但不会在相关场景主动应用」的隐式关联盲点。现有基准无法区分「记忆未存储、模型缺关联知识、检索漏召」三类故障，无法定位根因。

### 方法关键点
- InMind基准包含125个专家验证任务，覆盖10个生活领域，113个任务的关联逻辑来自FDA、OSHA等可公开溯源的权威来源
- 每个任务配套三类对照：直接naive查询测记忆存储有效性、上下文注入目标记忆测模型关联知识储备、目标召回测检索是否将记忆送入上下文，明确区分三类故障
- 任务经过严格相似度过滤，保证目标记忆与间接查询的语义相似度和干扰样本无差异，避免检索系统靠语义匹配蒙混过关

### 关键实验结果
测试6类主流记忆系统（向量、知识图谱、Agentic检索等），结果显示：目标记忆直接注入上下文时，GPT-5-mini回答准确率达84.0%；检索式系统的直接召回率最高达100%，但隐式关联场景的应用准确率最高仅14.4%；将高优先级记忆常驻上下文的always-in-state方案准确率达68.8%，大幅缩小性能差距。

### 最值得记住的一句话
Query驱动的检索把需要世界知识的关联判断交给了仅懂语义匹配的检索器，相当于先做relevance决策再调用能理解知识的LLM，结构上存在无法仅靠更强嵌入、更复杂检索逻辑弥补的先天缺陷。
