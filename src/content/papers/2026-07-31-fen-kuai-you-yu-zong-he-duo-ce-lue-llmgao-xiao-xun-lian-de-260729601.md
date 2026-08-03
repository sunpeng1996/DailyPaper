---
title: 'The Parts Are Greater Than the Sum: Automated Task Sequencing for Efficient
  Training of Multi-Policy LLMs'
title_zh: 分块优于总和：多策略LLM高效训练的自动任务序列优化方法
authors:
- Jiajia Tang
- Sizhe Yuen
- Francisco Gomez Medina
- Yali Du
- Adam Sobey
affiliations:
- The Alan Turing Institute
- University of Southampton
- King's College London
arxiv_id: '2607.29601'
url: https://arxiv.org/abs/2607.29601
pdf_url: https://arxiv.org/pdf/2607.29601
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: LLM参数高效微调 · 多策略训练优化
tags:
- PEFT
- LoRA
- QLoRA
- Multi-task Learning
- Continual Learning
one_liner: 通过自动任务分组与排序实现多策略PEFT优化，同等参数量下性能优于单策略与单任务LoRA方案
practical_value: '- 多业务场景PEFT微调可复用任务分组思路：无需用单一LoRA承接全量异构业务，可按梯度冲突+业务行为特征（如文案生成/召回打分/推理类任务）拆分独立LoRA，总参数量不变的前提下提升整体效果

  - 同组业务的微调顺序可复用自动排序逻辑：优先训练复杂度高的通用任务，再训练垂直场景任务，减少灾难性遗忘，提升正向迁移收益

  - PEFT资源分配上，同等总参数量下，均衡分配多LoRA的rank比倾斜分配效果更好，无需刻意给某类业务更高参数预算'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有PEFT方案多采用单一共享LoRA承接异构任务，易出现梯度冲突、负向迁移甚至灾难性遗忘；而单任务独立LoRA方案会丢失跨任务迁移收益，参数量利用率低；现有优化多聚焦提升Adapter容量，未关注训练前的任务组织逻辑，异构任务序列的PEFT训练效率存在明显优化空间。

### 方法关键点
- 提出多策略PEFT框架，总训练参数量与单LoRA基线严格对齐，通过**任务分组+序列排序**两级机制优化训练路径
- 任务分组：融合梯度相似度（PCA降维后计算任务梯度距离）与任务行为特征（prompt长度、输出格式、任务类型等特征计算行为距离），生成统一任务距离矩阵，按均衡聚类拆分任务组，每组对应独立QLoRA
- 任务排序：每个组内按相邻迁移成本、首任务复杂度、尾任务干扰度、全局能力平滑度等指标自动生成最优训练序列，降低任务切换成本与遗忘

### 关键实验结果
- 测试基准为TRACE（含8个异构NLP任务），对比基线包括单QLoRA（rank 128）、O-LoRA（8个独立rank16 LoRA）、随机分组+随机排序多QLoRA等
- LLaMA-2-7B-Chat上，所提方法整体性能（OP）达44.78，比单QLoRA基线高2.66，比O-LoRA高14.02，反向转移（BWT）达0.013实现正向迁移；Vicuna-7B-V1.5上OP达41.14，比随机多QLoRA基线高4.65

### 核心结论
异构任务PEFT优化中，优化路径的组织效率远高于单纯提升Adapter的参数容量。
