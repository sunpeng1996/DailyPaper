---
title: 'UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using
  Multi-Structural Internal Representations'
title_zh: UniProbe：基于多结构内部表征的LVLM可学习Token级幻觉检测器
authors:
- Dvir Samuel
- Guy Bar-Shalom
- Fabrizio Frasca
- Ethan Fetaya
- Yftah Ziser
- Gal Chechik
- Haggai Maron
affiliations:
- NVIDIA Research
- Technion
- Bar-Ilan University
- University of Groningen
arxiv_id: '2608.10835'
url: https://arxiv.org/abs/2608.10835
pdf_url: https://arxiv.org/pdf/2608.10835
published: '2026-08-11'
collected: '2026-08-17'
category: Multimodal
direction: 多模态大模型 · Token级幻觉检测
tags:
- LVLM
- Hallucination Detection
- GNN
- ViT
- GRU
- Lightweight Fine-tuning
one_liner: 面向多架构LVLM的轻量可学习Token级幻觉检测器，解码降55%幻觉仅增6%延迟
practical_value: '- 多模态导购Agent、图文生成式推荐场景可复用该Token级幻觉检测思路，快速定位生成内容中不符合商品图的错误描述，无需丢弃整段生成结果

  - 可借鉴「冻结基座+轻量结构感知模块（GNN/ViT/GRU组合）提取内部表征」的范式，用极低微调成本适配业务侧多模态大模型的幻觉检测需求

  - 流式检测+错误Token重采样的解码策略可直接复用到生成式内容生产链路，仅增加6%延迟即可大幅降低多模态生成内容的错误率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LVLM在图文推理、对话场景性能优异，但常生成不符合视觉输入的幻觉内容，现有检测方案要么需全量微调成本高，要么依赖外部验证器忽略生成过程，丢弃了空间、序列、关系结构信息。

### 方法关键点
1. 轻量检测器UniProbe冻结LVLM基座，仅用单次前向传播的异构计算轨迹建模，基于图像块、Query Token、生成Token及注意力权重构建有向图；
2. 交替使用GNN（建模关系）、ViT（建模2D视觉结构）、GRU（建模响应序列）三类结构感知模块，融合多维度证据；
3. 支持流式检测解码，生成时实时识别幻觉Token并重采样，配套自适配策略对齐LVLM生成特性。

### 关键结果
跨多种LVLM基座取得SOTA的Token级、物体级幻觉检测效果，解码阶段物体幻觉最多降低55%，延迟仅为标准生成的1.06倍。
