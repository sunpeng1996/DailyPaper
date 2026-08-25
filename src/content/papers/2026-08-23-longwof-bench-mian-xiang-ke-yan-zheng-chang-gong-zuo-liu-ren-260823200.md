---
title: 'LongWoF-Bench: Evaluating EvoMap Genes for Verifiable Long-Workflow Tasks'
title_zh: LongWoF-Bench：面向可验证长工作流任务的EvoMap基因评估基准
authors:
- Xiao Zhang
- Qumeng Sun
- Jihao Li
- Yiming Ren
- Xiang Liu
- Haoyang Zhang
- Junjie Wang
affiliations:
- Infinite Evolution Lab, EvoMap
- Tsinghua University
arxiv_id: '2608.23200'
url: https://arxiv.org/abs/2608.23200
pdf_url: https://arxiv.org/pdf/2608.23200
published: '2026-08-23'
collected: '2026-08-25'
category: Agent
direction: 长工作流Agent · 可验证经验复用
tags:
- Long-Workflow Agent
- EvoMap Gene
- Benchmark
- Verifiable Execution
- Experience Reuse
one_liner: 提出含778个可验证长工作流任务的评估基准，验证EvoMap经验基因的跨模型复用价值
practical_value: '- 可复用经验资产构建：电商复杂运营、大促活动执行、多平台商品上新等长工作流Agent场景，可将经过实际验证（上线无故障、转化达标等）的执行轨迹提炼为结构化经验基因，替代静态规则，跨不同模型复用提升任务成功率

  - 推理成本优化：对高重复度的长工作流任务（如商品合规审核、营销活动规则校验），沉淀经验基因可减少重复试错的token消耗，实测可降低近10%的推理成本，同时提升执行效率

  - 经验质量管控：所有可复用经验必须经过严格端到端验证，未经过实际校验的参考蒸馏经验效果反而不如静态规则，避免盲目积累无效经验

  - 落地优先级参考：经验基因优先在规则依赖强、操作约束多的场景落地，这类场景增益最稳定，无明显模型依赖'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM执行复杂长工作流时，单次成功的执行经验无法沉淀，后续执行需要重新探索策略、重复踩坑；同时现有Agent评估基准缺少对长工作流端到端可验证效果的统一评测框架，也未对静态规则（Skill）和经过验证的执行经验（Gene）的效果差异做可控对比。

### 方法关键点
- 构建LongWoF-Bench基准，共778个机器可自动验证的长工作流任务，覆盖代码生成、Agent环境合成、数学推理、规则遵循4大类，所有任务都要求输出满足端到端约束，可通过统一验证器判断是否成功
- 对比三类执行条件：无辅助上下文、静态Skill（抽象的任务执行流程规则）、EvoMap Gene（从验证器确认的成功执行轨迹中蒸馏的结构化经验，包含踩坑记录、边界条件、有效策略等）
- 采用可控评估协议，所有对比组的任务说明、运行环境、验证逻辑完全一致，仅辅助上下文不同

### 关键实验
- 在252个Claude Opus生成了经验Gene的任务上，7个测试模型的平均严格通过率：无上下文41.0%、Skill 51.2%、EvoMap Gene 62.9%，Gene比Skill高出8.7~15.5个百分点，增益跨模型家族通用
- Claude Opus用Gene比用Skill多完成39个任务，求解阶段token消耗降低9.9%；对比多轮探索生成经验的过程，单次Gene复用可降低45.8%的token消耗
- 参考蒸馏的无验证轨迹的Gene效果反而比Skill低3.3~11.3个百分点，证明经验的验证来源比表示形式更重要

### 核心结论
经过端到端验证的执行经验作为可复用资产，效果远好于抽象的静态流程规则，且可跨模型复用、大幅降低重复探索成本
