---
title: 'ARLoop: Fully-Open Pre-trained Looped Transformers with Attention Residuals'
title_zh: ARLoop：基于注意力残差的完全开源预训练循环Transformer
authors:
- Yuekun Yao
- Yupei Du
- Dawei Zhu
- Huan Sun
affiliations:
- The Ohio State University
- Saarland University
arxiv_id: '2611.05234'
url: https://arxiv.org/abs/2611.05234
pdf_url: https://arxiv.org/pdf/2611.05234
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: LLM架构优化 · 循环Transformer
tags:
- Looped Transformer
- Attention Residual
- Sliding Window Attention
- LLM Pretraining
- Parameter Efficient
one_liner: 提出带滑动窗口注意力残差的循环Transformer架构，性能超现有开源循环LLM及同规模非循环模型
practical_value: '- 低算力场景的垂直业务LLM（如电商客服、推荐理由生成专用小模型）可复用ARLoop的循环Transformer+滑动窗口注意力残差设计，无需增加参数量即可提升多步推理类任务效果

  - 现有业务中使用循环结构小模型的场景，可将原PreNorm残差替换为注意力残差+滑动窗口设计，仅增加约10%训练算力开销，即可获得复杂任务的显著增益

  - 多轮Agent推理场景可借鉴注意力残差思路，对历史对话/推理步骤表示做加权聚合而非全量拼接，既能降低冗余信息干扰，又能减少内存占用'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Looped Transformer通过复用Transformer层提升有效深度，参数量效率高，但传统PreNorm残差只能固定聚合历史信息，无法选择性复用不同深度的中间表示，现有残差设计多在小场景验证，在数学、代码等复杂生成任务上的效果未得到充分验证。

### 方法关键点
- 将注意力残差适配到循环Transformer，对不同深度的残差块做注意力加权聚合，替代PreNorm的固定系数累加，支持灵活选择历史表示
- 针对循环Transformer不同轮次表示冗余高的特性，设计滑动窗口深度注意力：仅保留输入嵌入和最近3个残差块做注意力，无需访问全量历史残差，降低计算开销
- 采用分组查询注意力、SwiGLU激活函数对齐现代LLM架构，分阶段使用FineWeb-Edu、FineMath、Stack-Edu等高质量数据预训练，全量开源训练代码、数据处理脚本和模型权重

### 关键结果
- 140M、370M参数量下，ARLoop在R=1到5的循环深度下均优于PreNorm及现有循环Transformer残差设计，验证困惑度最高降低0.5
- 0.6B参数量模型相比同规模PreNorm循环基线，GSM8K提升5.2个点，MBPP提升3.1个点，数学、代码任务增益显著
- 1.2B参数量模型仅用0.5T token预训练，全任务优于3.5B参数量的开源循环LLM Huginn，且效果媲美2B参数量的非循环模型Qwen3.5-2B

**值得记住的核心结论**：循环Transformer无需全量历史残差，滑动窗口注意力残差即可在更低开销下实现更优的多轮计算效果，为小参数模型提升推理能力提供了高效路径
