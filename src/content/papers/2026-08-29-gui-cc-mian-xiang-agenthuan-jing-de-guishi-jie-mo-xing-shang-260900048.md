---
title: 'GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments'
title_zh: GUI-CC：面向Agent环境的GUI世界模型上下文一致性评估基准
authors:
- Lin Fu
- Zheyuan Yang
- Tianhui Zhang
- Jinbiao Wei
- Guo Gan
- Boxu Liu
- Yilun Zhao
- Yu Rong
affiliations:
- Zhejiang University
- Tongji University
- University of California, San Diego
- Yale University
- DAMO Academy, Alibaba Group
arxiv_id: '2609.00048'
url: https://arxiv.org/abs/2609.00048
pdf_url: https://arxiv.org/pdf/2609.00048
published: '2026-08-29'
collected: '2026-09-02'
category: Agent
direction: GUI Agent 世界模型一致性评估
tags:
- GUI_Agent
- World_Model
- Benchmark
- Contextual_Consistency
- Autoregressive_Rollout
one_liner: 推出双轨评估基准GUI-CC，专门测试GUI世界模型作为Agent环境的多步滚动上下文一致性
practical_value: '- 自研电商端内导购Agent、自动化运营Agent的世界模型时，可复用双轨评估思路：离线基于真实用户操作轨迹做固定动作序列滚动测试，快速定位上下文漂移、状态丢失问题，无需全量对接真实业务环境，降低测试成本

  - 优化GUI世界模型时，可复用论文提出的4类评估维度，优先保障任务进度指标而非仅单步生成视觉质量，避免出现「看起来可用但实际无法支撑多步交互」的无效生成

  - 训练GUI世界模型时，可参考论文的失败归因，重点补充App/端内页面的专属交互规则知识、优化3步以上历史上下文的状态持久化机制，降低错误累积效应'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有GUI世界模型的评估多聚焦单步下一个屏幕的生成质量，忽略了作为Agent交互环境的核心需求——多步滚动时的上下文一致性，视觉合理的生成页面可能出现App漂移、状态丢失、动作效果延迟等问题，无法支撑Agent完成长序列任务，亟需针对性评估基准。
### 方法关键点
- 双轨评估设计：离线参考动作轨基于真实GUI轨迹，从初始真实UI出发沿参考语义动作序列自回归滚动，仅用真实截图做评分不参与生成；在线Agent环轨用固定探测Agent与生成UI交互，直接测试闭环任务完成能力
- 语义动作表示：统一8类通用交互动作（点击、长按、滚动等）加2类终端动作，解耦像素坐标与语义目标，避免像素对齐偏差干扰评估
- 4维评估指标：过渡保真度、过渡合理性、上下文一致性、任务进度，区分局部生成质量与轨迹级环境可用性
### 关键实验
构造500条来自GUIOdyssey的离线轨迹任务、200条模拟器验证的在线任务，覆盖30个移动App；测试18种GUI世界模型配置，最优模型离线任务进度仅16.7、在线里程碑进度仅70.9，加入历史上下文可提升整体得分但任务进度增益有限，近42%的失败源于世界知识缺失、33%源于错误累积、25%源于上下文不一致。
### 核心结论
单步生成的视觉合理性完全无法保证多步交互的环境可用性，GUI世界模型的核心价值是支撑Agent完成任务而非生成好看的界面
