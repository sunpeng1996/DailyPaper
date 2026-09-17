---
title: 'The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained
  Routing Prediction'
title_zh: 突破内存墙另一半：基于路由预测从SSD部署35B MoE模型
authors:
- Yu Lin
- Yiming Wang
- Runyuan Cai
- Hanze Liu
- Xiaodong Zeng
affiliations:
- AutoArk
arxiv_id: '2609.18063'
url: https://arxiv.org/abs/2609.18063
pdf_url: https://arxiv.org/pdf/2609.18063
published: '2026-09-15'
collected: '2026-09-17'
category: LLM
direction: 大模型推理 · MoE 边缘部署优化
tags:
- MoE
- Inference Optimization
- LoRA
- SSD Offloading
- Quantization
one_liner: 通过预路由+非融合恢复LoRA，单24GB消费级设备跑35B MoE达20tok/s
practical_value: '- 端侧/边缘部署LLM Agent、生成式推荐模型时，可借鉴预路由提前预测下一层MoE专家的思路，将权重存在SSD降低内存占用，适配消费级硬件的大模型部署需求

  - 量化+近似路由带来的效果损失，可采用非融合Recovery LoRA方案，无需合并到int4基模型重量化，仅增加极小内存开销即可补回大部分效果，适配电商多场景多LoRA的部署需求

  - MoE大模型推理优化不要仅聚焦计算量裁剪，可通过存储分层+预取调度的系统优化，在普通硬件上即可跑通35B级大模型，大幅降低业务部署大模型的硬件成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
MoE大模型推理受限于静态权重内存墙：35B级int4量化模型占19.5GB内存，普通24GB消费级设备无法全量加载，会挤占OS和KV缓存空间导致速度极慢；直接SSD offloading会因下一层专家选择依赖当前层输出，磁盘读无法和计算重叠，吞吐量远达不到可用水平。
### 方法关键点
- 每层附加轻量prerouter头部，用上一个token的当前层隐藏状态预测下一个token的下一层路由，预测结果直接作为路由使用，让SSD读专家权重和当前层前向计算完全重叠，消除磁盘延迟瓶颈
- 训练非融合Recovery LoRA：在int4基模型上附加LoRA，在采用预路由的学生路径上蒸馏训练，补偿量化和近似路由的效果损失；部署时不合并到基模型，避免重量化导致的LoRA效果丢失，仅增加42MB内存开销
- 分层SSD流加载机制：专家权重以int4格式存在SSD，通过mmap按需加载，适配prefill、decode不同阶段的执行路径，进一步降低内存占用
### 关键结果
- 24GB Mac mini M4 Pro上，35B MoE峰值活跃内存仅2.9GiB，decode速度达20.4tok/s，5个公开基准平均仅比fp16教师模型低3.9个点；8B MoE峰值活跃内存1.5GiB，速度28tok/s，平均低2.8个点
- 16GB MacBook M2上，相比按需加载，预路由在K=2/4/8配置下分别提升decode速度80%/82%/84%
### 核心结论
大模型部署的内存墙一半是KV缓存动态内存，另一半是权重静态内存，后者可通过存储分层+预调度的系统优化，在普通消费级设备上突破规模限制。
