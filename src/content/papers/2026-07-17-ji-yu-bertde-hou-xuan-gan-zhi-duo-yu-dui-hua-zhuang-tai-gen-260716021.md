---
title: Candidate Attended Dialogue State Tracking Using BERT
title_zh: 基于BERT的候选感知多域对话状态跟踪方法
authors:
- Junyuan Zheng
- Onkar Salvi
- John Chan
affiliations:
- OneConnect US Research Institute
arxiv_id: '2607.16021'
url: https://arxiv.org/abs/2607.16021
pdf_url: https://arxiv.org/pdf/2607.16021
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: 对话Agent · 对话状态跟踪优化
tags:
- BERT
- Dialogue State Tracking
- Zero-shot Learning
- Multi-domain Dialogue
- Task-oriented Agent
one_liner: 提出基于BERT的候选感知多域对话状态跟踪框架，支持零样本泛化，在SGD数据集上显著优于基线
practical_value: '- 电商智能客服/导购类任务型Agent可复用预训练BERT做DST的思路，新业务域无需额外训练即可快速适配，降低冷启动成本

  - 零样本泛化的DST设计可迁移至多域对话意图识别、槽位填充场景，大幅减少小样本服务域的数据标注量

  - 候选感知的匹配逻辑可复用至推荐系统实时用户意图更新模块，基于交互历史动态修正用户偏好表征'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
任务导向对话系统的Dialogue State Tracking（DST）是上游核心模块，直接决定下游动作预测与回复生成的准确率。随着语音助手、智能客服等应用覆盖的服务域快速扩张，现有DST方案新增服务域时需要大量标注数据重新训练，扩展性差，无法满足低资源/零资源新域的快速上线需求。
### 方法关键点
1. 基于预训练BERT构建可扩展多域DST框架，引入候选感知机制关联对话上下文与槽位候选值，提升状态识别准确率；
2. 依托BERT的通用语义表征能力实现零样本泛化，新增业务域无需额外训练即可直接适配。
### 关键结果
在公开SGD（Schema-Guided Dialogue）数据集上测评，性能较此前基线实现显著提升，无额外训练开销即可支撑新域的对话状态跟踪任务。
