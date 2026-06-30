---
title: Self-Evolving World Models for LLM Agent Planning
title_zh: 面向LLM智能体规划的自进化世界模型
authors:
- Xuan Zhang
- Wenxuan Zhang
- See-Kiong Ng
- Yang Deng
affiliations:
- National University of Singapore
- Singapore University of Technology and Design
- Singapore Management University
arxiv_id: '2606.30639'
url: https://arxiv.org/abs/2606.30639
pdf_url: https://arxiv.org/pdf/2606.30639
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: LLM Agent · 自进化世界模型规划
tags:
- World Model
- LLM Agent
- Planning
- Self-Evolution
- Memory
one_liner: 提出无需更新参数的自进化世界模型框架，提升LLM智能体规划性能
practical_value: '- 线上部署在动态环境的LLM Agent（如电商导购Agent、搜索Agent），可采用非参数内存演进替代在线参数更新，避免灾难性遗忘，大幅降低计算适配成本

  - 双内存架构可直接复用：情景内存存储真实交互转移做检索增强，语义内存从预测错误中提取可解释的启发式规则，两者互补适配动态环境变化

  - 本文验证了「不可靠的前瞻预测比没有前瞻伤害更大」的结论，任何带预判的推荐/Agent系统都需要增加置信度过滤环节，避免错误信号误导决策'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent的世界模型要么冻结参数，在动态部署环境的分布偏移下预测不准；要么需要在线梯度更新参数，计算成本高、易引发灾难性遗忘；同时已有验证表明不可靠的前瞻预测反而会降低下游规划决策性能，因此需要低成本的在线自进化方案。

### 方法关键点
- 核心设计：保持下游Agent和世界模型参数完全冻结，仅通过非参数化外部记忆演进推理上下文，无需训练；
- 双记忆模块：① Episodic Memory存储已执行的动作-状态真实转移，基于动作token的Jaccard相似度检索相似历史，加入预测上下文；② Semantic Memory将预测与观测的不匹配转换为文本启发式规则，维护规则置信度，仅保留正置信度规则；
- Selective Foresight：基于预测输出的平均token概率计算置信度，仅把超过阈值的预测传给Agent，过滤低质量前瞻。

### 关键结果
在ALFWorld、ScienceWorld两个基准测试，对比Zero-Shot、RAWM-ϕ、ITP-I三个基线：① 预测准确率：Gemma-4-31B backbone下，ALFWorld精确匹配率达到56.41%，较次优基线提升22个百分点以上；② 规划成功率：Gemma-4-26B-A4B下，ALFWorld ReflAct成功率从26.12%提升至27.61%，ScienceWorld ReAct从44.44%提升至52.22%；③ 自进化收益随交互次数累积持续提升。

最值得记住的结论：参数冻结、内存驱动的自进化，是动态环境下世界模型低成本适配的有效方案
