---
title: 'Timeline-Bench: Evaluating Agents on Realistic Video-Editing Tasks, from Raw
  Footage to Final Cut'
title_zh: Timeline-Bench：面向真实视频编辑全流程的Agent评测基准
authors:
- Gunin Gupta
- Nirmit Arora
- Pavan Kalyan Tankala
affiliations:
- TensorTest (Ritivel Labs Inc.)
arxiv_id: '2609.35143'
url: https://arxiv.org/abs/2609.35143
pdf_url: https://arxiv.org/pdf/2609.35143
published: '2026-09-28'
collected: '2026-10-04'
category: Eval
direction: Agent长周期创意任务评测
tags:
- Agent
- Benchmark
- Long-Horizon Task
- Video Editing
- Evaluation
one_liner: 构建含56个真实视频编辑任务的基准，量化前沿Agent在长周期创意任务的性能
practical_value: '- 做电商短视频生成类Agent时，可复用「规则校验+人工校准质量评估」的两阶段评测框架，避免仅考核格式合规忽略创意质量

  - 长周期工具调用类Agent的评测可参考「任务分层+交付物全链路校验」设计思路，覆盖从输入素材到最终产出的全流程

  - 当前前沿Agent在创意类任务上达标率不足30%，落地电商短视频生成等场景时需加入人工复审环节，不可完全端到端依赖Agent'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前面向长周期专业任务的Agent评测普遍不要求产出完整可交付的创意成果，缺乏贴近真实产业场景的标准化评测范式。
### 方法关键点
1. 构建Timeline-Bench基准，包含56个真实视频编辑任务，覆盖访谈剪辑、广告剪片等场景，每个任务配套需求说明、原始素材、工程容器与多维度校验规则
2. 评测采用「硬性规则校验+专业人工校准质量评估」双路径，覆盖格式合规、内容匹配、需求满足三类刚性指标，质量评估基于43位专业剪辑师的2582次盲评结果校准
3. 测试16款搭配Codex、Claude Code等代码Agent框架的前沿大模型Agent
### 关键结果
最优GPT-6 Astra Agent任务通过率仅26.8%，平均通过率为14.0%；83.5%的盲评中人类剪辑师更偏好人工参考成片，72.9%的失败案例仅未通过质量校验，Agent普遍缺乏创意打磨能力。
