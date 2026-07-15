---
title: 'Less Experts, Faster Decoding: Cost-Aware Speculative Decoding for Mixture-of-Experts'
title_zh: 少专家、快解码：面向MoE模型的成本感知推测解码方法
authors:
- Jincheng Xie
- Runheng Liu
- Heyan Huang
- Yawen Ling
- Hanbin Dai
- Yu Zheng
- Wen Hu
arxiv_id: '2607.12696'
url: https://arxiv.org/abs/2607.12696
pdf_url: https://arxiv.org/pdf/2607.12696
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: MoE大语言模型 推理解码效率优化
tags:
- MoE
- Speculative Decoding
- LLM Inference
- Decoding Optimization
- Cost-Aware
one_liner: 提出成本感知的EcoSpec推测解码框架，无需修改目标模型即可大幅提升MoE大模型的解码效率
practical_value: '- 部署大参数量MoE LLM做推荐文案生成、Agent意图推理时，可直接复用EcoSpec框架降低推理时延，无需调整原模型权重，仅修改解码逻辑即可，落地门槛低

  - 做MoE模型推理优化时，可参考「专家激活成本+token接受率」联合做draft选择的思路，替代纯置信度选draft的策略，降低显存访问开销

  - 轻量专家预测器+动态专家缓存的设计可复用到RAG、多轮对话等场景的MoE推理链路，进一步降低高频业务请求的响应延迟'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
稀疏MoE是LLM规模化扩容的核心路径，但现有推测解码（SD）仅优化draft token的接受概率，高置信度draft token常路由到离散专家，引发「专家散射」问题，大幅提升专家权重显存访问开销，抵消SD的加速收益。

### 方法关键点
提出EcoSpec成本感知推测解码框架：1）新增轻量专家预测器，预估计draft token的边际专家激活成本；2）设计动态专家buffer，draft选择时优先兼顾高接受率、复用当前验证集已激活专家的路径，无需修改目标模型的验证规则。

### 关键结果
在DeepSeek-V3.1（671B）、Qwen3-235B-A22B、GPT-OSS-120B三个大规模MoE模型上，覆盖推理、编码、问答、对话四类benchmark，均一致降低激活专家规模，端到端解码速度最高提升1.62×。
