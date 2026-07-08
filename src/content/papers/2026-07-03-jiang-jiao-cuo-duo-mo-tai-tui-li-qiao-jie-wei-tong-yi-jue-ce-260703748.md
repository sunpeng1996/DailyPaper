---
title: Bridging Interleaved Multi-Modal Reasoning as a Unified Decision Process
title_zh: 将交错多模态推理桥接为统一决策过程的BRAID框架
authors:
- Zican Hu
- Xuyang Hu
- Yiming Liu
- Zuwei Long
- Wei Liu
- Yunzhuo Hao
- Jiawei Gu
- Linjie Li
- Yu Cheng
- Zhenhong Sun
affiliations:
- Nanjing University
- Tencent Youtu Lab
- Shanghai AI Laboratory
- Tsinghua University
- Zhejiang University
arxiv_id: '2607.03748'
url: https://arxiv.org/abs/2607.03748
pdf_url: https://arxiv.org/pdf/2607.03748
published: '2026-07-03'
collected: '2026-07-08'
category: Reasoning
direction: 多模态推理 · RL联合优化
tags:
- Multi-modal Reasoning
- Reinforcement Learning
- Markov Decision Process
- Policy Gradient
- Vision-Language Model
one_liner: 提出统一MDP框架BRAID，通过单RL目标联合优化交错多模态推理的文本与图像生成链路
practical_value: '- 电商多模态导购Agent、生成式图文广告优化可复用BRAID的统一MDP思路，无需拆分文本、图像生成链路，用同一RL目标联合调优，降低流程复杂度

  - 长序列多步生成任务的信用分配问题，可借鉴VLM judge做中间步稠密反馈的方案，比如多轮对话中每一步生成的图文内容单独打分，加快收敛效率

  - 跨模态梯度传播可参考模态原生策略梯度机制，文本走token级梯度、图像走diffusion去噪路径梯度，无需统一模态空间即可联合优化，减少工程改造量'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有统一多模态模型（UMM）的RL优化仅覆盖文本生成步骤，图像生成仅依赖监督微调，策略梯度无法跨异质模态的全交错轨迹传播，RL的优化潜力未被充分释放。
### 方法关键点
1. 提出BRAID框架，将多轮文本-图像-文本推理过程建模为统一MDP，通过单一RL目标联合优化文本、视觉生成链路；
2. 计算共享的轨迹级优势，分别通过文本token、图像去噪路径的模态原生策略梯度机制传播梯度，无需统一模态空间；
3. 引入VLM judge对中间图像的推理效用打分，提供稠密轮次级反馈，解决长序列生成的信用分配问题。
### 关键结果
在空间推理、视觉感知基准测试中，BRAID效果持续优于各类基线方案，验证了统一MDP建模+视觉思维指导的优化有效性。
