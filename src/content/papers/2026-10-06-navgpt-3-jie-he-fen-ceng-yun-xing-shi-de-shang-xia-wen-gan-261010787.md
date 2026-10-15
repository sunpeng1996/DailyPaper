---
title: 'NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime'
title_zh: NavGPT-3：结合分层运行时的上下文感知具身导航Agent
authors:
- Gengze Zhou
- Yicong Hong
- Jiazhao Zhang
- Xunyi Zhao
- Jian Zhou
- Zixing Lei
- Zun Wang
- Chongyang Zhao
- Xionghui Chen
- Stephen Gould
affiliations:
- Adelaide University
- Metacognition
- ANU
- Roblox
- PKU
arxiv_id: '2610.10787'
url: https://arxiv.org/abs/2610.10787
pdf_url: https://arxiv.org/pdf/2610.10787
published: '2026-10-06'
collected: '2026-10-15'
category: Agent
direction: 具身Agent · 规划执行分层协作
tags:
- Embodied Agent
- VLA
- Hierarchical Planning
- Runtime System
- Vision-Language Navigation
one_liner: 提出类OS异步运行时连接LLM规划器与VLA执行器，在RxR-CE导航任务上达到人类水平
practical_value: '- 分层异步架构可直接复用：将LLM规划层与小模型执行层拆为独立线程，用优先级中断调度，既保留LLM复杂推理能力，又将执行延迟从3-19s降至0.5-1s，适合长会话导购等场景，LLM后台推理不阻塞实时推荐响应

  - 视觉token的codec分配方法可迁移：按内容变化量分配token配额（I帧全量、P帧按变化比例分配），比纯位置加权效率高2-5个百分点，适合多模态推荐长序列用户行为建模，将配额向变化大的行为/内容倾斜

  - 递归自优化（RSI）接口迭代方法可复用：用自动树搜索迭代工具定义、Prompt格式，无需修改模型权重即可将成功率从66%提升至81%，适合业务侧LLM工具调用系统调优，无需频繁微调即可快速涨点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有具身Agent要么用LLM直接决策延迟过高，无法应对实时环境变化；要么用端到端VLA缺乏长程推理能力，两者协同缺乏统一的上下文管理、优先级调度机制，无法兼顾推理准确性与执行实时性。

### 方法关键点
- 类OS异步运行时设计：将规划、执行、监控拆为独立线程，按优先级分配运动控制权，高优先级事件可直接中断低优先级操作，支持线程上下文保留与无缝切换
- 分层协同机制：上层LLM规划器通过空间工具集调用下层NavGPT VLA执行导航，VLA执行后返回路径关键帧、状态反馈，规划器可基于反馈做路径修正、回溯、终止判断
- NavGPT VLA优化：基于视频I/P帧思想做codec视觉token分配，按帧间变化比例分配token配额；训练集覆盖19.28M多场景多任务样本，融合行动回归与next-token预训练

### 关键结果
- 基准测试：R2R-CE上SR达81.51，比SOTA高4.11个百分点；RxR-CE上SR达90.43、nDTW达78.47，首次追平人类表现，单episode耗时仅82s，远低于人类的3分钟
- 消融实验：单独8B VLA的RxR-CE SR达82.39，分层架构相比纯LLM决策延迟从3-19s降至0.78s，成本降低40%-64%

最值得记住的结论：LLM与小模型执行器的系统层协同设计，比单一模型性能优化的收益更大，是兼顾推理能力与实时性的核心路径
