---
title: Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for
  AI Scientists
title_zh: 大模型是否适合科学发现？面向AI科学家的能力导向评测基准
authors:
- Chuhan Shi
- Xiaoquan Ren
- Sicheng Song
- Haobo Li
- Rui Sheng
- Yushi Sun
affiliations:
- Southeast University
- East China Normal University
- Hong Kong University of Science and Technology
arxiv_id: '2607.11079'
url: https://arxiv.org/abs/2607.11079
pdf_url: https://arxiv.org/pdf/2607.11079
published: '2026-07-12'
collected: '2026-07-16'
category: Eval
direction: 大模型科学数据分析能力评测
tags:
- LLM Evaluation
- Scientific Discovery
- Benchmark
- AI Scientist
- Reasoning
one_liner: 提出覆盖6类核心能力5个学科的SDABench基准，配套15个LLM评测结果与五级错误分析框架
practical_value: '- 可复用五阶段错误分析框架，对LLM4Rec、电商Agent的效果做归因拆解，定位从输入理解到决策输出各环节的失效点

  - 能力分层评测思路可迁移到业务场景，比如将电商Agent的能力拆分为用户意图理解、商品匹配、解释生成、因果归因等维度分级评估

  - 真实+合成数据混合的自动化评测集构建pipeline可复用，低成本扩充搜索、推荐、广告场景的评测Case'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM科学数据分析评测基准多聚焦代码执行或工作流完成度，忽略不同科学论断（假设探索、统计推断、机理解释等）的底层假设与有效性标准差异，缺乏分层的能力维度评估。
### 方法关键点
1. 提出SDABench评测基准，围绕描述、探索、推断、预测、因果、机理6类核心能力，覆盖生物、化学、环境、地理、物理5个领域；
2. 包含527条真实数据实例SDA-Real、6000条合成实例SDA-Synth，支持单选、开放题两种题型，基于自动化流水线构建；
3. 配套五阶段错误分析框架，可精准定位LLM任务失效环节。
### 关键结果
评测15个代表性LLM发现，模型在描述类任务表现较好，但在假设选择、隐过程建模、机理推理类任务上性能骤降；高阶模型可更可靠识别相关范围与变量，但仍难以选择合适分析流程、建模变量关系、得出有效结论。
