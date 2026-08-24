---
title: 'HIERA: Workload-Aware Planning Across Implementation Spaces for GPU Kernel
  Optimization'
title_zh: HIERA：面向GPU内核优化的跨实现空间负载感知规划
authors:
- Jinghao Wang
- Qiqi Gu
- Chenpeng Wu
- Jianguo Yao
- Haibing Guan
- Xijun Li
affiliations:
- Shanghai Key Laboratory of Scalable Computing and Systems
- School of Computer Science, Shanghai Jiao Tong University
arxiv_id: '2608.21157'
url: https://arxiv.org/abs/2608.21157
pdf_url: https://arxiv.org/pdf/2608.21157
published: '2026-08-21'
collected: '2026-08-24'
category: Other
direction: GPU内核自动优化 · 层级空间规划
tags:
- GPU Kernel Optimization
- Hierarchical Planning
- Auto-Tuning
- Workload-Aware
- LLM for System
one_liner: 提出层级搜索空间规划框架HIERA，跨多实现空间自动优化GPU内核，无需额外训练性能比肩有训练方案
practical_value: '- 大模型推理/训练服务的GPU内核优化可复用「跨实现空间选型+profiling反馈迭代」思路，替代固定空间搜索，大幅提升优化效率

  - 多实现空间分层搜索的思想可迁移到推荐系统召回/排序链路的多算法选型调优场景，平衡优化灵活性与搜索效率

  - 无需额外训练的零样本优化策略可直接复用在算力紧张的业务GPU算子迭代场景，降低算子优化的额外训练成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有基于LLM的GPU内核优化方法仅在固定实现空间内搜索，要么灵活性不足，要么搜索效率低下，无法适配日益多样化的负载与快速迭代的GPU硬件。
### 方法关键点
HIERA为层级搜索空间规划框架：首先构建合约增强的任务规格，跨PyTorch算子、CUDA库、自定义CUDA内核三类实现空间自适应选择适配方案，再结合profiling反馈与专家知识引导结构化迭代优化，全程无需额外训练LLM。
### 关键结果
- 在KernelBench多负载、多基座LLM测试集上，实现有效性、样本效率、优化性能均优于现有免训练方案，性能比肩需预训练的CUDA-L1
- 科学计算stencil算子案例中，相比cuDNN实现1.53×提速
