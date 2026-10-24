---
title: 'MixiSpeech: Progressive State Distillation for One-Step Vietnamese TTS'
title_zh: MixiSpeech：面向单步越南语TTS的渐进式状态蒸馏方法
authors:
- Tran Quoc Bao Le
- Binh Mai
- Hung Dinh
- Lam Nguyen
- Cong Tran
affiliations:
- Posts and Telecommunications Institute of Technology, Hanoi, Vietnam
arxiv_id: '2610.25394'
url: https://arxiv.org/abs/2610.25394
pdf_url: https://arxiv.org/pdf/2610.25394
published: '2026-10-18'
collected: '2026-10-24'
category: Other
direction: 单步TTS优化 · 知识蒸馏
tags:
- Text-to-Speech
- Knowledge Distillation
- Conditional Flow Matching
- One-step Inference
one_liner: 提出渐进式状态蒸馏框架，将多步条件流TTS压缩为单步模型，质量损失极小且提速2.12倍
practical_value: '- 多步生成模型压缩为单步的10→4→2→1课程式蒸馏策略可直接复用在生成式推荐场景，如文案、海报生成的扩散/流模型推理提速

  - masked state-matching蒸馏目标可迁移到各类多步生成大模型的蒸馏任务，在保留生成质量的前提下降低推理延迟

  - 电商智能客服、直播语音助手等端侧语音交互场景的TTS落地可直接参考该框架，2倍提速几乎无感知质量损失'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
条件流TTS模型只需少次采样即可实现高合成质量，但直接压缩为单步推理会出现严重的质量下降，无法落地低延迟交互场景。

### 方法关键点
提出渐进式状态蒸馏框架MixiSpeech，不直接训练单步模型，而是采用10→4→2→1的课程式蒸馏策略逐步降低采样步数，每轮学生模型通过masked状态匹配目标拟合教师模型的局部集成端点，蒸馏过程保留原模型架构与说话人条件能力。

### 关键结果数字
在710说话人越南语TTS任务上，蒸馏后的单步模型UTMOS22-Strong得分2.2678（10步教师为2.2923，直接单步推理仅为1.6846），WER 4.63%（教师为4.65%，直接单步为6.21%），CER 2.83%；端到端推理延迟从0.0662s降至0.0312s，实现2.12倍提速，几乎无感知质量损失。
