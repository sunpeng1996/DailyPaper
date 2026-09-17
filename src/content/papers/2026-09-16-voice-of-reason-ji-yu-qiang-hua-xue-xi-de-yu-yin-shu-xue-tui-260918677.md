---
title: 'Voice of Reason: Reinforcement Learning for Spoken Math'
title_zh: Voice of Reason：基于强化学习的语音数学推理优化方案
authors:
- Timothée Weisselberger
- Edouard Graves
- Alexandre Défossez
affiliations:
- Kyutai
- Gradium
arxiv_id: '2609.18677'
url: https://arxiv.org/abs/2609.18677
pdf_url: https://arxiv.org/pdf/2609.18677
published: '2026-09-16'
collected: '2026-09-17'
category: LLM
direction: 语音大模型 · RL微调推理优化
tags:
- Speech-LLM
- Reinforcement Learning
- Mathematical Reasoning
- Supervised Fine-tuning
- GLM-4-Voice
one_liner: 对GLM-4-Voice做SFT+RL微调，无需额外推理token即可将语音数学推理精度提至SOTA
practical_value: '- 电商语音导购、语音客服类Agent可复用「合成领域问答数据SFT + 可验证奖励RL微调」的两阶段范式，提升垂直领域语音交互的推理准确率，减少幻觉

  - 无需新增推理token的RL优化方案可降低端侧语音模型推理 overhead，适配低延迟实时语音交互场景（如语音搜索应答、实时客服对话）

  - RL微调+流式推理的组合优化思路可直接迁移到实时语音类搜索/推荐交互场景的模型迭代，兼顾精度与延迟要求'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
端到端语音大模型相较级联ASR+文本大模型+TTS方案延迟更低、可利用副语言信息，但数学推理精度远低于同级别文本大模型，现有优化方案依赖额外推理标记，推理开销高。
### 方法关键点
1. 先基于合成的口语化数学问答数据对GLM-4-Voice做领域适配SFT；
2. 引入带可验证奖励的RL微调，无需新增推理token即可优化模型推理逻辑，减少幻觉；
3. 结合现有流式推理技术进一步提升实时推理效果。
### 关键结果
在GSM8K基准上，RL微调后的精度超过此前所有仅依赖补充推理轨迹的语音模型，结合流式推理后自由格式回答准确率达74.8%，为原生语音模型数学推理能力SOTA。
