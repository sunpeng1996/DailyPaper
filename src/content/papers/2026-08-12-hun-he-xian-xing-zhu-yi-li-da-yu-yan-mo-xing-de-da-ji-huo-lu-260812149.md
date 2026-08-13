---
title: 'Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attention
  Spikes and Inter-Spike Plateaus'
title_zh: 混合线性注意力大语言模型的大激活规律：注意力前尖峰与峰间平台
authors:
- Zunhai Su
- Bohan Sun
- Xialie Zhuang
- Shuibai Zhang
- He Xiao
- Jing Xiong
- Hengyuan Zhang
- Zhongzhu Zhou
- Tiantian Zhang
- Ngai Wong
affiliations:
- Startlux
- Tsinghua University
- University of Chinese Academy of Sciences
- The University of Hong Kong
- University of Sydney
arxiv_id: '2608.12149'
url: https://arxiv.org/abs/2608.12149
pdf_url: https://arxiv.org/pdf/2608.12149
published: '2026-08-12'
collected: '2026-08-13'
category: LLM
direction: LLM 混合线性注意力可解释性研究
tags:
- Hybrid Linear Attention
- Massive Activations
- Pre-Attention Spike
- Inter-Spike Plateau
- LLM Interpretability
one_liner: 首次系统揭示混合线性注意力LLM中两类架构对齐的大激活形态及统一生命周期机制
practical_value: '- 部署Qwen3.5、Kimi Linear等混合注意力LLM做Rec/Agent服务时，可针对全注意力层前的Pre-Attention
  Spike做针对性outlier感知KV cache量化，大幅降低量化误差

  - 自研混合注意力小模型用于长上下文推荐场景时，可优先给全注意力层加输出门控，能在不损失效果的前提下大幅降低大激活幅度，提升数值稳定性

  - 混合注意力LLM推理优化时，可根据PAS/ISP的固定层位分布做层间混合精度调度：尖峰/平台层用FP16，其余层用INT4/INT8，平衡推理 latency
  与效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
混合线性注意力（HLA）LLM结合线性注意力的长上下文推理效率与全注意力的强建模能力，是Qwen3.5、Kimi等当前主流开源大模型的标配架构，但层间混合调度如何重塑内部激活动力学长期不明确；大激活（MAs）作为与注意力机制强耦合的核心内部特征，是模型可解释性、低比特量化、推理优化的关键抓手，此前仅在纯全注意力LLM中被研究，HLA场景下的演化规律完全空白。
### 方法关键点
- 提出注意力sink引导的大激活追踪方法，解决HLA中单纯依赖幅度排序无法跨层稳定追踪大激活的问题，以共识注意力sink为锚点跟踪对应token的跨层最大激活幅度
- 实验覆盖5类主流线性注意力架构（RetNet、HGRN、GLA、DeltaNet、GDN）、6种混合比例配置、5类数据域，验证范围涵盖1.2B~397B参数的主流开源混合模型
- 设计受控预训练实验（340M/1.3B规模GDN模型）追踪大激活形态的训练阶段演化，结合符号化离群点分析推导底层统一生命周期机制
### 关键结果数字
- 12:1混合比例（每12层线性注意力插1层全注意力）下，5类线性注意力架构的sink-尖峰对齐率均超过99.4%，大激活稳定出现在全注意力层前形成Pre-Attention Spike（PAS）
- 随着全注意力密度提升，峰间保留度（ISR）从12:1的7.2%~27.3%逐步提升到3:1的77.8%~92.5%，相邻尖峰间形成持续的Inter-Spike Plateau（ISP），全注意力极限下收敛为全层稳定大激活形态
- 全注意力输出门控可大幅降低PAS幅度，但不会消除其层间分布规律；移除GDN门控仅带来激活幅度的小幅提升

**最值得记住的结论**：混合线性注意力LLM的大激活形态完全由全注意力层的位置与密度决定，遵循统一的写入-sink-取消生命周期，仅在取消时机上存在差异。
