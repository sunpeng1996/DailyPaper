---
title: 'SpaceCast-Bench: Evaluating Predictive Spatial Reasoning in Vision-Language
  Models'
title_zh: SpaceCast-Bench：视觉语言模型预测性空间推理评测基准
authors:
- Hongxing Li
- Jinyue Su
- Dingming Li
- Wenqi Zhang
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
- Yongliang Shen
affiliations:
- Zhejiang University
arxiv_id: '2610.12402'
url: https://arxiv.org/abs/2610.12402
pdf_url: https://arxiv.org/pdf/2610.12402
published: '2026-10-07'
collected: '2026-10-09'
category: Eval
direction: 多模态大模型 · 空间推理能力评测
tags:
- Spatial Reasoning
- VLM
- Benchmark
- Predictive Reasoning
- Multimodal Evaluation
one_liner: 首个面向视觉语言模型预测性空间推理的诊断式评测基准，暴露现有模型与人类的显著性能差距
practical_value: '- 做多模态Agent、AR导购、虚拟逛店等涉及空间交互的业务时，可复用observe-transform-infer框架评测模型空间推理能力

  - 优化多模态推荐/Agent空间推理性能时，优先接入显式3D证据而非生成的结果图/视频，可获得更稳定的效果提升

  - 小参数VLMs落地空间相关任务（如AR商品摆放推荐、户型软装推荐）时，可采用程序化生成的空间推理数据做微调，实现跨域性能提升'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有空间推理基准仅测试输入中已可见的空间感知能力，无法覆盖真实场景所需的「基于观测构建场景、预测干预后未可见变化」的预测性空间推理需求。
### 方法关键点
基于observe-transform-infer框架构建SpaceCast-Bench，覆盖182个真实场景的3862个问题，包含16类任务，分为静态感知、局部预测、全局预测三个难度层级，逐级要求场景理解、空间状态更新、未观测结果关系推理能力。
### 关键结果数字
21个模型评测显示最强模型准确率仅58.0%，远低于人类的87.2%，空间专项模型性能接近随机水平；控制实验证明桥接视角对整合分布式观测至关重要，显式3D证据比生成的结果图/视频更能稳定提升模型性能；基于程序化生成数据微调后，Qwen3-VL-4B准确率从34.0%提升至65.7%，在6个跨域基准上获得宏观平均收益
