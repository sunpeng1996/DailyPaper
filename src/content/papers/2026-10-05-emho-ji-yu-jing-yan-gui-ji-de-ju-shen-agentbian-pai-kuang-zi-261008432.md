---
title: 'EMHO: EMbodied Agent Harness Optimization via Experience Traces'
title_zh: EMHO：基于经验轨迹的具身Agent编排框架自优化方法
authors:
- Hyun Jung Lee
- Jungtaek Kim
- Jongwon Jeong
- Tae-Eui Kam
- Donghyun Kim
- Yong Jae Lee
affiliations:
- Korea University
- University of Arkansas
- University of Wisconsin–Madison
arxiv_id: '2610.08432'
url: https://arxiv.org/abs/2610.08432
pdf_url: https://arxiv.org/pdf/2610.08432
published: '2026-10-05'
collected: '2026-10-14'
category: Agent
direction: 具身Agent · 编排层自优化
tags:
- Embodied Agent
- Harness Optimization
- Experience Trace
- Self-Evolution
- Multi-task Adaptation
one_liner: 冻结底层模型，通过经验轨迹迭代优化具身Agent编排层，支持多子Task共享框架的性能提升
practical_value: '- 落地Agent业务时可优先优化harness层而非直接微调底层LLM，基于业务轨迹迭代调整prompt、工具调用逻辑、失败处理规则，成本低见效快，尤其适合电商导购/客服/内容生成类Agent场景。

  - 多场景共享Agent框架可借鉴EMHO-Merge的损益对比思路，针对不同场景的正/负向Case细化规则触发条件，平衡多场景性能，避免单场景优化对其他场景的负向影响。

  - 稀疏反馈场景下的系统优化可复用「内循环采集全量轨迹+外循环迭代规则+效果验证通过才生效」的迭代范式，避免无依据的人工规则调整。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有具身Agent优化多聚焦微调底层多模态模型，或仅优化技能、错误恢复逻辑等单一组件，而决定Agent规划、工具调用、上下文管理、失败响应的核心编排层（harness）大多依赖人工设计；且具身环境只有稀疏的最终成败反馈，难以定位问题根因，无法充分释放底层模型的已有能力，亟需低门槛的自动化harness自优化方法。

### 方法关键点
- 双循环迭代架构：内循环用当前harness执行任务，采集包含观测、规划、工具调用、动作、环境反馈、最终结果的全量经验轨迹；外循环基于历史轨迹和过往harness迭代记录，定位共性行为缺陷，生成harness修改方案，仅当新方案在搜索集成功率更高时才替换旧版本。
- EMHO-Merge解决多子任务共享harness的优化冲突：对比修订前后的轨迹，识别改动能带来收益的场景和造成劣化的场景，细化规则触发条件，保留收益的同时降低跨场景负迁移。
- 全程冻结底层模型，仅修改harness的prompt、工具调用逻辑、状态检测规则、上下文拼接逻辑等组件，优化成本极低。

### 关键实验
在EmbodiedBench的导航、操作两类任务上验证，覆盖Qwen 9B、27B两种基座模型。对比初始手工harness，EMHO在导航任务最高提升23.3%成功率，操作任务最高提升33.3%；EMHO-Merge相比跨任务合并经验的基线，在导航、操作任务的平均成功率分别提升6.7pp、5.1pp，泛化性优于单任务独立优化。

### 核心结论
Agent落地中，优化编排层对性能的提升潜力远超过微调底层模型，通过业务轨迹迭代的自优化范式可以用极低的成本充分释放现有模型的能力。
