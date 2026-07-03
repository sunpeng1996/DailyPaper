---
title: 'WattGPU: Predicting Inference Power and Latency on Unseen GPUs and LLMs'
title_zh: WattGPU：预测未知GPU与LLM组合的推理功耗与延迟
authors:
- Mauricio Fadel Argerich
- Jonathan Fürst
- Marta Patiño-Martínez
affiliations:
- Universidad Politécnica de Madrid
- Zurich University of Applied Sciences
arxiv_id: '2607.02391'
url: https://arxiv.org/abs/2607.02391
pdf_url: https://arxiv.org/pdf/2607.02391
published: '2026-07-02'
collected: '2026-07-03'
category: LLM
direction: LLM推理部署 · 功耗延迟预测
tags:
- LLM Inference
- Power Prediction
- Latency Prediction
- GPU Scheduling
- XGBoost
one_liner: 仅用公开GPU和LLM元数据，无需 profiling 即可预测未知硬件上的LLM推理性能
practical_value: '- 部署LLM驱动的推荐/Agent服务时，可直接复用WattGPU工具预选型GPU，在满足ITL SLA的前提下最多降43%推理功耗，无需提前租卡
  profiling，节省选型成本

  - 特征工程思路可复用：做跨硬件/模型的性能预测时，优先用公开静态特征（如GPU显存带宽、LLM参数量）+ 简单推导特征（如带宽延迟、计算延迟），无需依赖运行时数据即可实现不错的泛化性

  - 做LLM服务成本优化时，可参考其GPU/LLM排序能力，Kendall τ≥0.76的准确率足够支撑异构GPU集群的任务调度，将推理任务分配到能效最优的GPU上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM推理占数据中心能耗比例快速上升，中小规模部署普遍缺乏多GPU-LLM组合的profiling能力，无法通过最优硬件选型降本节能；现有预测方法依赖运行时profiling数据，无法泛化到训练阶段未见过的GPU，硬件选型效率极低。

### 方法关键点
- 仅使用两类公开静态特征：GPU厂商规格参数（TDP、显存带宽、FP16算力等）、Hugging Face可查的LLM元数据（参数量、层数、注意力头数等），补充3个推导特征（升压比、带宽延迟、计算延迟），无需任何运行时profiling数据
- 功耗预测模型将目标值除以GPU TDP做归一化，提升对未知GPU的泛化能力，功耗与ITL两个预测模型均采用XGBoost实现，通过网格搜索调优超参

### 关键实验结果
在包含8款NVIDIA服务器级GPU、42款0.1B-27B参数量密集LLM的Watt Counts数据集上验证，对比TDP、Roofline等物理基线：
- 未知GPU场景下，功耗预测离线MdAPE≤3.4%、服务器场景≤13.5%，ITL预测服务器场景≤8.5%，GPU排序Kendall τ≥0.76
- 服务器场景下，未知LLM-GPU组合的MdAPE较基线降低约4倍，完全未知GPU场景降低约2倍

最值得记住的一句话：LLM推理硬件选型不能只看TDP或单位功耗算力，比如部署Llama3.1 8B低负载服务时，选A30比H100能降43%功耗同时满足25ms ITL SLA
