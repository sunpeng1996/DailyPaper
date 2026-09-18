---
title: Parallelism, critical windows, and separations among diffusion language models
title_zh: 《扩散语言模型的并行性、临界窗口及三类范式的性能分隔》
authors:
- Sitan Chen
- Liye Wang
affiliations:
- Harvard University
- Tsinghua University
- Simons Institute for the Theory of Computing
arxiv_id: '2609.20539'
url: https://arxiv.org/abs/2609.20539
pdf_url: https://arxiv.org/pdf/2609.20539
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: 扩散大语言模型 并行性理论分析
tags:
- Diffusion LLM
- Parallelism
- Masked Diffusion
- Uniform Diffusion
- Gaussian Diffusion
one_liner: 从理论层面证明三类主流扩散大语言模型的并行性差异及内在成因
practical_value: '- 做生成式推荐/广告文案生成时，若追求高并行生成效率，优先选型Uniform/Gaussian diffusion LLM，可比masked
  diffusion减少O(√d)量级的推理步数

  - 扩散LLM采样步数可适配目标分布的对偶总相关度优化，无需硬卡context length上限，短序列文案/推荐理由生成可进一步压缩推理步数

  - 业务落地dLLM做生成任务时，可根据临界窗口特性调整mask策略，缓解窄临界窗口带来的并行度损失'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
扩散大语言模型（dLLM）相比自回归LLM并行生成效率优势明显，但masked、uniform、Gaussian三类主流dLLM范式的并行性差异缺乏理论层面的量化对比依据。

### 方法关键点
引入对偶总相关度作为分布内在复杂度度量，对三类dLLM的采样前向传播步数边界、临界窗口特性进行严格的理论推导与对比。

### 关键结果
1. uniform与Gaussian diffusion的采样步数仅和目标分布的对偶总相关度正相关，远小于context length，此前仅masked diffusion被验证具备该特性
2. 随机经验测度场景下，uniform/Gaussian diffusion仅需$	ilde{	heta}(	extrm{d})$步即可完成采样，而masked diffusion在近似得分oracle下需要$	ilde{	extrm{Ω}}(	extrm{d})$步，并行效率差异首次得到理论证明
3. 并行性差异本质来自masked diffusion的采样临界窗口渐近宽度窄于另外两类范式，和传统认知的token提交约束无关
