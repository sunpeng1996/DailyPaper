---
title: VibeVoice-ASR-Streaming Technical Report
title_zh: VibeVoice-ASR-Streaming 流式说话人归因ASR技术报告
authors:
- Yujie Tu
- Zhiliang Peng
- Jianwei Yu
- Li Dong
- Songchen Xu
- Yaoyao Chang
- Wenhui Wang
- Zilong Wang
- Zehua Wang
- Yan Xia
affiliations:
- Microsoft Research
- University of Chinese Academy of Sciences
- Shanghai Jiao Tong University
arxiv_id: '2609.02812'
url: https://arxiv.org/abs/2609.02812
pdf_url: https://arxiv.org/pdf/2609.02812
published: '2026-09-01'
collected: '2026-09-04'
category: LLM
direction: LLM 流式语音识别优化
tags:
- ASR
- Streaming Processing
- Speaker Diarization
- LLM
- Low Latency
one_liner: 首个基于LLM的端到端流式说话人归因ASR系统，低延迟下精度优于主流商用方案
practical_value: '- 电商语音导购Agent、直播内容理解类业务可直接复用开源的1.5B/7B权重，替代原有「ASR+说话人分镜」两阶段pipeline，大幅降低链路延迟

  - 流式输入多模态LLM架构可参考「固定大小分块+少量前瞻窗口+上文历史拼接」的范式，平衡实时性与输出精度

  - 客服语音质检、直播话术审核类场景可直接替换现有商用流式ASR方案，在降低转写错误率的同时自动实现说话人归因'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
传统说话人归因ASR将语音识别与说话人分镜拆为两个独立任务，现有端到端统一方案仅支持离线识别，无法满足实时语音助手、Agent的低延迟要求。
### 方法关键点
首个基于LLM的端到端流式说话人归因ASR架构，输入侧交错拼接固定大小音频块、少量前瞻音频、历史输出文本，无需独立分镜阶段，语音输入过程中即可实时输出「谁在说什么」。
### 关键结果
7B模型在5个测试集上取得最低平均WER/CER，13个说话人归因测试设置中12个取得最优或并列最优，效果优于Gemini 3.5 Transcribe Live、GPT Realtime Whisper等主流商用方案，已开源1.5B、7B权重与推理代码。
