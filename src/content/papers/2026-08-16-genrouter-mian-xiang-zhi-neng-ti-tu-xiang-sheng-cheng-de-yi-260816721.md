---
title: 'GenRouter: Unified Workflow Routing for Agentic Image Generation'
title_zh: GenRouter：面向智能体图像生成的统一工作流路由框架
authors:
- Harold Haodong Chen
- Zhiyu Hou
- Wen-Jie Shu
- Weilin Ruan
- Yingjie Xu
- Litao Guo
- Ying-Cong Chen
affiliations:
- HKUST(GZ)
- HKUST
- SUSTech
- ZODA
- CUHK
arxiv_id: '2608.16721'
url: https://arxiv.org/abs/2608.16721
pdf_url: https://arxiv.org/pdf/2608.16721
published: '2026-08-16'
collected: '2026-08-18'
category: Agent
direction: Agent 工作流动态路由优化
tags:
- Agent Routing
- Workflow Abstraction
- Text-to-Image
- Dynamic Scheduling
- Self-Evolving System
one_liner: 提出统一工作流抽象GenCanvas+动态路由GenRouter，平衡图像生成质量与算力开销
practical_value: '- 电商AI服务（素材生成、文案生成、多模态内容创作）可先将原子能力拆解为标准化原语（如检索、改写、校验、布局），再搭建梯度复杂度的工作流模板池，避免重复造轮子，解决系统碎片化问题

  - 三阶段路由框架可直接复用：先通过轻量小模型做需求画像（如7维任务签名）过滤无效候选，再用历史经验匹配估算效用，最后Pareto过滤劣化方案，适配不同复杂度的用户请求，大幅降本提效

  - 双内存经验积累机制可复用：实例级轨迹内存+桶级统计内存的设计，解决冷启动和跨场景泛化问题，不需要频繁重训路由模型，适合推荐系统多召回源路由、多Agent服务调度等场景

  - 算力优化思路可复用：仅对复杂请求调用重链路，简单请求走轻量化路径，电商个性化素材生成、智能客服回答、推荐理由生成等场景均可参考，理论可压减90%+算力成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent图像生成工作流均为孤立的固定架构，「一刀切」模式导致严重算力不匹配：简单请求也被迫走带检索、多轮校验的重型链路，浪费算力且延迟极高，同时各框架能力无法复用，碎片化问题突出。

### 方法关键点
- **GenCanvas统一抽象**：将所有Agent图像生成流程拆解为8个标准化原语（rewrite、search、reason、sketch、verify等），基于原语搭建9种梯度复杂度的工作流模板，覆盖从轻量直接生成到多轮迭代校验的全场景需求。
- **GenRouter三阶段路由**：①需求画像：用4B小模型将prompt提取为7维任务签名，基于签名过滤无效候选，大幅缩小搜索空间；②经验匹配：双内存机制，实例级轨迹内存存储历史执行记录，桶级路由内存存储聚合统计数据，加权融合估算各候选方案的质量、成本、延迟；③Pareto过滤：剔除全维度劣化的候选方案，选择效用最高的最优执行计划。
- 自进化机制：每次执行后自动沉淀经验到内存，不需要重新训练即可持续优化路由效果。

### 关键实验
跨5个主流图像生成基准（WISE、DPG-Bench、GenEval2、OneIG-EN/CN）对比静态Agent工作流（Mind-Brush、SCOPE、GEMS），在生成质量超过最优静态基线的前提下，执行成本降低95%以上，端到端延迟降低65%；积累经验后可进一步降低8.7%成本、7.9%延迟，跨场景零样本泛化时性能优于直接用LLM做路由，同时成本减半。

### 核心结论
动态分层路由的投入产出比远高于一刀切的复杂链路架构，仅需不到5%的算力即可获得同等顶级效果。
