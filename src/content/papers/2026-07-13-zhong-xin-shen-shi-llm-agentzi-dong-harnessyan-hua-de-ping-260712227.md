---
title: Rethinking the Evaluation of Harness Evolution for Agents
title_zh: 重新审视LLM Agent自动Harness演化的评估范式
authors:
- Yike Wang
- Huaisheng Zhu
- Zhengyu Hu
- Yige Yuan
- Zhengyu Chen
- Shakti Senthil
- Hannaneh Hajishirzi
- Yulia Tsvetkov
- Pradeep Dasigi
- Teng Xiao
affiliations:
- Allen Institute for AI
- University of Washington
- Independent
arxiv_id: '2607.12227'
url: https://arxiv.org/abs/2607.12227
pdf_url: https://arxiv.org/pdf/2607.12227
published: '2026-07-13'
collected: '2026-07-18'
category: Agent
direction: Agent 自动Harness演化评估
tags:
- LLM Agent
- Harness Evolution
- Evaluation Protocol
- Test-time Scaling
- Generalization
one_liner: 揭示现有Agent自动harness演化评估的漏洞，证明其未优于简单测试时缩放基线且泛化性差
practical_value: '- 落地Agent系统（如电商导购Agent、客服Agent）时，评估harness优化效果必须加Parallel Sampling、Sequential
  Refinement两个简单基线，避免把额外计算带来的收益误认为是harness优化的价值

  - 无可信外部业务反馈（如用户点击、转化信号）时，优先选用Parallel Sampling这类简单测试时缩放方案，投入产出比远高于自动harness演化

  - 若要落地自动harness演化，必须严格拆分harness优化的训练集、验证集与最终评估的测试集，避免harness过拟合到特定任务导致上线后性能骤降

  - 资源有限的业务场景下，优先把额外推理预算分配给测试时缩放（多候选投票、多轮自修正），比优化harness的收益更稳定可预期'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent自动harness演化的评估范式存在两大核心缺陷：一是用同一套基准任务完成harness搜索和最终性能测试，无法区分性能增益来自harness设计优化还是额外搜索计算投入；二是未在相同推理预算、反馈条件下与简单测试时缩放基线对比，导致结果严重高估harness优化的实际价值，容易误导Agent研发方向，亟需建立公平的评估标准。

### 方法关键点
- 统一控制所有对比方法的推理预算K=5、反馈条件一致，对比四类方案：Parallel Sampling（并行采样多轨迹选优）、Sequential Refinement（基于历史轨迹迭代修正答案）、Harness Evolution（跨任务批量优化通用harness）、Harness Scaling（单任务专属harness自适应）
- 设置三类实验场景：无单元测试反馈（仅靠LLM自评估）、有单元测试反馈（有明确正确性信号）、跨任务泛化（harness优化集与评估集完全拆分）

### 关键实验结果
基于Terminal-Bench 2.1 benchmark，在Claude Opus 4.6、GPT-5.4、GPT-5.4 mini三个模型上测试：
1. 无单元测试场景：Harness Evolution平均pass@1仅67.4，低于Parallel Sampling的72.3，甚至低于初始harness基线的68.2
2. 有单元测试场景：Harness Evolution平均pass@1仅75.8，远低于Parallel Sampling的86.0；pass@5仅86.2，低于Sequential Refinement的91.8
3. 泛化测试场景：优化后的harness在未见任务上平均仅比初始harness提升0.6个百分点，几乎无泛化增益

### 核心结论
当前自动harness演化的收益大多来自额外的测试时计算而非harness设计本身，相同预算下，简单测试时缩放方案的投入产出比远高于自动harness演化。
