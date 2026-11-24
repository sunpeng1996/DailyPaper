---
title: 'Feedback Shortcut: Speculative Decoding for Latent Feedback Transformers'
title_zh: Feedback Shortcut：面向潜反馈Transformer的推测解码方法
authors:
- Benhao Huang
- Xuezhe Ma
- Hector Liu
affiliations:
- Institute of Foundation Models
- USC
- CMU
arxiv_id: '2611.28227'
url: https://arxiv.org/abs/2611.28227
pdf_url: https://arxiv.org/pdf/2611.28227
published: '2026-11-19'
collected: '2026-11-24'
category: LLM
direction: LLM推理优化 · 潜反馈Transformer解码加速
tags:
- speculative decoding
- latent feedback transformer
- state alignment
- pipelined correction
- inference acceleration
one_liner: 通过状态对齐与流水线修正实现潜反馈Transformer的低损高速推测解码
practical_value: '- 若业务中使用了带反馈机制的自定义LLM（如Agent长序列推理、多轮状态记忆模型），可直接复用状态对齐+流水线修正框架，在不修改基座模型的前提下将推测解码速度拉到接近普通Transformer水平，仅新增2%左右训练开销，落地成本极低

  - 大流量高并发LLM服务场景（如电商智能客服、推荐文案批量生成），可根据负载动态切换D值：低峰用D=1保精度，高峰切D=0，速度与普通Transformer一致还能保留80%以上潜反馈效果收益，平衡算力成本与业务效果

  - MTP头复用思路可迁移到生成式推荐场景：用推荐模型的多输出头做轻量投影得到候选item的语义状态，替代传统精确匹配逻辑，提升召回/排序阶段的并行度，降低响应延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
潜反馈Transformer通过将每个位置顶层隐状态反馈到下一个位置输入，相同显存开销下效果优于普通Transformer，但时序依赖完全破坏了常规推测解码的并行性：要么逐token精确解码速度极低，要么用近似代理状态会产生双向效果损失——训练时适配代理会降低模型效果上限，推理时用代理会引入额外近似误差，现有方案无法兼顾效果、速度、训练开销。
### 方法关键点
- 状态对齐：仅训练一个轻量MLP投影层，将多Token预测（MTP）头的输出映射为潜反馈所需的代理状态，完全不修改基座模型权重，既避免基座效果上限下降，又将单步近似误差压到最低
- 流水线修正：将草稿token的校正步骤嵌入到下一轮草稿的验证阶段，无需额外前向调用即可逐步消除代理状态引入的近似误差，校正次数D可灵活调整精度与速度的tradeoff
- 支持动态负载策略：D=0时完全不做校正，速度与普通Transformer推测解码一致；D≥1时逐步逼近精确解码效果
### 关键结果
在135M、780M两种参数规模的潜反馈Transformer上验证，覆盖Paloma、Math、Code、QA等基准，对比普通Transformer推测解码、潜反馈精确解码基线：
1. 精度损失控制在10⁻⁴ BPB以内，与精确解码效果基本持平
2. 解码速度相对精确解码提升2.4×~2.8×，训练开销仅比普通Transformer多2%左右
3. 大batch size场景下切换D=0，速度与普通Transformer一致，仍保留80%以上潜反馈的效果收益

最值得记住的一句话：带依赖的特殊Transformer结构做推测解码优化时，优先选择仅新增轻量附属模块、不修改基座的方案，再用流水线复用前向过程消除误差，是兼顾落地成本与效果的最优路径。
