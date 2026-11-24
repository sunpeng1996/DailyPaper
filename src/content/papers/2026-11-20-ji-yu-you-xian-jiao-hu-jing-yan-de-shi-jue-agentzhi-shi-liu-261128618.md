---
title: Distilling Visual Agents from Limited Interaction Experience
title_zh: 基于有限交互经验的视觉Agent知识蒸馏
authors:
- Siyu Zhou
- Jing Jiang
- Chengqi Zhang
- Guodong Long
affiliations:
- University of Technology Sydney
- Hong Kong Polytechnic University
arxiv_id: '2611.28618'
url: https://arxiv.org/abs/2611.28618
pdf_url: https://arxiv.org/pdf/2611.28618
published: '2026-11-20'
collected: '2026-11-24'
category: Agent
direction: 视觉Agent · 少样本知识蒸馏
tags:
- Visual Agent
- Knowledge Distillation
- Few-shot Learning
- Trajectory Selection
- On-policy Distillation
one_liner: 通过覆盖性优先的轨迹选择策略，仅用4条交互经验即可实现视觉Agent高效蒸馏
practical_value: '- 做电商导购、内容理解类多轮交互Agent蒸馏时，可复用「技能-场景覆盖优先+决策序列相似度」的贪心轨迹筛选策略，仅用少量代表性数据即可达到接近全量的效果，大幅降低数据采集标注成本

  - 离线场景可直接采用固定历史前缀的OPD蒸馏，无需训练过程中与环境实时交互，工程实现难度低，且能保留90%以上的在线蒸馏收益，适合存量用户交互轨迹的离线建模

  - 少样本Agent微调无需盲目堆数据，少量高质量代表性轨迹重复训练的效果优于大量低质量轨迹，可优先投入资源做数据筛选而非数据扩容'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视觉Agent知识蒸馏依赖大量交互数据，采集、标注成本极高，且多轮交互存在动作诱导的状态分布偏移问题，小样本下蒸馏效果差，难以落地到对成本敏感的业务场景。
### 方法关键点
- 预构建统一的技能-上下文标签体系，对全量交互轨迹标注技能覆盖情况、决策序列语义特征，标注结果仅用于轨迹筛选，不输入模型
- 贪心选择代表性轨迹：优先选择覆盖更多技能-上下文组合的轨迹，覆盖度相同时选择决策序列与全量轨迹池相似度最高的，最大化少量数据的价值
- 支持两种蒸馏模式：离线OPD基于固定历史前缀重放，无需实时环境交互；在线OPD基于少量任务实时交互，适配场景更新需求
### 关键实验
以Qwen3.5 27B为教师模型、4B为学生模型，仅用4条筛选的轨迹：① Navigation任务成功率从49.17%提升至82.08%，回收91.86%的师生性能差；② Sokoban任务成功率从60.16%提升至85.55%，回收90.28%的师生性能差；③ 离线OPD保留91.36%的在线蒸馏收益，无需训练时交互。
### 核心结论
视觉Agent蒸馏的效果不取决于数据量，而是取决于少量代表性轨迹的技能覆盖度与重复训练强度
