---
title: 'Memory as Plans: World-Action Modeling with Memory-Grounded Planning'
title_zh: 《记忆即规划：基于记忆锚定规划的世界-动作建模框架MaP-WAM》
authors:
- Sizhe Zhao
- Haozhe Xie
- Weiyu Zhao
- Chenchu Zhang
- Huan Wang
- Chenyang Wang
- Qinglin Liu
- Shengping Zhang
affiliations:
- 哈尔滨工业大学
- 南洋理工大学
- 山东大学
- 哈尔滨工业大学（威海）青岛研究院
arxiv_id: '2609.11561'
url: https://arxiv.org/abs/2609.11561
pdf_url: https://arxiv.org/pdf/2609.11561
published: '2026-09-09'
collected: '2026-09-11'
category: Agent
direction: Agent 长时序记忆与规划执行优化
tags:
- Long-Horizon Agent
- Memory Mechanism
- Planning Execution
- KV Cache
- MoT
- Embodied AI
one_liner: 将长时序多模态 episodic 记忆转化为紧凑规划，实现固定上下文的高效长周期任务执行
practical_value: '- 长时序依赖场景（如用户全生命周期行为建模）可借鉴「记忆转规划+固定上下文执行」架构，避免上下文长度爆炸导致的推理延迟随历史线性增长

  - 可复用KV缓存优化思路：将静态规划/历史记忆前缀做KV缓存，仅动态更新当前状态相关token的KV，大幅降低长周期任务的推理开销

  - 多模态任务的进度校准机制可迁移到生成式推荐的路径规划场景：如用户浏览路径的进度预测+实时行为对齐，减少规划漂移

  - 结构化记忆存储设计：仅存储每个完成片段的稀疏关键帧/关键行为，而非全量历史，平衡记忆精度和存储/计算开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有机器人长周期任务的记忆机制要么采用语言摘要丢失细粒度视觉证据，要么用增长窗口导致推理延迟、显存占用随历史线性上升，无法平衡记忆完整性和执行效率，非马尔可夫的长时序依赖任务性能受限。

### 方法关键点
- 架构解耦为记忆锚定规划、规划条件执行两个模块：将长时序多模态 episodic 记忆（每个完成片段的指令+8帧稀疏关键帧）作为规划输入，输出包含片段级语言计划+对应视觉引导的紧凑规划
- 提出World-Action-Progress (WAP)模型：基于Mixture-of-Transformers (MoT)架构，联合预测动作块、执行进度、未来视觉动态，进度作为显式时间坐标对齐当前状态与规划
- 设计闭环机制：通过计划-观测对齐校准预测进度，避免长时序推理漂移；进度达到阈值自动触发重规划，更新结构化记忆，执行端上下文长度全程固定
- 全链路支持KV缓存：规划模块的完成片段前缀、执行模块的静态规划前缀均可缓存复用，进一步降低推理开销

### 关键实验
在RMBench长周期机器人操作基准上对比7个主流基线，整体成功率达83.3%，超越最优基线6.2个百分点；真实机器人任务平均成功率达78%；执行端推理延迟稳定在827ms左右，不随历史帧长度增长，而全上下文基线在1700帧时OOM。

### 核心结论
长时序记忆不需要在每一步执行都全量输入执行器，仅需要在规划阶段作为证据生成紧凑指导，即可在保证精度的同时大幅提升效率。
