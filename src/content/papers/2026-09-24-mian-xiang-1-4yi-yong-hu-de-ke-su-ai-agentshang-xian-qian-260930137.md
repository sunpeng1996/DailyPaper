---
title: 'Screen Before You Serve: Simulation for Production Customer Experience AI
  Agents at 140M Scale'
title_zh: 面向1.4亿用户的客诉AI Agent上线前仿真校验框架
authors:
- Edesio Alcoba
- Kevin Rossell
- Aman Gupta
- Shao Tang
- Jiwoo Hong
- Pabel Carrillo-Mendoza
- Wanderson Conceição Ferreira
- Alvaro Tedeschi
- Zayd Simjee
- Shreya Rajpal
affiliations:
- Nubank
- Guardrails AI
arxiv_id: '2609.30137'
url: https://arxiv.org/abs/2609.30137
pdf_url: https://arxiv.org/pdf/2609.30137
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: Agent 上线前仿真校验优化
tags:
- LLM Agent
- User Simulation
- Customer Experience
- LLM Evaluation
- A-B Testing
one_liner: 提出假设驱动的Agent上线前仿真校验流程，在亿级客诉场景获显著业务增益
practical_value: '- 电商/金融的智能客服CX Agent上线前可直接复用该仿真流程：基于persona生成模拟用户，仅在工具边界做mock无需调用生产后端，提前拦截bad
  case，避免上线后损伤用户体验

  - 仿真落地无需追求100%还原生产行为，只要能方向正确区分候选版本优劣即可，大幅降低仿真方案的落地门槛

  - 可通过仿真低成本穷举模型、prompt、推理参数组合：论文中跑了29种模型配置共16000轮对话，快速选出最优开源模型替换闭源，实现降本提效

  - 仿真落地前需先做校准：通过小范围上线验证仿真评估分数和线上SSR、NPS等核心业务指标的相关性，避免仿真结果误导迭代方向'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
CX Agent上线前的验证存在两大痛点：人工编写测试用例覆盖度低，无法覆盖真实用户的边缘场景；直接上线A/B测试风险高，糟糕的交互会降低用户信任、拉低NPS，且迭代周期长。传统用户仿真方案存在保真度不足、和线上结果相关性弱的问题，难以支撑生产决策。
### 方法关键点
- 采用SnowGlobe仿真框架：输入Agent描述、工具定义，可选历史对话数据，自动生成覆盖不同用例、用户persona的多轮对话轨迹，工具调用层做mock，无需调用生产后端，保证工具返回和上下文一致。
- 假设驱动的筛选流程：先在仿真环境跑 incumbent 和 candidate 版本的对话，用LLM-as-Judge评估预设的核心指标，只有满足阈值的候选才进入线上A/B，避免无效上线。
- 四层保真度校验：通过对话长度统计、embedding相似度、评估分数相关性、人工盲测四个维度校准仿真和生产的一致性，确保仿真结果方向可靠。
### 关键结果
基于Nubank亿级用户的卡片配送、卡片管理客诉Agent场景验证：
1. 仿真筛选后的Card Management Agent上线后，tNPS提升36.69点，SSR提升4.9个百分点；
2. 用仿真跑了29种开源模型配置共16000轮对话，选出的Qwen3.5-122B上线后SSR再提升8.82个百分点，p95 latency降低25%，tNPS无显著变化；
3. 迭代效率提升4.8倍，单版本迭代周期从21.2天缩短到4.4天。
> 最值得记住的一句话：仿真的核心价值是支撑迭代决策，而非完美复刻生产，只要方向正确即可带来巨大业务收益。
