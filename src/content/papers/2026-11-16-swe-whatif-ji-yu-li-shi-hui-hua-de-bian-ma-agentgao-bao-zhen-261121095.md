---
title: 'SWE-WhatIf: Simulating Real Users of Coding Agents from Recorded Session'
title_zh: SWE-WhatIf：基于历史会话的编码Agent高保真用户仿真框架
authors:
- Tae Soo Kim
- Tongshuang Wu
- Juho Kim
affiliations:
- KAIST
- SkillBench
- Carnegie Mellon University
arxiv_id: '2611.21095'
url: https://arxiv.org/abs/2611.21095
pdf_url: https://arxiv.org/pdf/2611.21095
published: '2026-11-16'
collected: '2026-11-18'
category: Agent
direction: Agent评测 · 用户仿真
tags:
- UserSimulator
- AgentEvaluation
- IntentModel
- CodingAgent
- LLM-as-Judge
one_liner: 从用户与编码Agent的历史交互会话提取意图模型，生成适配新Agent轨迹的高保真用户模拟器
practical_value: '- 做Agent（导购/客服/编码Agent）评测时，可复用从历史交互会话构建仿真用户的思路，大幅降低真实用户招募成本，提升评测效率

  - 意图建模方法可直接迁移：将用户历史交互拆解为「意图+满足标准+触发条件」的结构化模型，比固定话术回放的适配性高30%+，支持适配新Agent的未知交互轨迹

  - 负担调整的效果指标可复用：除任务完成率外，加入交互轮数权重做加权得分，更贴合真实场景下的用户体验和运营成本，适合搜索推荐、广告Agent的效果评估'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有编码Agent评测方案存在三类缺陷：静态基准任务无用户交互，无法反映真实多轮引导场景；直接回放历史会话的方法无法适配新Agent偏离原始轨迹的行为；通用用户模拟器无法对齐特定用户的决策逻辑和交互风格，导致评测结果和真实用户反馈偏差大。
### 方法关键点
- 构建锚定原始会话的意图模型：每个用户意图包含预期目标、满足标准、触发/丢弃条件，所有规则全部来自原始用户的交互行为，不生成无依据的额外需求
- 逐轮仿真流程：每轮先通过LLM-as-Judge评估Agent当前行为对已触发意图的满足度，更新意图状态，再匹配用户原始交互风格生成对应回复
- 负担调整成功指标：任务完成率乘以（原始会话交互轮数+1）/（仿真会话交互轮数+1），同时覆盖任务效果和用户交互成本
### 关键实验
基于89个SWE-Chat、SWE-Together公开真实交互会话测试，对比4个基线模拟器：单轮回复与真实用户相似度达53.2（排名第一）；适配新Agent轨迹时，主动规避用户反感动作的Agent胜率达66.3%（p=0.001，显著高于基线）；基于仿真结果的LLM排名与真实用户排名的Kendall τb达0.8，远高于其他评测方法。
### 核心结论
用户仿真的核心不是复刻用户话术，而是还原用户的意图判断逻辑和交互风格，才能让评测结果充分对齐真实用户体验。
