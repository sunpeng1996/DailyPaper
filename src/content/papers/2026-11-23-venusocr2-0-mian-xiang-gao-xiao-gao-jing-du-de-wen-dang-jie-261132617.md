---
title: 'VenusOCR2.0: Towards Efficient and Effective Document Parsing'
title_zh: VenusOCR2.0：面向高效高精度的文档解析模型
authors:
- Lei Li
- Zheng Wei
- Yi Yuan
- Qingbin Liu
- Jiang Bian
- Zang Li
affiliations:
- VenusOCR Team, Tencent Inc.
arxiv_id: '2611.32617'
url: https://arxiv.org/abs/2611.32617
pdf_url: https://arxiv.org/pdf/2611.32617
published: '2026-11-23'
collected: '2026-11-25'
category: Multimodal
direction: 多模态文档解析 · 高效解码优化
tags:
- OCR
- VLM
- Decoding Optimization
- Lightweight Model
- Data Engine
one_liner: 1B参数量轻量多模态OCR模型，精度超千亿通用VLM，解码速度最高提升3倍
practical_value: '- 电商场景商品资质、详情页、用户手写评价的结构化解析，可复用「轻量SigLIP2编码器+小参数量LLM解码器」架构，比通用大VLM降本80%以上

  - PTPv2轻量并行无损解码模块可直接迁移到生成式推荐、LLM Agent的推理链路，单卡吞吐提升2倍以上

  - 有界递归自改进数据引擎的bad case挖掘+外部校验思路，可复用在搜索推荐的模型迭代流程，避免自训练坍缩'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有通用VLM做文档解析参数量大、推理效率低，自训练迭代易坍缩，表格、公式等结构化内容识别误差高，难以满足工业级高吞吐高准确率需求。
### 方法关键点
1. 构建有界递归自改进（RSI）数据引擎，模型仅作为弱点探针，结合多专家共识、VLM视觉校验、因子化合成提供可靠监督，覆盖预训练、SFT、RLVR全流程
2. 架构搭配动态分辨率SigLIP2编码器+2x2空间token合并+Qwen3-0.6B解码器，引入OTSL原子token压缩表格序列长度，降低结构识别误差
3. 新增67M参数量PTPv2并行draft模块，实现与标准自回归完全等价的无损解码加速
### 关键结果
OmniDocBenchv1.6总分96.45，公式CDM达SOTA的98.57，大幅领先Gemini-3-Pro（92.91）、Qwen3-VL-235B（89.78）；单H20 GPU上单请求提速2.96倍，批量吞吐最高提升2.36倍
