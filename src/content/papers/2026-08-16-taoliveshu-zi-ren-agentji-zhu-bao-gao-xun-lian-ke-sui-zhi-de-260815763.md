---
title: 'TaoLive Digital Avatar Agent Technical Report: Training Agents to Evolve with
  Their Harness'
title_zh: TaoLive数字人Agent技术报告：训练可随执行框架演进的模型
authors:
- TaoLive AIGC LLM Team
- Yuhan Sun
- Wenhao Lin
- Yongdong Luo
- Yibo Hu
- Meiguang Jin
- Junfeng Ma
- Weihang Pan
- Jiaxin Zhao
- Zulong Chen
affiliations:
- TaoLive AIGC LLM Team
arxiv_id: '2608.15763'
url: https://arxiv.org/abs/2608.15763
pdf_url: https://arxiv.org/pdf/2608.15763
published: '2026-08-16'
collected: '2026-08-18'
category: Agent
direction: 电商直播数字人Agent 训练与架构优化
tags:
- Digital Avatar
- Agent Training
- E-commerce Live Streaming
- Low Latency Inference
- Domain Adaptation
one_liner: 提出Harness感知训练框架，让小参数模型兼顾低延迟、业务效果与执行框架演进鲁棒性
practical_value: '- 业务规则迭代快的Agent场景可复用Harness架构，将技能、提示词、钩子、工具模块与模型权重解耦，无需重训即可完成业务逻辑更新，迭代周期从周级压缩到小时级

  - 领域小参数Agent训练可引入Harness-State Augmentation (HSA)，训练时对技能ID、工具定义、提示结构做任务保留变换，避免模型过拟合固定执行配置，大幅降低领域SFT后的通用能力掉点

  - 可复用三阶段训练Pipeline：HSA-SFT完成领域适配→General OPD恢复通用指令遵循能力→HSA-RL在模拟环境下提升多轮交互鲁棒性，平衡业务效果和泛化性

  - 低延迟要求的Agent场景，可在单H20上用MTP speculative decoding做推理优化，本次实践中35B模型P50 latency降至3.4s，P95
  8.1s，满足直播实时交互要求'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
电商直播数字人Agent需同时满足三个矛盾要求：实时交互低延迟、营销/合规策略高频更新、回复准确无幻觉。现有方案要么大模型零-shot泛化性好但延迟过高（DeepSeek-V4-flash P95超21s），要么小模型固定Harness SFT过拟合配置，Harness更新后效果暴跌，还会损失7.7分IFEval通用能力，无法适配业务高频迭代需求。

### 方法关键点
- 可演进Harness架构：将技能、提示词流水线、钩子、工具注册四个模块与模型权重解耦，支持人在环的诊断-编辑-评估迭代，无需重训即可更新业务逻辑
- Harness感知训练（HAT）三阶段Pipeline：① HSA-SFT：对Harness的技能标识、内容、工具schema、提示结构、钩子做任务保留变换，生成多样化训练数据避免过拟合；② General OPD：用通用指令数据集蒸馏恢复SFT损失的通用能力；③ HSA-RL：在直播模拟环境下做带HSA的RL训练，提升多轮交互和错误恢复能力

### 关键结果
基于Qwen3.6-35B-A3B训练的模型：① 直播QA平均分94.8，超基线14.5分，也超过最强通用大模型的93.0分；② Harness变种QA得分94.6，超基线19.2分；③ IFEval得分83.5，避免了固定SFT的7.7分掉点；④ 单H20加MTP优化后P50延迟3.407s，P95 8.114s，满足直播实时要求。线上A/B测试相对ReAct基线GMV和订单量均有显著提升。

最值得记住的一句话：高频迭代的业务Agent系统，需将执行逻辑与模型权重解耦，训练阶段就引入执行环境扰动，避免模型过拟合固定配置
