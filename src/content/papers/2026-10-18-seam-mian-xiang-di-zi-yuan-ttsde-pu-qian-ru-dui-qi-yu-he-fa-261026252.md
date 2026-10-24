---
title: 'SEAM: Spectral Embedding Alignment and Merging for Low-Resource TTS'
title_zh: SEAM：面向低资源TTS的谱嵌入对齐与合并方法
authors:
- Walaa Othman
- Baher Mohammad
- Stamatios Lefkimmiatis
- Ammar Ali
affiliations:
- ITMO University
- SPC RAS
- MWS AI
arxiv_id: '2610.26252'
url: https://arxiv.org/abs/2610.26252
pdf_url: https://arxiv.org/pdf/2610.26252
published: '2026-10-18'
collected: '2026-10-24'
category: Other
direction: 低资源语音合成 · 词表扩展优化
tags:
- TTS
- Low-Resource
- Embedding Alignment
- Spectral Filter
- Cross-Lingual
one_liner: 提出无音频初始化的SEAM方法，大幅降低低资源TTS词表扩展的训练数据需求
practical_value: '- Agent 语音交互模块落地时，小语种/垂直领域专有名词的 TTS 词表扩展可复用 SEAM 零音频初始化思路，大幅降低配对音频标注成本

  - 跨模态推荐、语音广告生成场景下，可复用「谱滤波保留序列结构+闭式岭回归对齐预训练流形」的 trick，降低75%样本需求

  - 小语种市场业务扩张时，可直接集成 SEAM 到现有 TTS 管线，快速适配新语言的语音输出能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
低资源/跨语言场景下 TTS 词表扩展依赖大量配对音频微调，是 Agent 全球部署语音交互、多模态内容生成的核心瓶颈，现有随机初始化、均值池化方案忽略序列结构，样本效率极低。
### 方法关键点
1. 零音频初始化架构，直接从已知子 token 构造未知 token 的 embedding，无需任何目标场景音频数据
2. 引入谱滤波处理子 token 序列，保留语音时序 phonetic 结构，解决标准池化丢失序列信息的问题
3. 用闭式岭回归将新生成的 embedding 对齐到预训练条件流形，无需额外训练开销
### 关键结果
跨 3 种语言、2 种 TTS 架构测试，SEAM 仅需基线方案 1/4 训练数据即可达到相当性能，相比随机初始化/均值池化方案样本复杂度降低 75%，轻量化易复现
