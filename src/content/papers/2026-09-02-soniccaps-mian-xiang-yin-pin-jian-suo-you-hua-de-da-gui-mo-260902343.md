---
title: 'SonicCaps: Large-Scale Diverse and Fine-Grained Captioning for Improved Audio-Retrieval'
title_zh: SonicCaps：面向音频检索优化的大规模多样化细粒度字幕数据集
authors:
- Zineb Lahrichi
- Marc Ferras
- Gaël Richard
- Geoffroy Peeters
affiliations:
- Sony CTC, France
- LTCI, Telecom Paris, Institut polytechnique de Paris, France
arxiv_id: '2609.02343'
url: https://arxiv.org/abs/2609.02343
pdf_url: https://arxiv.org/pdf/2609.02343
published: '2026-09-02'
collected: '2026-09-05'
category: Multimodal
direction: 多模态音频·文本检索数据集构建
tags:
- Audio Captioning
- Audio Retrieval
- Multimodal Dataset
- CLAP
- Prompt Engineering
one_liner: 构建含1500万条多粒度标注的音频字幕数据集，优化音频检索与零样本分类效果
practical_value: '- 短视频/直播电商的音频内容检索场景，可复用单样本多字幕标注策略，用结构化prompt生成不同粒度、风格的语义标签，大幅降低人工标注成本

  - 跨模态召回训练阶段，可采用单样本多正例采样策略，提升模型对模糊语义的泛化能力，适配用户口语化Query的检索需求

  - 商品口播、音效素材等短音频类内容的标签生成，可借鉴few-shot+结构化prompt的生成范式，快速生成多维度语义标注'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音频-语言数据集存在语义多样性低、描述泛化缺少声学细节、一对一映射不符合听觉感知歧义的问题，限制了音频检索等跨模态任务的效果上限。
### 方法关键点
1. 基于Qwen3-Omni多模态大模型，以音频+文本为条件生成SonicCaps数据集，包含~700k条音频、~15M条字幕；
2. 单音频生成约24条字幕，覆盖主描述、不同verbose度/风格的改写、语义标签三类，通过结构化prompt工程与few-shot生成保障多样性；
3. 采用多字幕采样策略训练CLAP模型，适配数据特性。
### 关键结果数字
人类评估显示SonicCaps标注质量显著优于现有数据集，描述精准度更高；基于该数据集训练的CLAP模型在音频检索、零样本分类任务上效果持续提升，公域与商业基准泛化性更强。
