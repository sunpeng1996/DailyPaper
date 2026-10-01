---
title: 'Evaluating Bounded Autonomy in Regulated Agentic AI: A Diagnostic Harness
  with Constitutional Rewards, Escalation Labels, and Runtime Governance'
title_zh: 受监管智能体有限自主性评估工具包：含规则奖励、升级标签与运行时治理
authors:
- Dipankar Sarkar
affiliations:
- Skelf Research
arxiv_id: '2609.37501'
url: https://arxiv.org/abs/2609.37501
pdf_url: https://arxiv.org/pdf/2609.37501
published: '2026-09-27'
collected: '2026-10-01'
category: Agent
direction: Agent · 受监管场景有限自主性评估
tags:
- Agent Governance
- Bounded Autonomy
- DPO
- LoRA
- Runtime Guardrails
- Evaluation Harness
one_liner: 提出REGLLM诊断框架，用统一领域规则覆盖评估训练推理，揭示小样本Agent评估的高方差问题
practical_value: '- 做高风险场景（电商合规客服、金融类广告合规Agent）时，可复用「统一领域规则同时作为训练奖励项与运行时护栏」的设计，降低多链路规则维护成本

  - 小样本做Agent对齐（比如LoRA微调合规Agent）时，必须做多种子、多批次重复实验，不能轻信单跑结果，避免把随机方差当成策略效果

  - 可将「是否应该转人工」作为可标注的训练信号，用DPO等偏好优化方法训练Agent的转人工决策，替代生硬的人工阈值规则

  - Agent评估时可拆分三类可信度信号：程序可验证信号（格式合规、引用有效性）、任务级标签（是否转人工）、大模型打分信号，分别审计追溯，避免混淆问题来源'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent正大规模落地金融合规、医疗咨询等受监管高风险场景，现有对齐方法要么依赖手调的转人工阈值，鲁棒性差，要么缺乏可审计的可信度度量，小样本试点的评估结果经常不可靠，容易把随机波动当成策略效果，甚至引发合规风险。

### 方法关键点
- 核心将「是否应该转人工（escalate）」作为可标注的任务级信号，把Agent的有限自主性行为转化为可训练、可验证的RL优化目标，替代手调阈值
- 设计统一可插拔的领域宪法（如试点中16条英国FCA金融合规规则），同时承担两个角色：作为混合奖励的软项，和引用有效性、来源落地性、格式合规、转人工正确性4个硬可验证信号加权计算奖励；作为运行时确定性护栏，拦截无依据回答、强制触发转人工，全链路生成可审计日志
- 训练采用DPO+LoRA微调小参数开源模型，评估刻意拆分三类可信度信号，分别对应不同审计要求，避免混淆误差来源

### 关键实验
离线参考实验n=12，运行时护栏将弱基线的转人工召回从0提升到0.67，不安全行为率从0.33降到0.08；单GPU小样本试点（n=8）发现，完全相同的配置两次跑的结果差异极大：基础RL的任务成功率0.25 vs 0.12，转人工召回1.0 vs 0.5，相同DPO适配器的效果甚至完全反向，小样本下适配器效果无法和采样、硬件方差区分。

### 核心结论
在当前Agent小样本试点常用的样本量和训练预算下，有限自主性相关指标的噪声会完全淹没适配器的真实效果，负责任的评估必须做多种子、更大样本量的实验
