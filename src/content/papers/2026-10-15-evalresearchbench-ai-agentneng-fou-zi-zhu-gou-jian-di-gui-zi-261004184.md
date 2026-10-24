---
title: 'EvalResearchBench: Can AI Agents Build Their Own Feedback for Recursive Self-Improvement?'
title_zh: EvalResearchBench：AI Agent能否自主构建递归自优化的评估反馈
authors:
- Yaolun Zhang
- Tianyi Xu
- Yujie Zhao
- Jishen Zhao
- Qingyun Wu
- Huazheng Wang
affiliations:
- Oregon State University
- University of California, San Diego
- Pennsylvania State University
- AG2 AI
arxiv_id: '2610.04184'
url: https://arxiv.org/abs/2610.04184
pdf_url: https://arxiv.org/pdf/2610.04184
published: '2026-10-15'
collected: '2026-10-24'
category: Agent
direction: Agent 自主评估设计能力测评
tags:
- Autonomous Evaluation
- Recursive Self-Improvement
- Agent Benchmark
- Evaluation Design
- RSI
one_liner: 提出测评AI Agent自主设计评估套件能力的基准ERB，覆盖编码、协作、推理三类任务
practical_value: '- 做推荐/广告系统AB测试评估时，可复用ERB的轻量套件设计思路：先选少量代表性任务+低成本grader，校准后替代全量Benchmark，降低API/算力成本

  - 迭代业务LLM Agent（如电商导购、客服Agent）时，可借鉴预算拆分方案：研发测试预算与上线后批量评估预算分开，避免迭代阶段资源浪费

  - 评估推荐排序效果时，可同时用Score（Lin''s CCC）和pairwise agreement两个指标，前者对齐分数绝对值，后者保证排序一致性，覆盖不同业务需求

  - 自研Agent自优化链路时，优先用人设计的公共任务子集作为强基线，不要盲目让Agent纯自主生成评估任务，避免过拟合开发集导致泛化性差'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
递归自优化（RSI）是AI Agent迭代的核心能力，但当前RSI系统均依赖人工预设的评估基准，重复运行全量Benchmark算力成本高、迭代效率低，现有工作仅覆盖评估设计的部分环节，未完整测评Agent在固定预算约束下自主设计可复用、高一致性评估套件的能力。
### 方法关键点
- 提出ERB基准，定义Researcher Agent任务：在3小时、100美元推理预算、100美元开发测试预算约束下，设计覆盖编码、协作、推理3个领域的可执行评估套件，包含至少100道测试题、自动grader、固定打分规则
- 评估分两阶段：开发阶段仅开放4个候选模型API、6个公开基准的参考分数；提交冻结的评估套件后，在9个未见过的密封候选模型、8个密封基准上测试一致性
- 核心评估指标：Score（100倍Lin's CCC，对齐分数分布与绝对值）、Pairwise Agreement（PA，候选模型排序与基准的一致性），同时统计构建成本、运行成本
### 关键结果
测试9个不同的Researcher Agent配置，对比人工采样公共任务的强基线Random120：① 最优Agent的PA达75%，低于多基准间一致性上限91%；② 7/8的Agent设计套件Score超过基线，但仅4/8的PA超过基线；③ 开发集表现最优的套件在密封集上并非最优，存在过拟合问题；④ 运行成本最低的套件拿到最高PA，轻量化设计优先级更高。
### 核心结论
Agent自主设计的评估套件仍未超过人工设计的公共任务子集基线，且开发集拟合好不代表泛化性强，评估设计必须同时兼顾信号一致性、泛化性与运行成本。
