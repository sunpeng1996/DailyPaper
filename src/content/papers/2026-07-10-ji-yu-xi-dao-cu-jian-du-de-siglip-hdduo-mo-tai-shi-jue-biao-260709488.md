---
title: SigLIP-HD by Fine-to-Coarse Supervision
title_zh: 基于细到粗监督的SigLIP-HD多模态视觉表征优化模型
authors:
- Lihe Yang
- Zhen Zhao
- Hengshuang Zhao
affiliations:
- The University of Hong Kong
- Shanghai AI Laboratory
arxiv_id: '2607.09488'
url: https://arxiv.org/abs/2607.09488
pdf_url: https://arxiv.org/pdf/2607.09488
published: '2026-07-10'
collected: '2026-07-13'
category: Multimodal
direction: 多模态LLM · 视觉表征蒸馏优化
tags:
- SigLIP
- Multimodal
- Knowledge Distillation
- Visual Representation
- MLLM
one_liner: 通过细到粗监督蒸馏，在相同推理成本下让标准分辨率SigLIP输出更高质量视觉特征
practical_value: '- 电商多模态商品检索、图文详情理解场景可复用该蒸馏方案，无需升级高分辨率输入即可提升OCR、细粒度商品属性识别效果，无额外推理成本

  - 现有多模态召回、粗排链路中可直接替换原有SigLIP视觉编码器，无需改造链路结构即可获得视觉特征质量的普适性提升

  - 低算力端多模态Agent的视觉感知模块可参考该范式，无需接入高分辨率图像输入即可优化细粒度目标识别、文字识别能力'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
多模态LLM（MLLM）采用高分辨率图像输入可生成更细粒度的视觉token，但会带来多轮前向计算、高数量token后处理的额外复杂度，现有方案未充分挖掘标准分辨率输入下模型的感知能力上限，亟需在不提升推理成本的前提下优化细粒度视觉感知的方案。
### 方法关键点
基于SigLIP 2搭建训练框架，核心采用极简的细到粗监督蒸馏策略：强制中等分辨率输入的粗特征对齐同一张图高分辨率版本的细粒度特征，仅训练阶段增加蒸馏损失，推理阶段完全沿用原SigLIP的标准分辨率输入流程，无额外开销。
### 关键结果
在多类MLLM基准测试中效果全面优于基线SigLIP 2，OCR相关任务提升尤为突出，全程推理成本与原基线完全一致。
