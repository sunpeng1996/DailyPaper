---
title: 'LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models'
title_zh: LoopSkim：面向循环语言模型的无损多深度推测解码
authors:
- Muhan Xiao
- Shijian Li
affiliations:
- Zhejiang University
arxiv_id: '2611.19896'
url: https://arxiv.org/abs/2611.19896
pdf_url: https://arxiv.org/pdf/2611.19896
published: '2026-11-15'
collected: '2026-11-17'
category: LLM
direction: LLM推理优化 · 推测解码
tags:
- Speculative Decoding
- Looped LLM
- Inference Acceleration
- Lossless Decoding
- Gumbel Sampling
one_liner: 提出无需训练的循环语言模型无损多深度推测解码方法，速度超现有基线最高2.08倍
practical_value: '- 业务中若使用循环轻量LLM做推荐文案生成、Query理解、Agent推理，可直接复用LoopSkim解码逻辑，无需额外训练即可获得1.6x+推理速度提升，降低在线延迟

  - 可借鉴固定Gumbel噪声设计，在商品文案生成、Agent确定性决策等要求输出一致的场景下，既通过推测解码提速，又保证输出与原生AR解码完全一致，规避合规风险

  - 多深度中途校验思路可迁移到MoE、LoRA微调大模型的推测解码场景，无需等全层计算完成即可提前校验错误draft，减少无效计算，提升小batch推理吞吐量'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
循环语言模型（如Ouro、Raven）通过共享权重块多次迭代实现了小参数效果媲美10x+大模型的能力，但自回归（AR）解码需要跑完所有迭代步才能输出下一个token，延迟极高；现有流水线自推测解码方案要么单步仅能生成1个token效率低下，要么多token draft错误后需回滚全量计算开销大，且采样场景下无法保证输出无损。
### 方法关键点
- 多深度推测机制：利用循环LM本身的多层迭代作为天然校验节点，每个迭代步的浅读头直接校验draft token，发现错误立刻替换并截断后续无效计算，无需额外前向传播
- 固定随机采样：对每个生成位置预先生成固定Gumbel噪声，所有深度的采样都复用同一噪声，保证采样场景下输出与原生AR完全一致，解码过程严格无损
- 双draft链设计：默认复用prompt n-gram匹配生成draft token，完全无需训练；可选训练1层轻量draft头进一步提升draft准确率，不会影响输出一致性
### 关键结果
在Ouro（1.4B/2.6B）、Raven系列共5款模型上测试数学推理、代码生成、常识推理等任务，对比基线LoopSpec、CopyLoop：无训练版LoopSkim平均速度是LoopSpec的1.73倍，同引擎下速度是LoopSpec调度方案的1.64~2.08倍；加16.8M参数的轻量draft头后平均提速比提升到1.99倍，全场景输出与AR解码一致。
### 核心结论
循环结构模型的推测解码完全可以复用自身中间层输出做校验，无需额外引入小模型做draft，即可实现无损提速。
