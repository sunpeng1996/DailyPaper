---
title: 'V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned
  Representations'
title_zh: V-JEPA-LM：超越静态文本对齐表征、可识别动态信息的视频语言模型
authors:
- Keuntae Kim
- Dongjun Kim
- Yong Suk Choi
affiliations:
- Department of Computer Science, Hanyang University, Seoul, Republic of Korea
arxiv_id: '2611.17831'
url: https://arxiv.org/abs/2611.17831
pdf_url: https://arxiv.org/pdf/2611.17831
published: '2026-11-12'
collected: '2026-11-16'
category: Multimodal
direction: 多模态大模型 · 视频动态信息理解
tags:
- Video-LLM
- V-JEPA
- Counterfactual Supervision
- Multimodal Representation
- Dynamic Understanding
one_liner: 通过反事实监督激活V-JEPA编码器的动态特征，单阶段训练出性能领先的轻量视频大模型
practical_value: '- 商品短视频/直播内容理解场景，可复用V-JEPA编码器提取动态特征（如商品展示动作、速度），替换SigLIP等静态对齐编码器，提升动态信息召回准确率

  - 标注数据不足时，可复用反事实数据增强思路：对原始视频做像素级变换（如变速、倒放）自动生成标注平衡的训练样本，大幅降低标注成本

  - 资源有限的多模态模型训练场景，可尝试单阶段训练范式，对比多阶段训练能降低复杂度，用更少样本达到SOTA性能'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有V-JEPA类世界模型编码器已学习到丰富的视频动态信息（速度、方向、状态变化等），但和LLM对接时，因caption/QA标注仅覆盖少量属性，模型只会检索标注属性，不会读取视频动态特征，线性探针能从V-JEPA特征读出87%的速度信息，而现有VLM对速度问题回答准确率仅为随机水平。
### 方法关键点
1. 定位到V-JEPA等预测式编码器的动态信息存储在跨视频共享的子空间，SigLIP等帧级文本对齐编码器无该共享子空间；
2. 设计反事实监督：通过像素变换将公开视频转为答案平衡的变体，答案由变换规则自动生成，仅差异在动态变化；
3. 单阶段训练，仅用4.53M公开样本、每帧32个视觉token，远低于现有开源Video-LLM的训练成本。
### 关键结果
1B-8B全参数规模的V-JEPA-LM（基于Qwen3、Llama）在11个视频基准上各尺寸均领先；4B模型得分72.1，优于现有最优开源4B模型的61.1，甚至超过最优开源8B模型的64.8；相同训练预算下，反事实监督平均提升4.5分，速度类问题提升38分。
