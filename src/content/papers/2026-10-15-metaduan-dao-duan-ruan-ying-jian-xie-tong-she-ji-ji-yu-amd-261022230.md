---
title: 'Architecting for Hardware Diversity: Meta''s End-to-End Co-Design for High-Performance
  AI Training on AMD GPUs'
title_zh: Meta端到端软硬件协同设计：基于AMD GPU的高性能AI训练架构
authors:
- Haoyu Zhang
- Arshad Rahman
- Adnan Aziz
- Ajith Prabhudev
- Amin Farmahini
- Ben Rhoads
- Benson Ma
- Brian Shi
- Cen Zhao
- CK Luk
affiliations:
- Meta
- AMD
arxiv_id: '2610.22230'
url: https://arxiv.org/abs/2610.22230
pdf_url: https://arxiv.org/pdf/2610.22230
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: 推荐模型训练 · 异构GPU适配优化
tags:
- DLRM
- HeterogeneousComputing
- GPUTraining
- ROCm
- AgenticWorkflow
one_liner: Meta首次实现AMD MI350X在大规模DLRM训练场景下性能追平高度优化的NVIDIA B200
practical_value: '- 异构GPU选型可优先考量显存容量优势：针对DLRM等显存瓶颈模型，可通过扩大单卡batch、减少重计算、增大embedding表/序列长度，同时实现训练效率和模型效果提升

  - 可复用Origami解析性能模型思路：针对推荐系统多不规则矩阵GEMM场景，替代离线调优，微秒级选出最优kernel配置，93%精度接近穷举调优效果

  - Agentic workflow可落地到自定义算子优化：将算子优化经验沉淀为可复用技能，自动完成瓶颈分析、代码改写、正确性校验，80%+场景达到专家优化水平，降本提效

  - 多芯片GPU原子操作优化可参考层级树缩减方案：针对embedding反向传播等原子冲突密集场景，通过共享内存内聚合减少全局原子操作，最高实现4x kernel加速'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Meta为降本、避免供应商锁定，部署包含NVIDIA/AMD/自研MTIA的异构算力集群，但此前大量NVIDIA专属优化导致软件迁移性能差，尤其是DLRM类训练任务（不规则矩阵、复杂访存、原子操作多）迁移难度远高于推理，行业缺乏超大规模落地的可复用方案。

### 方法关键点
- 软硬件协同设计：针对MI350X 1.6倍于B200的HBM显存优势，调整单卡batch、并行策略、embedding分片，同时扩大模型容量提升效果
- Origami解析性能模型：无需离线调优，微秒级预测GEMM最优tile配置，支持多芯粒架构，93%精度匹配穷举调优效果
- Agentic算子优化工作流：将AMD架构专属优化技巧（PID swizzle、occupancy调整、原子操作转树缩减等）沉淀为可调用技能，自动完成算子瓶颈分析、改写、验证
- 底层库全链路优化：覆盖hipBLAS GEMM、RCCL集体通信、rocSOLVER特征分解、PyTorch Inductor代码生成全栈适配

### 关键结果
对比直接迁移的基线，端到端DLRM训练吞吐最高提升1.5x，几何平均吞吐达到高度优化的B200基线的101%，实现性能持平；定制GEMM kernel比基线提效1.6-2x，原子密集算子最高提效4x，RCCL通信性能拉近到NCCL的85%-90%；方案已在Meta数万张MI350X GPU上生产落地，相关优化已上游到PyTorch、Triton、ROCm开源社区。

> 最值得记住的话：异构算力适配的核心不是硬迁原有实现，而是结合硬件特性做软硬件协同设计，可同时实现效率和效果的双重提升
