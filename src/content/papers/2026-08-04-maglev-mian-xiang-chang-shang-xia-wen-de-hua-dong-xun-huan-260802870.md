---
title: 'Maglev: Sliding Recurrent Memory'
title_zh: Maglev：面向长上下文的滑动循环记忆Transformer架构
authors:
- Bo Liu
- Qiang Liu
affiliations:
- The University of Texas at Austin
arxiv_id: '2608.02870'
url: https://arxiv.org/abs/2608.02870
pdf_url: https://arxiv.org/pdf/2608.02870
published: '2026-08-04'
collected: '2026-08-15'
category: LLM
direction: LLM长上下文 · 循环记忆架构优化
tags:
- Transformer
- Recurrent Memory
- Sliding Window Attention
- Long Context
- Knowledge Distillation
one_liner: 通过预填充器-解码器一致性损失训练固定内存循环Transformer，兼顾并行训练与低推理开销
practical_value: '- 推荐系统长序列用户建模可复用这套一致性训练思路：用全注意力教师模型生成长序列记忆标签，蒸馏到仅用滑动窗口的轻量推理模型，兼顾长程兴趣捕捉与线上延迟要求

  - Agent长对话记忆模块可复用循环K/V注入设计：无需额外增加KV cache大小，通过门控混合当前token K/V与历史记忆K/V，在固定显存开销下保留更长对话上下文

  - 生成式推荐大模型部署可参考参数共享方案：预填充教师模型与推理解码器共享大部分参数，降低训练显存占用的同时几乎不损失效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
滑动窗口Transformer推理成本固定但会丢失窗口外的长程信息，传统循环模型要么训练并行度低、要么是线性更新表达能力弱，当前缺少兼具非线性token级记忆、固定推理开销、并行训练能力的长上下文架构。

### 方法关键点
- 双模型架构：预填充器Q采用交错全注意力+滑动窗口注意力，并行生成全序列记忆目标m'_t；解码器P纯用滑动窗口注意力，接收上一步记忆目标做K/V注入，预测下一个token并输出记忆m_t
- 训练目标：结合交叉熵损失与记忆一致性损失，对齐解码器输出的m_t与预填充器生成的m'_t，推理阶段直接丢弃Q，P用自身输出的上一步记忆闭环运行
- 工程优化：Q和P可共享大部分Transformer层参数，仅保留少量独立缩放参数降低训练开销；循环记忆通过门控混合进当前K/V，不额外增加KV cache大小，推理成本与普通滑动窗口Transformer完全一致

### 关键实验
435M参数模型在43.52B token上训练，对比滑动窗口Transformer、LRT基线：最佳独立参数版本FineWeb-Edu验证集BPB从0.7413降至0.7251，下游任务平均准确率从54.1提升至56.4；参数共享版本BPB降至0.7295，平均准确率56.2，仅损失极微效果。

### 核心结论
用高能力教师模型并行生成记忆标签做蒸馏，能在不增加推理开销的前提下给轻量滑动窗口模型注入长程记忆能力。
