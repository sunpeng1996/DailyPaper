---
title: 'From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research'
title_zh: 《从任务委派到协同：高效多智能体深度研究训练框架LEAD-RL》
authors:
- Yuyang Wu
- Yang Liu
- Zequn Xie
- Junjie Wang
- Dan Yang
- Zehao Tan
- Ding-Chu Zhang
- Junming Yang
- Yue Shen
- Jian Wang
affiliations:
- Ant Group
- University of Electronic Science and Technology of China
- Zhejiang University
- Southeast University
arxiv_id: '2611.17041'
url: https://arxiv.org/abs/2611.17041
pdf_url: https://arxiv.org/pdf/2611.17041
published: '2026-11-12'
collected: '2026-11-13'
category: MultiAgent
direction: 多智能体协作 · 信用分配优化
tags:
- MultiAgent
- ReinforcementLearning
- CreditAssignment
- DeepResearch
- AgentDelegation
one_liner: 提出带贡献感知信用分配的多智能体联合RL训练框架LEAD-RL，优化深度研究的准确率与效率
practical_value: '- 电商复杂导购/选品多Agent场景可复用贡献感知信用分配逻辑：子Agent执行候选挖掘、属性校验、合规审核等子任务时，可通过规则/轻量评审模型打分过滤团队奖励，避免有效子任务被全局失败惩罚、无效子任务被全局成功奖励，提升子任务执行准确率

  - 大流量搜索推荐Agent可参考动态委派+并行子任务架构：将用户复杂查询拆分为独立子任务（如价格查询、库存校验、权益计算）并行执行，仅返回结构化结果到主Agent上下文，降低主Agent上下文长度压力，缩短关键路径响应时延

  - 多Agent RL训练可复用纯结果导向的奖励设计：不需要额外添加步数、token消耗等过程类奖励项，仅通过信用分配门控即可同时优化效果与效率，大幅降低奖励工程的调参成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多智能体深度研究系统通过任务委派并行执行子任务，既可以降低主Agent上下文长度压力，还能通过并行缩短执行耗时，但联合训练时全局团队奖励无差别分配给所有子Agent，会出现有效子报告因全局失败被惩罚、无效子报告因全局成功被奖励的错配问题，反而拖累系统准确率与执行效率。
### 方法关键点
- 提出LEAD-RL联合训练框架，主Agent与子Agent共享参数，主Agent负责任务分解、委派与结果整合，子Agent在独立上下文执行子任务，仅返回结构化报告，配合本地/全局双重校验过滤无效结果
- 设计贡献感知信用分配机制：训练阶段用独立评审器将子Agent报告分为helpful/neutral/harmful三类，通过门控过滤团队奖励：helpful报告仅继承正奖励，harmful报告仅继承负奖励，neutral保留原奖励；全程仅用最终答案正确性作为唯一全局奖励，无任何过程类奖励项
- 定义critical-path cost、理想加速比两个效率指标，衡量并行多智能体系统的真实执行效率，避免无意义的并行任务膨胀
### 关键实验
在BrowseComp、GAIA等5个深度研究基准、2个模型家族上验证，对比共享团队信用的联合RL baseline，BrowseComp数据集上准确率提升2.49个百分点，关键路径成本降低24.5%；验证集上准确率提升6.78个百分点的同时关键路径成本基本持平；124B参数的LEAD-RL效果超过参数量2倍以上的DeepSeek V4 Flash，接近1.6T参数的DeepSeek V4 Pro。
**最值得记住的一句话**：多智能体协同优化的核心不是增加智能体数量，而是通过精准的信用分配让每个子智能体的贡献得到公平反馈，无需额外过程奖励即可同时提升效果与效率。
