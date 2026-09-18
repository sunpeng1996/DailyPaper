---
title: Multi-Dimensional Prosody Judgment For Live Streaming Speech Synthesis
title_zh: 面向直播场景语音合成的多维韵律评判方法
authors:
- Zifan Guan
- Longyu Lu
- Junan Zhang
- Zhizheng Wu
- Meiguang Jin
- Junfeng Ma
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- TaoLive-AIGC Team, Taobao & Tmall Group of Alibaba
arxiv_id: '2609.20124'
url: https://arxiv.org/abs/2609.20124
pdf_url: https://arxiv.org/pdf/2609.20124
published: '2026-09-17'
collected: '2026-09-18'
category: Eval
direction: 多模态评估 · 语音合成韵律打分
tags:
- TTS
- Reward Model
- LLM Distillation
- GRPO
- LoRA
- Prosody Evaluation
one_liner: 从专有大模型蒸馏低成本直播TTS多维韵律评估器，解决多维度评分耦合问题
practical_value: '- 电商多维度内容评估（如直播话术、商品文案的吸引力/可信度/卖点清晰度打分）可复用解耦思路：移除总评分目标，避免模型偷懒将所有维度评分对齐整体偏好，得到可指导优化的细粒度结果

  - 从GPT/Gemini等专有大模型蒸馏轻量业务评估器时，可采用swap-consistent蒸馏+顺序平衡训练，大幅降低评估结果的位置偏差，比普通蒸馏效果更稳定

  - 多维度RLHF优化内容生成时，可复用span-local GRPO思路：将每个维度的奖励只作用到对应生成段落，避免不同维度奖励抵消，提升细粒度反馈的准确性

  - 电商直播TTS话术生成场景可直接复用7维度韵律评估框架，低成本筛选更符合带货氛围的合成语音，提升用户停留和转化'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
直播场景TTS需要评估流畅度、语调、情感、带货表现力等细粒度韵律特征，传统MOS预测器无法捕捉这类复杂表达特征；Gemini等专有大模型虽然能实现细粒度评估，但推理成本过高，无法支撑大规模TTS迭代和RLHF优化；同时现有多维度评估存在严重的判决耦合问题，模型会偷懒让所有维度评分对齐整体偏好，浪费细维度标注的价值。

### 方法关键点
- 蒸馏Gemini的评估能力到Qwen3-Omni，得到基础评估器LPJ，定义7维度韵律评估规则：4个核心全量维度（流畅度、语调、情感、直播表现力）+3个文本触发维度（信息强调、情绪切换、交互模式切换）
- 针对判决耦合问题提出D-LPJ：移除整体判决目标，SFT阶段屏蔽不确定的样本-维度对而非直接丢弃整个样本；提出span-local GRPO策略，每个维度的归一化优势只作用到对应理由的token span，避免跨维度奖励抵消
- 训练采用swap-consistent蒸馏，每个样本正反序各判一次，只保留高一致的标注，结合课程学习提升模型泛化性

### 关键结果
- 10样本平衡顺序推理的LPJ准确率超过单轮Gemini调用，位置偏差极低：对比SpeechJudge-GRM的66.8%偏B胜率，LPJ仅0.7%
- D-LPJ在4个核心维度的 pooled 准确率达86.10%，24.3%~60.6%的样本会输出不同维度的独立判决，完全避免评分耦合问题
- 8候选TTS选优场景下，LPJ选中的语音在高置信case里有85.29%进入人工Top3，远高于随机37.5%的基线

多维度细粒度评估的核心瓶颈不是标注量，而是如何避免模型偷懒用整体偏好替代独立维度判断，解耦监督目标和奖励分配是关键。
