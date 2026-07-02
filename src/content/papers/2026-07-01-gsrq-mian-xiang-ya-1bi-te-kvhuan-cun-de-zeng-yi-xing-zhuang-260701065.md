---
title: 'GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache'
title_zh: GSRQ：面向亚1比特KV缓存的增益-形状残差量化
authors:
- Soosung Kim
- Minjae Park
- Eui-Young Chung
- Jaeyong Chung
affiliations:
- Yonsei University
arxiv_id: '2607.01065'
url: https://arxiv.org/abs/2607.01065
pdf_url: https://arxiv.org/pdf/2607.01065
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: LLM推理优化 · KV缓存量化
tags:
- KV_cache
- Vector_Quantization
- Residual_Quantization
- LLM_Serving
- Low_Bit_Quantization
one_liner: 提出可直接替换K-means的GSKM聚类，结合加权残差量化实现亚1比特KV缓存压缩，性能大幅领先现有基线
practical_value: '- 部署LLM驱动的电商Agent、生成式推荐、长文本query理解服务时，可直接集成GSRQ替换现有KV缓存量化方案，1比特位宽下仍能保持90%+的FP16性能，大幅提升长上下文推理吞吐量，降低GPU部署成本

  - GSKM是无额外超参数的K-means drop-in替换，可复用在高维弱结构化向量（如用户兴趣embedding、长尾item embedding）的聚类召回场景，解决高维下L2质心收缩导致的方向匹配精度下降问题

  - 对数平滑的梯度加权策略可迁移到向量量化的重要性感知优化场景，比如广告特征压缩、用户行为序列向量压缩，避免长尾异常梯度主导码本学习'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM长上下文推理的核心瓶颈是KV缓存内存随序列长度、batch size线性增长，现有残差量化（RQ）类KV缓存压缩方案依赖标准L2 K-means学习码本，高维下向量方向分散会导致质心收缩，弱化角度对齐项的优化优先级，低比特（亚1比特）下方向保真度暴跌，推理性能严重退化。
### 方法关键点
- 提出Gain-Shape K-means（GSKM），将聚类质心解耦为增益（幅度标量）和形状（单位方向向量）两个变量分别更新：方向更新用归一化后的输入向量均值做角度对齐，幅度更新为输入向量在方向上的投影均值，完全避免高维质心收缩，复杂度与标准K-means一致，可直接替换
- 构建GSRQ残差量化流水线，将每个KV向量拆分为低维子空间，用梯度加权的GSKM逐阶段量化残差，梯度权重采用对数平滑处理，抑制长尾大梯度的异常影响
- 支持0.375~2比特的灵活位宽配置，兼容现有anchor token保留、KV缓存裁剪等正交优化技术
### 关键结果
在LLaMA-3-8B、Mistral-7B、Qwen3-8B等开源模型上测试，对比VQLLM、KIVI、CQ等SOTA基线：
1. 1比特位宽下，LongBench平均准确率从VQLLM的11.34提升至33.54，涨幅22.2pp；0.75比特的GSRQ精度超过1比特的VQLLM
2. 0.375比特位宽下，WikiText-2的perplexity比基于标准K-means的RQ低7.03，仅比FP16基线高4.23
3. 128K长上下文解码时，GSRQ比FP16基线提速3.4倍，可在FP16 OOM的单A100场景下正常运行
### 核心结论
高维弱结构化向量的低比特压缩场景中，对幅度和方向解耦优化的收益，远高于对向量结构的复杂适配设计
