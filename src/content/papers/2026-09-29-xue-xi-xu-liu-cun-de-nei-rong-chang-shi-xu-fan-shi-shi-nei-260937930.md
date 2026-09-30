---
title: 'Learning What to Remember: Long-horizon Counterfactual Memory Optimization'
title_zh: 学习需留存的内容：长时序反事实内存优化方法
authors:
- Jiaming Tang
- Mingyan Liu
- Armin Sarabi
affiliations:
- University of Michigan
arxiv_id: '2609.37930'
url: https://arxiv.org/abs/2609.37930
pdf_url: https://arxiv.org/pdf/2609.37930
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agent 长时序记忆优化
tags:
- Memory Optimization
- Reinforcement Learning
- Credit Assignment
- Long-context LLM
- Policy Optimization
one_liner: 提出记忆增益策略优化MGPO，通过反事实信用分配实现高效持久化内存学习
practical_value: '- 可复用MGPO反事实信用分配逻辑优化电商导购Agent长记忆：每次更新记忆时对比新旧版本对当前+未来用户咨询、推荐转化的增益，淘汰冗余记忆降低KV
  cache占用，减少长会话推理成本

  - 记忆-读者解耦架构可迁移到生成式推荐系统：独立训练记忆写入模块沉淀用户长期兴趣，无需重训即可适配不同下游召回/排序模型，降低跨业务场景迁移成本

  - 长时序边际增益评估方法可优化用户兴趣建模：区分每一次用户行为对未来推荐效果的增量贡献，精准决策兴趣标签的留存/淘汰，提升长周期推荐准确度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM持久化内存是长交互Agent、长序列理解任务的核心能力，但现有内存学习存在两个核心痛点：一是记忆更新的价值可能间隔多步才显现，信用分配存在严重延迟；二是记忆的效用大多来自之前已存储的内容，无法区分单次更新的真实增量贡献，最终导致内存冗余度高、有效信息留存率低，长距离推理性能差。
### 方法关键点
- 解耦记忆写入与下游读取：记忆写入器是唯一可训练模块，下游读取器完全固定，确保记忆效用的差异完全来自记忆内容本身，消除其他变量干扰
- 反事实记忆增益（MG）计算：对每次记忆更新，同时用更新前后的两个记忆版本在当前及未来所有下游任务上评估效用差，隔离单次更新的增量贡献
- PPO适配优化：将长时序累加MG作为reward，加入位置相关EMA归一化消除不同位置回报的尺度差异，采用token级裁剪目标优化写入策略
### 关键实验结果
在SciREX科学文档信息抽取、AIPAN-10K隐私政策抽取两个长序列数据集上测试，对比Direct Readout、LightRAG、Mem0、MemAgent等基线：
1. 相对初始未优化策略，MGPO平均内存长度降低78.7%，同时实体聚类F1提升30.9%，二元关系抽取F1提升60.6%
2. 跨域迁移到AIPAN-10K无需任何重训，相对最优基线实体聚类F1高0.4个点，二元关系F1高1.6个点
3. 同一个训练好的8B写入器可适配Qwen3、Llama3.1、Phi-4等6款不同结构、不同参数量的读取器，均稳定提升任务性能

学习该记住什么的核心不是保留所有有用信息，而是精准识别每次记忆更新带来的长期增量价值
