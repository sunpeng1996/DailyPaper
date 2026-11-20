---
title: 'Evolve Where It Matters: Coverage-Guided Self-Evolution of Agent Skills'
title_zh: 基于覆盖度引导的Agent技能自进化框架SKILLPLUMBER
authors:
- Boyin Tan
- Jiadong Zhang
- Xiaosong Ma
- Chun Jason Xue
- Xiaowei Huang
- Youcheng Sun
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- University of Liverpool
arxiv_id: '2611.25429'
url: https://arxiv.org/abs/2611.25429
pdf_url: https://arxiv.org/pdf/2611.25429
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent 技能自进化优化
tags:
- Agent_Skill_Evolution
- Coverage_Guidance
- Self_Evolution
- RCA
- Skill_Library
one_liner: 利用指令级覆盖度信号定位技能缺陷，实现Agent技能无人工干预的自进化优化
practical_value: '- 电商导购/客服/流程类Agent可复用指令级覆盖度机制，精准区分失败是技能指令错误还是Agent未遵循，避免误改正确的Prompt/技能规则

  - 可借鉴持久化RCA Agent+跨任务策略库的设计，将业务场景下的多次失败根因沉淀为通用修复策略，降低重复诊断成本

  - 生成式推荐的Prompt/技能迭代场景可套用这套覆盖度引导的修复流程，相比全链路反馈修复方法减少约20%的修复次数，无需人工标注即可实现技能自动优化'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent技能自进化方法仅能基于整条运行轨迹的成败做全链路诊断，无法区分失败根因是技能指令本身错误，还是Agent未正确遵循指令，常出现误改正确指令、重复优化Agent不会执行的内容等问题，修复效率和效果均不佳。
### 方法关键点
- 引入指令级覆盖度信号，对每条技能指令打三类标签：follow（Agent遵循执行）、not-follow（Agent未遵循）、not covered（对应场景未出现），精准定位缺陷位置
- 设计持久化根因分析（RCA）Agent，单任务内跨轮次保留诊断上下文，基于标签针对性优化：not-follow指令优化表述降低执行门槛，follow但失败的指令修正错误内容，not covered指令判断是否冗余
- 新增跨任务策略维护模块，将不同任务的修复经验沉淀为共享策略库，供后续任务直接复用
### 关键结果
在SkillsBench、SkillLearnBench、SWE-Skills-Bench三个基准测试集，搭配GPT-5.5、Claude Opus 4.8、DeepSeek-V4-Pro三个执行器验证：
- 任务解决率达64.7%~70.5%，较初始技能提升25.6~30.4个百分点，较最优基线提升8.7~14.0个百分点
- 移除覆盖度信号后，GPT-5.5在SkillsBench上的失败修复率下降20.8%
- 单失败平均修复轮次仅3.4次，远低于基线CoEvoSkills的11.6次

> 最值得记住的一句话：知道Agent如何使用每条指令，对技能优化的价值就像代码覆盖度对程序调试的价值一样基础
