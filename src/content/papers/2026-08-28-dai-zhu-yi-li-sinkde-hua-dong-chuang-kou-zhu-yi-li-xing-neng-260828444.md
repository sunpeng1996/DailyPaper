---
title: Sliding-window beats linear attention
title_zh: 带注意力sink的滑动窗口注意力性能优于后训练线性注意力模型
authors:
- Alexia Jolicoeur-Martineau
- Rhea Sanjay Sukthanker
- Pashmina Cameron
- Emy Gervais
affiliations:
- Microsoft Applied Sciences Group (ASG)
- Independent
arxiv_id: '2608.28444'
url: https://arxiv.org/abs/2608.28444
pdf_url: https://arxiv.org/pdf/2608.28444
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM推理优化 · 注意力机制
tags:
- Sliding Window Attention
- Linear Attention
- KV cache
- LLM Inference
- Attention Sink
one_liner: 无需训练的带sink滑动窗口注意力在多任务上优于各类后训练线性注意力方案
practical_value: '- 现有业务侧LLM推理服务可直接复用带4个sink、窗口大小64/128的SWA方案，无需额外训练即可降低KV cache占用、提升解码速度，尤其适合Agent会话、商品文案生成等中等长度上下文场景。

  - 做长上下文LLM优化时，优先评估SWA基线再考虑线性注意力改造，避免浪费后训练成本；4K上下文下SWA的长程召回性能是线性注意力的2~10倍，完全满足电商用户行为序列建模、长会话导购等场景需求。

  - SWA的FlashAttention生态完善，无需适配特殊硬件/内核，工程落地成本远低于线性注意力，适合快速上线性能折衷的轻量LLM服务。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM原生自注意力随上下文长度二次缩放，KV cache持续增长导致推理内存、时延居高不下；线性注意力作为主流优化方案需大量后训练、硬件适配成本，且过往研究未与带注意力sink的滑动窗口注意力（SWA）做公平对比。

### 方法关键点
- 采用无训练的SWA(w,s)方案：w为滑动窗口大小（取值64~512），s固定为4个注意力sink（始终关注序列前4个token，避免窗口滑过初始token后的性能暴跌），无需任何后训练或内核修改。
- 对比基线覆盖LoLCATs、Liger-GLA、QRWKV等10+主流后训练线性注意力方案，以及原生全注意力基线。

### 关键实验结果
- 短上下文任务：在1.3B~72B参数范围的11款主流LLM上测试6个通用benchmark，SWA平均性能恢复率达99%，MMLU恢复率93.2%，优于所有后训练线性注意力方案，且0训练成本。
- 长上下文任务：4K上下文下，SWA在Needle-in-a-Haystack任务准确率是LoLCATs的2~4倍、Liger-GLA的20倍以上；BABILong任务准确率是LoLCATs的5倍。
- 开销对比：SWA解码吞吐量高于线性注意力，窗口64的SWA内存占用低于线性注意力，上下文超过1K后速度是全注意力的数倍。

### 核心结论
对于绝大多数不需要超超长上下文的业务场景，带sink的无训练SWA是性价比最高的LLM推理注意力优化方案，远好于投入大量成本做线性注意力后训练改造。
