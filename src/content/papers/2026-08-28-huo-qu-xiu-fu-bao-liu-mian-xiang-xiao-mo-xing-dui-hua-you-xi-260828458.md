---
title: 'Acquire, Repair, Preserve: A Diagnosis-Guided Post-Training Recipe for Small-Model
  Dialogue Game Agents'
title_zh: 获取-修复-保留：面向小模型对话游戏Agent的诊断引导后训练方案
authors:
- Nan Li
affiliations:
- Utrecht University
arxiv_id: '2608.28458'
url: https://arxiv.org/abs/2608.28458
pdf_url: https://arxiv.org/pdf/2608.28458
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: 对话Agent 小模型后训练优化
tags:
- Small LLM
- Agent Training
- DPO
- LoRA
- Post-Training
- Interactive Agent
one_liner: 提出诊断引导的三阶段后训练范式，保留通用能力的同时大幅提升小模型对话Agent交互性能
practical_value: '- 针对交互式Agent（如电商导购Agent、游戏化营销对话Agent）的故障修复，可复用「先诊断可机械校验的局部错误，再构造turn-local
  DPO偏好对」的方案，比全对话DPO效果更稳定，不会破坏原有协议合规性

  - 小模型垂类优化后需保留通用能力时，可直接使用LoRA delta缩放trick：$W(s) = W_{base} + s \times \Delta_{LoRA}$，通过调整$s$在专项能力和通用能力间做无训练成本的tradeoff，适配电商场景既要垂类效果又要基础指令遵循的需求

  - 小模型Agent训练的阶段优先级：先做全量SFT拉满场景参与度（对应推荐系统的召回兜底），再针对bad case做定向修复，比直接上偏好优化的ROI更高，适配业务先拉基线再迭代优化的节奏'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
小模型部署成本低、推理延迟低，是端侧/低资源交互Agent的首选方案，但在对话游戏、电商导购等交互式任务中，容易出现重复输出、违反实时反馈约束、格式错误等局部决策问题，传统全对话微调容易破坏模型原有通用能力和协议合规性，需要更精准的后训练范式。

### 方法关键点
- 三阶段后训练流程：①Acquire：全场景成功交互样本SFT，先解决模型无法参与任务的问题，提升交互完成率；②Repair：诊断出可机械校验的局部错误（如重复猜测、长度错误），构造相同对话上下文下的正负偏好对做turn-local DPO，定向修复错误不影响其他行为；③Preserve：训练后对LoRA权重做delta缩放，通过调整缩放系数$s$在交互性能和通用能力间找到最优平衡点，无额外训练成本。
- 对比全对话DPO，turn-local偏好对仅在错误发生的单轮做对比，不会破坏其他轮次的行为逻辑，避免协议合规性下降。

### 关键结果
基于Qwen3.5-2B模型在LM Playschool Challenge基准测试：公开clemscore从10.67提升到38.92，闭域内分数从13.41提升到41.17，超过官方4B、9B基线；通用静态得分Statscore仅从44.24降到44.14，几乎无损失；域外clemscore仅从3.72提升到7.88，增益集中在同类型任务变体上。

**最值得记住的一句话**：小模型交互式Agent优化的最高ROI路径是「先拉宽场景覆盖基线，再定向修复可明确校验的局部错误，最后做权重空间的能力平衡」，盲目全量偏好优化反而容易破坏原有能力。
