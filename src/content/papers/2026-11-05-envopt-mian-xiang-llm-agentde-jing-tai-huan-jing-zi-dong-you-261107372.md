---
title: 'EnvOpt: Automated Optimization for Agent Environments'
title_zh: EnvOpt：面向LLM Agent的静态环境自动优化方法
authors:
- Mingxuan Li
- Huanzhi Mao
- Qiuyang Mang
- Hanchen Li
- Joseph E. Gonzalez
- Alex Dimakis
affiliations:
- University of California, Berkeley
- University of Chicago
- Bespoke Labs
arxiv_id: '2611.07372'
url: https://arxiv.org/abs/2611.07372
pdf_url: https://arxiv.org/pdf/2611.07372
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 静态环境自动化优化
tags:
- LLM-Agent
- Environment-Optimization
- Cost-Reduction
- Transferable-Optimization
- No-Verifier-Training
one_liner: 提出LLM Agent优化第三维度：静态环境自动优化框架，无需标注即可实现降本提效
practical_value: '- 电商客服、工单处理、商品审核等静态环境复用的Agent场景，可直接复用EnvOpt思路做前置环境优化：比如预先构建常用商品库索引、工单分类cheatsheet、格式转换工具，无需修改模型和Harness即可实现降本提效

  - 训练阶段可使用无标注的同分布业务任务做环境优化，仅需少量带标注验证集做早停，大幅降低标注成本，适合内部业务场景缺标注的现状

  - 优化后的环境可跨模型、跨Harness迁移，无需针对每个新模型重新优化，一次优化所有同场景Agent均可受益，ROI极高，通常千次调用即可赚回10倍优化成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent优化仅聚焦参数调优、Harness优化两个方向，静态环境（如企业知识库、代码库、工作台等多任务共享的固定资源）的组织方式对Agent执行成本、成功率影响极大，却长期被视为不可修改的固定项；过往环境优化依赖手动设计，且需要大量标注数据，落地成本高，缺乏自动化端到端的优化方案。
### 方法关键点
- 固定目标Agent的模型与Harness，仅优化静态环境的信息表示与对外暴露方式，优化目标为最小化Agent执行成本，同时保证成功率不低于设定阈值
- 采用双Agent架构：Research Agent基于无标注训练任务中Target Agent的执行轨迹，迭代生成环境优化方案（如构建索引、SQLite数据库、工具调用cheatsheet、文件优先级排序程序、格式转换脚本等），无需训练集标注，通过答案一致性、代理指标判断优化是否有效
- 每轮优化后用少量带标注验证集评估成本与准确率，出现成本上升或准确率下降超过阈值即早停，避免优化过拟合到训练任务
### 关键结果
在5类覆盖工作台、数据工程、软件工程的Benchmark上测试，对比基线、GEPA、Meta-Harness等SOTA方法：1. AutomationBench上，Claude Haiku 4.5成本降低72.7%，成功率提升14.34%；优化后环境可直接迁移到Opus 5，成本降低68.1%，成功率提升1.34%；2. 叠加在Meta-Harness优化结果之上，Haiku 4.5成本进一步下降83.4%，准确率额外提升11.17%；3. 全场景平均成本降低48%，单场景优化投入约150美元，仅需109次调用即可回本，千次调用收益可达投入的10倍。
### 核心结论
Agent的成本与成功率不仅取决于模型和Harness，信息向Agent的呈现方式同样关键，环境优化是可落地、高ROI的正交优化方向。
