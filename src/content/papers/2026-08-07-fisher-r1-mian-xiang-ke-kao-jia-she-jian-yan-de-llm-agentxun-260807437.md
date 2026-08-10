---
title: 'Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing'
title_zh: Fisher-R1：面向可靠假设检验的LLM Agent训练方法
authors:
- Jiacheng Miao
- Jin Mu
- Guanhua Chen
- James Zou
affiliations:
- Stanford University
- University of Wisconsin–Madison
arxiv_id: '2608.07437'
url: https://arxiv.org/abs/2608.07437
pdf_url: https://arxiv.org/pdf/2608.07437
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent 统计推理能力优化
tags:
- LLM Agent
- Hypothesis Testing
- Reinforcement Learning
- SFT
- Benchmark
one_liner: 构建P-Bench假设检验基准，用SFT+RL训练的Fisher-R1超越GPT-5.4等前沿模型
practical_value: '- 工具类Agent训练可复用「专家轨迹SFT + 可验证规则化奖励RL」范式：比如电商AB实验分析、用户行为归因类Agent，先收集分析师的标准操作流程做SFT，再用可自动校验的结果（如p值正确性、结论与统计结果一致性）做RL优化，效果远超纯SFT或prompt工程

  - 数值类输出的奖励设计trick：对p值、转化率、统计显著性这类区间压缩的数值，不要直接用原始差做奖励，可参考本文的z-score变换后再算相似度，避免极端值区间的奖励失真

  - 业务域Agent评测基准构建参考：可复用P-Bench的流水线，从真实业务场景（如活动效果分析、人群转化对比）提取任务，自动复现生成标准答案后专家抽检，比纯人工出题效率高、覆盖场景更全

  - 鲁棒性提升方法：训练数据中加入针对性的扰动（如电商数据的异常订单、离群用户、缺失值），可有效提升Agent对真实业务脏数据的处理能力，减少推理错误'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent已能自动化完成数据读取、代码生成、分析执行的全流程，但在假设检验场景下常出现代码可运行、但统计方法选择错误的问题，导致p值无效、结论完全错误；现有基准大多只考核代码可执行性或结论正确性，不验证统计推理的严谨性，缺乏针对性的评测基准和训练方案。
### 方法关键点
- 构建P-Bench基准：包含425个来自经济学、生物学、医学的真实假设检验任务，每个任务都有专家审核的标准答案，分Easy（203个）和Hard（222个）两个子集，覆盖17类常用统计方法
- Fisher-R1训练：先合成大量带标准答案的模拟训练数据，基于专家生成的标准分析轨迹做SFT warm start，再用DAPO强化学习算法优化，奖励由z-score变换后的p值相似度（权重0.9）和结论正确性（权重0.1）组成，无需人工偏好标注
### 关键实验
在P-Bench上对比GPT-5.4、DeepSeek-V4-Pro等前沿模型，Fisher-R1-14B单轮成功率相对DeepSeek-V4-Pro提升21%，难任务上提升达26%，在严格考核p值准确性的指标上超过GPT-5.4，相比同尺寸基线模型准确率提升超20%，运行稳定性也大幅提升。
### 核心结论
对垂直领域的严谨推理类Agent，基于可验证结果的定向SFT+RL训练，效果远优于单纯扩大模型规模。
