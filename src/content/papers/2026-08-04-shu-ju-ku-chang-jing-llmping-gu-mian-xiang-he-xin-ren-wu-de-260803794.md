---
title: 'Evaluating LLMs in Database Scenarios: A Lifecycle Benchmark for Assessing
  Their Potential in Core Database Tasks'
title_zh: 数据库场景LLM评估：面向核心任务的全生命周期基准测试
authors:
- Shunfan Zheng
- Dongsheng Shi
- Yue Li
- Xin Yi
- Linlin Wang
- Gerard de Melo
affiliations:
- East China Normal University
- Hasso Plattner Institute/University of Potsdam
arxiv_id: '2608.03794'
url: https://arxiv.org/abs/2608.03794
pdf_url: https://arxiv.org/pdf/2608.03794
published: '2026-08-04'
collected: '2026-08-06'
category: Eval
direction: LLM数据库任务全生命周期评估
tags:
- Benchmark
- Text-to-SQL
- LLM Evaluation
- Database Agent
- Reasoning
one_liner: 提出首个覆盖数据库全生命周期的LLM评估基准DBLifeBench及渐进式Text2SQL任务
practical_value: '- 做数据类Agent评估可复用全生命周期分阶段评估框架，避免仅测单任务漏判能力短板

  - 业务中Text-to-SQL需求可借鉴Progressive-Text2SQL的结构化推理思路，降低自然语言到SQL的认知差，提升生成准确率

  - 选型SQL相关LLM时注意：专用Text-to-SQL模型存在非编码阶段灾难性遗忘问题，全链路数据场景优先选通用大模型'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM数据库场景评估高度聚焦Text-to-SQL单任务，忽略了从初始schema设计到上线后运维的完整数据库生命周期，无法覆盖真实数据库管理所需的多元能力。

### 方法关键点
1. 构建DBLifeBench，是首个覆盖设计、实现、运行、调试、运维5个核心数据库生命周期阶段的LLM评估基准；
2. 提出Progressive-Text2SQL任务，通过结构化推理图模拟人类迭代解题过程，解决模糊自然语言与复杂SQL逻辑的认知不匹配问题。

### 关键结果
通用大模型在全生命周期5个阶段表现均衡；专用Text-to-SQL模型在设计、运维等非编码类阶段存在严重的灾难性遗忘，相关任务表现大幅落后于通用大模型。
