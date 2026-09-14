---
title: 'TART: A Modular Tool for Technique-Aware Audio-to-Tablature Guitar Transcription'
title_zh: TART：支持演奏技法感知的模块化吉他音频转六线谱工具
authors:
- Akshaj Gupta
- Hwi Joo Park
- Andrea Guzman
- Shamak Gowda
- Samhita Konduri
- Jiachen Lian
- Robin Netzorg
- Gopala Anumanchipalli
affiliations:
- University of California, Berkeley
arxiv_id: '2609.11904'
url: https://arxiv.org/abs/2609.11904
pdf_url: https://arxiv.org/pdf/2609.11904
published: '2026-09-10'
collected: '2026-09-14'
category: Other
direction: 多模态音频转写 · 结构化符号生成
tags:
- Audio_Processing
- Multimodal
- Modular_Pipeline
- T5
- Zero_Shot
one_liner: 提出四阶段模块化吉他音频转谱框架，可同时生成指法与演奏技法标注
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
吉他自动转谱存在三大核心痛点：无法捕捉滑音、推弦、打击音等表现力演奏技法，弦-品组合分配错误率高，仅在干净录音上训练导致真实场景泛化性差。

### 方法关键点
采用四阶段模块化pipeline：1. 音频转MIDI基础转录模型；2. 表现力演奏技法分类器；3. 音频条件增强的T5编解码器实现弦-品匹配；4. 自动化六线谱生成器，支持零样本推理。

### 关键结果数字
在GuitarSet、EGDB及两个加噪增强基准上平均效果：音频转MIDI F50达81.35%，超此前最优基线6.67个点；弦-品匹配Tab F1达71.8%，超此前最优基线8.5个点；端到端转谱Tab F1达54.08%，是首个可直接从音频生成同时带指法与演奏技法标注吉他六线谱的框架。
