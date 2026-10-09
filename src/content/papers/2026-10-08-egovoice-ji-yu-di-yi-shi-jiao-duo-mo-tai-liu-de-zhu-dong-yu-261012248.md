---
title: 'EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams'
title_zh: EgoVoice：基于第一视角多模态流的主动语音辅助框架
authors:
- Heeseung Kim
affiliations:
- Department of AI, University of Seoul
arxiv_id: '2610.12248'
url: https://arxiv.org/abs/2610.12248
pdf_url: https://arxiv.org/pdf/2610.12248
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: 多模态主动交互Agent 干预决策优化
tags:
- Egocentric Multimodal
- Proactive Agent
- Omni-modal LLM
- Direct Preference Optimization
- Spoken Assistant
one_liner: 面向第一视角多模态场景，提出主动语音辅助框架EgoVoice，用DPO优化干预时机与内容
practical_value: '- 电商直播/线下导购主动助手可复用「连续流是否干预+输出内容」联合建模思路，替代传统固定规则触发逻辑

  - 主动交互类Agent的行为优化可直接套用「监督微调+DPO偏好优化」两步范式，有效降低不合时宜的干预bad case

  - 多模态语音数据预处理阶段，采用声源分离+语音重合成方案，可大幅提升弱噪声场景下的语音信号识别准确率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有AR可穿戴语音助手均为被动响应模式，无法基于第一视角连续多模态流同时决策「何时主动干预」和「输出什么内容」，缺乏对应的训练与评估框架。
### 方法关键点
1. 基于HoloAssist真实人类讲师视频数据集，通过声源分离、语音重合成生成干净音频流，构造逐时刻判断「保持静默/输出引导语」的训练样本；2. 微调全模态LLM拟合任务逻辑，再通过直接偏好优化（DPO）对齐人类对主动干预的偏好。
### 关键结果
相比零样本基线模型，EgoVoice在干预时机准确率、内容相关性、人类偏好三个维度均实现显著提升，现有传统系统极少能输出时机合理、有价值的主动干预内容。
