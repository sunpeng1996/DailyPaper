---
title: Recurrent Looped Transformer
title_zh: 循环迭代Transformer（RLT）：长序列泛化增强的新型Transformer架构
authors:
- Yifan Zhang
- Jichen Feng
- Shihan Qin
affiliations:
- Princeton University
- University of Pennsylvania
arxiv_id: '2610.07591'
url: https://arxiv.org/abs/2610.07591
pdf_url: https://arxiv.org/pdf/2610.07591
published: '2026-10-05'
collected: '2026-10-08'
category: LLM
direction: 大模型架构 · 长序列泛化优化
tags:
- Transformer
- Long Sequence
- Recurrent Architecture
- Length Generalization
- KV Cache
one_liner: 拆分Transformer为并行因果编码器与循环解码器，大幅提升长序列任务的长度泛化能力
practical_value: '- 电商用户长周期行为序列建模可参考RLT的编码器并行+解码器循环架构，在固定单token计算成本下提升超训练长度序列的建模精度，避免普通Transformer长序列性能骤降的问题

  - 可复用RLT的反馈间隔设计tradeoff：用户长期兴趣建模等状态更新不频繁的任务采用多token chunk共享反馈状态提升训练/推理速度，实时会话推荐等状态敏感任务采用单token反馈保证精度

  - Agent多轮会话状态跟踪可借鉴RLT的门控合并模块融合当前输入与上轮解码器状态，配合跨轮cache复用机制，降低多轮对话的状态重建开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
普通Transformer对每个token的处理深度固定，无法支撑任意长度的序列状态跟踪需求，在超出训练长度的长序列上性能会骤降至随机水平，同时纯循环模型又存在训练并行性差的缺陷，亟需兼顾长序列泛化能力与计算效率的新型架构。

### 方法关键点
- 架构拆分：将固定总层数的Transformer拆分为并行因果编码器（LE层）与循环Transformer解码器（LD层），可灵活调整两者层数分配适配不同任务
- 循环状态传递：每个token处理时通过门控合并层融合当前编码器输出与上一token的最终解码器状态，解码器同时交叉注意力到编码器前缀与自身滑动窗口内的历史激活，递归路径随序列长度增长但单token计算成本固定为LE+LD层
- 可调试反馈间隔：支持三种反馈模式，RLT-1每token更新状态（精度最优）、RLT-2每B个token更新一次状态（兼顾并行度与精度）、RLT-0无反馈（并行度最高）

### 关键结果
总层数固定为8层的RLT与8层Decoder-only Transformer对比，在超出训练长度的长序列任务上优势显著：
1. 奇偶校验任务：训练最长40bit，RLT在256bit上准确率100%，Transformer仅50%（随机水平）
2. 交换式S5排列跟踪任务：训练最长32次操作，RLT在8倍训练长度的256次操作上准确率97%，Transformer不足1%
3. 模运算任务：训练最长39个token，RLT在63个token上准确率93%，Transformer仅33%
4. 消融验证：移除反馈机制后所有长序列任务性能均降至随机水平；4-token chunk的RLT-2保留64bit奇偶校验99%准确率，但对状态敏感的排列跟踪任务准确率降至20%

> 最值得记住的结论：通过循环解码器引入随序列长度增长的计算路径，是在固定单token计算成本下大幅提升Transformer长序列泛化能力的可行方案。
