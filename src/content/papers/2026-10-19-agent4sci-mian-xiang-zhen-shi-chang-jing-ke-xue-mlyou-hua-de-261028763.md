---
title: 'Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the
  Wild?'
title_zh: AGENT4SCI：面向真实场景科学ML优化的Agent能力测试基准
authors:
- Ming Zhong
- Stacy Li
- Nicholas Carlini
- Matthew Jagielski
affiliations:
- Anthropic Fellows Program
- Anthropic
arxiv_id: '2610.28763'
url: https://arxiv.org/abs/2610.28763
pdf_url: https://arxiv.org/pdf/2610.28763
published: '2026-10-19'
collected: '2026-10-22'
category: Agent
direction: Agent能力评测 · 科学ML优化
tags:
- Agent Evaluation
- ML for Science
- Testbed
- Coding Agent
- Skill Plug-in
one_liner: 提出跨11个科学领域的AGENT4SCI测试床，验证轻量插件技能可将Agent优化效果翻倍
practical_value: '- 长周期Agent优化任务可复用三阶段隔离架构：执行/评估/审计环节拆分，禁止优化阶段访问测试数据，避免Agent出现指标作弊、选择性报告等问题，可直接迁移到推荐算法迭代、广告策略优化等内部Agent场景

  - 无需微调基座即可提效的插件设计可直接复用：开场给探索导向的ideation prompt、增加资源调度规则避免算力浪费、每小时触发反思检查清单，避免Agent陷入局部调参的舒适区

  - Agent能力评测可复用分层评估逻辑：不要只看最终指标提升，要审计执行轨迹、区分优化是来自常规工程调参还是创新洞察，避免高估Agent的原创能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent评测多聚焦结构化任务、通用CS领域，未覆盖真实科学ML场景——这类场景代码不规范、需要领域洞察，且容易出现指标作弊问题，亟需能真实衡量Agent在非结构化场景下优化能力的基准。

### 方法关键点
- 构建AGENT4SCI测试床：经4层过滤筛选20个科学ML基准、25个任务，覆盖11个科学领域，每个任务都经过人工复现 baseline、标准化数据集拆分、环境隔离，解决原始仓库的作弊漏洞
- 三阶段评估协议：将Agent的优化执行（仅能访问训练/验证集）、离线测试（独立Agent跑测试集）、行为审计（独立Agent检查作弊行为）完全隔离，避免评估作弊
- 提出三类轻量插件技能：研究视角ideation prompt（开场引导跳出常规调参）、实验管理规则（提升资源利用率）、定时检查清单（每小时反思避免陷入局部调参），无需微调基座即可提升效果

### 关键结果
- 测试4款前沿编码Agent（Claude Opus/Sonnet、Codex、Gemini），均能在所有基准上超过已发表SOTA，Claude Opus无插件时平均相对提升10.4%，审计阶段未发现任何作弊行为
- 插件技能加持下，Claude Opus平均提升从10.4%涨到20.1%，Codex从4.4%涨到8.1%，同时Agent提出的优化方案更具领域相关性

### 最值得记住的话
当前前沿Agent的优化收益几乎全部来自ML工程技巧，而非研究级别的领域洞察，要让Agent做真正的原创研究还需要大量突破
