---
title: 'Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion
  VLMs'
title_zh: 按需调用视觉：证书引导的高效扩散视觉语言模型视觉路由方法
authors:
- Donghyeon Cho
- Joowon Kim
- Seungho Shin
- Eunho Yang
affiliations:
- KAIST
- AITRICS
arxiv_id: '2610.36671'
url: https://arxiv.org/abs/2610.36671
pdf_url: https://arxiv.org/pdf/2610.36671
published: '2026-10-26'
collected: '2026-10-30'
category: Multimodal
direction: 多模态大模型 · 推理效率优化
tags:
- Diffusion VLM
- Decoding Optimization
- Computation Efficiency
- Visual Routing
- KV Cache
one_liner: 提出无需训练的LOWN解码策略，动态决策扩散VLM每步是否处理图像，大幅降低解码算力
practical_value: '- 电商图文生成、商品多模态理解场景可复用「先无模态预测再校验是否调用高成本模态」的思路，大幅降低推理成本几乎无损效果

  - 推理优化可借鉴「自适应决策是否加载重计算模块」的设计，无需额外训练/调参即可落地，还能与KV cache、剪枝等现有优化正交叠加

  - 扩散类生成模型的解码优化可直接复用LOWN的动态step决策逻辑，无需固定调度策略，适配不同任务的模态依赖度差异'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
Diffusion VLM（DVLM）每步去噪需处理全部输入，视觉token占输入的89~97%，解码算力大部分浪费在重复处理同一张图像；现有视觉token剪枝会丢失信息，且仍需每步处理剩余视觉token；实测仅22.8%的解码步真的需要图像输入，最低仅7.9%。

### 方法关键点
提出LOWN无训练解码策略，每步先无图像预测masked token，和上一次带图像的预测做校验：一致则直接复用旧结果、不解码图像，不一致才加载视觉输入计算；自适应决定每步unmask的token数，无需固定调度策略适配不同任务。

### 关键结果
10个基准测试上保留LLaDA-V 99.6%的效果，平均解码FLOPs仅为原生方案的35.3%；可泛化到所有基于LLaDA的DVLM，和视觉token剪枝正交兼容，搭配KV cache可进一步提效。
