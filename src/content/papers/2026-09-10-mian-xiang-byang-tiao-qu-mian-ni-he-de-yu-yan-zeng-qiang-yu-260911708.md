---
title: Language-Augmented Semantic Priors for B-Spline Surface Fitting
title_zh: 面向B样条曲面拟合的语言增强语义先验框架
authors:
- Yunzhong Lou
- Yusheng Luo
- Jiahao Li
- Yu Song
- Xiangdong Zhou
affiliations:
- College of Computer Science and Artificial Intelligence, Fudan University
arxiv_id: '2609.11708'
url: https://arxiv.org/abs/2609.11708
pdf_url: https://arxiv.org/pdf/2609.11708
published: '2026-09-10'
collected: '2026-09-13'
category: Other
direction: LLM引导几何优化 · CAD曲面拟合
tags:
- LLM
- Semantic Prior
- B-spline Fitting
- CAD
- Geometric Optimization
one_liner: LASP语言增强语义先验框架借助LLM提取建模历史语义，优化B样条曲面拟合效果
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
传统CAD系统的B样条/NURBS曲面拟合高度依赖预设启发式初始化，忽略建模历史中存储的设计意图、过程语义信息，导致高层设计需求与底层几何求解配置脱节，易生成次优、语义不一致的拟合结果。
### 方法关键点
1. LASP语言增强语义先验框架作为独立语义推理层部署在现有几何求解器上层，无需修改原有内核逻辑
2. 首先将建模操作序列转换为覆盖设计意图、几何上下文、功能关联的结构化文本描述，再通过微调LLM输出求解器可直接使用的B样条先验参数
3. 采用两阶段训练策略，同时融合局部几何规则约束与长程上下文依赖，输出的先验兼具可解释性与语义一致性
### 关键结果
实验验证语言驱动的语义推理可为几何求解提供强归纳偏置，效果优于传统机器学习方案，为CAD系统提供了语言引导几何优化的新范式
