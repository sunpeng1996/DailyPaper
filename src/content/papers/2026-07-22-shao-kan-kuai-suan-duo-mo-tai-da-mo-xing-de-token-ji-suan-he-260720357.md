---
title: 'Look Less, Think Faster: Joint Token-Compute Adaptation for Multimodal LLMs'
title_zh: 少看快算：多模态大模型的Token-计算联合自适应推理框架
authors:
- Pengcheng Wang
- Zhiquan Wang
- Jayoung Lee
- Zhuoyan Xu
- Ran Xu
- Saurabh Bagchi
- Yin Li
- Somali Chaterji
affiliations:
- Purdue University
- University of Wisconsin–Madison
- NVIDIA
arxiv_id: '2607.20357'
url: https://arxiv.org/abs/2607.20357
pdf_url: https://arxiv.org/pdf/2607.20357
published: '2026-07-22'
collected: '2026-07-23'
category: LLM
direction: 多模态大模型 · 自适应推理优化
tags:
- Multimodal-LLM
- Adaptive-Inference
- Token-Pruning
- Compute-Scheduling
- Efficient-Deployment
one_liner: 提出SmartVL框架联合控制视觉Token与LLM计算量，实现多模态任务更优的精度-效率权衡
practical_value: '- 多模态商品理解/图文搜索场景可复用联合调度思路：根据输入复杂度（白底商品图/复杂场景图）动态分配视觉Token保留率与LLM计算量，在延迟约束下保证理解准确率

  - 可迁移差异化请求SLA控制方案：对不同优先级请求（VIP用户搜索/普通爬虫请求）配置不同FLOPs预算，用一套模型覆盖多档位服务要求，降低部署多套模型的成本

  - 轻量控制器适配技巧可复用：共享预算编码+可微延迟估计器+非对称预算损失的组合，不需要修改主模型结构，用LoRA即可快速适配现有MLLM，落地成本低

  - 推理兜底策略可参考：优先裁剪低置信度视觉Token、再削减LLM层数的优先级设计，对生成质量影响最小，适合在线服务的稳定性要求'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
多模态大模型（MLLM）是图文理解、VQA等任务的主流方案，但推理成本固定，无论输入复杂度高低都需全量计算，无法适配不同延迟约束、系统负载波动；现有优化方法要么单独裁剪视觉Token，要么单独跳过LLM层，忽略二者的耦合性，易丢失关键语义信息或算力分配不合理，导致精度掉点严重。

### 方法关键点
- 包含两个轻量控制器：视觉端Token控制器动态筛选高信息量视觉Token，LLM端计算控制器自适应调整激活层数、注意力头占比，覆盖序列长度、模型深度、模型宽度三个算力优化维度
- 两个控制器通过共享预算编码关联，用可微FLOPs估计器实现端到端训练，非对称预算损失二次惩罚超预算行为、线性惩罚算力浪费，平衡预算约束与精度要求
- 推理阶段按优先级兜底：先裁剪低置信度视觉Token，再削减LLM层/头，确保不超过目标预算的同时最小化精度损失

### 关键结果
在VQAv2、GQA、TextVQA等7个多模态基准测试，对比Token剪枝类（FastV/LLaVA-PruMerge+）、计算自适应类（AdaLLaVA）、二者简单拼接的基线：
- 50% FLOPs预算下，平均精度比AdaLLaVA高7.8%，在TextVQA、VizWiz等任务上避免了AdaLLaVA的严重精度暴跌
- 支持20%~100%全范围连续预算调节，远优于固定剪枝方法的离散档位限制
- 13B尺度LLaVA-1.5上同样生效，半预算下VQAv2精度比AdaLLaVA高3.18%

**最值得记住的一句话**：MLLM的视觉Token冗余度和LLM推理复杂度是强耦合的，跨维度联合算力调度比单独优化单一维度能获得好得多的精度-效率tradeoff。
