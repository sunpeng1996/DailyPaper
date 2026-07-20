---
title: 'PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization'
title_zh: PagedWeight：基于动态质量感知量化的MoE大模型高效服务系统
authors:
- Yuchen Yang
- Yifan Zhao
- Anisha Dasgupta
- Sasa Misailovic
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2607.16184'
url: https://arxiv.org/abs/2607.16184
pdf_url: https://arxiv.org/pdf/2607.16184
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: MoE LLM推理服务·内存优化
tags:
- MoE
- LLM Serving
- Quantization
- KV Cache
- Memory Management
one_liner: 通过页式动态调整MoE权重量化精度，平衡KV缓存与模型权重的GPU内存占用，兼顾精度与吞吐
practical_value: '- 部署MoE LLM的电商智能客服、Agent推理、生成式推荐业务，可复用分层量化调度思路：按专家调用频率、精度敏感度分层，KV缓存压力大时优先量化低敏感度冷专家，避免业务效果下降

  - 工程上可借鉴异步页式权重迁移+融合混合精度MoE kernel设计，将权重调整开销隐藏在推理间隙，吞吐损失控制在5%以内，满足线上延迟要求

  - 长上下文业务（如多轮对话、长商品文档理解）可复用这套动态内存平衡方案，同等GPU配置下支持更长上下文，或降低单实例部署成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE LLM推理时GPU内存需同时存储模型权重与KV缓存，静态量化无法适配KV缓存随上下文动态增长的压力，当权重占GPU内存超60%时，易出现内存不足导致长上下文推理失败、吞吐受限的问题。
### 方法关键点
- 借鉴PagedAttention思路，将MoE专家的线性块权重按bit-plane拆分为可换页单元，维护权重页表记录各模块当前精度、页位置与内存占用
- 质量感知调度器融合三类信号做量化决策：离线校准的全局Hessian敏感度、在线统计的专家路由热度、当前prompt的输入特征残差，优先选择精度损失最小的权重做降量化
- 采用异步页迁移管道隐藏CPU-GPU数据传输开销，搭配融合混合精度MoE kernel，支持不同专家模块动态使用不同位宽推理
### 关键结果
在Qwen1.5-MoE、Mixtral-8x7B、Gemma-4-26B三个主流MoE模型上测试，对比FP16、APL、MxMoE、DP-LLM基线：FP16等价精度下最高实现72.0% GPU内存节省、1.94×吞吐提升；同等内存预算下效果比基线最高高39.3%，吞吐损失最多4.1%；长上下文任务下10GB内存即可达到FP16同等效果，比均匀量化高4.8%平均得分。
### 核心结论
MoE推理的内存优化不能只聚焦KV缓存，动态调整权重精度释放内存是兼顾效果、成本、吞吐的有效路径
