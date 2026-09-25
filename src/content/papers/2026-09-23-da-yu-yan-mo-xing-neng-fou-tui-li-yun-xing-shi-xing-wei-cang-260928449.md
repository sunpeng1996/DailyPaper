---
title: Can LLMs Reason About Runtime Behavior? A Repository-Level Dynamic Benchmark
title_zh: 大语言模型能否推理运行时行为？仓库级动态评测基准
authors:
- Hamed Taherkhani
- Mohammad Abdollahi
- Melika Sepidband
- Hridya Dhulipala
- Tien N. Nguyen
- Hadi Hemmati
affiliations:
- York University
- The University of Texas at Dallas
arxiv_id: '2609.28449'
url: https://arxiv.org/abs/2609.28449
pdf_url: https://arxiv.org/pdf/2609.28449
published: '2026-09-23'
collected: '2026-09-25'
category: Eval
direction: LLM代码能力评测 · 动态基准构建
tags:
- LLM
- Benchmark
- Code Reasoning
- Dynamic Execution
- Evaluation
one_liner: 提出仓库级代码动态执行推理基准SWE-Flux，基于真实测试执行自动生成标准答案
practical_value: '- 自研代码Agent（用于推荐系统特征工程、A/B实验分析、策略自动调优）的推理能力评估，可参考SWE-Flux的自动打标逻辑，通过插桩执行获取真实标准答案，避免人工标注或LLM打分的偏差

  - 构建领域专属Agent评测集时，可复用输入扰动生成新评测样例的方法，低成本扩充高难度评测样本，提升Agent的鲁棒性

  - 代码Agent落地时，可优先优化局部逻辑推理能力（如规则校验、异常处理），跨模块数据流、多步状态推理场景可搭配代码执行器等工具补全能力短板'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有仓库级代码QA基准仅覆盖静态理解能力，多依赖LLM自动打分，执行推理类基准又局限于代码片段/函数，无法衡量LLM对完整仓库的运行时行为推理能力。
### 方法关键点
1. 推出SWE-Flux仓库级动态执行推理基准，覆盖12个真实Python仓库共480个执行驱动的评测样例，覆盖控制流、循环、程序状态、数据流、异常、不变量等场景
2. 标准答案通过插桩测试执行自动采集，无需人工标注或LLM判断，支持输入扰动自动生成新评测变体
### 关键结果
- 评测5款主流LLM，最优准确率仅37%
- 模型在局部场景（不变量、过程内控制流、异常、简单循环）表现较好，在数据流、跨过程执行、精确状态推理、多用例聚合场景表现较差
- 输入扰动可生成近90%样例的有效变体，且难度显著高于原有样例
