---
title: Reference-Free Post-Training of Open Large Language Models for Multilingual
  Machine Translation
title_zh: 面向多语言机器翻译的开放大模型无参考后训练方法
authors:
- Chris Han
- Pengzhi Gao
- Pei Fu
- Jian Luan
affiliations:
- Xiaomi Inc.
arxiv_id: '2608.10812'
url: https://arxiv.org/abs/2608.10812
pdf_url: https://arxiv.org/pdf/2608.10812
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: 大模型后训练 · 多语种翻译优化
tags:
- LLM
- Post-Training
- GRPO
- Reinforcement Learning
- Multilingual Translation
one_liner: 采用无参考GRPO训练+SFT/RL checkpoint插值，实现46语种翻译性能超越多类开源及商用基线
practical_value: '- 跨境电商多语种文案/评论翻译场景可直接复用无参考GRPO训练框架，无需标注平行语料即可优化翻译效果

  - 大模型SFT后做RL专项优化时，可尝试SFT与RL checkpoint线性插值的trick，平衡基础通用能力与专项优化目标

  - 低资源语种生成任务可借鉴语言识别门控的奖励设计，避免非目标语种输出的无效奖励干扰训练'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有多语种翻译SFT受限于高质量平行语料稀缺，低资源语种覆盖不足，而源端单语文本易得，无参考训练可充分挖掘这类数据价值。
### 方法关键点
1. 基于MiLMMT-46-v0.1 SFT模型，采用GRPO强化学习训练，奖励为两个无参考质量评估模型输出的均值，新增语言识别门控过滤无效输出；
2. 训练后对SFT与RL checkpoint做线性插值，得到最终模型MiLMMT-46-v1.0。
### 关键结果
46语种上翻译效果全面优于原SFT模型，超过Seed-X、HY-MT2、TranslateGemma等开源基线，无参考评分领先Google翻译、Gemini 3 Pro、GPT-5等商用系统；on-policy蒸馏效果仅能追平RL插值方案，无法超越。
