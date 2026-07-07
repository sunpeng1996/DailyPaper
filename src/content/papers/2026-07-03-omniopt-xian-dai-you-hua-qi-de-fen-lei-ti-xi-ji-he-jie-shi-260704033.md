---
title: 'OmniOpt: Taxonomy, Geometry, and Benchmarking of Modern Optimizers'
title_zh: OmniOpt：现代优化器的分类体系、几何解释与基准测试
authors:
- Siyuan Li
- Jiabao Pan
- Yumou Liu
- Zhuoli Ouyang
- Xin Jin
- Xinglong Xu
- Jingxuan Wei
- Shengye Pang
- Jintao Che
- Xuanhe Zhou
affiliations:
- 上海人工智能实验室
- 上海大学
- 西湖大学
- 上海交通大学
- 中国科学院大学
arxiv_id: '2607.04033'
url: https://arxiv.org/abs/2607.04033
pdf_url: https://arxiv.org/pdf/2607.04033
published: '2026-07-03'
collected: '2026-07-07'
category: Training
direction: 大模型训练优化器统一框架与基准
tags:
- Optimizer
- LLM Training
- Benchmark
- Taxonomy
- LMO
one_liner: 构建覆盖108种优化器的双维度分类体系与跨场景基准，统一优化器的理论解释与评估标准
practical_value: '- 训练LLM4Rec、推荐排序模型时可直接参考OmniOpt的优化器选型规则，根据显存、计算预算、收敛速度需求匹配T1-T5类优化器，避免盲目调优

  - 针对低资源场景下的小模型微调（如LoRA微调电商多轮对话Agent），可直接复用论文中状态压缩类优化器（如Adam-mini、8-bit Adam）的性能对比结论，优先选择适配长上下文/多模态的压缩方案

  - 自研场景适配优化器时可参考5阶段元流水线框架，仅针对性修改1-2个阶段的逻辑即可，比如在S3阶段自定义动量更新规则适配稀疏电商用户行为数据'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM等大模型训练的优化器选型已成为受算力、显存、调优成本、任务类型联合约束的系统级决策，但现有上百种优化器方法体系碎片化，不同研究的实验结论受协议影响波动大，缺乏统一的分类、理论解释与跨场景基准，工业界选型效率极低。

### 方法关键点
- 提出通用5阶段优化器更新元流水线（参数路由、梯度变换、状态演进、更新重建、最终写入），证明绝大多数优化器仅修改1-2个阶段逻辑
- 基于范数约束线性最小化预言机（LMO）构建四轴分解框架，从数学层面统一不同优化器的更新方向计算逻辑
- 构建双维度分类体系，维度A按机制将108种优化器分为自适应矩、矩阵结构、离散量化、状态压缩、曲率正则5大类，维度B按优化目标分为收敛效率、计算成本、显存开销、稳定性、超参鲁棒性、泛化性6类
- 跨域基准覆盖60M-1B参数LLM预训练、图像分类任务，系统对比不同优化器在多维度目标下的权衡关系

### 关键实验
在C4、FineWeb-Edu等数据集上对比AdamW、Lion、Muon、GaLore等主流优化器，核心结论：1）无单一优化器在所有目标下占优；2）激进状态压缩优化器在短上下文下表现优异，但长上下文下性能下降超15%；3）结构化矩阵方法跨架构迁移稳定性最高，但单步计算耗时提升30%以上。

**最值得记住的一句话**：优化器选型没有全局最优，只有基于场景约束（算力、显存、任务类型）的帕累托最优。
