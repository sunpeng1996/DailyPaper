---
title: 'Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent
  Half of a Hybrid 27B LLM'
title_zh: 门控DeltaNet支持4位量化的机制解析：混合27B LLM循环模块NVFP4 W4A4实现
authors:
- Sergii Kozyrev
- Davyd Maiboroda
affiliations:
- minima.ai
arxiv_id: '2609.04098'
url: https://arxiv.org/abs/2609.04098
pdf_url: https://arxiv.org/pdf/2609.04098
published: '2026-09-02'
collected: '2026-09-04'
category: LLM
direction: 大模型低比特量化 · 混合架构LLM推理优化
tags:
- Quantization
- NVFP4
- Gated DeltaNet
- Hybrid LLM
- W4A4
- KV Cache
one_liner: 首次实现混合27B LLM全GDN模块NVFP4 W4A4量化，性能追平BF16并揭示鲁棒性机制
practical_value: '- 采用带GDN/Mamba类循环模块的混合LLM搭建电商RAG导购、推荐文案生成、Agent服务时，可将所有循环模块全量做NVFP4
  W4A4量化，无需为门控层保留更高精度，显存可降为原BF16的1/3左右，Prefill速度提15%+，业务指标几乎无损失

  - 长上下文场景下给W4A4量化模型的FP8 KV Cache添加静态层级校准scale，可无性能损耗恢复83%的KV量化困惑度损失，同等显存下可支持的上下文长度提升近1倍

  - 部署NVFP4量化模型前需排查服务端GEMM融合逻辑，提前对齐被融合模块的全局scale，避免出现精度无声下降、长上下文指标虚高的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前混合架构LLM（如Qwen3.8-27B，48层GDN+16层注意力）成为主流，业界默认循环模块尤其是门控投影层的量化误差会随长上下文累积，仅敢用8/16位精度保存，大幅浪费显存和推理效率，4位W4A4全量化方案是否可行缺乏机制验证和落地指导。

### 方法关键点
- 提出Minima量化方案，将Qwen3.8-27B全部496个线性层（含所有GDN层的门控投影）全部做NVFP4 W4A4后训练量化，仅保留embedding、lm_head、卷积、Norm层为BF16
- 修正per-module校准与fused GEMM的全局scale不匹配问题，避免量化后计算精度无声下降
- 新增FP8 KV cache层级静态校准scale，无性能损耗修复量化模型长上下文困惑度损失
- 通过激活统计、单层重放、锁步FP32误差传播实验逐层验证GDN抗量化的底层机制

### 关键结果
对比BF16原生模型、Unsloth/RadixArk社区NVFP4量化方案（仅MLP做4位，GDN/注意力保留8/16位）：Minima权重显存仅17.5GiB，是BF16的1/2.9，比社区方案小7~13%；32K上下文Prefill速度比社区方案快14~19%；5项核心任务（MMLU-Pro/GSM8K/AIME'25/GPQA-Diamond/LiveCodeBench）平均得分仅比BF16低0.52，完全在种子噪声范围内；32K上下文困惑度差仅0.49，且随上下文长度增加反而缩小。

**最值得记住的一句话**：混合LLM的循环半区反而是更容易量化的部分，之前业界重点保护的门控投影层恰恰是架构自带鲁棒性、最安全的量化对象
