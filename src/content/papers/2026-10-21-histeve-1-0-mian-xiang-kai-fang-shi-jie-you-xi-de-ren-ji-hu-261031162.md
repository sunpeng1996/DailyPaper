---
title: 'HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games'
title_zh: HiSTEVE 1.0：面向开放世界游戏的人机交互VLA分层智能体
authors:
- Zecong Tang
- Zian Guan
- Yuncheng Guo
- Zhanqiu Zhang
- Yiwen Guo
- Bo Dai
affiliations:
- The University of Hong Kong
- Zhejiang University
- Fudan University
- LIGHTSPEED
arxiv_id: '2610.31162'
url: https://arxiv.org/abs/2610.31162
pdf_url: https://arxiv.org/pdf/2610.31162
published: '2026-10-21'
collected: '2026-10-26'
category: Agent
direction: 具身Agent · VLA分层架构设计
tags:
- VLA
- Embodied Agent
- Hierarchical Planning
- Minecraft
- Multimodal
one_liner: 提出分层VLA智能体HiSTEVE，融合能力感知编排与原生界面控制，在Minecraft任务上取得SOTA性能
practical_value: '- 分层编排+低阶执行的架构可直接复用：电商导购Agent、内容运营Agent可拆分上层VLM规划（对齐用户需求、子任务拆解）+下层固定能力执行（商品查询、订单操作），从架构层面避免规划脱离执行能力的问题

  - 异质任务轻量化分支设计可迁移：当模型同时处理多模式任务（比如推荐场景同时处理文本召回、GUI弹窗交互、语音指令响应），可采用分支RMSNorm+独立token表征方案，相比全参数分支架构参数量开销极低，同时避免负迁移

  - 轻量任务完成检测器思路可复用：推荐/广告系统的子目标判断（用户加购/下单是否成功、种草内容是否触达）无需调用大模型，可训练轻量小模型结合业务上下文做预测，大幅降低延迟和成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有开放世界具身Agent存在明显能力断层：要么仅支持原生界面控制但缺乏长时序任务规划与状态跟踪能力，要么上层规划依赖环境API、预定义技能，无法适配无官方接口的开放场景；同时GUI/非GUI异质交互的语义差异，会导致单模型联合训练出现负迁移，子任务完成时机判断偏差也会在长链路任务中累积错误，最终大幅降低成功率。

### 方法关键点
- 上层能力感知编排层：搭建包含工作/情景/程序/世界记忆的结构化记忆体系，VLM规划器仅从VLA已支持的原子子任务库中选择下一步动作，避免生成不可执行的规划；新增策略耦合的轻量任务完成检测器，结合VLA运行上下文判断子任务完成状态，触发控制权回传编排层做结果校验、错误恢复或动态重规划
- 下层VLA控制层：基于Qwen2.5-VL-7B改造，新增异质交互适配机制：RS-Norm为非GUI/GUI任务分设独立RMSNorm缩放向量、Dual-Mouse为两类场景分配独立的鼠标动作token集，仅增加极少量参数即可避免跨任务负迁移
- 三阶段训练策略：依次完成领域知识注入、模仿学习、结合环境反馈的RL微调（GRPO+DPO混合损失），提升执行可靠性

### 关键实验
在Minecraft三大基准测试：MineStudio Bench平均成功率85.0%，较SOTA基线提升20个百分点；OpenHA平均成功率37.4%；LongBench长时序任务中Resource&Crafting类成功率42.9%，较SOTA基线提升28.6个百分点；1.4B参数量的任务完成检测器F1达0.863，优于GPT-5.5的0.776。

### 核心结论
仅提升低阶执行能力不足以解决长时序任务性能瓶颈，必须搭配状态感知的编排层做任务跟踪、校验与动态规划调整
