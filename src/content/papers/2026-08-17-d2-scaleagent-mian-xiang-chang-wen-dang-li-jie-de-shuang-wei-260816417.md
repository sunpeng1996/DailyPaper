---
title: 'D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding'
title_zh: D2-ScaleAgent：面向长文档理解的双维度缩放智能体框架
authors:
- Hao Zhang
- Longrong Yang
- Lunhao Duan
- Ziyang Wang
- Qing-Guo Chen
- Shanshan Zhao
affiliations:
- Zhejiang University
- Alibaba Group
- University of Science and Technology of China
arxiv_id: '2608.16417'
url: https://arxiv.org/abs/2608.16417
pdf_url: https://arxiv.org/pdf/2608.16417
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: 长文档理解 · 智能体动态路由
tags:
- Multi-agent
- Long Document Understanding
- RAG
- Dynamic Routing
- Multimodal
one_liner: 提出验证器驱动的双维度缩放智能体框架，解决多模态长文档理解的证据不足问题
practical_value: '- 可复用Verifier驱动的闭环路由架构：电商场景下做商品详情页/售后文档/用户评价的QA类任务（如智能客服、商品信息查询）时，引入证据完备性校验，根据缺失证据动态触发召回扩容或细粒度解析，比固定Top-K召回+固定推理流程的方案准确率提升明显

  - 检索扩容的query属性分解+秩融合trick：做商品/内容多模态召回时，可将用户查询拆分为多维度加权子查询做并行召回，再用秩融合合并结果，无需额外训练就能提升召回的覆盖度和排序质量

  - 分层推理子agent的成本控制方法：可根据业务的精度/延迟要求，配置低中高成本的分层解析子agent，根据证据缺口按需调用，平衡推理精度和计算成本，适合非强实时的长文本/多模态理解场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多模态RAG和固定工作流的多智能体长文档理解方案，无法根据查询难度动态调整计算资源，常因证据覆盖不全（广度不足）或细粒度信息提取不充分（深度不足）导致结果错误，尤其在处理富视觉元素的跨页长文档（如电商商品手册、财报、论文）时准确率偏低。

### 方法关键点
- 核心架构：以持续更新的Evidence Bank为全局动态工作记忆，由Verifier智能体驱动闭环路由，根据当前证据的完备性评分和缺口类型，动态选择向外的检索扩容或向内的推理扩容
- 检索扩容：将原始查询分解为加权多维度属性子查询，并行召回后做秩融合，再通过证据集稳定性阈值自适应终止召回，替代固定Top-K召回策略
- 推理扩容：设计三类分层子agent（低成本全局巡检、中成本区域定位、高成本细粒度提取），根据证据缺口按需调用，提取不同粒度的信息存入Evidence Bank
- 终止条件：仅当证据完备性评分达到阈值且无缺口时，才基于已有的闭合证据链生成最终答案，避免幻觉

### 关键结果
在MMLongBench-Doc、LongDocURL等6个多模态长文档基准上测试，对比MoLoRAG、MDocAgent、ViDoRAG等SOTA基线：基于GPT-4o时平均准确率达63.7%，比最优基线MDocAgent高5.4个百分点；基于Qwen3-VL-8B时平均准确率达65.8%，比最优基线高8.2个百分点；所有检索指标（Recall、Precision、nDCG、MRR）均显著优于基线，计算成本随查询难度动态分配，无证据缺口时推理延迟可低至11.89s/query。

### 最值得记住的一句话
长文档理解的核心失败原因不是模型能力不足，而是证据不足，动态按需调配资源补全证据链的收益远高于单纯提升基础模型能力。
