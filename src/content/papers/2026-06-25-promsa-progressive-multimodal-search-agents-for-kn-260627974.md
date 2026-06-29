---
title: ProMSA:Progressive Multimodal Search Agents for Knowledge-Based Visual Question
  Answering
title_zh: ProMSA:Progressive Multimodal Search Agents for Kn
authors:
- ZhengXian Wu
- Hangrui Xu
- Kai Shi
- Zhuohong Chen
- Yunyao Yu
- Chuanrui Zhang
- Zirui Liao
- Jun Yang
- Zhenyu Yang
- Haonan Lu
arxiv_id: '2606.27974'
url: https://arxiv.org/abs/2606.27974
pdf_url: https://arxiv.org/pdf/2606.27974
published: '2026-06-25'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Knowledge-based Visual Question Answering (KB-VQA) requires models to combine
  image understandi...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: huggingface-daily
depth: abstract
---

### 摘要

Knowledge-based Visual Question Answering (KB-VQA) requires models to combine image understanding with external knowledge. Most prior methods use a fixed retrieve-then-generate pipeline with a pre-selected retriever and a static top-k setting, which is not adaptive during reasoning. We propose ProMSA, a progressive multimodal search agent for KB-VQA. Given an image-question pair, the agent iteratively chooses image search, text search, or stop, under explicit tool-call budgets and with deduplication to avoid redundant retrieval. For training, we first use rejection-sampling SFT to learn valid tool-use formats, then optimize the agent with TN-GSPO, a sequence-level RL objective that normalizes updates by both generation length and tool-interaction depth. Experiments on E-VQA and InfoSeek show consistent gains over strong RAG and agent baselines, and improved retrieval and end-to-end accuracy. The code is available at https://github.com/DingWu1021/Promsa.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
