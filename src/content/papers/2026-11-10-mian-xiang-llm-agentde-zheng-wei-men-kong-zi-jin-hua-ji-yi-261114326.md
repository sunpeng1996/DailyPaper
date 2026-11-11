---
title: When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents
title_zh: 面向LLM Agent的证伪门控自进化记忆更新框架
authors:
- Runxuan Tang
- Haoyu Gao
- Yuyan Ding
- Junyi Yao
- Zihao Zheng
- Zecheng Sheng
- Liwei Hou
affiliations:
- Nanyang Technological University
- Georgia Institute of Technology
- University of Washington
- Washington University in St. Louis
- National University of Singapore
arxiv_id: '2611.14326'
url: https://arxiv.org/abs/2611.14326
pdf_url: https://arxiv.org/pdf/2611.14326
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: LLM Agent 记忆更新与自进化优化
tags:
- LLM Agent
- Self-Evolution
- Long-Term Memory
- Falsification Test
- Verifier-Grounded
one_liner: 提出证伪门控自进化框架，通过结构化假设测试降低LLM Agent记忆更新风险
practical_value: '- 电商智能客服、履约助手等工具型Agent的记忆更新可复用FGSE的结构化假设范式，将每次会话总结的经验拆解为<适用场景、行为规则、预期效果、校验规则>四元组，避免直接存入记忆导致的错误泛化

  - Agent记忆写入前的三级测试逻辑（迁移增益测试、边界证伪测试、历史能力回归测试）可直接复用到推荐系统的策略迭代，新召回/排序策略上线前先在近线做三类校验，降低上线风险

  - 对于verifier丰富的场景（如电商履约Agent、广告投放Agent）可直接借鉴阈值门控逻辑，设置最低增益、最高证伪率、最高回归损伤阈值，自动完成策略/记忆的准入、修订、驳回，减少人工审核成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent自进化机制直接将单次任务的经验写入长期记忆，易出现局部有效经验过度泛化、冲突已有能力、积累无效记忆等问题，缺乏统一的记忆写入判断标准，无法平衡长期进化的收益与风险。

### 方法关键点
- 结构化假设表示：将每次经验生成的候选记忆拆解为四元组<适用前置条件、行为变换规则、预期效果、专属校验器>，仅在前置条件匹配时激活该记忆
- 三级临时测试机制：候选记忆仅临时生效，分别在目标迁移集（验证增益）、证伪集（验证边界鲁棒性）、回归集（验证不损伤历史能力）上测试，计算三类指标
- 门控决策逻辑：设置增益、证伪率、回归损伤三类阈值，符合要求的记忆直接提交，增益达标但边界有缺陷的记忆通过缩小适用范围修订后重测，不达标则直接驳回

### 关键结果
在WebArena、AppWorld、τ-Retail/τ-Airline等多类Agent基准上对比记忆、反思类基线：WebArena成功率达39.8%，AppWorld平均完成率78.8%，τ-Retail/τ-Airline Pass1分别达0.724/0.487；同时将证伪失败率降至5.0%，回归损伤降至1.3%，有害记忆写入率降至3.6%。

### 核心结论
LLM Agent的长期自进化不能仅依赖单次任务的成功信号，必须对每一次记忆更新做可验证的增益、鲁棒性、回归性测试，才能平衡进化效率与可靠性。
