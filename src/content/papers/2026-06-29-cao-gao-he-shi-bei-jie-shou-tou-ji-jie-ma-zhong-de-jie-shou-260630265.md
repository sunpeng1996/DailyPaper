---
title: When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding
title_zh: 草稿何时被接受？投机解码中的接受准则理论
authors:
- Aaryam Sharma
affiliations:
- Independent Researcher
- University of Waterloo
arxiv_id: '2606.30265'
url: https://arxiv.org/abs/2606.30265
pdf_url: https://arxiv.org/pdf/2606.30265
published: '2026-06-29'
collected: '2026-06-30'
category: LLM
direction: LLM推理加速 · 投机解码理论
tags:
- Speculative Decoding
- LLM Inference
- KL Divergence
- Acceptance Criterion
- Tree Decoding
one_liner: 给实际常用的多种投机解码接受规则推导了基于KL散度的可证明接受保证证书
practical_value: '- 训练投机解码draft模型时，可将本文推导的KL证书阈值作为训练约束，保证给定KL训练目标下的接受率，优化训练目标设计

  - 调参时放宽接受阈值到t>0.1（加法放松）、α<0.5（乘法放松）才能获得明显接受率提升，小阈值几乎无增益

  - 树分支投机解码每级保留top-m候选，可将接受证书上限从log2≈0.69提升到log(m+1)，m=8时可保证接受长度提升超10倍，是低延迟场景的高性价比方案

  - 对Agent等低延迟需求场景，Medusa式熵阈值接受可在输出质量变化不大的前提下，大幅提升低置信度步的接受率，适合工程落地'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现有投机解码的理论分析大多聚焦保持目标模型输出分布的随机采样场景，但工业界实际部署大多采用贪心解码、放松接受规则、树候选集等确定性局部推理方案，这类方案缺乏可证明的接受概率理论保证，无法指导draft模型训练和超参调优，需要填补这一理论空白。

**方法关键点**：
- 发现多数工业界常用的接受规则，其拒绝域均可表征为目标模型输出分布的低水平集，据此将接受问题转化为计算「导致拒绝发生的最小KL散度」，得到精确的接受保证证书：若目标和draft分布的KL小于证书，则一定接受。
- 分别推导了严格贪心、加法放松、乘法放松、top-m放松、熵阈值接受等单token场景的精确证书和紧致上下界，证明单token场景证书上限恒为log2≈0.69。
- 将框架扩展到树贪心解码，推导了每级保留top-m候选场景的精确接受条件，证明证书上限为log(m+1)，随候选数增加提升阈值上限。

**关键实验**：在Qwen3 1.7B/4B、UltraChat 200k数据集上验证：严格贪心的5%分位证书仅0.006~0.007，Medusa熵接受提升至0.375~0.378，树m=8提升至0.531~0.663；当KL上限ϵ=0.3时，严格贪心平均可保证接受长度仅2.9，树m=8提升至36+。

**核心结论**：放松接受规则和树分支可在可控质量损失下，大幅提升投机解码的接受率和推理吞吐量
