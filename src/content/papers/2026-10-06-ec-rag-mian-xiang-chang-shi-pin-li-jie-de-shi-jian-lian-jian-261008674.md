---
title: 'EC-RAG: Event Chain Retrieval-Augmented Generation for Long Video Understanding'
title_zh: EC-RAG：面向长视频理解的事件链检索增强生成框架
authors:
- Yuhao Qin
- Junbo Wang
- Yuke Li
- Yining Zhu
affiliations:
- Northwestern Polytechnical University
arxiv_id: '2610.08674'
url: https://arxiv.org/abs/2610.08674
pdf_url: https://arxiv.org/pdf/2610.08674
published: '2026-10-06'
collected: '2026-10-07'
category: RAG
direction: 多模态RAG · 长视频事件链时序建模
tags:
- RAG
- Long-Video-Understanding
- Event-Chain
- LVLM
- Multimodal-Reasoning
one_liner: 提出训练免微调的事件链RAG框架，结构化建模长视频时序依赖，适配任意开源LVLM提升理解性能
practical_value: '- 长内容理解场景（如电商直播/短视频内容解析、用户行为序列建模）可复用事件链结构化建模思路，替代零散片段检索，提升时序推理准确性

  - 多模态检索的关键帧选择可借鉴CLIP相似度+视觉方差加权策略，平衡语义相关性和信息丰富度，降低冗余计算

  - 训练免微调的RAG架构设计思路可迁移到业务场景，无需重训底座模型即可快速适配长时序多模态内容理解需求

  - 多模态信息融合时可复用ASR/OCR/DET分模态检索再聚合的逻辑，针对不同query类型按需调用对应模态能力，减少噪声输入'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有LVLM处理长视频时受限于上下文窗口，均匀采样帧易出现信息冗余、时序依赖丢失问题；现有视频RAG多在帧/片段级检索，未建模事件间因果与时序关联，无法支撑跨时间段的复杂推理需求，长视频问答、时序理解性能瓶颈显著。

### 方法关键点
- **查询解耦**：将用户query拆解为ASR、OCR、DET三类模态的检索请求，按需分配计算资源，避免无效模态输入
- **CLIP-方差引导的多模态提取**：融合CLIP语义相似度和帧像素方差选关键帧，兼顾查询相关性和视觉信息丰富度；并行抽取语音转录、屏幕文本、场景图三类多模态信息
- **时序事件链构建**：将视频切分为30s语义片段，聚合每段多模态信息生成事件描述，按时间顺序组装为带前驱后继关系的事件链，保留时序结构和事件关联
- **证据增强推理**：基于语义相似度定位query相关事件，聚合对应多模态证据，结合全局事件链摘要、相关事件详情、多模态原始证据输入LVLM生成答案

### 关键实验
在Video-MME、MLVU、LongVideoBench三个长视频基准测试，对比Video-RAG、TV-RAG等帧级检索方案，适配5种不同规模开源LVLM均获稳定提升：Video-MME上平均提升4%，LLaVA-Video-72B加持下达到75.7%准确率，超过GPT-4o、Gemini-1.5-Pro等闭源模型；MLVU上7B模型64帧输入达到72.9%准确率，超过32B参数128帧输入的Oryx-1.5；LongVideoBench上达到59.5%准确率，领先同类RAG方案。

最值得记住的一句话：对于长时序多模态内容理解，结构化的事件级时序建模带来的收益，远高于单纯增加采样帧数量或扩大模型参数规模。
