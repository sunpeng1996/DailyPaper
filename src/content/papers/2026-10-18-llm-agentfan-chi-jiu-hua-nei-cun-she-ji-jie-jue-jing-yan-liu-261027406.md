---
title: 'More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM
  Agents'
title_zh: LLM Agent反持久化内存设计：解决经验蒸馏的错误复现问题
authors:
- Ruhan Wang
- Kishan Panaganti
- Dongruo Zhou
affiliations:
- Indiana University
- Tencent HY
arxiv_id: '2610.27406'
url: https://arxiv.org/abs/2610.27406
pdf_url: https://arxiv.org/pdf/2610.27406
published: '2026-10-18'
collected: '2026-10-21'
category: Agent
direction: Agent 内存架构优化
tags:
- LLM Agent
- External Memory
- Self-improvement
- Error Propagation
- Contextual Bandit
one_liner: 提出反持久化Agent内存设计，阻断抽象经验错误复现，提升任务成功率同时降低LLM调用成本
practical_value: '- 做电商导购Agent、搜索场景query理解Agent时，放弃持久存储蒸馏的业务规则/经验策略的方案，改为每次从召回的历史成功/失败轨迹按需生成临时指导，可避免错误经验跨任务扩散，同时提升整体成功率

  - 可直接复用论文中的上下文老虎机模式选择逻辑，根据当前任务与历史任务的相似度、不同模式的历史效果，自动选择「直接用轨迹/蒸馏行为模式/生成全局策略/提取避坑规则」的经验处理方式，平衡效果与开销

  - 做Agent成本优化时可复用带LLM调用惩罚的奖励函数设计，将额外的经验蒸馏调用次数直接纳入奖励的扣分项，避免为了效果过度调用大模型推高推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于外部内存的LLM Agent自优化方案，普遍会将从历史轨迹蒸馏出的规则、策略等抽象知识持久存储复用，但蒸馏错误会通过「抽象→执行→再抽象」的反馈循环不断复现扩散，甚至出现内存越多效果越差的问题，单纯删除错误抽象也无法消除已被污染的轨迹带来的间接影响，急需从架构层面解决错误传播问题。

### 方法关键点
- 核心架构分离经验存储和抽象使用：仅持久存储原始交互轨迹和任务结果，不存储任何蒸馏的抽象知识，每次执行新任务时按需从检索到的轨迹生成临时指导，执行完成后直接丢弃，阻断错误的直接复用路径
- 自适应模式选择：基于上下文老虎机算法，根据历史反馈从4种模式中选最优：none（无抽象直接用轨迹）、imitation（提取可复用行为模式）、strategic（蒸馏高阶任务策略）、corrective（生成错误规避规则）
- 成本感知奖励设计：将额外的LLM合成调用次数纳入奖励计算，平衡任务效果和推理成本

### 关键实验
在ALFWorld、WebShop、ScienceWorld三个基准任务，用Llama-4-Scout、Qwen3-Coder-Next、Gemma-4-31B三个不同能力的backbone测试，对比ReAct、Reflexion等Agent基线，以及轨迹内存、抽象内存、联合内存三种方案：反持久化在9个测试场景中7个拿到最高成功率，平均成功率达59.9%，比最强基线Reflexion高7pct，同时平均LLM调用成本为所有内存方案最低。

**最值得记住的一句话**：Agent自优化的内存设计中，持久存储抽象知识带来的错误扩散风险往往远大于其复用价值，按需生成临时抽象是更可靠的选择。
