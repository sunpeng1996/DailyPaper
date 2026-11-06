---
title: 'From What Is Used to What Is Missing: Rethinking Dynamic Rank in LoRA'
title_zh: 面向缺失任务方向的几何引导LoRA动态自适应秩进化框架GEAR
authors:
- Peng Xue
- Guodong Fan
- Guang-Yong Chen
- Xing Chen
affiliations:
- Fuzhou University
- Shandong Technology and Business University
arxiv_id: '2611.07349'
url: https://arxiv.org/abs/2611.07349
pdf_url: https://arxiv.org/pdf/2611.07349
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: 参数高效微调 · LoRA动态秩优化
tags:
- LoRA
- PEFT
- Dynamic Rank
- Geometric Optimization
- Fine-tuning
one_liner: 提出几何引导的LoRA动态秩进化框架，以远低于基线的参数量实现跨模态任务性能全面提升
practical_value: '- 做LLM4Rec/Agent场景的LoRA微调时，可直接复用GEAR框架，相比固定秩LoRA可减少约2/3训练参数，同时提升下游推荐/推理任务效果，降低显存开销，适配资源受限的线上部署需求

  - 可借鉴切向-法向空间分解思路：先用切向梯度优化当前低秩空间参数，仅当法向频谱检测到高价值缺失任务方向时才扩容秩，避免无效参数浪费，尤其适合推荐多任务微调场景

  - 可复用任务诱导几何初始化（TGI）方法，基于小批量校准数据的梯度结构初始化LoRA子空间，减少初始随机误差，提升小样本/冷启动场景的微调收敛速度与效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LoRA动态秩方法仅基于当前已适配空间的统计信息做容量分配，无法区分「当前空间优化不足」和「存在超出空间的任务相关下降方向」两种情况，导致秩扩容盲目，参数利用率低，无法适配不同层、不同训练阶段的差异化适配需求。

### 方法关键点
- 从几何角度证明标准LoRA因子梯度的不可观测子空间恰好是低秩流形的法向空间：切向梯度对应当前秩下可优化的方向，法向梯度对应必须扩容才能访问的任务相关方向
- 核心框架包含三个模块：切空间优化（仅用切向梯度在当前低秩流形上更新参数，避免全梯度计算）、无矩阵法向频谱估计（通过随机探针高效估算法向梯度的主导谱，评估秩扩容增益）、任务诱导几何初始化（基于小批量校准数据的梯度结构初始化LoRA子空间，减少初始偏差）
- 秩扩容规则：仅当法向频谱的增益在小批量审计集上验证达到阈值时才扩容，严格控制参数总量

### 关键实验
跨语言、视觉多基准测试，对比LoRA、AdaLoRA、FlexLoRA等SOTA基线：LLaMA3-8B常识推理任务平均得分从86.61提升到88.45，训练参数从42.0M降至14.4M；DeBERTa-v3-base GLUE任务平均得分89.63，参数比基线少21%；ViT-B/16 VTAB-1K视觉任务平均得分73.48，参数仅0.2M，比基线少33%。

### 核心结论
LoRA动态秩优化不应仅做现有容量的分配，更应基于当前空间外的缺失任务方向的价值做可控进化，才能实现性能与参数效率的最优平衡。
