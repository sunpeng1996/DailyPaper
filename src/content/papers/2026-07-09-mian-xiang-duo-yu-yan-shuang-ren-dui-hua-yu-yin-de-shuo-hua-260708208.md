---
title: Diarization-Guided Qwen-ASR Adaptation for Multilingual Two-Speaker Conversational
  Speech
title_zh: 面向多语言双人对话语音的说话人分割引导Qwen-ASR适配方法
authors:
- Hao Wu
- RongQi Han
- Zhen Wang
- Wei Liang
- Wei Xu
affiliations:
- Shanghai Qi Zhi Institute
- Megatronix (Beijing) Technology Co., Ltd
arxiv_id: '2607.08208'
url: https://arxiv.org/abs/2607.08208
pdf_url: https://arxiv.org/pdf/2607.08208
published: '2026-07-09'
collected: '2026-07-10'
category: Other
direction: 多语言语音识别 · 说话人分割+大模型微调
tags:
- ASR
- Speaker Diarization
- LoRA
- TTS Augmentation
- GRPO
one_liner: 结合模块化说话人分割前端与多阶段微调Qwen3-ASR-1.7B，大幅提升多语言双人对话语音识别效果
practical_value: '- 电商客服/直播语音转写场景可复用「说话人分割前端+ASR微调」的串联架构，先区分说话人再做转写降低错误率

  - 垂直场景ASR适配可复用三阶段微调范式：先全参数有监督微调、再用TTS合成数据做LoRA微调、最后GRPO强化学习校准幻觉重复等问题

  - 强化学习优化ASR时可借鉴WER/CER为正奖励、幻觉/重复/长度偏差为负惩罚的reward设计'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
多语言双人对话语音转写面临短轮次、语音重叠、说话人切换频繁、21种语言/地区拼写差异大的痛点，单独优化说话人分割或ASR易出现错误传导，通用Qwen-ASR效果无法满足精度要求。
### 方法关键点
1. 前端采用模块化说话人分割pipeline：VAD→子段生成→CAMPPlus说话人嵌入提取→双人谱聚类→RTTM音频分割，输出带说话人属性的音频段；
2. ASR采用三阶段适配：先基于官方训练数据全参数有监督微调，再用三路TTS合成语音数据做LoRA微调，最后引入GRPO强化学习优化，奖励基于WER/CER，同时对幻觉、重复、长度偏差做负惩罚。
### 关键结果
开发集平均tcpMER为23.70，较原生Qwen-ASR-1.7B绝对降错6.83个百分点；最终测试集平均tcpMER达17.97；消融实验显示有监督微调增益最大，合成数据LoRA、强化学习可进一步提升鲁棒性。
