---
title: Human-Likeness and Conversational Preference Diverge for Synthesized Agent
  Speech in Customer-Service Calls
title_zh: 客服场景合成智能体语音的拟人度与用户对话偏好差异研究
authors:
- Jeffrey M. Girard
- Antony D'Avirro
- Jason Z. Zheng
- Jacqueline R. Vertino
- Benjamin Peloquin
affiliations:
- Fluid Concepts Research, San Francisco, USA
arxiv_id: '2611.16051'
url: https://arxiv.org/abs/2611.16051
pdf_url: https://arxiv.org/pdf/2611.16051
published: '2026-11-11'
collected: '2026-11-14'
category: Agent
direction: 语音Agent · 用户偏好评测
tags:
- Speech Agent
- Conversational Preference
- Perceptual Evaluation
- TTS
- Customer Service
one_liner: 发现客服场景下语音智能体的拟人度与用户对话偏好存在偏差，明确现有单维度评测的缺陷
practical_value: '- 搭建电商/客服语音Agent时，不要仅以拟人度为优化目标，需单独新增用户对话偏好评测项，优先选择语速快、分句停顿少、音调变化丰富的音色

  - 选型TTS系统时不能仅测试单款音色，同系统不同音色的效果差异可达系统间差异的75%，需覆盖多款音色做AB测试

  - 现有自动自然度评分无法有效预测对话偏好，线上语音类Agent的效果验证必须补充真人成对选择测试'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有语音Agent评测大多仅关注拟人度，极少衡量用户实际对话偏好，二者关联关系不明确，易导致优化方向偏离用户真实需求。
### 方法关键点
基于120组客服即兴话术做成对选择测试，Study1对比6款商用TTS系统的48款音色，Study2对比真人录音与TTS合成效果，分别统计拟人度、对话偏好两个维度的用户选择结果。
### 关键结果数字
1. 36%测试中用户偏好TTS合成音超过真人，最优TTS的偏好占比达49%，而拟人度维度仅19%测试中TTS超过真人；
2. 同TTS系统内不同音色的效果差异达系统间差异的75%；
3. 现有3种自动自然度评分均无法预测对话偏好，用户更偏好语速快、分句停顿少的语音，对话偏好额外要求更多音调变化。
