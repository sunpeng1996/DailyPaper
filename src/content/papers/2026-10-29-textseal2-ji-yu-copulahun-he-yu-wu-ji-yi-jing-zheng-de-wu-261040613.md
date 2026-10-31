---
title: 'TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless
  Races'
title_zh: TextSeal2：基于Copula混合与无记忆竞争的无失真LLM水印
authors:
- Tom Sander
- Pierre Fernandez
- Itai Gat
- Haiming Bao
- Jiaxin Shi
- Jason Park
- Valeriu Lacatusu
- Sylvestre-Alvise Rebuffi
- Hongyan Chang
- Hady Elsahar
affiliations:
- Meta Superintelligence Labs
arxiv_id: '2610.40613'
url: https://arxiv.org/abs/2610.40613
pdf_url: https://arxiv.org/pdf/2610.40613
published: '2026-10-29'
collected: '2026-10-31'
category: LLM
direction: LLM安全 · 生成内容水印技术
tags:
- LLM Watermarking
- Speculative Decoding
- Gaussian Copula
- Text Generation
- Content Governance
one_liner: 提出支持推测解码的无失真LLM水印方案TextSeal2，检测准确率大幅优于现有方案
practical_value: '- 电商/广告场景下LLM生成的营销文案、客服回复可直接接入该水印方案，无推理延迟，不影响生成内容多样性，满足合规要求

  - 针对业务中常用的推测解码加速生成场景，该方案不降低接受率、水印信号不丢失，无需改造现有推理链路即可落地

  - 多密钥混合机制可支持业务侧同时嵌入内部溯源密钥和合规要求的公共水印，互不干扰检测准确率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM水印方案要么损失生成多样性、增加推理延迟，在推测解码场景下水印信号易丢失；前代TextSeal双密钥路由机制检测效率低，无法满足大规模生成场景的合规、性能要求。
### 方法关键点
1. 基于高斯Copula将多个密钥合并为单个虚拟密钥，耦合新鲜噪声实现多密钥无损嵌入，避免检测得分稀释
2. 采用无记忆指数竞争机制验证推测解码的草稿，被拒绝的草稿替换token仍保留相同密钥水印，不改变推测解码接受率
3. 无后logits优化步骤，生成过程无额外推理延迟，完全保留原模型输出分布和多样性
### 关键结果数字
- 相同输出多样性、$10^{-3}$误检率下，100token文本检测率比TextSeal高8~22个百分点，性能与textGrain相当且无需后优化
- 相同推测解码接受率下，200token文本检测率比TextSeal高18个百分点、比textGrain高22个百分点
