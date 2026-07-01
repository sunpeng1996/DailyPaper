---
title: 'One Forward Beats Two: InnerZoom for Accurate and Efficient GUI Grounding'
title_zh: 单前向优于双前向：面向精准高效GUI定位的InnerZoom框架
authors:
- Chen Liu
- Ling Chen
- Hanzhang Zhou
- Liangyu Chen
- Chenglin Cai
- Xin Yu
- Steven Hoi
- Yue Wang
affiliations:
- Tongyi - MAI
arxiv_id: '2606.30084'
url: https://arxiv.org/abs/2606.30084
pdf_url: https://arxiv.org/pdf/2606.30084
published: '2026-06-28'
collected: '2026-07-01'
category: Agent
direction: Agent GUI交互 · 高效视觉定位优化
tags:
- MLLM
- GUI Grounding
- Efficient Inference
- Cross-layer Fusion
- Autoregressive Generation
one_liner: 提出单前向跨层证据桥接框架InnerZoom，提升GUI定位精度的同时降低推理成本
practical_value: '- 电商RPA、智能运营类Agent业务可直接复用InnerZoom的单前向跨层证据复用思路，替代传统双前向裁剪重跑方案，在提升GUI元素定位精度的同时降低推理延迟与算力成本

  - 生成式任务中若存在中间层已提取到有效特征但最终预测丢失的问题，可借鉴跨层证据状态的「保留-精炼-重注入」机制，提升最终输出准确率

  - 资源受限的端侧多模态推理场景，可参考该框架的低算力优化思路，无需额外增加前向次数即可实现任务效果提升'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有基于MLLM的GUI定位方法多采用自回归坐标生成，诊断分析发现中间解码器层已出现目标区域感知能力，但未被保留到最终坐标预测；传统ZoomIn双前向方案需裁剪重跑，精度提升但显著增加延迟与算力成本。
### 方法关键点
提出单前向跨层证据桥接框架InnerZoom，将原始前向过程中的目标相关线索转换为紧凑的跨层证据状态，在后续解码层全程保留、精炼并重新注入该状态引导坐标预测，无需额外前向pass。
### 关键结果
InnerZoom-4B在6个GUI定位基准上均达到SOTA，在OSWorld-G、UI-Vision、OSWorld-GR、MMBench-GUI上分别超出此前最优结果4.1、3.2、2.9、2.3分；同4B配置下，平均超出SFT+RL基线5.3分，超出双前向ZoomIn平均1.3分，端到端延迟最高降低31.8%，TFLOPs降低约29%。
