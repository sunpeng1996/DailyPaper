---
title: 'SlimWise: Decoupling Expert Pruning Across Prefill and Decode for Efficient
  MoE Serving'
title_zh: SlimWise：解耦Prefill与Decode阶段专家剪枝实现高效MoE推理服务
authors:
- Gunho Park
- Kyoungho Jeun
- Juntaek Oh
- Byeongjun Shin
- Baeseong Park
- Minsoo Rhu
affiliations:
- a2sys
- KAIST
arxiv_id: '2609.34117'
url: https://arxiv.org/abs/2609.34117
pdf_url: https://arxiv.org/pdf/2609.34117
published: '2026-09-27'
collected: '2026-10-07'
category: LLM
direction: MoE大模型推理 · 分阶段专家剪枝优化
tags:
- MoE
- Expert Pruning
- KV Cache
- LLM Serving
- vLLM
one_liner: 针对MoE推理解码带宽瓶颈，解耦prefill与decode专家剪枝，50%剪枝下解码吞吐量提1.81倍
practical_value: '- 业务侧用MoE LLM做文案生成、导购Agent推理时，可直接复用分阶段剪枝思路：prefill为计算 bound 剪枝无收益，保留全模型保证prompt理解准确率，decode阶段剪专家降带宽瓶颈，单卡吞吐量提升的同时推理成本降低30%以上

  - 可直接复用无训练KV缓存传递方案：只要剪枝不改变KV缓存结构，全模型prefill生成的KV可直接喂给剪枝后decode用，改造vLLM仅需加阶段感知router掩码，改造成本极低

  - 若剪枝后出现生成长度异常（过短/过长），可复用低成本蒸馏方案：仅更新路由器、归一化层、共享专家等<2.2%的参数，蒸馏时让剪枝模型学习承接全模型KV，无需全量微调即可修复精度和生成行为

  - 采用prefill-decode拆分部署架构时，剪枝后的decode模型可省出更多HBM给KV缓存，支持更大batch，高并发场景（如大促文案批量生成）下吞吐量收益可再放大20%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
MoE模型单token仅激活少量专家，但batch decode时会激活几乎全量专家池，专家权重加载的内存带宽成为核心性能瓶颈；传统专家剪枝对prefill、decode阶段统一剪枝，而prefill是计算 bound，剪枝几乎无吞吐量收益，反而会损失prompt表示质量，牺牲精度换不来实际收益。

### 方法关键点
- 分阶段剪枝策略：prefill阶段保留全量专家池保证prompt理解精度，decode阶段仅保留top重要专家降低权重加载开销，两阶段通过原生格式KV缓存直接传递，无需额外转换
- 双部署形态适配：PD拆分架构下decode侧直接加载剪枝后模型，省出的内存分给KV缓存扩大batch；PD同机部署下用阶段感知router掩码，prefill用原始router，decode用掩码屏蔽低重要性专家，无需维护双版本模型
- 低成本蒸馏纠偏：仅更新路由器、归一化层、新增小参数量共享专家（总参占比<2.2%），蒸馏时让剪枝decode模型学习承接全模型prefill生成的KV缓存，同时修复精度损失和剪枝导致的生成长度异常

### 关键实验结果
在Qwen3.6-35B-A3B、Gemma4-26B-A4B两个MoE backbone上验证，对比传统统一剪枝方案：
1. 50%专家剪枝下，PD拆分部署的decode吞吐量最高提升1.81倍，PD同机部署最高提升1.72倍，精度损失<2%
2. 75%剪枝下，decode吞吐量最高提升2.39倍，加蒸馏后精度仍接近全模型水平
3. 剪枝导致的生成长度异常在加蒸馏后与全模型偏差<10%

### 最值得记住的结论
MoE推理优化必须针对prefill、decode两个阶段的资源瓶颈差异做定制化策略，统一剪枝/压缩方案大概率会牺牲精度却换不来实际收益。
