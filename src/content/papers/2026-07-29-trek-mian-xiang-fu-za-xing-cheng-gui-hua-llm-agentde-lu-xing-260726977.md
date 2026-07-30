---
title: 'TREK: A Travel Reasoning and Evaluation Kit for LLM Agents in Complex Trip
  Planning'
title_zh: TREK：面向复杂行程规划LLM Agent的旅行推理与评测套件
authors:
- Jinhu Qi
- Wentao Zhang
- Siu Man Ng
- Feiyang Xu
- Yanyu Chen
- Yaoman Li
- Irwin King
affiliations:
- The Chinese University of Hong Kong
- Macao Polytechnic University
arxiv_id: '2607.26977'
url: https://arxiv.org/abs/2607.26977
pdf_url: https://arxiv.org/pdf/2607.26977
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: LLM Agent复杂行程规划评测基准
tags:
- LLM Agent
- Benchmark
- Travel Planning
- Tool Use
- Deterministic Evaluation
one_liner: 推出带确定性无LLM评测器、人类验证金标的复杂行程规划LLM Agent基准TREK
practical_value: '- 垂直领域（如电商定制套餐、旅游行程推荐）Agent评测可复用「纯规则无LLM评测器+人类验证金标+分类不可行任务」的范式，彻底规避LLM评测的偏置、不可复现问题

  - 多约束生成任务评估可采用「任务完美率」（所有约束全部满足才算通过）替代加权平均，更贴近真实用户体验——只要有一个硬约束不满足（如超预算、无货、超时），方案对用户就无价值

  - 隐式需求匹配可借鉴「用户persona→明确属性集合→精确集合交判断」的方法，完全不用embedding或LLM判断，适合电商用户偏好匹配、人群定向等高准确率要求的场景

  - 生产环境Agent基座选型不要盲目追捧推理能力强的模型，在严格工具调用/格式输出场景下，推理模型可能因格式漂移、冗余调用导致性能反而低于普通指令模型，且token成本更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent行程规划类基准多采用LLM评审或单一维度打分，无法验证输出方案的端到端可执行性，结果不可复现也不可审计，且缺乏对多约束联合满足、隐式用户需求、不可行任务识别能力的统一评测，无法有效衡量落地级Agent的真实能力。

### 方法关键点
- 构建包含212530条航班、酒店、景点、租车记录的内部一致合成知识库，覆盖375个城市、13类用户画像，通过生产级RESTful API沙箱供Agent调用，支持严格参数校验、语义搜索、结构化错误返回
- 设计800个多约束任务，其中533个可行、267个可证明不可行（按原因分为实体缺失、无可用路线、预算不足三类），每个任务附带人类验证的金标方案，金标在评测器下得分1.0，确保评测天花板可证明可达
- 采用完全规则化无LLM评测器，从约束满足、真实性、可执行性、不可行任务处理4大类共9个维度打分，核心指标为任务完美率（所有适用维度都得1才算通过）

### 关键结果
评测15款LLM Agent，最强的GPT-5.6在可行任务上的完美率仅46.2%，15款模型中位数仅6.6%，最低为0.0%；隐式需求满足是所有模型的通用瓶颈，GPT-5.6的满足率也仅46.3%；推理增强模型在严格工具调用场景下性能反而低于普通指令模型，且准确率和token消耗无正相关性。

### 核心结论
多约束复杂Agent任务的性能瓶颈早已不是显式指令遵循，而是用户未明确表述的隐式需求的精准满足。
