---
title: 'DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon Multimodal
  Agents'
title_zh: DeepVoyager-VL：面向长时序多模态Agent的环内视觉搜索框架
authors:
- Huanyao Zhang
- Jiepeng Zhou
- Runhao Zhao
- Yanzhe Shan
- Jiaoyang Chen
- Bowen Zhou
- Bo Li
- Fang Wang
- Jialong Wu
- Zhengwei Tao
affiliations:
- PKU
- HKUST(GZ)
- NUDT
- OUC
- Huawei Cloud BU
arxiv_id: '2608.01827'
url: https://arxiv.org/abs/2608.01827
pdf_url: https://arxiv.org/pdf/2608.01827
published: '2026-08-02'
collected: '2026-08-04'
category: Agent
direction: 长时序多模态Agent · 视觉环内搜索
tags:
- Multimodal Agent
- Vision-in-the-Loop
- SFT
- Multimodal Search
- Long-Horizon
- Event Graph
one_liner: 基于多模态事件图合成训练数据，无RL仅SFT实现长时序环内视觉搜索多模态Agent
practical_value: '- 多模态搜索Agent可借鉴「图像发现-按需加载」两级设计：搜索阶段仅返回轻量URL+caption引用，需要时再调用FETCHIMAGE/CROPIMAGE加载，大幅降低多模态上下文消耗，适合电商商品搜图、同款识别等场景

  - 训练数据合成可复用「结构先于语言」思路：先基于事件图构建带视觉依赖的推理链，再生成对应QA，避免伪视觉依赖问题，可用于生成电商多模态导购、商品属性识别的训练数据

  - 无需RL，仅用高质量多轮轨迹SFT即可让小尺寸MLLM获得优异的长时序多模态搜索能力，8B模型仅需7K环内视觉轨迹即可获得平均+19.5的性能提升，大幅降低落地成本

  - 电商导购Agent可直接复用该框架的工具设计：整合TEXTSEARCH/IMAGESEARCH/REVERSEIMAGESEARCH等工具，支持用户拍图找商品、查穿搭搭配、验证商品真伪等长交互场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态大模型的静态参数知识无法应对知识密集、动态变化的开放世界问题，现有多模态搜索方法通常将视觉局限在输入或答案阶段，忽略了其在中间推理的作用，也缺乏长时序交互设计，导致视觉证据难以驱动后续检索，限制了交互深度和推理跨度。

### 方法关键点
- 数据合成：提出EventVoyage-VL流水线，基于多模态事件图构建带中间视觉依赖、长推理链的搜索问题，通过「结构先于语言」的设计保证视觉证据是后续检索的必要条件
- Agent框架：设计主动视觉获取机制，分离图像发现和观测，搜索阶段仅返回轻量图像引用，按需触发FETCHIMAGE/CROPIMAGE加载，降低上下文消耗
- 训练方法：仅通过高质量多轮轨迹SFT训练，无需RL，冻结视觉编码器和多模态融合层，仅微调语言主干，降低训练成本

### 关键实验
在10个多模态搜索基准上测试，对比同尺寸开源多模态搜索Agent、闭源GPT-5.5/Gemini-3.1-Pro等baseline：8B版本相对基础Agent流程平均提升19.5个百分点，30B版本平均提升17.9个百分点，在9/10的基准上取得同尺寸最优成绩，仅比闭源模型低6.1-8.6个百分点；仅增加7K合成的环内视觉轨迹，即可在长时序图像密集任务上额外获得最高11.2个点的提升。

### 最值得记住的一句话
对于长时序多模态搜索Agent，仅用带明确中间视觉依赖的高质量轨迹做SFT，无需RL即可获得媲美闭源模型的性能，同时大幅降低上下文消耗。
