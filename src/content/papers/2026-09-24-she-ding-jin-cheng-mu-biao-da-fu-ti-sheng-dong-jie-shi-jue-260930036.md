---
title: 'Aim Short to Reach Far: Your Frozen World Model Can Plan Better Than You Think'
title_zh: 设定近程目标大幅提升冻结视觉世界模型的长程规划性能
authors:
- Xvyuan Liu
- Jianjie Fang
- Chen Gao
- Yong Li
affiliations:
- Tsinghua University
arxiv_id: '2609.30036'
url: https://arxiv.org/abs/2609.30036
pdf_url: https://arxiv.org/pdf/2609.30036
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: Agent 世界模型长程规划优化
tags:
- World Model
- Long-Horizon Planning
- Frozen Model
- Subgoal Planning
- Retrieval Augmented
one_liner: 无需额外训练，通过观测到的近程子目标提升冻结世界模型长程规划性能
practical_value: '- 电商长路径转化/用户旅程规划可复用锚定规划逻辑：无需直接匹配最终下单目标，先检索历史成功转化路径的近程中间节点作为短期优化目标，避免因部分转化步骤短期远离目标而被短视排序拒绝，尤其适合跨品类种草、多步营销活动的路径规划

  - 冻结大模型落地场景可借鉴核心思路：无需额外微调模型权重，仅通过更换打分目标为合理的近程子目标就能大幅提升任务性能，显著降低大模型适配业务的微调和推理成本

  - 检索增强的推荐/规划系统可复用设计trick：执行过程中动态缩小检索的历史轨迹跨度，仅取历史路径的早期后继作为子目标，比额外训练子目标生成模型的落地成本更低，鲁棒性更强'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于视觉世界模型的规划普遍直接用最终目标的距离打分选择动作，存在典型的局部最优缺陷：部分通向最终目标的动作会先短暂远离目标，导致短视的短程规划直接拒绝这些动作，即使预测完全准确、搜索全局最优也会卡住无法到达目标，长程规划场景下性能暴跌。

### 方法关键点
- 提出锚定规划（Anchored Planning, AP）：无需额外训练，直接从历史观测轨迹中检索头尾分别匹配当前状态和最终目标的片段，取该片段起始后5步的观测作为近程子目标
- 支持两类记忆库场景：仅观测无动作的记忆库用CEM方法合成动作，带动作标注的记忆库直接检索Top8候选动作片段，用冻结世界模型预测各动作的终点，选择离近程子目标最近的动作执行
- 执行过程中动态调整检索跨度：随着已执行动作增加，逐渐缩小检索的轨迹长度，最低不低于5步

### 关键实验结果
在LeWM的4个标准控制任务（Cube、PushT、Reacher、TwoRoom）上测试，基线为原生LeWM、直接用最终目标打分的CEM/排序方法：标准启动场景下，仅更换目标的CEM方法平均成功率从9.2%提升到59.8%，排序方法平均成功率从67%提升到83.8%；长程（100-150步目标偏移）场景下AP性能全面超过原生LeWM，2次CEM迭代的性能就超过30次迭代的最终目标打分方法。

### 最值得记住的结论
世界模型的规划性能不仅取决于预测精度，目标选择的影响甚至更大，更低的子目标预测误差不一定对应更好的控制成功率，换个近程目标就能让原本失效的冻结模型完成长程任务。
