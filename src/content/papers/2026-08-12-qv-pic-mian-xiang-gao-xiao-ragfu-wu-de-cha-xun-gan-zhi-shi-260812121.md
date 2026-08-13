---
title: 'QV-PIC: Query-Aware Visual Position-Independent Caching for Efficient RAG
  Serving'
title_zh: QV-PIC：面向高效RAG服务的查询感知视觉无关位置缓存
authors:
- Yilin Liu
- Rui Meng
- Wangze Ni
- Jianxin Yan
- Heng Cao
- Libin Zheng
- Peng Cheng
- Jinfei Liu
affiliations:
- 浙江大学
- 北京师范大学-香港浸会大学联合国际学院统计与数据科学系
- 微软
- 中山大学
- 同济大学
arxiv_id: '2608.12121'
url: https://arxiv.org/abs/2608.12121
pdf_url: https://arxiv.org/pdf/2608.12121
published: '2026-08-12'
collected: '2026-08-13'
category: RAG
direction: RAG服务优化 · KV缓存复用
tags:
- RAG
- KV cache
- Position-Independent Caching
- VLM
- Latency Optimization
one_liner: 提出融合模型原生模板编译与查询感知双分辨率的视觉PIC框架，大幅优化RAG服务的效果与延迟
practical_value: '- 电商/客服RAG系统可直接复用该架构：将高频召回的商品详情、售后规则等文档离线预渲染为高低分辨率视觉缓存，预计算KV后存储，在线仅需处理query和少量高相关块的高分辨率缓存，可大幅降低首包响应时间（TTFT），提升用户体验。

  - PIC缓存编译技巧可迁移：所有PIC系统（文本/多模态）都可以在离线编译时加模型原生对话模板前缀，再剥离前缀对应的KV，无需额外在线计算即可提升独立缓存的复用质量，效果优于dummy前缀或在线重算首token的方案。

  - 资源动态分配思路可复用：推荐/搜索链路中可对召回结果按用户query相关性动态分配计算资源，高相关内容用完整特征/高分辨率表示，低相关内容用压缩特征，在几乎不损失效果的前提下降低整体链路耗时。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长文档RAG服务中相同文档块会被不同query重复预填充，产生大量冗余计算；Position-Independent Caching（PIC）可跨位置复用预计算KV cache，但文本PIC的KV规模随上下文长度线性增长，传输和计算成本高。将文本渲染为图像用VLM编码可实现3-4倍token压缩，但原生渲染图像PIC的F1比文本PIC低12.2点，效果退化严重，核心源于两个问题：独立编译的缓存缺少全局上下文导致状态不匹配、视觉压缩丢失细粒度文本证据，现有修复方法依赖在线重计算，无法恢复丢失的文本细节。
### 方法关键点
- 离线预处理：每个文档块渲染72DPI低分辨率、120DPI高分辨率两个版本的图像，在模型原生对话模板前缀下编译KV cache，剥离前缀对应KV后存储，同时预计算文档块的BGE-M3 embedding用于后续相关性排序。
- 在线调度拼接：召回的所有文档块默认用低分辨率缓存保证全局上下文覆盖，通过query embedding与块embedding的余弦相似度排序，选择累计相关性达65%、最多4个高相关性块升级为高分辨率缓存，经M-RoPE位置重锚定后拼接为完整KV，在线仅需计算query预填充和答案生成。
### 关键结果
在LongBench的6个长文档QA任务上测试，对比基线包括原生渲染图像PIC、优化文本PIC、全预填充等：QV-PIC比原生渲染图像PIC平均F1高21.6点，完全消除与文本PIC的效果差距，还比优化文本PIC高2.58个F1点，同时TTFT降低17.2%；相比全预填充，TTFT降低83.8%，在GLM-4.1V、LLaVA-OneVision-2等通用VLM上也能稳定取得效果-延迟的共同提升。

最值得记住的一句话：通过离线预处理对齐模型原生输入范式、在线按query相关性动态分配计算资源，可在几乎不损失效果的前提下大幅降低多模态RAG的服务延迟。
