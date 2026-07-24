---
title: Error Certificates for KV-Cache Eviction via Randomized Design
title_zh: 基于随机化设计的KV缓存逐出误差证书
authors:
- Peng Xie
affiliations:
- Technical University of Munich
arxiv_id: '2607.21475'
url: https://arxiv.org/abs/2607.21475
pdf_url: https://arxiv.org/pdf/2607.21475
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: LLM推理优化 · KV cache逐出
tags:
- KV-cache
- Long-Context Inference
- Eviction Policy
- Randomized Sampling
- Error Attribution
one_liner: 证明确定性KV缓存逐出无法估计自身误差，提出随机采样方案生成可实现故障归因的误差证书
practical_value: '- 做长上下文Agent（电商多轮导购、用户历史记忆压缩）的流式KV缓存时，可采用「确定性保留高优token+泊松尾部采样+Hajek
  logit校正」方案，25%-50%预算下无精度损失，还可感知逐出误差

  - 需做LLM服务故障归因时，直接用本文的误差证书区分缓存导致的错误与模型固有能力不足，比输出置信度AUC高20个百分点左右，无需额外跑两次采样对比

  - 预fill阶段已知query的KV压缩场景（如搜索问答、商品文案生成），25%-50%缓存预算下确定性/随机逐出几乎无精度损失，无需额外监控，可直接落地

  - 流式压缩（多轮对话、Agent长记忆）场景下用误差证书做重计算调度，相同重算预算下准确率比随机/置信度门控高1.9-3.7个百分点，可有效降低服务错误率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文LLM推理中KV缓存随上下文线性增长，内存占用极高，主流确定性KV逐出方案（H2O、SnapKV等）仅按重要性保留top-k token，但无法感知逐出带来的精度损失，甚至存在静默故障：修改已逐出token的value，所有保留的状态完全不变，但真实输出误差可任意放大，对高可靠LLM服务（电商客服、搜索问答、推荐理由生成）存在不可控风险。
### 方法关键点
- 理论证明确定性KV逐出的误差不可识别：任何仅基于保留状态的误差估计器都不具备一致性，无法准确估计真实输出误差
- 采用「确定性集+泊松尾部采样」逐出策略：高重要性token（注意力sink、最近32个token、分数top slice）100%保留，尾部token按与分数成正比的概率π_i做泊松采样保留
- 无偏差校正与误差证书：给保留的尾部token logit加log(1/π_i)实现Hajek校正，消除采样偏差；基于保留集计算无偏方差估计生成每步误差证书，无训练、无新增参数，仅需O(尾部保留token数)的额外计算
### 关键结果
在LongBench 6k/16k上下文、4个主流开源LLM（Qwen2.5、Llama3.1、Mistral等）上测试，对比H2O、SnapKV、StreamingLLM等基线：
1. 误差证书与真实注意力输出误差的Spearman相关系数达0.94~0.98，覆盖率约97%，无精度损失
2. 区分逐出诱导故障与模型固有故障的AUC达0.73~0.75，而输出置信度仅0.47~0.54，接近随机
3. 流式压缩场景下用误差证书做重计算调度，25%重算预算下准确率比随机/置信度门控高1.9~3.7个百分点

> 最值得记住的结论：随机化给KV缓存带来的不是更高的逐出精度，而是压缩通道误差的可识别性，核心价值是归因能力，而非故障预测能力
