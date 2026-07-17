---
title: 'SAGA: Schema-Aware Grounding for Agentic Text-to-SPARQL Generation'
title_zh: SAGA：面向Agent化Text-to-SPARQL生成的Schema感知接地框架
authors:
- Yiming Zhang
- Koji Tsuda
affiliations:
- The University of Tokyo
- National Institute for Materials Science
- RIKEN Center for Advanced Intelligence Project
arxiv_id: '2607.14494'
url: https://arxiv.org/abs/2607.14494
pdf_url: https://arxiv.org/pdf/2607.14494
published: '2026-07-16'
collected: '2026-07-17'
category: Agent
direction: Agent KBQA · Schema感知接地优化
tags:
- KBQA
- Text-to-SPARQL
- Schema-Aware
- Agent Grounding
- Training-free
one_liner: 训练免的Schema感知接地框架，解决Agent化Text-to-SPARQL类型盲接地问题，9个基准F1全最优
practical_value: '- 电商/广告知识库问答场景（商品属性问答、商家合规查询等）可直接复用「Schema预索引+构造时属性过滤」思路，提前过滤类型不兼容的候选属性，大幅减少LLM无效选择，降低空结果率

  - Agent工具返回结果时可仿照SAGA为实体/属性增加类型标注，无需额外LLM调用剪枝，缩小决策空间的同时降低推理成本

  - 多轮Agent交互可复用「持久化类型状态+答案类型反向传播」设计，全局复用多轮得到的类型信息，避免重复走错误分支，提升交互效率

  - 不完备知识库场景可借鉴软Schema归纳思路，从历史三元组统计高频主客体类型作为软约束，同样能实现类型过滤效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent化Text-to-SPARQL方案多通过词法相关性或实例观测剪枝候选属性，未系统考虑实体类型、属性定义域/值域、预期答案类型等Schema信息，存在**类型盲接地**问题：易生成大量语义不兼容的三元组模式，导致查询空结果率高、多轮交互频繁走错误分支；现有Schema用法要么放在Prompt中靠LLM自行理解，要么事后校验，均未从根源缩小接地搜索空间。

### 方法关键点
- 训练免框架，仅修改Agent与知识库的接地接口，无需微调LLM或访问解码器，兼容闭源/开源大模型
- 预构建轻量Schema索引，提前存储每个属性的定义域/值域，无官方声明的属性从知识库采样统计高频主客体类型作为软约束
- 维护跨轮次持久化双向类型状态：正向积累观测到的实体/变量类型，反向从问题推理预期答案类型作为软引导
- 构造时过滤：每次属性检索直接过滤与当前实体类型存在明确定义域冲突的候选，剩余候选携带类型标注返回给LLM；无类型信息的实体 fallback 到原LLM剪枝逻辑，避免误过滤

### 关键实验
在Wikidata、Freebase共9个KBQA基准上测评，对比SPINACH、Interactive-KBQA等8个强基线：SAGA在全部9个基准上取得F1最优，8个基准取得Exact Match最优；相比各基准最强基线，Wikidata上F1提升2.4~20.3个百分点，Freebase上提升0.2~11.2个百分点，所有Wikidata基准空结果率均显著下降，WWQ-test上从75.5%降至27.0%。

最值得记住的一句话：知识库Schema应该在Agent接地的动作空间构造阶段就作为约束生效，而不是仅作为Prompt上下文或事后校验规则。
