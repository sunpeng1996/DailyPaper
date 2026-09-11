---
title: 'RetroThinker: Enabling Retrospective Thinking in Speech LLMs'
title_zh: RetroThinker：为语音大模型赋予回溯推理能力
authors:
- Yi-Jen Shih
- Puyuan Peng
- Abdelrahman Mohamed
- David Harwath
affiliations:
- The University of Texas at Austin
- FAIR, Meta Superintelligence Labs
arxiv_id: '2609.11864'
url: https://arxiv.org/abs/2609.11864
pdf_url: https://arxiv.org/pdf/2609.11864
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: 语音大模型 · 推理效率优化
tags:
- SpeechLLM
- Chain-of-Thought
- DPO
- SFT
- Reasoning
one_liner: 提出多阶段后训练框架RetroThinker，优化语音大模型推理精度-延迟权衡，同延迟下GSM8K精度绝对提升11%
practical_value: '- 可借鉴SFT+定制化DPO的多阶段后训练范式，优化实时语音交互类Agent（如语音导购、智能客服）的精度-延迟权衡，在不提升响应
  latency 的前提下提升任务准确率

  - 可复用动态修正CoT推理轨迹的设计思路，在推荐理由生成、搜索query联想、直播话术生成等流式响应场景中，边接收用户输入边迭代修正输出内容，降低用户等待时长

  - 基于长度约束的DPO偏好优化目标可直接迁移到所有低延迟要求的生成任务，通过偏好对齐在推理阶段自然控制生成长度，避免冗余内容带来的延迟升高'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
SpeechLLM相比级联ASR+文本LLM架构延迟更低、可保留语音副语言信息，但复杂推理能力显著弱于纯文本LLM，同时实时语音交互对延迟有严苛要求，现有CoT、并发推理方案仍无法解决固有的精度-延迟权衡问题。
## 方法关键点
提出RetroThinker多阶段后训练框架，让Moshi语音大模型支持推理过程中的自验证与CoT步骤前向修正：首先在人工构造的回溯推理数据集上做SFT，再引入基于长度的DPO优化用户说话阶段的并发早期推理效果，无需修改模型架构即可生效。
## 关键结果
在GSM8K数学推理基准上相比无回溯基线大幅优化精度-延迟权衡，同等延迟条件下实现11%的绝对精度提升。
