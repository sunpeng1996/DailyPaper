---
title: 'GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment
  Simulations'
title_zh: GlobeBench：面向可扩展环境仿真的文本世界模型测评基准
authors:
- Nicholas Saban
- Charvi Bannur
- Mariya Vasileva
- Darshan Deshpande
affiliations:
- Patronus AI
arxiv_id: '2610.22708'
url: https://arxiv.org/abs/2610.22708
pdf_url: https://arxiv.org/pdf/2610.22708
published: '2026-10-14'
collected: '2026-10-20'
category: Eval
direction: LLM 世界模型仿真能力评估
tags:
- World Model
- Benchmark
- LLM Evaluation
- Agent Simulation
- Text Environment
one_liner: 推出覆盖5个领域19项技能的1632条测评任务集，配套混合评分体系衡量文本世界模型仿真准确率
practical_value: '- 做电商/推荐Agent仿真（如库存联动、用户权益变更、活动规则校验场景）时，可复用19项仿真技能分类框架拆解测评点，避免漏测隐式状态更新错误

  - 业务仿真评测的评分架构可直接照搬：先做确定性规则校验（数值、格式、错误码匹配），歧义场景才调用LLM judge，比纯LLM打分效率更高，结果一致性更强

  - 开发长周期多轮推荐Agent/对话Agent时，需重点优化隐式状态跨轮跟踪能力：当前LLM在动作影响未显式提及实体（L3级）场景平均成功率仅5.1%，是核心故障点

  - 自建业务仿真基准时，可复用其12道自动质量门规则，确保每个用例仅测试单一能力，方便快速定位模型缺陷根因'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
文本世界模型作为Agent训练的仿真环境需求快速增长，但无标准化基准衡量其仿真保真度，若仿真结果存在可被Agent利用的错误，RL训练出的Agent会习得不符合真实环境的规则，无法落地。
### 方法关键点
- 定义4大核心能力（State Coherence、Causal Correctness、Interface Fidelity、Constraint Enforcement）和19项细分仿真技能，每个测评用例仅对应单一技能，可直接定位模型缺陷
- 共1632个用例覆盖代码、企业工具、游戏、数理、对话5个领域，金标准全部来自真实环境执行结果，无人工标注；每个用例标注reach-back（依赖历史步长）、impact radius（动作影响范围）两个难度维度
- 混合评分体系：先通过确定性规则判断完全匹配/矛盾的结果，歧义场景才调用LLM judge，兼顾效率和准确率
### 关键结果
- 测试20款主流通用LLM和专用世界模型，GPT-6 Astra最高准确率仅49.57%，专用世界模型性能低于通用LLM中位数
- 当动作影响未显式提及的关联实体（L3级impact radius）时，所有模型平均成功率仅5.1%；超过40轮回溯的长周期任务，平均成功率从42.3%降至11.4%
- 共631个任务无任何模型可解决，占比达38.7%
### 核心结论
当前所有LLM的文本世界模型能力远未达标，隐式状态跨轮跟踪、多实体联动更新是最大短板
