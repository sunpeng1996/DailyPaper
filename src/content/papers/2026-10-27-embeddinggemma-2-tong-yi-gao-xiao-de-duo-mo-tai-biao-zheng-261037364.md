---
title: 'EmbeddingGemma 2: Unified and Efficient Multimodal Representations'
title_zh: EmbeddingGemma 2：统一高效的多模态表征模型
authors:
- Henrique Schechter Vera
- Sahil Dua
- Jovan Andonov
- Sara Smoot
- Sebastian Russo
- Ivan Llanos
- Max Matveev
- Jae Hyeon Yoo
- Kat Black
- Shih-Cheng Huang
affiliations:
- Google DeepMind
arxiv_id: '2610.37364'
url: https://arxiv.org/abs/2610.37364
pdf_url: https://arxiv.org/pdf/2610.37364
published: '2026-10-27'
collected: '2026-10-28'
category: Multimodal
direction: 多模态统一表征 · 轻量嵌入模型
tags:
- MultimodalEmbedding
- EfficientInference
- RAG
- VectorRetrieval
- Quantization
one_liner: 744M参数开源多模态嵌入模型，统一映射多模态输入到同一空间，效果超2-12倍更大的专用/通用模型
practical_value: '- 多模态商品/内容检索场景可直接复用该模型架构：模块化加载模态编码器，按需裁剪参数（文本仅271M、图文439M），适配不同算力的部署场景

  - 训练多模态嵌入模型时可借鉴三阶段课程学习方案：先文本预微调、再多模态蒸馏预微调、最后切换对比损失+正则优化，平衡效果与训练效率

  - 向量检索场景可复用Matryoshka表征学习+int4量化方案：768维截断到256维效果仅降3%左右，int4量化后内存占用降低70%+，检索精度损失小于1%

  - 跨模态商品匹配任务可复用同塔负例+spread-out正则策略，解决嵌入空间塌陷问题，提升向量检索的召回精度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多模态嵌入模型要么仅支持单/双模态、无法处理混合模态输入，要么参数量达数十亿级，无法适配高吞吐、低延迟的线上业务或端侧部署场景；依赖ASR、图像字幕等预处理工具还会丢失细粒度模态信息，导致检索、匹配效果下降。
### 方法关键点
- 模块化架构：以271M双向Transformer为通用backbone，搭配167M ViT视觉编码器、305M USM音频编码器，支持按需加载编码器减少运行时参数，最小仅271M即可运行文本嵌入任务
- 三阶段课程训练：先文本预微调（蒸馏损失为主），再引入全模态数据做蒸馏预微调对齐空间，最后切换对比损失+spread-out正则+Matryoshka表征学习优化，支持嵌入维度动态截断
- 工程适配：支持int4量化感知训练、可配置视觉token预算（70~1120可选）、最长8192序列输入，适配不同资源场景
### 关键结果
在MTEB、MMEB-v2、MIEB、MAEB等7个覆盖文本/代码/图像/音视频的基准测试中，744M全参数版本效果优于2~12倍参数的专用/通用模型；代码检索任务78.68分超所有4B以下模型，多模态任务整体优于同等大小的Jina Embed v5等模型10~15分；768维截断到256维效果仅降2~3%，int4量化后精度损失小于1%。
最值得记住的结论：多模态嵌入模型的效率优化需从架构模块化、训练策略、工程裁剪三个维度协同设计，才能兼顾多模态能力与业务部署的算力要求
