---
title: 'FACET: Preserving Source Intent and Executable State in Terminal Task Synthesis'
title_zh: FACET：保留源意图与可执行状态的终端Agent任务合成框架
authors:
- Kou Shi
- Zun Wang
- Qisheng Su
- Shiting Huang
- Ziao Zhang
- Zhen Fang
- Qingnan Ren
- Jin Liu
- Yu Zeng
- Yiming Zhao
affiliations:
- University of Science and Technology of China
- Shanghai AI Laboratory
- Fudan University
arxiv_id: '2608.18580'
url: https://arxiv.org/abs/2608.18580
pdf_url: https://arxiv.org/pdf/2608.18580
published: '2026-08-18'
collected: '2026-08-20'
category: Agent
direction: 终端Agent · 训练数据合成
tags:
- Agent
- Task Synthesis
- Terminal Agent
- SFT Data
- Execution Grounding
one_liner: 提出基于共享可执行状态的终端Agent任务合成框架，生成高质量监督数据提升终端交互性能
practical_value: '- 做Agent训练数据合成时，可复用「先构造真实可执行环境，再按指令→解决方案→验证器顺序生成组件」的范式，避免各组件基于不同假设生成导致的无效数据

  - 多模块生成的任务/工作流管线，可参考针对性修复机制，仅修改出错的单一组件无需全量重生成，大幅提升复杂数据的生产效率

  - 构建长链路交互类Agent的训练集时，可参考多维度场景建模方法，还原跨技能依赖、状态流转、约束等信息，提升训练数据的信息密度和迁移效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
终端Agent训练需要规模化可执行监督数据，但现有多阶段任务合成方案易丢失源技能的目标、依赖、状态流转等信息，且指令、环境、解决方案、验证器等组件易出现不一致，导致任务不可解或评估错误，亟需兼顾信息保留和跨组件一致性的合成框架。
### 方法关键点
- 三阶段流水线：首先从公开技能库采集过滤得到71K有效技能，通过场景提取、相似性检索构建高质量场景-技能关联库
- 多维度Agentic场景重建：从目标、上下文、能力、状态、工具5个维度还原跨技能依赖、状态流转、约束信息，生成对齐的解决方案、指令参考
- 共享可执行状态范式：先构造并修复容器环境，将真实落地的环境状态作为所有下游组件的共享锚点，按指令→解决方案→验证器的顺序依次生成各组件
- 针对性修复机制：执行验证失败时仅定位修复出错的单一组件，无需全量重生成，大幅提升合成效率
### 关键结果
生成6K有效终端任务，采集1.2K成功轨迹做SFT后，Qwen3.5-4B/9B/27B在Terminal-Bench 2.1上分别获得7.12/8.24/6.75的绝对性能提升，27B模型性能接近参数规模15倍的Qwen3.5-397B；相比逆向/联合生成顺序，正向生成的初始任务有效率最高达46.5%，修复后最终产出率达83%。

**最值得记住的结论**：多组件任务合成的核心是用真实可执行状态作为共享锚点，而非依赖文本描述传递信息，可大幅降低组件漂移率、提升数据有效性。
