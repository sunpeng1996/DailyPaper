---
title: 'Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent
  Harnesses'
title_zh: AHE-Beta：以需求为中心的Agent Harness自动化演化框架
authors:
- Jiahang Lin
- Jiahao Chen
- Yiding Wang
- Shichun Liu
- Chengjun Pan
- Shihan Dou
- Honglin Guo
- Yuyang Hu
- Changhao Jiang
- Zhenhua Han
affiliations:
- Fudan University
- Peking University
- Renmin University of China
- Shanghai Qiji Zhifeng Co., Ltd
arxiv_id: '2611.24924'
url: https://arxiv.org/abs/2611.24924
pdf_url: https://arxiv.org/pdf/2611.24924
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent 自动化Harness演化优化
tags:
- Agent Harness
- Multi-Agent Collaboration
- User Simulation
- Requirement Alignment
- Automated Evolution
one_liner: 提出需求驱动的多角色Agent协作Harness演化框架，兼顾效果、效率与用户体验
practical_value: '- 电商客服/导购类直面用户的Agent迭代可抛弃纯benchmark打分选版本的逻辑，改用需求对齐的迭代方案，避免过拟合测试集，提升真实场景迁移性

  - 多角色分工的Agent开发协作流程（Triage/Architect/PM/Developer）可直接复用在企业内部Agent系统的自动化迭代上，替代人工梳理需求改代码的流程，降低人力成本

  - 用户模拟器的设计思路可迁移到电商推荐/广告系统的用户满意度评估，基于多维度用户persona模拟真实交互，挖掘隐性需求，无需全量上线AB测即可提前发现体验问题

  - 跨模型迁移特性验证了Harness层优化与基座解耦的价值，业务Agent优化可优先在Harness层迭代，无需频繁微调基座，适配不同基座的成本更低'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent Harness演化方法纯靠benchmark打分选择优化方向，忽略用户隐性需求与交互体验，容易生成任务专属补丁，陷入测试集局部最优，优化效果难以迁移到真实场景与其他基座模型。

### 方法关键点
- 三阶段闭环演化逻辑：用户驱动评估→团队化修改→需求驱动准入，全程不依赖benchmark得分选择变更
- 用户驱动评估：基于50个真实开发者persona构建用户模拟器，通过多轮交互输出issue和用户评分，同时挖掘显性与隐性需求
- 多角色团队化修改：Triage过滤无效issue，Architect合并同根因需求，PM挖掘跨会话隐性需求输出PRD，Developer基于需求实现通用化修复而非临时补丁
- 需求驱动准入：只有可解决已验证需求、通过代码评审的PR才会合入，所有变更都可追溯到真实交互证据

### 关键实验
在Harbor-index 38个跨领域held-out任务上测试，对比Base Harness、Claude Code、Meta-Harness、AHE等基线：
- pass@1从21.9%提升至33.3%，同时token消耗降低40.8%
- 盲测中31/48真实用户偏好AHE-Beta，5个体验维度评分全高于基线
- 无额外演化直接迁移到GLM-5.3、DeepSeek-V4.1-Flash，pass@1分别提升15.8、5.3个百分点

### 核心结论
纯靠benchmark得分驱动的Agent优化会遗漏大量用户隐性需求，基于真实交互的需求对齐才能得到效果、效率、迁移性三者兼顾的优化结果
