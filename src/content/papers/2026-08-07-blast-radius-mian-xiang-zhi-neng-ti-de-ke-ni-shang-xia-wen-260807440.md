---
title: Blast Radius
title_zh: Blast Radius：面向智能体的可逆上下文管理层降低token开销
authors:
- MY Pitsane
- Hope Mogale
affiliations:
- Mankind Research Labs
- North-West University, RSA
- University of Pretoria, RSA
arxiv_id: '2608.07440'
url: https://arxiv.org/abs/2608.07440
pdf_url: https://arxiv.org/pdf/2608.07440
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent 可逆上下文优化 降token成本
tags:
- Agent
- Context Management
- Token Efficiency
- Reversible Eviction
- Memory Optimization
one_liner: 提出可逆上下文管理框架，配合重复内容识别降低token消耗17-26%无精度损失
practical_value: '- 电商导购Agent、推荐系统用户会话记忆可复用可逆驱逐机制：将已完成任务的上下文归档到本地存储，仅保留精简检索骨架，token开销降低17-26%且可无损恢复，避免截断/摘要丢失关键信息

  - 重复出现的上下文（如电商Agent重复调用的库存、订单查询结果）可复用RDM策略：仅保留每个重复类别的最新实例，旧实例直接归档，实测无召回需求，可额外贡献近40%的回收token量

  - 可借鉴「先预测下一轮上下文需求再做驱逐预算」的思路：在LLM排序、生成式推荐场景中，提前预判query需要的上下文长度，动态清理无效历史，在不影响效果的前提下降低推理成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Agent多轮会话每轮都需要重传全量历史上下文，大量已完成子任务的无效内容长期占用token，导致推理成本随轮次线性上涨；现有滑动窗口截断、摘要压缩方案均为不可逆操作，存在丢失关键信息的不可控风险，亟需低风险的上下文压缩方案。

### 方法关键点
- 双层Blast Radius预测架构：上下文通道预测下一轮prompt的上下文增量，计算所需驱逐预算；代码通道基于依赖图预测修改的影响范围，输出提交压力信号。
- 可逆NECROPHORESIS驱逐机制：将判定为死亡的上下文原封不动归档到本地midden存储，上下文窗口仅保留带检索key的精简骨架，需要时可O(1)无损恢复，错误驱逐代价仅为固定召回开销κ。
- RDM重复内容识别：通过归一化映射匹配重复工具调用结果，仅保留每个类别的最新实例，基于拉普拉斯继承法则计算旧实例的复活概率，低于阈值直接归档。

### 关键结果
在7款OpenAI模型（gpt-4.1至gpt-5.6系列）上测试，对比全量携带、滑动窗口截断、MemGPT式摘要3个基线，搭载RDM的Blast Radius降低token消耗17-26%，任务成功率保持100%，上下文溢出率为所有方案最低；累计归档450份上下文，其中378份为RDM，无一次召回需求，完全符合安全阈值要求。

> 最值得记住的一句话：可逆遗忘把删除上下文的不可控风险变成了固定代价的有限下注，只要死亡上下文的复活概率低于阈值，携带它的成本永远高于驱逐的成本
