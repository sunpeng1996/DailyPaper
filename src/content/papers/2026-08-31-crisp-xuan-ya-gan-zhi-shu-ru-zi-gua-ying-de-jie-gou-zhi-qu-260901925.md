---
title: 'CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated
  Routing'
title_zh: CRISP：悬崖感知输入自适应的结构质量驱动稀疏预填充算法
authors:
- Huu Huy Nguyen
- Chien Van Nguyen
- Franck Dernoncourt
- Ryan A. Rossi
- Linh Ngo Van
- Jieyang Chen
- Thien Huu Nguyen
affiliations:
- University of Oregon
- Adobe Research
- Hanoi University of Science and Technology
arxiv_id: '2609.01925'
url: https://arxiv.org/abs/2609.01925
pdf_url: https://arxiv.org/pdf/2609.01925
published: '2026-08-31'
collected: '2026-09-03'
category: LLM
direction: 长上下文LLM · 稀疏预填充推理优化
tags:
- Sparse Attention
- Long-Context LLM
- Prefilling
- Inference Optimization
- Attention Sink
one_liner: 提出CRISP稀疏预填充算法，降低长上下文LLM推理开销，512k token下速度提5.3倍且精度持平全注意力
practical_value: '- 处理长用户行为序列的LLM召回/生成场景（如电商用户全生命周期点击序列建模、RAG超长商品评价解析），可直接复用CRISP方案，512k序列下预填充速度提5倍左右，检索类任务精度不降反升

  - Cstruct路由思路可迁移到低延迟业务的注意力优化：无需复杂的JSD计算，仅统计注意力sink和局部窗口的质量占比即可判断头的稀疏模式，零额外开销，适合端侧、大促高并发场景

  - 替换传统累积覆盖率阈值为sink感知噪声基线阈值，可解决长序列下“漏信号/攒噪声”的两难问题，适配Agent的长对话记忆、多文档召回等场景

  - 业务上线需加上下文长度开关：8k以内短序列稀疏预填充开销高于FlashAttention，仅对超过阈值的长序列请求开启稀疏优化，避免负收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM推理预填充阶段的自注意力复杂度随序列长度平方增长，成为性能瓶颈。传统固定稀疏模式无法适配输入依赖的注意力结构，SOTA动态路由方法FlexPrefill存在两大缺陷：基于JSD的路由额外开销高，累积覆盖率阈值会因softmax后的质量悬崖产生两种失效——要么提前终止漏掉任务信号，要么累积O(n)背景噪声，长序列下精度和延迟表现均不理想。
### 方法关键点
- 提出Cstruct结构质量代理：直接统计预计算的代理注意力图中注意力sink区和局部近邻窗口的质量占比做路由，和JSD路由决策匹配度达94%（Llama3.1）、88.1%（Qwen2.5），完全消除JSD的额外矩阵乘和KL散度开销
- 形式化定义softmax后的质量悬崖：将注意力块分为架构sink、任务相关信号、背景噪声三层，替换累积覆盖率阈值为sink感知的噪声基线阈值，仅保留质量高于α倍噪声基线的块，从根源避免O(n)噪声积累
- 低熵注意力头走Vertical-Slash路径用噪声阈值选块，高熵头走Pooled-Estimation路径保留原累积阈值，兼顾精度和效率
### 关键结果
在Llama3.1-8B、Qwen2.5-7B上测试InfiniteBench、RULER、LongBench，对比FlashAttention、MInference、FlexPrefill：检索任务精度较FlexPrefill最高提升28pp，精度与全量注意力持平甚至更高；512k token下预填充速度较FlashAttention最高提升5.3倍，较同精度FlexPrefill快25%。
> 最值得记住：长上下文稀疏注意力优化的核心不是盲目提升覆盖率，而是精准过滤软最大化产生的架构性背景噪声
