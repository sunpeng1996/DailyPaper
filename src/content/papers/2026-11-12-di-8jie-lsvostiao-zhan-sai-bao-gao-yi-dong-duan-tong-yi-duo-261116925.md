---
title: 'Report of the 8th LSVOS Challenge: Mobile Unified Multimodal Understanding'
title_zh: 第8届LSVOS挑战赛报告：移动端统一多模态理解
authors:
- Chang Liu
- Henghui Ding
- Tong Yang
- Dayoung Kil
- Seong-heum Kim
- Qilin Xiang
- Ronghao Zheng
- Ziyang Zhang
- Shanlin Jiang
- Ruohan Shi
affiliations:
- Shanghai University of Finance and Economics
- Transsion
- Institute of Big Data, Fudan University
arxiv_id: '2611.16925'
url: https://arxiv.org/abs/2611.16925
pdf_url: https://arxiv.org/pdf/2611.16925
published: '2026-11-12'
collected: '2026-11-13'
category: Multimodal
direction: 端侧统一多模态理解 挑战赛方案总结
tags:
- Unified Multimodal Understanding
- Efficient VLM
- Florence-2
- LoRA
- Test-time Augmentation
one_liner: 总结ECCV2026 MUMU赛道方案，给出0.5B参数内端侧多模态任务落地路径
practical_value: '- 端侧电商商品理解等多模态场景可优先选用Florence-2-base这类轻量VLM作为基座，0.5B参数即可适配8GB内存限制，避免多模型部署冗余

  - 跨多模态任务优化时可复用「共享LoRA+任务专属解码」方案，相比全量微调训练成本低，可同时兼顾打标、检测、caption三类任务效果

  - 低资源落地场景可尝试无训练pipeline：通过caption映射标签+检测测试时增广，无需微调基座即可快速上线多模态理解能力'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
端侧视觉理解场景通常需要同时支持图像打标、目标检测、文案生成多类任务，单独部署多套专属模型存在参数冗余、内存占用高、维护成本高的问题，MUMU赛道聚焦0.5B参数、峰值8GB推理内存限制下的单模型多任务统一建模。
### 方法关键点
参赛Top3方案均以轻量Florence-2-base为基座，采用三类差异化优化路径：1）新增轻量打标头+跨任务推理结果校准；2）基于覆盖感知多源数据训练共享LoRA+任务专属解码逻辑；3）无训练pipeline：将生成的caption映射为标签+检测阶段测试时增广。
### 关键结果
经效率因子加权的综合评分验证，紧凑型prompt-based VLM只要针对任务设计适配的监督策略、解码逻辑、跨任务提示，即可同时输出三类任务结果，当前开放词汇下新类别的检测仍是性能核心瓶颈。
