---
title: Co-occurrence Patterns of LoRA Adapters in Production Diffusion Model Inference
  Services
title_zh: 生产级扩散模型推理服务中LoRA适配器的共现模式研究
authors:
- Tao Zhang
- Bin Liao
- Tao Zhou
- Yanping Liu
affiliations:
- 贵州中医药大学信息工程学院
- 贵州财经大学大数据与统计学院
- 贵州财经大学数学与统计学院
- 北京工商大学数学与统计学院
arxiv_id: '2609.23321'
url: https://arxiv.org/abs/2609.23321
pdf_url: https://arxiv.org/pdf/2609.23321
published: '2026-09-20'
collected: '2026-09-22'
category: LLM
direction: LoRA推理服务 · 负载特征与缓存优化
tags:
- LoRA
- Diffusion Model
- Inference Optimization
- Workload Characterization
- Cache Preloading
one_liner: 基于阿里生产GenTD26数据集量化LoRA共现规律，提出数据驱动的缓存预加载优化策略
practical_value: '- 电商/广告场景的AI生成服务（如商品图、文案生成）部署多租户LoRA推理时，可直接复用共现预加载策略：为每个高频适配器维护top-3共现伙伴表，存储开销仅2k+条记录，可覆盖81%共现请求，大幅降低加载延迟

  - 可直接复用分层缓存架构：占比<1%的跨模型核心适配器永久驻留GPU显存，top50高频适配器（覆盖55%请求）固定缓存，长尾适配器按需加载，总显存占用可控制在数百MB级，几乎无额外成本

  - 缓存淘汰策略可优化为中心度加权LRU：优先保留共现网络中高中心度的hub适配器，可提升89%以上多适配器请求的缓存命中率，适合GPU显存受限的部署场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LoRA推理系统的调度、缓存策略多采用通用LRU等方案，缺乏生产真实负载的共现结构特征支撑，无法针对性优化多适配器请求的加载延迟、GPU显存利用率，业界尚未对生产环境下LoRA适配器的共现规律、资源竞争关系做系统量化分析。
### 方法关键点
- 基于图论框架构建LoRA适配器共现网络，设置频率阈值τmin、共现权重阈值wmin过滤偶发关联，从静态结构、动态演化两个维度做特征分析
- 量化适配器使用频率分布、共现稀疏性、基模型关联关系、多时间粒度演化规律四类核心特征
- 输出top-k共现预加载、时间感知分层缓存、中心度加权LRU淘汰三类可落地的系统优化方案
### 关键实验结果
基于阿里生产GenTD26数据集（24天运营数据、2.68万请求、874个唯一LoRA适配器）验证：适配器共现网络极度稀疏，边密度仅0.18%，90.6%多适配器请求的所有适配器共享同一基模型；首适配器加载带来66.1%执行延迟 overhead，后续适配器边际成本显著递减；k=3时共现预加载策略可覆盖81.0%测试集共现对，策略稳定性经多阈值敏感性分析验证；基模型周级Jaccard相似度达0.696，top10热门模型12小时 churn率高达54.5%。
### 核心结论
LoRA适配器的共现关系高度聚集在同基模型生态内，基于共现特征的轻量化优化即可大幅提升推理服务效率。
