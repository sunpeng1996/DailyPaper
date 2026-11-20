---
title: Beam Model Technical Report
title_zh: Beam MoE大模型技术报告
authors:
- Reflection Team
- Adam Abdulhamid
- Osama Abuelsorour
- Yasmin Alameddine
- Carlo Alfano
- Duarte Alves
- Brandon Amos
- Selvaraj Anandaraj
- Arseni Anisimovich
- George Antoniadis
affiliations:
- Reflection
arxiv_id: '2611.26358'
url: https://arxiv.org/abs/2611.26358
pdf_url: https://arxiv.org/pdf/2611.26358
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: Agent专用MoE大模型训练与优化
tags:
- MoE
- LLM
- Agent
- Reinforcement Learning
- Quantization
- Speculative Decoding
one_liner: 开源501.3B总参/23.4B活参MoE大模型，推理效率超同类模型3-4倍，适配编码、推理与Agent负载
practical_value: '- 训练自有小参数MoE推荐/Agent模型时，可复用自适应专家偏置更新+深度缩放残差连接方案，解决专家负载不均、训练不稳定的问题

  - 电商/推荐场景语料清洗可复用domain分区过滤+质量感知上采样逻辑，分领域做分级筛选，平衡数据质量与数量，减少低质数据干扰

  - 电商导购Agent训练可套用三阶段范式：通用预训练→业务域mid训练扩上下文→RL对齐业务目标，搭配小模型ablation降低大模型试错成本

  - 大模型线上部署（如文案生成、智能导购）可采用FP8/NVFP4量化+小参数投机解码drafter的组合，降低推理成本，提升并发吞吐量'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
面向Agent、编码、推理场景的开源大模型普遍存在推理成本高、长上下文支持不足、安全对齐效果差的问题，同类大参数量模型推理算力需求过高，难以落地到高并发业务场景。
### 方法关键点
- 架构：采用稀疏MoE架构，总参数501.3B，单token仅激活23.4B参数，内置无辅助损失负载均衡、深度缩放残差连接、混洗本地-全局注意力，支持1M token上下文窗口
- 数据：预训练使用23.8T高质量清洗token，按数学/代码/STEM/普通网页分域过滤，自研分布式OCR pipeline处理PDF等非结构化数据，通过质量感知上采样平衡数据质量与重复率
- 训练：采用三阶段流程，预训练→mid训练用正确性锚定数据扩展上下文→后训练调用10.5K GB300 GPU跑4周RL，生成超1亿条rollouts，通过多教师在线蒸馏合并工具调用、安全对齐等专家能力
- 推理优化：搭配FP8/NVFP4量化+1.93B参数投机解码模型DFlash2，最大化部署吞吐量
### 关键结果
- 推理效率比同能力级模型高3-4倍，性能对标GLM-5.2，长文本表现接近Qwen3.8-Max
- 安全对齐表现达开源模型Pareto最优：有害请求拒绝/转义率88.9%，无害请求通过率81.5%；对齐教师从100B扩容到501B后，误拒率下降48.7%
- 预训练阶段专家利用率最终达1.04倍均匀负载，训练goodput达92.3%
### 核心结论
大模型能力与效率的提升依赖数据、架构、训练流程、工程基础设施的全栈协同，而非单点优化
