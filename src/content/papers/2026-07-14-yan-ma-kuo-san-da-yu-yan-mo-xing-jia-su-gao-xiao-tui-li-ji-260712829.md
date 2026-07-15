---
title: 'Accelerating Masked Diffusion Large Language Models: A Survey of Efficient
  Inference Techniques'
title_zh: 掩码扩散大语言模型加速：高效推理技术综述
authors:
- Daehoon Gwak
- Minhyung Lee
- Junwoo Park
- Jaegul Choo
arxiv_id: '2607.12829'
url: https://arxiv.org/abs/2607.12829
pdf_url: https://arxiv.org/pdf/2607.12829
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: 大语言模型 · 推理优化技术综述
tags:
- Diffusion LLM
- Inference Acceleration
- Latency Decomposition
- Parallel Generation
- Survey
one_liner: 提出dLLM统一延迟分解框架，系统梳理三类推理加速技术，给出可复现基准测试指南
practical_value: '- 做生成式推荐/Agent推理场景可优先评估dLLM替代传统自回归LLM，利用并行生成特性降低长文本/多候选生成的延迟

  - 可复用论文提出的延迟分解框架，拆解业务侧LLM推理链路的算法/架构/系统层瓶颈，针对性制定优化优先级

  - 做LLM相关优化效果验证时，参考其可复现benchmark设计准则，避免不同维度优化的混淆对比，提升上线收益评估准确性'
score: 8
source: arxiv-cs.LG
depth: abstract
---

### 动机
Diffusion大语言模型（dLLM）相较传统自回归LLM具备并行生成的理论效率优势，但实际落地需要适配扩散特性的专属推理优化机制，现有技术分散在算法、架构、系统多个维度，端到端延迟的权衡关系难以拆解，不同技术的基准对比缺乏统一标准，无法指导落地选型。
### 方法关键点
1. 提出统一的dLLM延迟分解框架，解耦算法、架构、系统三个层级的延迟影响因子，明确各维度优化的独立作用；
2. 从算法创新、架构与系统优化、推理时动态伸缩三个维度，系统性分类梳理现有dLLM推理加速技术；
3. 给出可复现的基准测试设计指南，总结并行生成能力落地的开放挑战。
### 关键结果
梳理了数十种现有dLLM加速技术的适用场景，明确了不同业务负载下的技术选型路径，澄清了过往benchmark中常见的混淆变量问题。
