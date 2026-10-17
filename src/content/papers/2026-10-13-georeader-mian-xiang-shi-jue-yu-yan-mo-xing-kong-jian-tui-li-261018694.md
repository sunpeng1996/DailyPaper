---
title: 'GeoReader: Learning Latent Geometry for Spatial Reasoning in Vision-Language
  Models'
title_zh: GeoReader：面向视觉语言模型空间推理的隐式几何学习
authors:
- Rong Li
- Shijie Li
- Jiangyong Huang
- Lingdong Kong
- Jiaming Zhou
- Dongyue Lu
- Zeying Gong
- Baoxiong Jia
- Junwei Liang
- Siyuan Huang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- A*STAR
- Peking University
- National University of Singapore
- Beijing Institute for General Artificial Intelligence
arxiv_id: '2610.18694'
url: https://arxiv.org/abs/2610.18694
pdf_url: https://arxiv.org/pdf/2610.18694
published: '2026-10-13'
collected: '2026-10-17'
category: Multimodal
direction: 多模态大模型 · VLM空间推理优化
tags:
- VLM
- Spatial Reasoning
- Geometric Representation
- Multimodal
- Fine-tuning
one_liner: 提出GeoReader框架，将几何特征转换为VLM原生可读取token，提升空间推理性能
practical_value: '- 多模态特征融合时可借鉴「先将外部特征转换为目标模型原生可读取的token表示」的思路，避免特征对齐后模型实际不使用的问题

  - 涉及空间/几何属性的多模态推荐（如家装、服饰穿搭、3D商品推荐）场景，可引入轻量几何读取模块增强VLM对3D商品的空间理解能力

  - 训练时用大模型生成的语义描述作为中间监督信号，推理阶段省略中间生成步骤，可在提升效果的同时不增加推理延迟'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有VLM难以从RGB图像中挖掘隐含的度量、多视角空间关系，传统几何特征对齐方案存在“仅对齐特征但模型不实际使用”的缺陷，零值化对齐后特征对模型精度无影响。
### 方法关键点
1. 训练轻量Geometric Readers生成连续输入token，采用冻结VLM解码的几何描述作为监督信号，确保生成的几何表征是目标VLM可原生读取的格式；
2. 冻结Reader模块固定输入接口，仅微调VLM完成空间QA任务，几何注入可根据输入query动态触发；
3. 几何描述仅作为训练监督，推理阶段无需生成几何思维链，直接基于几何token输出结果，无额外推理开销。
### 关键结果
基于Qwen3-VL-4B在MindCube-Tiny基准得分达94.3；基于Qwen3.5-9B在6个空间推理基准平均得分72.5，显著优于现有方案。
