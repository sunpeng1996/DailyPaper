---
title: Multi-Branch Transformer
title_zh: 多分支Transformer：兼顾训练效果与推理效率的LLM架构
authors:
- Gaotang Li
- Lingjie Chen
- Chunyuan Deng
- Zhiwei Xu
- Hongzheng Chen
- Christopher De Sa
- Jingrui He
- Yingheng Wang
- Hanghang Tong
affiliations:
- University of Illinois Urbana-Champaign
- Rice University
- University of Michigan
- Cornell University
arxiv_id: '2611.19800'
url: https://arxiv.org/abs/2611.19800
pdf_url: https://arxiv.org/pdf/2611.19800
published: '2026-11-15'
collected: '2026-11-17'
category: LLM
direction: LLM 多分支架构与KV缓存优化
tags:
- Transformer
- KV cache
- LLM
- Inference Optimization
- Model Architecture
one_liner: 提出多分支Transformer架构与Joint-KV机制，同等算力下效果优于标准Transformer，推理吞吐量最高提升51.4%
practical_value: '- 落地LLM驱动的电商推荐/Agent服务时，可复用MBT的中间层多分支设计，在不增加训练算力的前提下提升模型对用户行为序列的建模效果，同时降低长上下文下的KV缓存开销

  - Joint-KV的跨分支共享KV缓存思路可直接迁移至多任务推荐LLM：针对点击、收藏、加购等不同行为分支共享KV，在高并发推荐场景下可减少30%左右的内存占用，提升推理吞吐量

  - 多分支的工程落地可直接复用论文给出的轻量化方案：分支放置在模型中间层、融合用concat+线性投影即可，无需复杂算子，适配现有vLLM等推理引擎，改造代价低

  - 分支分组+头折叠的推理优化trick可直接复用在多分支模型的服务部署上，能将多分支的串行执行步骤减少近一半，进一步提升解码速度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统Transformer仅通过加宽、加深两条路径实现规模扩展，二者均会推高推理成本，尤其长上下文场景下KV cache占用高、解码吞吐量低，亟需新的架构设计在匹配训练算力预算的前提下，同时实现模型效果与推理效率的提升。

### 方法关键点
- 提出Multi-Branch Transformer（MBT）架构：输入先经过共享的prelude初始层，拆分到多个独立参数的并行Transformer分支执行，分支输出融合后送入共享的coda最终层输出，提供Wide-Shallow、Narrow-Deep、Balanced三种与标准Transformer训练算力匹配的分支配置
- 提出Joint-KV机制：同深度的所有分支共享同一KV cache，仅保留分支独立的Query，将分支区域的KV cache存储降到Independent-KV方案的1/K（K为分支数）
- 配套推理优化：基于nano-vLLM实现分支分组（同深度分支批量执行，减少串行步骤）、头折叠（分支维度合并到Query头维度，减少KV重复读取）

### 关键结果
在0.8B~2.1B参数的MoE模型上开展预训练实验，对比标准Transformer：2分支Wide-Shallow MBT需要标准Transformer付出1.23倍训练算力才能达到同等验证损失；Balanced MBT搭配Joint-KV的最终方案，KV cache最多减少34%，单H200 GPU上解码吞吐量最高提升51.4%，零-shot下游任务平均准确率从54.23%提升至56.03%。

**最值得记住的结论**：Transformer的规模扩展除了加宽、加深两条传统路径，还可以通过多分支并行组织全量Transformer块的新路径实现，兼顾建模效果与推理效率。
