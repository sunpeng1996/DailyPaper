---
title: 'TRACE: Trajectory-robust Admission with Evidence Ordering for Efficient GUI
  Agents'
title_zh: TRACE：面向高效GUI Agent的轨迹鲁棒准入与证据排序框架
authors:
- Yuhao Wang
- Mu Qiao
- Xindong Zhang
- Yunzhi Zhuge
- Lei Zhang
- Huchuan Lu
affiliations:
- Dalian University of Technology
- OPPO Research Institute
- The Hong Kong Polytechnic University
arxiv_id: '2609.10297'
url: https://arxiv.org/abs/2609.10297
pdf_url: https://arxiv.org/pdf/2609.10297
published: '2026-09-08'
collected: '2026-09-15'
category: Agent
direction: GUI Agent · 视觉KV cache压缩
tags:
- GUI Agent
- KV Cache
- Visual Token Pruning
- Training-free
- Inference Optimization
one_liner: 提出训练免微调的TRACE框架，大幅降低多步GUI Agent推理时延与内存占用同时保持性能
practical_value: '- 做交互类多模态Agent（如电商导购Agent、自动化操作Agent）时，可复用LIP布局先验模块，无需训练即可提升视觉token剪枝后操作区域的保留率，避免后续操作找不到交互元素

  - 多轮交互场景的KV cache优化可直接套用MKC单调收缩机制，历史帧仅裁剪无需重编码，实测可降59% TTFT、58% KV内存，工程改造成本低

  - 多模态输入的token排序可借鉴NEO嵌套证据排序思路，融合先验、相关性、新颖度三个维度打分，不同裁剪预算直接取前缀，无需每次重选

  - 高分辨率界面的token裁剪可叠加NCR原生覆盖修复策略，当前帧用步长采样、历史帧用区域聚类取中心，低预算下避免空间覆盖坍塌导致精度暴跌'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多步GUI Agent随交互轨迹拉长，历史截图视觉token持续累积，推理时延与内存占用激增；现有训练免微调的视觉token剪枝为不可逆操作，丢弃后无法恢复，且未考虑未来未知操作的交互区域覆盖，低预算下精度暴跌。
### 方法关键点
- Layout-derived Interaction Prior (LIP)：用UI检测器提取可交互区域，计算熵、对比度、包含度、共振度生成与query无关的交互先验，优先保留操作区域token
- Nested Evidence Ordering (NEO)：融合交互先验、指令相关性、特征新颖度生成嵌套token排序，不同裁剪预算直接取前缀，无需重选
- Native-token Coverage Repair (NCR)：当前帧步长采样、历史帧区域聚类取中心补全空间覆盖，低预算下避免重要区域零token
- Monotone KV Contraction (MKC)：历史帧仅裁剪保留排序前缀，无需重编码，KV缓存单调收缩，全程复用已编码特征
### 关键实验
在6个GUI benchmark（含ScreenSpot-v2、Mind2Web等单/多步任务）上对比10+SOTA剪枝方法：GUI-Owl-1.5-8B温和预算（单步10%token/多步当前50%/历史10%）下保留78.7%全量性能，紧凑预算（单步5%/多步当前25%/历史5%）下保留61.1%性能；端到端推理降59% TTFT、58% KV缓存占用，跨2B/7B/8B多尺度模型均有效。
### 核心insight
多轮交互场景的视觉token剪枝不能仅关注当前指令相关性，提前为可交互区域加权并保留嵌套排序，才能同时兼顾效率与未来操作的鲁棒性
