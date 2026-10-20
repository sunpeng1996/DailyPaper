---
title: Xiaomi-Lens-0 Technical Report
title_zh: Xiaomi-Lens-0 多模态大模型技术报告
authors:
- Pei Fu
- Yike Liu
- Yue Sun
- Hanmo Wang
- Xiuwen Xi
- Ruoceng Zhang
- Shaojie Zhang
- Chao Jiang
- Hang Li
- Bingrui Liu
affiliations:
- XiaoaiPlus
- SeerRayTeam
arxiv_id: '2610.23279'
url: https://arxiv.org/abs/2610.23279
pdf_url: https://arxiv.org/pdf/2610.23279
published: '2026-10-15'
collected: '2026-10-20'
category: Multimodal
direction: 多模态大模型 · 细粒度视觉理解
tags:
- MLLM
- Visual Grounding
- Mask Prediction
- Fine-grained Perception
- Qwen3.5
one_liner: 基于Qwen3.5的4B多模态大模型，通过内置掩码预测提升细粒度视觉区域理解能力
practical_value: '- 电商多模态导购Agent可复用轻量掩码解码架构，无需额外接入分割模型即可实现商品图细粒度区域识别，降低部署资源开销

  - 图搜/多模态推荐场景可借鉴视觉潜变量与推理绑定机制，提升用户指定图中区域找同款/相似款的召回准确率

  - 多模态模型训练可采用联合语言+掩码监督方案，仅加轻量解码器即可让主干获得区域感知能力，省去额外分割编码器成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有MLLM整图问答表现优异，但细粒度区域理解能力薄弱，核心原因是纯文本监督未关联答案对应的图像支撑区域，无法支撑落地级grounded推理需求。
### 方法关键点
基于Qwen3.5搭建4B参数的Xiaomi-Lens-0，引入轻量掩码解码器，融合视觉编码器patch特征、视觉潜变量与大模型mask-token状态，无需额外分割编码器即可让掩码监督信号传递到共享主干；将视觉潜变量与推理过程绑定，支持Chain-of-Thought过程中关联访问对应图像区域，同时用grounded推理轨迹监督模型访问的区域。
### 关键结果
在RefCOCO、RefCOCO+、RefCOCOg共8个拆分数据集上，指代理解准确率平均较Qwen3.5提升5.6pp，分割cIoU为对比模型中最高，所有感知类基准测试效果均优于Qwen3.5。
