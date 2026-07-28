---
title: 'Interactive Training 2: Auditable Control Plane for Live Model Training'
title_zh: Interactive Training 2：面向在线模型训练的可审计控制平面
authors:
- Wentao Zhang
- Xuanhe Pan
- Han Zhou
- Yang Lu
- Yuntian Deng
affiliations:
- University of Waterloo
- University of Wisconsin-Madison
arxiv_id: '2607.18314'
url: https://arxiv.org/abs/2607.18314
pdf_url: https://arxiv.org/pdf/2607.18314
published: '2026-07-16'
collected: '2026-07-28'
category: Training
direction: 模型训练 · 可审计Agent引导训练工具
tags:
- Model Training
- Control Plane
- Auditable Training
- Agent-guided Training
- Open Source Tool
one_liner: 提出开源可审计的在线训练通用控制平面，支持人与Agent通过统一协议安全干预训练流程
practical_value: '- 微调LLM4Rec/电商Agent模型时可复用这套控制协议，实现Agent自动干预训练（如动态调参、早停），降低人工值守成本

  - 合规要求高的广告/推荐模型训练场景，可直接复用带全链路操作日志的控制框架，满足训练过程可溯源的审计需求

  - 推荐模型在线迭代训练场景，可基于这套通用接口自定义可调控参数/动作，无需重复编写专属回调逻辑'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有实验追踪工具仅支持监控训练进度，无通用化的在线训练干预能力，不同训练任务需定制专属回调代码，工具碎片化严重，无法支撑人/Agent自动引导训练的可审计需求。
### 方法关键点
1. 定义统一交互协议，训练任务主动声明可暴露的可调参数（如学习率）与可执行动作（如保存checkpoint、启动评估）；
2. 人/自动化控制器/LLM Agent通过统一接口提交请求，训练循环在预设安全控制点完成请求校验、执行并记录结果；
3. 定制Aim工作空间，整合实时指标、控制操作、请求与结果的时序全链路记录，满足审计溯源要求。
### 关键结果
在5个NLP、强化学习工作流上验证了系统可行性，开源代码与训练轨迹可直接复用为可审计的人/Agent引导训练的基础框架。
