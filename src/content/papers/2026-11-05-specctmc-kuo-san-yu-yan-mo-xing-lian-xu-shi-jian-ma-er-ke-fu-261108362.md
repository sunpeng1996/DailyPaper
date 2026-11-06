---
title: 'SpecCTMC: Exact Speculative Simulation of Diffusion Language Model Continuous-Time
  Markov Chains'
title_zh: SpecCTMC：扩散语言模型连续时间马尔可夫链精确投机模拟方法
authors:
- Siva Rajesh Kasa
- Yasong Dai
- Sumit Negi
- Hongdong Li
affiliations:
- Australian National University
- Amazon
- National University of Singapore
arxiv_id: '2611.08362'
url: https://arxiv.org/abs/2611.08362
pdf_url: https://arxiv.org/pdf/2611.08362
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: 扩散LLM · 推理采样加速
tags:
- Speculative Decoding
- Diffusion LLM
- CTMC
- Inference Acceleration
- Distribution-Preserving
one_liner: 无需额外草稿模型的无训练投机采样器，降低扩散LLM推理成本同时严格保生成分布
practical_value: '- 扩散LLM做生成式推荐文案、商品描述生成时，可直接复用SpecCTMC的无训练加速逻辑，无需额外微调或小模型，降低推理延迟同时100%保留原有生成质量，适配对生成一致性要求高的业务场景

  - 投机采样的验证+残差修正框架可迁移到其他生成式推荐模型的推理优化，比如基于掩码扩散的Semantic ID生成任务，在保分布的前提下减少顺序推理步数

  - 业务侧部署时可根据GPU显存（如B200/L40S的差异）自适应调整投机深度，短序列生成场景可堆高超参获得更大加速比，长序列场景降低深度避免显存溢出

  - 多候选生成场景（如推荐候选集扩量、多版文案试投）可复用其随机采样加速能力，在不改变Pass@k的前提下降低集群计算成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
掩码扩散语言模型（MDLM）支持非左到右的并行文本生成，在长文本生成、多模态生成场景优势显著，但现有精确连续时间采样需每生成1个token执行1次顺序模型推理，成本极高无法落地；近似采样法又会引入分布偏移，破坏token间依赖关系，无法适配对生成质量、分布一致性要求高的业务场景（如代码生成、推理、生成式推荐）。

### 方法关键点
- 无训练、无独立草稿模型：直接复用已计算的模型预测结果生成连续多步的候选token更新序列，并行评估所有中间状态
- 事件时间预采样：利用吸收掩码扩散的特性，事件时间仅和扩散时间、剩余掩码数相关，和已解掩码token无关，可预先采样所有事件时间，投机过程仅针对token位置和取值优化
- 精确接受-修正机制：逐token验证候选，首次拒绝时从残差分布采样修正token，重启下一轮投机，理论证明完全保留原CTMC的事件时间、生成顺序、token取值联合分布

### 关键实验
在LLaDA-8B-Instruct、Dream-v0-Instruct-7B两个主流扩散LLM上跨GSM8K、MBPP等5个基准测试，相比直接CTMC采样，顺序模型推理次数降低1.73~4.38倍，NVIDIA B200上实际端到端延迟最高提升2.88倍；多模态扩散LLM LLaDA-V上推理次数最多降低6.69倍，所有场景下生成准确率和基线完全持平，无分布损失。

最值得记住的一句话：扩散LLM的推理加速无需依赖微调、小模型草稿，仅靠采样流程的架构优化就能实现零质量损失的数倍效率提升
