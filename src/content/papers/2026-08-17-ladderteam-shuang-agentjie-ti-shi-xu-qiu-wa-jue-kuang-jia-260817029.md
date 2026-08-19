---
title: 'LadderTeam: Dual-Agent Laddering Elicitation Framework'
title_zh: LadderTeam：双Agent阶梯式需求挖掘框架
authors:
- Manjushree Aithal
- Alexander Kotz
- James Mitchell
affiliations:
- University of Colorado Anschutz
arxiv_id: '2608.17029'
url: https://arxiv.org/abs/2608.17029
pdf_url: https://arxiv.org/pdf/2608.17029
published: '2026-08-17'
collected: '2026-08-19'
category: Agent
direction: Agent 协作 隐性需求深度挖掘
tags:
- Dual-Agent
- LLM
- Elicitation
- Guardrail
- Usability
one_liner: 双LLM Agent架构自动化执行阶梯式访谈，高效提取可落地的用户软件需求
practical_value: '- 做用户反馈/访谈类Agent可复用双Agent架构：前台执行任务+后台静默Judge做漂移检测、异常拦截，不打断用户会话同时保障流程合规，适配电商用户调研、客诉深度挖掘等场景

  - 需求挖掘场景可直接复用三种探测策略选型经验：ACV适合早期模糊需求提取、5-Whys适合已知问题根因定位、JTBD适合中期功能目标验证，可直接套用到用户体验调研、产品需求收集流程

  - 评估多轮对话Agent时可复用控制变量法：用脚本化的固定用户应答消除用户方差，仅评估Agent的提问/引导质量，大幅降低评估成本

  - 多轮会话的状态机设计可借鉴：加DecayingMemoryBuffer控制历史长度，加程序层面的State Gate做终止、循环、停滞判断，比纯LLM判断更稳定高效'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
传统阶梯式访谈是挖掘用户隐性需求、提取可落地反馈的有效手段，但完全依赖人力成本高、规模化难，且对访谈者的引导能力要求高，容易出现话题漂移、挖掘深度不足的问题，现有单Agent自动化方案缺乏流程校验机制，准确率不稳定。

### 方法关键点
- 双LLM Agent架构：前台Interviewer Agent负责执行访谈，后台Judge Agent静默评估每轮问答质量，支持阴影/主动/跳过三种工作模式，主动模式下可干预下一轮提问，两个Agent的模型可互换（云侧GPT-5.5/Claude Sonnet 4.6互换，端侧Gemma4/Qwen3.6互换）避免评估偏差
- 内置三种标准化探测策略：ACV拆解属性-后果-价值提取落地需求、5-Whys追问根因、JTBD拆解场景-目标-结果-阻碍，各配独立状态机控制流程
- 多层防护机制：访谈前先通过MCQ锚定核心问题避免漂移，每轮对话走固定5步流程（提取-状态校验-Judge评估-生成问题-接收应答），配置Drift Guard检测话题漂移、Abort Path强制终止循环/停滞会话，用DecayingMemoryBuffer（λ=0.85，最多20轮）管理会话历史

### 关键结果
基于脚本化的两类极端用户（被动回避型/寡言型）应答做控制变量评估，共216轮访谈，覆盖4个模型、3种探测策略、3类UI场景：整体链路收敛率99.1%，和真值可落地应答匹配率81%（被动回避型86.1%，寡言型75.9%），全量实验零话题漂移，ACV策略表现最优，匹配率可达94.4%。

**最值得记住的一句话**：多轮引导类Agent的链路收敛率不等于效果，仅用收敛率做指标会遗漏「提前终止、挖掘深度不足」的核心问题，必须结合真值匹配率、偏转率、重复率等多维度评估
