---
title: Decoding Looped Transformers Better for (Almost) Free
title_zh: 无需训练的Looped Transformer低开销对比解码方法LoopCD
authors:
- Weihao Liu
- Huangjie Zheng
- Tianrong Chen
- Rohit Dilip
- Richard He Bai
- Yizhu Jiao
- Yuyang Wang
- Ruixiang Zhang
affiliations:
- Apple
arxiv_id: '2610.02185'
url: https://arxiv.org/abs/2610.02185
pdf_url: https://arxiv.org/pdf/2610.02185
published: '2026-10-01'
collected: '2026-10-02'
category: LLM
direction: LLM推理优化 · 无训练对比解码
tags:
- Looped-Transformer
- Contrastive-Decoding
- Training-Free
- Inference-Optimization
- LLM-Decoding
one_liner: 利用Looped Transformer中间循环状态实现无训练低开销的对比解码效果提升与推理加速
practical_value: '- 业务侧如果已落地Looped Transformer做Agent推理、商品文案生成、搜索query改写等生成任务，可直接复用LoopCD-Hidden变体，零额外输出开销即可提升生成准确率，无需重新训练模型

  - 高并发推荐/广告生成场景算力紧张时，可直接将Looped Transformer的循环次数减半，搭配LoopCD即可达到原全循环深度的效果，节省22.5%~48.2%的推理FLOPs，降低部署成本

  - 做生成式推荐/Agent推理的解码优化时，可复用「同模型弱-强中间状态对比指导+自适应强度调整」的思路，不需要引入额外小模型做对比，降低架构复杂度与维护成本

  - 自适应强度调整的trick可直接复用到各类生成场景：根据预测top2概率差动态调整指导强度，仅在模型不确定的决策点生效，避免生成漂移，保障文案、query等生成内容的稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Looped Transformer通过循环执行共享参数块实现参数效率与推理深度解耦，但标准解码仅保留最终循环状态，丢弃了天然对齐的弱-强中间预测对；传统对比解码需要额外辅助模型、扰动上下文或多模型配合，引入的额外成本较高，无法低成本挖掘Looped Transformer的中间状态价值。

### 方法关键点
- 提出训练-free的LoopCD对比解码框架，直接复用首次循环的弱预测与最终循环的强预测做对比指导，无需引入额外模型、修改训练逻辑或调整prompt
- 两种落地变体：LoopCD-Logits在logit空间做对比，仅新增1次输出层前向开销；LoopCD-Hidden在隐藏状态空间做融合，完全无额外输出开销
- 支持两种强度策略：固定强度适配特定任务，自适应强度根据预测top2概率差动态调整指导力度，仅在模型决策不确定时生效，避免生成漂移

### 关键结果
- 覆盖Ouro、Huginn、Parcae、Looped-Qwen3四类主流Looped Transformer架构，在数学推理、代码生成、通用多选基准上全场景验证效果
- 全循环深度下：LoopCD-Logits将Ouro-2.6B-Thinking的AIME 2024 pass@1从61.88%提升至73.33%；LoopCD-Hidden将Huginn的HumanEval pass@1从22.56%提升至31.71%
- 半循环深度下：仅用原循环次数的50%搭配LoopCD，效果匹配甚至超过全深度无指导基线，前向FLOPs降低22.5%~48.2%

### 核心记忆点
Looped Transformer的循环中间状态天然自带同输入对齐的弱-强预测对，无需额外成本即可用于对比解码，实现效果提升与推理降本的双重收益。
