---
title: 'MoE-Context: Show the Model Only What It Needs'
title_zh: MoE-Context：仅向模型展示当前步骤所需的上下文块
authors:
- Vedant Navale
affiliations:
- UpThink EduTech Services Pvt. Ltd.
arxiv_id: '2611.24379'
url: https://arxiv.org/abs/2611.24379
pdf_url: https://arxiv.org/pdf/2611.24379
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent 长上下文内存管理优化
tags:
- MoE
- KV cache
- LLM Agent
- Context Management
- Memory
one_liner: 提出基于KV cache掩码的上下文块动态选择机制，无信息删除前提下降低长上下文推理噪声
practical_value: '- 做电商导购Agent/用户个性化推荐的LLM推理模块时，可复用KV cache掩码方案，仅保留当前查询相关的用户历史/商品上下文，既不丢失全量历史信息，又能减少无关内容干扰，提升推荐/回答准确率

  - 可复用单缓存块切换思路，无需重建上下文即可实现Agent推理步骤回退（如用户修改需求时撤销之前的推荐逻辑），或拆分多子任务并行处理，大幅降低工程实现复杂度

  - 简单业务场景下的上下文选择可先用关键词匹配做基线，实测其效果优于小模型自主选择，后续再逐步迭代监督探针等复杂方案'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent每步推理都加载全部历史上下文，无关内容会严重干扰小模型推理准确率，现有上下文压缩/裁剪方案易丢失原始信息，RAG类检索方案又需额外重编码开销，针对小模型长上下文推理噪声高、成本高的痛点设计该方案。
### 方法关键点
- 上下文拆分为独立块，每步推理前做快速选块：仅保留所需块的完整内容，其余块仅展示一行摘要，所有块内容永久存储可随时召回，支持固定块置顶
- 单模型单KV cache实现：所有块仅编码一次写入KV cache，隐藏块仅修改注意力掩码，无需重编码，位置信息保持不变，无额外计算开销
- 可选监督线性探针优化选块准确率，探针参数写入模型未使用的输出行，不影响正常推理输出
### 关键结果
基于Qwen3-1.7B在8GB笔记本GPU上的synthetic lookup任务（120条查询）测试：
- 仅展示所需块时准确率从全量上下文的93/120提升到119/120
- 加入线性探针后模型自主选块的准确率从80/120提升到110/120，简单关键词匹配基线可做到100%选块正确
- 掩码隐藏的块信息泄露程度和直接删除相当，无额外信息泄露
### 核心结论
小模型长上下文推理的主要干扰来自无关内容，仅展示所需内容的收益远高于优化模型本身的推理能力。
