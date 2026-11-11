---
title: 'Don''t Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced
  Degradation in LLM Agents'
title_zh: 带证据链路的记忆系统缓解LLM Agent记忆诱导性能退化
authors:
- Yukyeong Lee
- Yumin Choi
- Jinheon Baek
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2611.14320'
url: https://arxiv.org/abs/2611.14320
pdf_url: https://arxiv.org/pdf/2611.14320
published: '2026-11-09'
collected: '2026-11-11'
category: Agent
direction: LLM Agent 记忆机制优化
tags:
- LLM_Agent
- Memory_System
- Experience_Reuse
- Memory_Degradation
- Procedural_Memory
one_liner: 提出证据关联的三层记忆系统WikiTrace，缓解LLM Agent记忆诱导性能退化
practical_value: '- 电商导购、客服类Agent的经验沉淀可复用三层记忆架构：上层存可复用的回复/操作规则，中层存规则对应的场景原因总结，底层存原始用户交互轨迹，避免错误规则误导服务流程

  - 新增记忆触发回溯规则：当规则冲突、规则缺执行细节、规则来自失败场景时，主动拉取原始轨迹校验适用性，可降低记忆带来的错误回复率

  - 评估记忆系统效果时需拆分Gain（记忆解决的历史失败任务占比）和Regression（记忆导致的历史成功任务失败占比），避免只看平均准确率掩盖负向影响

  - 失败经验无需丢弃，关联原始失败轨迹后复用效果优于仅用成功经验，同时可通过回溯避免错误复用'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent的外部记忆仅存储从历史轨迹蒸馏的精简规则/经验，未关联原始轨迹，易出现**记忆诱导退化**：Agent无记忆时可正确执行的任务，加载记忆后反而出错，52%的此类错误源于规则错误、适用范围错配、误用规则等问题，现有方案无法验证记忆的正确性。

### 方法关键点
- 三层关联的只读记忆架构：上层为Insight（单条轨迹蒸馏的精简规则，标注来源轨迹成败状态、适用范围），中层为Compilation（轨迹成败原因、关键决策及支撑证据），底层为Raw Trajectory（未修改的完整原始交互轨迹），三层双向关联
- 测试阶段触发回溯规则：当经验缺乏执行细节、多经验冲突、经验来自失败轨迹时，Agent主动下钻读取关联的中/底层数据，修正或补充经验后再执行

### 关键实验
在5个Agent基准（含零售场景τ3-bench）共8个测试集上对比无记忆基线、AWM、ExpeL等主流记忆方法，以及仅提供相同Insight无链路的基线：
- 平均准确率90.2，较无记忆基线提升10.7个点，较仅Insight基线提升3.2个点，全测试集性能排名第一
- 记忆诱导退化率（Regression）从仅Insight的6.5%降至4.5%，远低于无记忆重跑的9.7%基线，记忆增益（Gain）较仅Insight基线高8个百分点
- 测试阶段仅增加17%的推理成本，跨不同LLM底座效果稳定

### 最值得记住的一句话
Agent记忆不仅要存储可复用的经验，还要保留验证经验正确性所需的原始证据链路
