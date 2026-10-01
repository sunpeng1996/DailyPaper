---
title: Learning Functional Subspaces for Neural Network Compression
title_zh: 面向神经网络压缩的功能子空间学习方法
authors:
- Massimo Bini
- Anders Christensen
- Stephan Alaniz
- Judah Goldfeder
- Ole Winther
- Yann LeCun
- Ravid Shwartz-Ziv
- Zeynep Akata
affiliations:
- Helmholtz Munich
- Technical University of Munich
- New York University
- University of Copenhagen
- Columbia University
arxiv_id: '2609.40127'
url: https://arxiv.org/abs/2609.40127
pdf_url: https://arxiv.org/pdf/2609.40127
published: '2026-09-30'
collected: '2026-10-01'
category: LLM
direction: 大模型低秩压缩 · KV缓存优化
tags:
- Model-Compression
- Low-Rank-Factorization
- KV-Cache
- LLM-Optimization
- SVD
one_liner: 提出端到端学习可删除子空间的低秩压缩方法LSP，大幅提升高压缩比下模型性能与推理效率
practical_value: '- 业务侧小算力部署LLM可直接复用LSP方案：冻结预训练权重仅学习正交投影器，仅需少量无标注校准数据就能获得远优于传统SVD的压缩效果，适配推荐/Agent场景的端侧、边缘端部署需求

  - 推荐/Agent场景的LLM服务KV缓存压力大时，可借鉴Q/K/V层绑定共享投影器的设计，配合latent cache能将128k上下文的权重+KV缓存总内存降低13.5倍，大幅提升单卡上下文承载量与并发数

  - 低秩压缩的秩分配可参考measured-KL方法：通过单截断对全局输出KL的影响来分配各层秩，比传统均匀分配、层级准则分配的效果更好，相同压缩比下能保留更多业务相关的功能'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有低秩压缩方法依赖层级局部准则（激活能量、层重建误差等）选择待删除子空间，忽略误差在网络深度中的传播效应，高压缩比下性能骤降；同时无法兼顾推理效率尤其是KV缓存的优化，难以满足大模型业务部署的低内存、高吞吐需求。
### 方法关键点
- 为共享输入的层组（如Q/K/V、gate/up）分配绑定的正交投影器，冻结预训练权重，端到端联合优化所有投影器，优化目标为与稠密模型输出的KL散度或原训练损失
- 初始化采用白化SVD截断，通过measured-KL方法分配各层秩：测量单一层截断对全局输出KL的影响，优先删除KL代价/节省参数量比值最低的方向
- 训练后投影器合并为标准低秩因子，无额外算子开销；Q/K/V绑定投影支持缓存共享latent，大幅降低KV缓存占用
### 关键实验
在OPT-125M/1.3B、Qwen3-4B、Llama-2-7B等LLM上验证，对比SliceGPT、SVD-LLM、LLM-Surgeon等主流基线：70%压缩比下，Llama-2-7B的WikiText-2困惑度仅10.9（基线最优为13.3），零-shot平均准确率达42.2%（基线最优为36.0%）；小batch解码速度比稠密模型高1.6倍，128k上下文下权重+KV缓存总内存比稠密模型低13.5倍（基线最优仅6.5倍），单张GH200可承载322k上下文。
### 核心结论
激活的统计冗余不等于功能冗余，基于全局输出损失学习的可删除子空间，能在高压缩比下同时保留模型性能与推理效率。
