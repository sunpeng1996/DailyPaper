---
title: 'NeMo-DCR: Bit-Exact Delta-Compressed Refit for Scalable Agentic RL at Trillion-Parameter
  Scale'
title_zh: NeMo-DCR：万亿参数智能体RL的比特精确增量压缩权重同步方案
authors:
- Songlin Jiang
- Zhiyu Li
- Terry Kong
- Yu Yao
- Youngeun Kwon
- Bernard Nguyen
- Ashwath Aithal
- Mario Di Francesco
affiliations:
- Aalto University
- NVIDIA
arxiv_id: '2610.08430'
url: https://arxiv.org/abs/2610.08430
pdf_url: https://arxiv.org/pdf/2610.08430
published: '2026-10-05'
collected: '2026-10-07'
category: Agent
direction: Agent 训练-推理集群权重同步优化
tags:
- Agentic RL
- Weight Synchronization
- Delta Compression
- LLM
- System Optimization
one_liner: 提出比特精确的增量权重同步方案NeMo-DCR，跨集群万亿参数模型同步速度最高提升40倍
practical_value: '- 跨集群部署Agent RL训练（比如推荐场景用户偏好对齐RLHF、电商Agent工具调用微调）时，可直接复用增量同步思路，仅传输变化的权重，将大模型同步耗时从小时级降到分钟级，大幅提升训练迭代效率

  - 混合XOR/overwrite的比特精确编码方案可直接复用，避免增量同步引入的浮点误差导致RL训练不稳定，彻底解决训练-推理权重不匹配问题

  - 采用canonical坐标作为中间层、复用推理框架原生loader的架构设计，无需重写张量布局适配逻辑，可快速接入vLLM等主流推理框架，工程改造成本极低

  - 原地更新+overwrite重试的故障恢复机制无需在推理端备份全量权重，可节省1倍以上的推理端显存开销，适合GPU资源紧张的在线业务场景'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
Agentic RL 通常将训练和rollout（推理采样）集群拆分部署，每次策略更新需跨集群同步全量权重，1T参数模型跨AWS区域同步需要87.5分钟，严重影响训练效率；而BF16训练每步仅约1%的权重存储值发生变化，全量同步存在极大带宽浪费，现有增量同步方案存在布局适配难、比特不精确、无故障恢复、效率低等问题，无法满足万亿参数规模需求。

### 方法关键点
- 基于Hugging Face checkpoint的canonical坐标作为中间层，通过固定仿射映射直接投影训练端分片的权重变化到统一坐标，剩余残差变化通过张量转换覆盖，96%以上权重变化可直接投影，无需全量张量组装
- 混合XOR/overwrite编码：表示不变的变化用XOR掩码编码，压缩率比纯overwrite高38-40%，其余变化用overwrite编码，保证比特完全精确
- 可恢复的原地更新：推理端复用原生loader加载增量，原地应用更新无需备份全量权重，失败重试用overwrite全量覆盖修复部分写入，联合commit保证多节点版本对齐
- 流水线传输：支持对象存储/中继树两种传输模式，无需跨集群集合通信，传输和增量构造、应用流水线重叠，降低端到端延迟

### 关键实验
测试覆盖30B到1T参数的MoE模型，对比baseline为仅传输全量checkpoint的最优方案：1T参数模型3%变化率下，中继树传输仅需150s，比全量同步的87.5分钟快35倍；30B-1T参数模型在3%/5%变化率的压力测试下，同步速度是全量方案的12-40倍；RL训练过程中即使中途杀死推理节点，NeMo-DCR的奖励和KL散度曲线和全量NCCL同步完全一致，无性能损失。

BF16训练每步仅1%左右的权重发生实际存储值变化，基于增量压缩的跨集群权重同步可以将万亿参数模型的同步耗时从小时级降到分钟级，是大规模Agentic RL落地的核心基础能力之一
