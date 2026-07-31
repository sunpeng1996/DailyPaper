---
title: Multi-Head Attention Residuals
title_zh: 多头注意力残差：零参数优化Transformer跨层深度路由
authors:
- Cheng Luo
- Zefan Cai
- Junjie Hu
affiliations:
- Independent Researcher
- University of Wisconsin–Madison
arxiv_id: '2607.27230'
url: https://arxiv.org/abs/2607.27230
pdf_url: https://arxiv.org/pdf/2607.27230
published: '2026-07-21'
collected: '2026-07-31'
category: LLM
direction: 大语言模型 · Transformer残差架构优化
tags:
- Transformer
- ResidualConnection
- MultiHeadAttention
- DepthRouting
- TritonKernel
- Scaling
one_liner: 零参数拆分跨层深度路由查询为多头，解决大模型下单头路由性能退化问题，提升训练效果与可扩展性
practical_value: '- 业务垂域LLM从零训练时可直接集成MHAR，路由头数默认与KV头数对齐，零参数新增即可获得稳定效果提升，几乎无额外成本

  - 已有预训练垂域大模型可通过delta残差身份保持转换插入MHAR做增量训练，无需重新预训练，即可提升多步推理能力（如智能导购需求拆解、规则理解类任务）

  - 工程侧可直接复用论文融合Triton路由kernel，将深度路由训练吞吐量从基线的0.2-0.5倍提升至0.55-0.88倍，内存开销接近原生Transformer'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统注意力残差采用单个共享查询做跨层深度路由，所有特征子空间必须复用同一套历史层读取分布，模型宽度越大，不同子空间的层偏好差异越显著，单头路由的强制妥协成本越高，甚至在大参数量场景下效果弱于普通加法残差。
### 方法关键点
- 零参数修改：将单路由查询拆分为H个对应特征子空间的头，每个头独立对历史层输出做softmax路由，无新增参数与FLOPs，H=1时完全等价于原生注意力残差
- 无超参默认配置：路由头数设置为与Transformer KV头数一致即可达到近最优效果，无需额外调优
- 工程优化：提供融合Triton路由内核，大幅降低深度路由的内存开销与训练耗时
- 兼容预训练模型：支持delta残差身份保持转换，可无损失插入预训练模型做增量训练
### 关键结果
- 从零训练100M/350M/1B参数模型，对比普通Transformer验证loss分别下降0.049/0.080/0.063，单头注意力残差在1B参数场景下比基线差0.105
- 8B参数增量训练场景下，GSM8K提升3.2、GPQA提升3.1，统计显著
- 融合内核将深度路由训练吞吐量提升至原生Transformer的0.55~0.88倍，峰值内存接近基线
### 核心结论
如果注意力本身是多头的，那么注意力残差旁路也应该是多头的，零成本的查询拆分即可解决大模型下的单路由头性能退化问题
