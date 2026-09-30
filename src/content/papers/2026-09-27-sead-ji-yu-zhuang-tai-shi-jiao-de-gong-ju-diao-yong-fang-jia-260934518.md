---
title: 'SEAD: A State-Based Perspective on Attack and Defense in Tool-Using Agents'
title_zh: SEAD：基于状态视角的工具调用Agent攻防框架
authors:
- Xinjie Shen
- Junran Wang
- Rongzhe Wei
- Pan Li
affiliations:
- Georgia Institute of Technology
arxiv_id: '2609.34518'
url: https://arxiv.org/abs/2609.34518
pdf_url: https://arxiv.org/pdf/2609.34518
published: '2026-09-27'
collected: '2026-09-30'
category: Agent
direction: Agent 工具调用安全攻防优化
tags:
- Tool-using Agent
- Agent Safety
- Adversarial Attack
- Runtime Defense
- State Control
one_liner: 提出基于状态控制的工具调用Agent攻防框架，配套自适应攻击、状态感知防御及可验证数据集
practical_value: '- 电商/广告场景的工具调用Agent（如智能运营、客服Agent）可复用SAGE前置防御逻辑，执行工具调用前用只读查询校验环境状态，避免恶意诱导的敏感数据泄露、越权操作

  - 做Agent安全评测可复用DART的自适应攻击思路，用工具执行反馈引导攻击路径搜索，比固定步骤渗透测试覆盖率高18%以上，更易发现隐性安全漏洞

  - SAGE仅用文件系统/终端域数据训练即可泛化到数据库、Web场景，业务落地时可大幅减少跨场景的安全规则标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前工具调用Agent广泛应用于数据库操作、Web交互、运营任务执行等场景，多步操作的状态累积效应会导致局部看似合理的动作组合后产生危害，传统攻防方法仅依赖可见交互历史判断风险，无法对齐实际环境状态，存在攻击成功率高、防御误拦截率高的问题。

### 方法关键点
- 将工具Agent攻防统一建模为部分观测的状态控制问题，明确攻击者、目标Agent、防御者三方的状态观测边界与决策逻辑
- DART自适应攻击：将有害目标拆解为局部合理步骤，通过树搜索结合工具执行反馈动态调整攻击路径，用LLM打分和可执行验证共同评估路径价值
- SAGE状态感知防御：执行工具动作前可发起只读状态查询补全环境信息，再决策放行/拦截，拦截后重规划的动作会再次进入校验流程
- 构建可环境验证的攻防数据集，覆盖四大域，配套可控初始状态、可重放环境和可执行校验逻辑

### 关键结果
- DART攻击成功率较最优基线提升18.8~35.9个百分点，覆盖4款主流大模型
- 离线防御：SAGE保留95.79%的良性轨迹，同时在危害发生边界拦截92.73%的有害路径
- 在线攻防：SAGE将DART的可执行攻击成功率从48.0%降至4.0%，且仅用两类域数据训练即可泛化到未见过的数据库、Web场景

最值得记住的结论：工具调用Agent的安全是多步执行后累积状态的安全，攻防都需要对齐环境实际状态而非仅依赖可见交互历史。
