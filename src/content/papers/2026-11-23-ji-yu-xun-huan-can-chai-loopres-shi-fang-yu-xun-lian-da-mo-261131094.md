---
title: Unlocking the Power of Loops in Pretrained LLMs with Loop Residuals
title_zh: 基于循环残差（LoopRes）释放预训练大模型的循环计算潜力
authors:
- Xuanlei Zhao
- Hailun Xu
- Kai Wang
- Yang Luo
- Yingxuan Ren
- Zirui Zhu
- Yuxuan Lou
- Kun Xu
- Yan Wang
- Kanchan Sarkar
affiliations:
- National University of Singapore
- Independent Researcher
arxiv_id: '2611.31094'
url: https://arxiv.org/abs/2611.31094
pdf_url: https://arxiv.org/pdf/2611.31094
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: LLM性能优化 · 循环残差
tags:
- Looped Transformer
- LoopRes
- Attention Residual
- Test-time Scaling
- Finetuning
one_liner: 提出轻量LoopRes方法，无需新增参数即可通过循环计算大幅提升预训练LLM推理性能
practical_value: '- 电商垂域小模型优化可复用LoopRes思路，无需升级大参数量模型，仅通过循环计算+微调即可提升复杂query理解、商品属性匹配准确率，降低部署成本

  - Agent推理模块可直接复用两个核心trick：给不同推理步加可训练的步感知key区分相似迭代状态，限制仅关注最近W步推理状态，既提升推理连贯性又控制开销

  - 生成式推荐多轮生成场景（如多轮召回后的排序优化）可参考残差窗口设计，仅保留最近几轮生成状态，避免长序列注意力开销过高，同时保证生成质量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Looped Transformer通过复用Transformer层实现无参数新增的计算能力增强，可灵活实现测试时算力缩放，但现有方案存在明显瓶颈：从头预训练循环模型成本极高，直接微调预训练LLM为循环结构仅能获得边际收益，核心原因是循环迭代的同层输出相似度高难以区分、注意力易跳步导致深层循环计算无效。

### 方法关键点
- 基于Attention Residuals改进，给每个循环的块输出新增可训练的循环感知key，与内容key共同计算注意力权重，解决同层循环输出语义相似无法区分的问题
- 引入固定大小的残差窗口，每层仅关注最近W个循环的输出，避免注意力跳步跳过中间循环，同时控制计算、内存开销不随循环深度增长
- 通过Triton核融合注意力计算步骤，仅带来4.8%的训练步时长增加和0.7%的峰值内存增长， overhead极低

### 关键实验结果
覆盖Qwen3、Llama3.2等3个模型家族共6个预训练LLM，在9个数学、代码基准上测试，对比SFT和8种现有循环方案：2倍计算量下，Qwen3-1.7B平均得分较SFT提升29.1%，是SOTA基线收益的2倍以上；Qwen3-4B叠加LoopRes的性能超过8B模型的SFT效果；4倍计算量下收益进一步提升至33.7%，且推理时可通过调整循环深度灵活平衡性能和延迟。

### 核心结论
无需盲目堆叠模型参数，通过优化循环计算的信息传递机制，小模型也能获得接近大参数量模型的性能，同时支持测试时的算力灵活调优
