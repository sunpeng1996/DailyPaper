---
title: Agentic On-Policy Distillation Implicitly Reshapes LLMs' ReAct Patterns
title_zh: 智能体On-Policy蒸馏隐式重塑大模型ReAct交互模式
authors:
- Deyang Kong
- Zhaoyi Li
- Sijian Ren
- Yuan Wei
- Ying Wei
- Defu Lian
- Shikun Zhang
- Wei Ye
affiliations:
- Peking University
- University of Science and Technology of China
- Tsinghua University
- Zhejiang University
arxiv_id: '2611.19244'
url: https://arxiv.org/abs/2611.19244
pdf_url: https://arxiv.org/pdf/2611.19244
published: '2026-11-13'
collected: '2026-11-18'
category: Agent
direction: Agent训练 · 跨域蒸馏负迁移缓解
tags:
- LLM Agent
- On-Policy Distillation
- ReAct
- Cross-domain Transfer
- Negative Transfer
one_liner: 揭示OPD对ReAct模式的跨域迁移规律，提出基于偏好差的选择性蒸馏缓解负迁移
practical_value: '- 搭建电商客服/导购Agent时，跨域OPD蒸馏需提前校验ReAct模式迁移风险：若源域不需要等待用户反馈，直接蒸馏可能导致Agent不等用户返回必要信息（如订单ID、收货地址）就调用工具，大幅升高错误率

  - 缓解跨域负迁移可复用论文的选择性蒸馏trick：用领域RL前后的teacher checkpoint计算token级log概率差∆，剔除尾部5%低∆的任务特定token，即可保留87%源域性能增益，同时将跨域负迁移掉点幅度降低70%以上

  - 多域Agent能力整合时可优先选择Code Interpreter（CI）类通用交互能力作为蒸馏源：其训练出的反馈调整、查询完整性能力可正向迁移到零售、实体交互等场景，降低24%的工具调用错误率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-Policy蒸馏（OPD）是当前LLM Agent跨域迁移能力的核心技术，但业界对其如何改变ReAct交互模式的规律缺乏认知，常出现意料之外的正负迁移，甚至出现任务准确率暴跌的灾难性负向效果，缺乏可解释的缓解方案。

### 方法关键点
- 从**推理路径、动作选择、观测获取**三个维度拆解ReAct模式的跨域变化，定位负迁移的根因是过拟合任务特定的表层交互模式
- 提出选择性OPD策略：计算同一个teacher在领域RL训练前后两个checkpoint对student生成token的log概率差∆，仅保留top 95%高∆的token做蒸馏，剔除和特定任务强绑定的低∆token
- 对比了工具调用符掩码、随机筛选、优势值筛选等多种缓解方案的效果差异

### 关键实验
数据集覆盖纯推理、Code Interpreter（CI）、ALFWorld实体交互、τ²-bench客服交互四大领域，基线为普通OPD、多教师OPD：
1. 负迁移案例：ALFWorld域OPD直接蒸馏会让τ²客服任务准确率从41.5%暴跌到6.6%，55.8%的轨迹存在未等用户返回信息就调用工具的依赖违规
2. 正迁移案例：CI域OPD可让ALFWorld准确率提升27.3%、τ²零售任务准确率提升17.2%，重复操作率从4.5%降到0.7%
3. 缓解效果：用∆筛选top95% token的方案，可让τ²准确率从普通OPD的11.5%回升到29.9%，同时保留87%的ALFWorld域性能增益

### 核心结论
Agent OPD蒸馏的迁移效果不能只看任务准确率，还需关注推理、动作、信息获取三类ReAct交互模式的变化，仅剔除5%的任务特定token就能大幅缓解跨域负迁移。
