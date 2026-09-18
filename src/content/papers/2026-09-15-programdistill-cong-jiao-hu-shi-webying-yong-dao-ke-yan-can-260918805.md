---
title: 'ProgramDistill: From Interactive Web Apps to Verifiable Reference-Guided SWE
  Tasks'
title_zh: ProgramDistill：从交互式Web应用到可验证参考引导SWE任务基准
authors:
- Jeonghye Kim
- Minseon Kim
- Young Jin Kim
- Matheus Pereira
- Marc-Alexandre Côté
- Alessandro Sordoni
- Xingdi Yuan
- Zhengyan Shi
affiliations:
- KAIST
- Microsoft Research Montréal
- Microsoft AI
arxiv_id: '2609.18805'
url: https://arxiv.org/abs/2609.18805
pdf_url: https://arxiv.org/pdf/2609.18805
published: '2026-09-15'
collected: '2026-09-18'
category: Agent
direction: 编码Agent能力评测基准构建
tags:
- Coding Agent
- Benchmark
- SWE
- LLM Agent
- Program Synthesis
one_liner: 提出无人工干预构建的参考引导编码Agent评测基准ProgramDistill，覆盖4000+可控难度Web开发任务
practical_value: '- 业务Agent评测任务构建可复用mine-craft-patch思路：针对电商页面生成Agent、活动规则配置Agent等代码类业务Agent，可基于现有可用参考系统自动生成无人工标注的评测任务，大幅降低评测数据集构建成本

  - 分阶能力评测框架可迁移：参考按功能粒度、恢复深度划分任务难度的设计，为业务Agent搭建分层评测体系，精准诊断不同复杂度场景下的能力瓶颈，针对性迭代优化

  - 自动验证逻辑可直接复用：将可重放交互行为与金标准补丁绑定的校验方式，可套用到代码生成类Agent的效果自动校验环节，替代部分人工审核，提升迭代效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有编码Agent评测多依赖预先明确的需求描述，不符合实际Web开发中需从可用参考系统（如旧版本、竞品原型）反推预期行为再落地实现的真实场景，缺少对应方向的标准化评测基准。

### 方法关键点
1. 提出ProgramDistill基准，聚焦参考引导的软件工程任务评测；
2. 设计mine-craft-patch无人工干预流水线，将应用拆解为不同粒度的独立功能，每个功能关联可重放交互行为与金标准补丁，自动批量生成任务。

### 关键结果
- 覆盖26个应用的1975个经回放验证的行为，共构建4063个可控难度任务；
- 9款前沿编码Agent中，GPT-6 Astra、Claude Opus 5在全应用重构累计工作流的成功率分别为49.2%、28.8%；
- 部分应用重构场景下，恢复深度从1提升至8时，二者成功率分别从100%降至64.0%、96%降至32%。
