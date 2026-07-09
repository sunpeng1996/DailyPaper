---
title: 'HunyuanOCR-1.5: Making Lightweight OCR VLMs Faster and Better'
title_zh: HunyuanOCR-1.5：更高效更强大的轻量级OCR多模态大模型
authors:
- Gengluo Li
- Xingyu Wan
- Shangpin Peng
- Weinong Wang
- Hao Feng
- Yongkun Du
- Binghong Wu
- Zheng Ruan
- Zhiqiong Lu
- Liang Wu
affiliations:
- 中国科学院信息工程研究所
- 腾讯大语言模型部
- 南开大学
arxiv_id: '2607.04884'
url: https://arxiv.org/abs/2607.04884
pdf_url: https://arxiv.org/pdf/2607.04884
published: '2026-07-05'
collected: '2026-07-09'
category: Multimodal
direction: 多模态大模型 · 轻量OCR VLM优化
tags:
- OCR
- VLM
- Inference Acceleration
- Agentic Data Construction
- Lightweight Model
one_liner: 基于原有轻量架构，通过DFlash推理加速和Agent驱动数据构建，实现OCR VLM性能与速度双提升
practical_value: '- 可复用DFlash推理加速方案优化长文本/结构化输出（如商品详情页OCR、订单表格解析）的解码延迟，适配vLLM部署场景降本提效

  - Agent驱动的自动化数据构建流程可迁移到垂域模型迭代，自动定位模型短板、生成对应训练数据，降低长尾场景数据标注成本

  - 轻量端到端OCR VLM架构可直接嵌入电商商品信息爬取、商户资质审核、用户手写/印刷评价解析等业务链路，替代多阶段OCR方案'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有轻量OCR VLM普遍存在长结构化输出推理延迟高、长尾场景（小语种、古文字、复杂表格解析）能力不足的问题，需无需重构backbone即可落地的兼顾效率与能力的端到端优化方案。
### 方法关键点
1. 效率侧适配DFlash加速OCR解码，保留输出分布的同时降低密集文档、表格、公式等长结构化输出的推理延迟；
2. 能力侧提出Agentic Data Flow，基于Agent自动将模型短板转化为数据需求，自主完成素材搜索、质量校验、流水线开发，针对性补强长尾能力；
3. 升级预训练与后训练流程，适配高分辨率、长上下文、多任务场景。
### 关键结果数字
Transformer推理速度提升6.37倍，vLLM下速度提升2.14倍，为当前最快轻量OCR VLM；在OmniDocBench v1.6上达到端到端OCR方案第一梯队，古文字OCR、复杂表格解析、多图文QA等长尾任务性能达新里程碑。
