---
title: 'Symmetry in Time: A Representation Theory of Linear Recurrent Memory'
title_zh: 时间中的对称性：线性循环记忆的表示理论
authors:
- Anif N. Shikder
- Ramit Dey
- Jan Minac
- Lyle E. Muller
affiliations:
- Fields Institute
- Western University
- University of Texas at Dallas
arxiv_id: '2611.17162'
url: https://arxiv.org/abs/2611.17162
pdf_url: https://arxiv.org/pdf/2611.17162
published: '2026-11-12'
collected: '2026-11-13'
category: Training
direction: 序列模型 · 状态空间模型优化
tags:
- SSM
- State Tracking
- Representation Theory
- HyperSSM
- Quaternion
one_liner: 用表示理论解释SSM顺序记忆缺陷，提出带四元数通道的HyperSSM实现高精度长程状态跟踪
practical_value: '- 长上下文Agent记忆模块选型：对需跟踪非交换操作顺序的场景（如用户交互行为序列、Agent工具调用链路），可引入四元数通道的SSM替代普通Mamba，既避免顺序丢失，又保留线性推理速度

  - 长序列推荐建模优化：对需泛化到远超训练长度的序列任务（如用户年度行为建模、长会话推荐），可参考代数通道选择思路，根据任务群结构选最小代数块，降参同时提升长程精度

  - 可解释推荐模型设计：HyperSSM权重可直接映射到任务操作结构，可用于用户行为隐式操作挖掘、推荐归因分析，提升黑盒序列模型的可解释性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有主流对角化SSM（如Mamba系列）依赖实数/复数乘法实现并行扫描，天然可交换，无法跟踪非交换操作的先后顺序，在状态跟踪类任务（如操作序列、长程序执行）上表现失效，此前缺乏统一理论框架解释这一缺陷并指导SSM架构设计。
### 方法关键点
- 基于群表示理论形式化线性循环记忆的跟踪能力：证明SSM的状态更新是输入序列幺半群的线性表示，仅当目标群是过渡矩阵生成群的商群时可被精确跟踪
- 证明所有线性循环记忆可拆分为实数、复数、四元数三种独立块，低于4实维的通道仅能跟踪交换群，无法保留顺序信息
- 提出HyperSSM：每个通道独立选择代数系统（实数/复数/四元数/矩阵块），保留原SSM的线性推理和并行训练能力，无需修改并行扫描逻辑
### 关键实验
在状态跟踪基准上，HyperSSM仅用1-5个状态就实现精确解，其中S5（5对象排列，32生成器）任务上原有SSM准确率接近随机（<2%），HyperSSM准确率100%，且能泛化到25倍训练长度的序列；在陀螺仪、量子门、蛋白质骨架三个物理序列任务上，单四元数通道的HyperSSM性能超过128维复数SSM和LSTM，泛化到60倍训练长度时误差仍低于物理模型。
### 核心结论
线性循环记忆的顺序保留能力由其代数系统决定，而非参数量或宽度，针对任务的群结构选择最小代数块是实现长程精确序列建模的关键
