---
title: 'ADAPT: Attention Dynamics Alignment with Preference Tuning for Faithful MLLMs'
title_zh: ADAPT：注意力动态对齐与偏好优化提升MLLM事实性
authors:
- Zhiyuan Yao
- Zheren Fu
- Zhixiao Zheng
- Jiajun Li
- Yi Tu
- Zhendong Mao
affiliations:
- 中国科学技术大学
- 华为技术有限公司
- 传播内容认知国家重点实验室（人民网）
arxiv_id: '2606.31054'
url: https://arxiv.org/abs/2606.31054
pdf_url: https://arxiv.org/pdf/2606.31054
published: '2026-06-30'
collected: '2026-07-01'
category: Multimodal
direction: 多模态大模型 · 幻觉抑制优化
tags:
- MLLM
- Hallucination Mitigation
- Cross-Attention
- DPO
- Inference Optimization
one_liner: 基于跨注意力退化机制，提出训练推理协同的MLLM幻觉抑制框架，幻觉率降40-60%
practical_value: '- 电商多模态导购Agent可复用注意力锚定逻辑：对商品图的跨注意力做早期锚定+漂移检测，减少生成商品属性（颜色、尺寸、配件）的幻觉，提升导购可信度

  - 训练侧VAG-DPO设计可迁移到多模态推荐偏好对齐：用锚定增强的正样本+噪声干扰的负样本构造偏好对，比普通DPO更能在保留模型通用能力的同时提升视觉对齐度

  - 推理侧选择性干预机制工程性价比高：仅在注意力漂移低于阈值时修正，仅带来1.42x推理开销，远低于其他幻觉抑制方案，适合高并发的电商商品理解、直播内容审核场景'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
MLLM在图文理解、生成场景中广泛存在幻觉，现有方案多为输出端驱动，未针对生成过程中文本到图像跨注意力逐步退化、后期依赖语言先验的核心问题，导致幻觉抑制效率低、泛化性差，尤其在长文本生成场景下后期幻觉率大幅提升。

### 方法关键点
- 跨注意力视觉锚定：提取生成前K个token的多层跨注意力，通过频谱平滑度、空间连续性、query相关熵三个维度加权融合，再去位置偏置得到稳定的查询相关注意力锚
- 注意力监督推理：在线计算当前跨注意力与锚的AMC匹配度，低于阈值时仅做稀疏注意力权重修正，不强制对齐锚，兼顾生成灵活性与事实性
- 视觉注意力引导DPO（VAG-DPO）：构造偏好对时，正样本用锚增强的图像+事实回复，负样本用噪声图像+幻觉回复，让模型学会依赖有效视觉证据而非语言先验生成内容

### 关键结果
在AMBER、POPE-Adv、MM-Hal、Obj-Hal四个主流幻觉基准上测试，覆盖LLaVA-1.5、Qwen2.5-VL等主流MLLM backbone；全量方案相比基线幻觉率降低40-60%，POPE-Adv精度最高达94%，推理开销仅为基线的1.42x，远低于对比方案；VAG-DPO相比普通DPO，通用能力损失减少25%以上。

> 最值得记住的一句话：针对模型内部状态的动态干预，比单纯的输出端约束能更高效、低损地解决多模态模型的幻觉问题
