---
title: 'Greedy Decoding Is Not Precision-Invariant: Cross-Precision Output Divergence
  in LLM Inference'
title_zh: LLM贪心解码跨精度输出分歧的机制与低开销缓解方案
authors:
- Gaoyuan Du
- Anam Nawaz Khan
- Rex Zhou
- Xiaoyang Liu
- Deepayan Chakrabarti
- Fnu Suya
- Xueping Li
affiliations:
- University of Tennessee, Knoxville
- University of Chicago
- Amazon
- University of Texas at Austin
arxiv_id: '2609.26621'
url: https://arxiv.org/abs/2609.26621
pdf_url: https://arxiv.org/pdf/2609.26621
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: LLM推理优化 · 跨精度一致性修复
tags:
- Greedy Decoding
- LLM Inference
- Precision Consistency
- Low-overhead Optimization
- LLM Serving
one_liner: 发现LLM贪心解码跨精度输出分歧机制，提出低开销选择性FP32 lm_head重计算方案
practical_value: '- 做LLM驱动的电商文案生成、推荐理由生成、智能Agent多轮调用等要求输出稳定的场景，可复用本文门控逻辑：先算当前step的top-2
  logit margin，低于阈值1e-3时触发lm_head的FP32重计算，仅增加<4% latency就能提升22-36pp的精确一致率，适合低batch（bs≤4）的实时线上场景

  - 若线上服务同时存在BF16/FP16两种精度副本做A/B测试，需注意19%的prompt可能出现结果正确性翻转，不能直接归因到模型迭代效果，建议要么统一精度，要么用本文方法修复后再做实验，避免评估偏差

  - 若采用FP8量化部署LLM服务，仅当量化仅作用于lm_head时本方案有效，端到端FP8下body误差占主导，该方案收益仅1pp，需额外做训练阶段的精度稳定性优化'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM serving中不同副本常采用BF16/FP16等不同精度部署，默认贪心解码是确定性的，但实际相同模型、prompt、硬件下跨精度输出不一致，会导致审计无法复现、A/B测试结果偏差、高精准参考输出漂移等问题，现有确定性工具仅能保证单精度内一致，无法解决跨精度分歧。

### 方法关键点
- 机制定位：跨精度分歧不是transformer body误差导致，而是lm_head层的top-2 logit margin小于精度扰动尺度时，argmax结果翻转，单个token翻转会级联导致全序列分歧
- 缓解方案：设计选择性触发的FP32 lm_head重计算策略，仅当当前step的top-2 logit margin低于阈值τ=1e-3时触发，其余步骤保持原生低精度计算，避免全量FP32的高开销
- 验证5个机制预测：整数量化、温度锐化无效果，top-K≥2的FP32重计算效果等同于全词表FP32重计算，扩大FP32范围到body层反而降低一致率

### 关键结果
实验覆盖6个1.1B-7B模型、3个基准（GSM8K、HumanEval、MBPP），BF16 vs FP16下49%-100%的prompt输出分歧，序列平均长度差34token，Qwen2.5-3B上19%的prompt最终答案正确性翻转；最优方案在A10G上提升22-36pp的精确一致率，L4/A100上提升12-21pp，latency开销<4%，仅适用于bs≤4的场景，bs≥8或端到端FP8下收益消失。

**最值得记住的一句话**：LLM贪心解码的跨精度一致性问题本质是lm_head层的低margin事件，仅修复该层就能以极低开销获得大幅收益，不需要改动模型结构或重训练。
