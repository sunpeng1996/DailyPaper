---
title: 'The Missing Primitive: Diagnosing and Repairing Mathematical Reasoning in
  Large Language Models'
title_zh: 大模型数学推理缺失核心基元的诊断与修复方法
authors:
- Shuo Xing
- Zilin Dai
- Chengyuan Qian
- Fangzhou Lin
- Wenjing Chen
- Ping He
- Pan Lu
- Alvaro Velasquez
- Mohit Bansal
- Zhengzhong Tu
affiliations:
- Texas A&M University
- Harvard University
- Vanderbilt University
- Stanford University
- University of North Carolina at Chapel Hill
arxiv_id: '2610.02191'
url: https://arxiv.org/abs/2610.02191
pdf_url: https://arxiv.org/pdf/2610.02191
published: '2026-10-01'
collected: '2026-10-02'
category: Reasoning
direction: 大模型数学推理诊断与优化
tags:
- Mathematical Reasoning
- LLM
- Self-Distillation
- Benchmark
- Privileged Information
one_liner: 提出数学基元概念拆解大模型推理能力，通过特权自蒸馏框架ABSORB提升数学推理性能
practical_value: '- 做垂直领域Agent推理时，可将任务拆解为「核心决策基元+执行步骤」两部分，先引导模型识别业务核心决策点再执行，大幅降低推理错误率

  - 小模型垂直场景调优时，可采用「特权信息自蒸馏+边界覆盖」机制，用人工标注的核心决策逻辑作为教师额外输入，避免全量SFT导致的原有能力退化

  - 业务效果评估不要仅看最终指标，需拆解核心能力维度（如推荐的需求理解、匹配、排序能力），定位真实瓶颈，避免不同路径达标的能力缺陷被掩盖'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有大模型数学推理评估仅以最终答案准确率为核心指标，无法区分正确结果来自对问题结构的真实理解还是巧合式推导，也难以定位真实能力瓶颈；多数训练方案在修复短板时容易造成原有能力的退化，同时大量案例显示模型常具备解题执行能力，却因找不到核心思路而失败。
### 方法关键点
1. 定义**Mathematical Primitive（数学基元）**：即支撑解题的核心结构思想，是问题与解法共有的底层本质属性，区别于通用定理提示或步骤规划
2. 构建PRIM benchmark：从Discovery（从问题独立识别基元）、Generation（零样本CoT直接解题）、Digestion（从正确解法提取基元）、Execution（给定基元后解题）四个维度拆解推理能力，覆盖182道专家校验的高难度数学题
3. 提出ABSORB自蒸馏框架：将基元作为教师模型的特权输入，采用单边钳位的反向KL损失实现边界覆盖，仅正向引导学生推理方向，不强行覆盖学生原有正确偏好，避免训练后的能力退化
### 关键结果
1. 诊断显示给定正确基元后，12款不同规模模型的解题准确率提升17.58~29.67个百分点，83.6%的解题失败来源于基元发现能力的瓶颈
2. 在Qwen3.5 4B/9B/27B三个尺度模型上，ABSORB相比SFT、OPSD基线，平均推理性能提升2.42~4.48个百分点，无原有能力的负向退化

> 核心结论：复杂推理任务的核心瓶颈往往是核心结构的发现能力而非下游执行能力，基于特权信息的选择性引导比全量监督训练的稳定性和收益更高
