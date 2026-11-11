---
title: 'Sable: A Small-Field Sumcheck Argument for Bit-Exact Inference of Large Language
  Models'
title_zh: Sable：面向大语言模型比特精确推理的小域和校验证明系统
authors:
- Tomer Solberg
affiliations:
- MoonMath.ai
arxiv_id: '2611.14083'
url: https://arxiv.org/abs/2611.14083
pdf_url: https://arxiv.org/pdf/2611.14083
published: '2026-11-09'
collected: '2026-11-11'
category: LLM
direction: LLM可验证推理 · 零知识证明
tags:
- Verifiable Inference
- Sumcheck
- Zero-knowledge Proof
- LLM Quantization
- GPU Acceleration
one_liner: 提出单GPU可运行的LLM比特精确推理证明系统Sable，速度较zkLLM提升40-64倍
practical_value: '- 全整数无浮点的LLM推理方案可直接复用在端侧LLM推荐/Agent部署场景，提升推理速度的同时保证多端运行结果一致性

  - 单GPU流式层处理、CUDA Graph重放相同层的工程优化技巧，可迁移到大模型推荐系统的在线推理服务，降低单卡显存占用和请求延迟

  - Q/K split的量化校准方法可复用在LLM4Rec的量化流程中，无需额外推理成本即可降低量化带来的推荐精度损失

  - LLM可验证输出能力可用于电商Agent对外服务场景，给商家/消费者提供AI生成文案、推荐结果的溯源证明，规避内容合规纠纷'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前托管LLM服务的输出无法证明其来自指定公开模型、未被篡改/截断、采样逻辑符合承诺，现有可验证推理方案要么仅支持小模型、推理证明耗时过长，要么无法保证比特级结果精确性，难以落地到电商、广告等需要可信AI输出的业务场景。
### 方法关键点
- 定义全整数推理函数FO，覆盖普通Transformer、QK-norm、MoE等所有主流LLM算子，无任何浮点步骤，所有运算结果完全确定
- 基于31位KoalaBear素域构造无溢出约束系统，所有运算关系在素域和整数域严格等价，从密码学层面避免证明伪造
- 设计流式证明协议，层间流式处理、两轮遍历模型无需存储全量见证数据，Lookup分块保证LogUp论证的可靠性
- 单GPU Prover优化：设备端运行Fiat-Shamir transcript无需主机往返，相同层复用CUDA Graph重放，自动生成适配约束程序的和校验内核
### 关键结果
单NVIDIA RTX PRO 6000 Blackwell GPU上，证明Qwen2.5-32B 64层4096token序列仅需92.5s，单位参数和token的证明速度比zkLLM快40~64倍；FO整数模型与BF16原模型相比，WikiText-2贪心token匹配率达86.3%，MMLU得分差距小于1.6点，GSM8K得分差距小于1.7点；4096token序列的证明大小为134.8MiB，CPU单核仅需19~56s即可完成验证。

可验证LLM推理的落地瓶颈已经从理论可行性转向工程性能优化，全整数确定推理+小域密码学证明的组合可以在精度损失可控的前提下实现生产级大模型的高效可信证明。
