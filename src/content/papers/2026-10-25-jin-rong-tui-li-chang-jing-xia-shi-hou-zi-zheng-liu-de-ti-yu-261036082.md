---
title: How Much Does the Hint Matter? Scope Conditions for Hindsight Self-Distillation
  in Financial Reasoning
title_zh: 金融推理场景下事后自蒸馏的提示作用边界与优化方案
authors:
- Johnny Yu
- Cyril Gorlla
affiliations:
- University of California, Berkeley
- CTGT
arxiv_id: '2610.36082'
url: https://arxiv.org/abs/2610.36082
pdf_url: https://arxiv.org/pdf/2610.36082
published: '2026-10-25'
collected: '2026-10-29'
category: Training
direction: LLM自蒸馏 · 垂域推理优化
tags:
- self-distillation
- on-policy-training
- financial-reasoning
- LoRA
- knowledge-distillation
one_liner: 提出无外部教师的金融推理事后自蒸馏方案Fin-SD，仅靠错误定位即可提升推理精度
practical_value: '- 垂域LLM/Agent微调（如电商风控、交易推理、选品策略推理）可复用该自蒸馏范式：无需调用外部大模型当教师，仅靠错误位置定位加通用提示就能实现效果提升，完全适配数据不能出域的合规要求

  - 自蒸馏训练时选择reverse KL、仅蒸馏错误点后100token的短rollout：既可以提升推理准确率，还能减少推理生成的token数，降低部署latency，适配推荐/广告场景的实时响应需求

  - 训练迭代时每轮动态挖掘当前模型的错误样本更新训练集：相比固定训练集的SFT效果更优，且不会显著遗忘通用能力与合规行为，适合垂域Agent的持续迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
金融场景受数据驻留法规约束，仅能部署本地开源小参数LLM，其多步定量推理能力远落后于前沿闭源大模型；传统在策略自蒸馏要么依赖外部强教师，要么需要完整参考解答，成本高且不符合数据合规要求，亟需探索无外部依赖的高效蒸馏方案。

### 方法关键点
- 提出Fin-SD自蒸馏流程：学生模型生成推理轨迹后，自行定位首个错误步骤并截断轨迹；给冻结的学生副本输入错误前缀加提示，生成正确后续推理，用reverse KL对齐学生与教师在错误点后100token rollout的分布，全程无外部模型参与梯度更新
- 过滤纯算术错误，仅对概念类错误做蒸馏，避免无效梯度
- 每轮迭代重新挖掘当前模型的错误样本，并重冻教师副本，训练集随模型能力动态更新

### 关键结果
在FinanceReasoning Hard多步金融推理基准测试：
- Fin-SD较base模型精度提升3.03pp，推理token数减少3.3%，合规性（FinTrust14项指标）、通用推理能力（MMLU-Pro）无明显退化
- 与使用完整参考解的OPSD自蒸馏精度相当，推理token数减少9.5%，远优于SFT基线
- 通用无信息提示、6倍参数大模型生成的提示与自写提示效果无显著差异，增益核心来自错误位置的局部监督而非提示内容

### 核心结论
只要基座模型已经具备相关领域的latent知识，自蒸馏的增益核心来自对错误发生位置的精准定位和局部监督，而非提示的信息量或外部教师的强度
