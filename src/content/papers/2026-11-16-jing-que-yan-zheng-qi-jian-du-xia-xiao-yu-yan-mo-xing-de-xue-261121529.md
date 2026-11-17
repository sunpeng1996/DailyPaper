---
title: 'Procedure without Judgment: What Small Language Models Learn under an Exact
  Verifier'
title_zh: 精确验证器监督下小语言模型的学习特性与蒸馏效果研究
authors:
- Arunkumar V
- Manoranjan Gandhudi
- Gangadharan G. R.
- Arun Prakash
- S. Senthilkumar
affiliations:
- Anna University
- Central University of Karnataka
- NIT Tiruchirappalli
- Jawaharlal Nehru University
arxiv_id: '2611.21529'
url: https://arxiv.org/abs/2611.21529
pdf_url: https://arxiv.org/pdf/2611.21529
published: '2026-11-16'
collected: '2026-11-17'
category: Training
direction: 小语言模型蒸馏 · 精确验证监督
tags:
- SLM
- Knowledge Distillation
- Exact Verifier
- SFT
- Reinforcement Learning
- XAI
one_liner: 对比算法与大模型作为教师的小模型微调效果 揭示小模型仅学到任务固定流程而非通用判断
practical_value: '- 垂直场景小模型SFT优先用确定性算法生成的正确轨迹做训练数据，同数据量下效果比大模型生成的正确轨迹高16~61个点，适合电商风控、规则解释等确定性强的场景

  - 小模型在规则类任务上泛化性差，仅能复用流程框架（如先校验再缩减的逻辑），无法迁移最小化判断能力，跨场景部署必须针对性重训，不要期待通用迁移能力

  - Agent任务的prompt优化收益极高，仅增加一句缩减冗余特征的指令可让Claude Haiku准确率从58%提升到75%，做电商query理解、规则解释类Agent时优先优化prompt再考虑微调

  - 用精确reward做RL训练时要警惕策略退化，即使verifier完全准确也可能只调整工具调用策略不提升准确率，甚至出现reward hacking，RL调优必须加跨分布校验'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前基于验证器的LLM训练多关注近似验证器的误差问题，少有研究完全精确的验证器能让模型学到什么核心能力；授权策略可解释性任务存在精确的最小充分理由（MSR）标注，可作为无误差验证的理想场景，能清晰区分模型学到的是执行流程还是底层判断逻辑。

### 方法关键点
- 任务设定：解释器仅可见请求和决策，无法访问策略本身，可调用`decide`（修改请求查询决策）、`check`（校验特征集是否充分）工具，30轮内输出最小充分理由（MSR）
- 训练方案：对比两类教师对Qwen3-4B的LoRA微调效果：① 删除算法生成的2000/148条正确轨迹；② Claude Opus/Sonnet生成的148条正确轨迹；额外测试基于精确reward的RL训练效果
- 评估体系：用精确oracle计算Exact（输出为MSR的比例）、Suff（输出充分的比例）等指标，跨分布测试采用3个未见过的公开OPA/Cedar策略

### 关键结果
- 数据集：自研10特征GlassGate授权策略（12万+上下文）+5个公开规则策略，基线覆盖Claude全系列、Gemini Flash-Lite、删除算法、单变量翻转启发式
- 仅添加一句“删除不影响决策的特征”的指令，Haiku 4.5的Exact准确率从58%升至75%，Gemini Flash-Lite从16%升至43%
- 2000条算法轨迹微调的4B模型分布内Exact达92%，比同数据量大模型教师的微调结果高39个点，仅比删除算法 ceiling 低8个点
- 分布外测试时算法微调的模型Suff仍保持94%，但Exact骤降至48%，仅学到固定校验流程，无通用最小化判断能力
- 精确reward的RL训练仅改变工具调用策略（从混合调用探针/校验变为全量调用校验），完全不提升跨分布准确率

### 最值得记住的一句话
在精确验证器监督下训练小模型，学到的是固定的流程形状而非流程背后的判断逻辑，分布内的性能提升不能代表通用能力的增强。
