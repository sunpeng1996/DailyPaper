---
title: Leading-Silence Augmentation and Multi-Stage Synthetic Supervision for the
  Second MLC-SLM Challenge
title_zh: 第二届MLC-SLM挑战赛的前置静音增强与多阶段合成监督方案
authors:
- Kexin Shi
- Renhe Sun
- Yuge Huang
- Ximeng Wang
- Jiayi Zhou
- Jian Liu
- Malu Zhang
affiliations:
- Ant Group
- UESTC
arxiv_id: '2608.14150'
url: https://arxiv.org/abs/2608.14150
pdf_url: https://arxiv.org/pdf/2608.14150
published: '2026-08-14'
collected: '2026-08-17'
category: Other
direction: 多语种对话语音优化 · 竞赛方案
tags:
- SpeechRecognition
- SpokenLanguageUnderstanding
- DataAugmentation
- SyntheticSupervision
- EMA
one_liner: 针对第二届MLC-SLM挑战赛双任务提出定制优化策略，显著提升语音识别与口语理解性能
practical_value: '- 智能客服/语音交互类Agent的ASR模块可复用随机前置静音裁剪+时间戳校正trick，降低长语音输入的识别误差

  - 缺少标注训练数据的下游任务，可借鉴多模态候选生成+分布匹配增强的合成监督方案，低成本扩增高质量训练集

  - 大模型微调场景可直接复用EMA训练策略，无需改动推理逻辑即可稳定提升下游任务表现'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
第二届MLC-SLM挑战赛面向无分段多语种对话设置两类任务，均不提供真值语句边界与说话人标签，其中Task2无官方问答训练集，仅提供少量开发样例，现有baseline效果不足。

### 方法关键点
Task1基于VibeVoice-ASR-7B微调，引入随机前置静音裁剪、一致时间戳校正、EMA训练策略三类优化；Task2通过多模态候选生成、静音音频过滤、分布匹配增强pipeline构造合成问答对，基于Qwen3-Omni-30B-A3B-Instruct微调实现带标签直接回答。

### 关键结果
Task1验证集上，静音裁剪将tcpMER从18.30%降至17.27%，叠加EMA策略进一步降至16.73%；Task2验证集上，分布匹配增强+带标签直接回答联合应用将准确率从83.0%提升至86.0%
