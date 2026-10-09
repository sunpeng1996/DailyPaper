---
title: 'SAIL: Scientific Agentic Intelligence via a Science-Aware Loop'
title_zh: SAIL：基于科学感知迭代环的开源科研智能体
authors:
- SAIL Model Team
- Boyuan Sun
- Bryan Dai
- Che Liu
- Chi Liu
- Derek Li
- Hongming Piao
- Mengzhuo Chen
- Xidong Wang
- Yan Shu
affiliations:
- IQuest Research
arxiv_id: '2610.11451'
url: https://arxiv.org/abs/2610.11451
pdf_url: https://arxiv.org/pdf/2610.11451
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: Agent 垂直领域智能体训练优化
tags:
- Agent
- MoE
- On-Policy Training
- Knowledge Distillation
- Reinforcement Learning
one_liner: 35B总参3B激活参的开源科研智能体，通过科学感知迭代环训练，性能媲美大参数量模型
practical_value: '- 可复用「失败根因诊断→针对性构造训练任务」的迭代范式：做电商导购/客服Agent时，先定位用户交互失败的具体短板（如商品检索不准、优惠规则理解错误），再针对性生成训练样本，比盲目标注效率提升数倍

  - 可复用「多专项专家模型→MOPD在线蒸馏→通用Agent」的训练范式：电商场景可先训练搜品、售后、订单查询等专项小模型，再蒸馏到统一的低参Agent，既保留各专项能力又降低推理成本

  - 低激活参MoE的选型思路适合高QPS业务落地：3B激活参的推理延迟与7B模型相当，性能媲美百亿级大模型，可直接用于对性能和延迟要求都高的电商推荐、实时导购场景

  - 解耦式在线训练架构可直接复用：将模型推理、环境执行、参数优化三层解耦的设计，支持接入商品库、订单系统等多种业务工具，无需修改训练框架即可新增工具能力'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前垂直领域Agent训练普遍面临标注成本高、能力短板难以针对性补全、大参数模型推理成本过高无法落地的问题，科研场景更是要求Agent同时掌握文献检索、科学编码、多步工具调用等复合能力，现有通用模型无法兼顾效果和部署成本。
### 方法关键点
- 科学感知迭代环：用前沿大模型驱动的Agent诊断当前模型的能力缺口，针对性从论文、代码仓库中构造匹配缺口的训练任务、交互轨迹和可执行环境，持续迭代训练
- 四阶段训练范式：先通过SFT打底通用能力，再训练多个专项能力专家模型，通过Multi-Teacher On-Policy Distillation（MOPD）将专家能力蒸馏到通用学生模型，最后用智能体RL在可执行环境中训练多步交互能力
- 解耦式训练基础设施：将模型rollout、任务执行、参数优化三层解耦，支持多工具、多环境接入，同时兼容MOPD和RL两种在线训练范式
- 模型选型：基于Qwen3.6-35B-A3B MoE训练，总参数35B，激活参数仅3B，推理成本极低
### 关键实验
在13个科研基准（含SciCode、AstaBench、DRB2等）上对比35B到1.6T参的13款开源模型：
- SAIL在SciCode得分50.35，超过744B参GLM-5.2的47.57；ArxivDIGESTables得分35.24位列第一
- 12项任务平均得分59.76，超过284B参DeepSeek-V4-Flash，仅略低于744B的GLM-5.2
- 相比基座模型，LitQA-search提升37.33分，E2E-Bench基础版提升30.71分
### 核心结论
针对垂直领域Agent的训练，基于失败诊断的闭环迭代造数，配合多专家蒸馏+低激活参MoE的方案，可以用远低于大模型的推理成本实现媲美大模型的效果。
