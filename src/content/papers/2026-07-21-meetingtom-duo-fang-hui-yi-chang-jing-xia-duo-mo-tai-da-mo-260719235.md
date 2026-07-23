---
title: 'MeetingToM: Evaluating Multimodal LLMs on Theory-of-Mind Reasoning in Multi-Party
  Meetings'
title_zh: MeetingToM：多方会议场景下多模态大模型心理理论推理能力评测基准
authors:
- Ziyi Wang
- Yuhang Wu
- Dongxu Piao
- Xingyu Liu
- Tianhui Zhou
- Miao Liu
affiliations:
- Tsinghua University
- Duke University
arxiv_id: '2607.19235'
url: https://arxiv.org/abs/2607.19235
pdf_url: https://arxiv.org/pdf/2607.19235
published: '2026-07-21'
collected: '2026-07-23'
category: Eval
direction: 多模态大模型 · 心理理论推理评测
tags:
- Multimodal-LLM
- Theory-of-Mind
- Evaluation-Benchmark
- Multi-party-Meeting
- Reasoning
one_liner: 构建覆盖多方会议分层心理理论推理的多模态大模型专用评测基准MeetingToM
practical_value: '- 开发办公Agent、智能会议助手的团队可直接复用MeetingToM的分层评测框架，测试模型的社交意图推理能力，优化参会人状态感知、会议决策辅助功能

  - 做电商直播场控Agent、多轮客服Agent的团队可参考其个体-双人-群体三层拆解社交推理任务的思路，提升用户隐藏态度、群体共识判断的准确率

  - 做用户隐性意图建模的推荐团队可借鉴其潜社交状态的标注逻辑，补充用户非言语信号（如浏览停留、点击犹豫）与显式反馈的融合特征'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有多模态ToM评测基准仅聚焦显式可验证信号的视频问答，对多方会议场景下的潜社交状态、群体动态覆盖不足，无法支撑社交交互类AI的能力评估。
### 方法关键点
构建MeetingToM基准，覆盖会议特有伪共识等特殊社交现象，分层设计三级评测任务：①个体层心理状态预测 ②双人层发言受众理解 ③群体层共识推理，配套统一评测协议。
### 关键结果
对主流代表性MLLM的系统测试显示，现有模型在非言语线索融合、隐藏态度推断、真伪共识区分三类任务上均存在明显性能缺陷，三类任务平均准确率普遍低于60%，暂无模型能覆盖全场景的ToM推理需求。
