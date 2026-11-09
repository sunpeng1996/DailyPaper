---
title: 'ROSE: Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing
  in Multimodal Large Language Models'
title_zh: ROSE：面向多模态大模型终身知识编辑的风险感知正交子空间导航框架
authors:
- Lingyun Song
- Ziyao Chen
- Kang Pan
- Xiaolin Han
- Yifei Zhang
- Xiaoqi Wang
- Yudai Pan
- Xuequn Shang
affiliations:
- Northwestern Polytechnical University
- Shenzhen Research Institute of Northwestern Polytechnical University
- Independent Researcher
arxiv_id: '2611.09770'
url: https://arxiv.org/abs/2611.09770
pdf_url: https://arxiv.org/pdf/2611.09770
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: 多模态大模型 · 终身知识编辑
tags:
- Knowledge Editing
- Multimodal LLM
- Catastrophic Forgetting
- Orthogonal Subspace
- Lifelong Learning
one_liner: 通过风险感知正交子空间约束解决多模态大模型终身知识编辑的遗忘与能力退化问题
practical_value: '- 电商多模态导购Agent的实时知识更新可复用ROSE的正交子空间隔离方案，避免频繁更新商品、活动信息时出现旧知识遗忘、通用交互能力退化的问题

  - 生成式推荐的MLLM推理模块可复用原型锚定语义门控+扰动驱动融合的路由逻辑，仅激活与用户查询、待推商品相关的更新知识，降低无关内容干扰，减少幻觉

  - 多模态模型增量更新的工程实现可借鉴风险掩码、静态锚点设计，严格控制参数更新范围，千次连续更新的内存开销仅增加200MB级，推理延迟几乎无增长，适合线上高并发场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多模态大模型（MLLM）依赖预训练阶段获取的静态知识，在电商商品信息更新、实时热点事件响应、多模态导购Agent知识迭代等场景，需要对模型进行连续的知识修改，但现有编辑方案大多针对单次孤立更新，连续编辑时会出现严重的灾难性遗忘（旧编辑知识失效）和局部性侵蚀（预训练通用能力退化），多模态场景下的跨模态特征纠缠进一步放大了该问题，无法适配终身连续编辑需求。

### 方法关键点
- 编辑阶段：将参数更新严格限制在历史编辑子空间的正交补集，拆分视觉、文本独立子空间避免跨模态干扰；引入动态风险掩码锚定预训练核心参数，仅更新与新知识相关的活跃参数区间，降低对通用能力的影响
- 推理阶段：采用多粒度知识融合策略，先通过原型锚定语义门控计算输入与编辑知识的相似度，仅触发相关编辑分支；再通过扰动驱动子空间融合，仅替换输出中与编辑知识相关的特征维度，其余特征完全保留预训练结果

### 关键实验
在VLKEB、MMEdit两个多模态知识编辑基准上对比LiveEdit、LEMoE、RECIPE等SOTA方案，基于LLaVA-v1.5-7B backbone测试：1000次连续编辑后，知识可靠性达95.24%，较次优方案高3.02个百分点，文本局部性保持100%；千次编辑仅增加224MB显存开销，单条推理latency稳定在1.1s左右，几乎无额外延迟。

### 核心洞察
终身知识编辑的核心是在参数空间实现新旧知识的几何隔离，同时在推理阶段实现知识的精准路由，才能有效平衡新知识学习的可塑性与旧知识保留的稳定性。
