---
title: 'HAFI-VLM: A Frequency Perspective for Diagnosing and Enhancing Visual Perception
  in Vision-Language Models'
title_zh: HAFI-VLM：从频域视角诊断并增强视觉语言模型的视觉感知能力
authors:
- Jin Cui
- Chuanchang Su
- Jiayi Lu
- Xinyue Long
- Boran Zhao
- Pengju Ren
affiliations:
- State Key Laboratory of Human-Machine Hybrid Augmented Intelligence, Xi'an Jiaotong
  University
- School of Computer Science and Technology, Xi'an Jiaotong University
- School of Software Engineering, Xi'an Jiaotong University
arxiv_id: '2608.02124'
url: https://arxiv.org/abs/2608.02124
pdf_url: https://arxiv.org/pdf/2608.02124
published: '2026-08-03'
collected: '2026-08-05'
category: Multimodal
direction: 多模态大模型 · 频域感知增强
tags:
- VLM
- Frequency Enhancement
- Fine-grained Perception
- Adapter
- Hallucination Reduction
one_liner: 针对VLM细粒度视觉感知不可靠问题，提出任务条件频域注入框架，无需额外高分辨率编码即可提升多模态性能
practical_value: '- 做多模态商品理解、多模态搜推的团队可复用HAFI分层频域注入思路，无需提升图像输入分辨率即可增强细粒度属性（如商品logo、材质、小字参数）识别准确率，降低推理成本

  - 多模态Agent场景可借鉴文本调制的跨注意力机制，用任务query自适应调整视觉频域特征提取权重，降低细粒度视觉信息幻觉率，适配商品审核、直播内容理解等场景

  - 基于开源VLM做轻量迭代的业务可直接复用「不动预训练主干、仅用Adapter做特征增强」的架构，迭代效率高、适配性强'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有VLM在需细粒度视觉证据的任务上可靠性差，核心被忽略的底层原因是预训练视觉编码器存在**频谱响应刚性**：不同图像、任务的频域需求差异极大，但微调时编码器分层频谱分布几乎无变化，无法根据文本query自适应调整频域特征提取逻辑。
### 方法关键点
1. 设计分层自适应频域注入（HAFI）模块，在视觉编码器多层级分别抽取低/中/高频互补特征，通过文本调制、空间对齐的交叉注意力构建任务条件的频域通路；
2. 新增视觉增强层Adapter，重校准LLM浅层注意力，更高效利用增强后的视觉token，全程保留预训练语义表征不受破坏。
### 关键结果
在LLaVA-1.5、Qwen2.5-VL上验证，通用VQA、富文本理解、幻觉鲁棒性均获得一致提升，性能超过所有表征级增强方法及大部分基于分辨率提升/裁剪的方案，且无额外高分辨率编码开销。
