---
title: 'Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments'
title_zh: Terminal-Universe：从Agent轨迹生成可扩展终端执行环境
authors:
- Jie Wu
- Zhenru Zhang
- Beichen Zhang
- Xuwu Wang
- Yuhui Su
- Mouxiang Chen
- Peng Wang
- Zhihai Wang
- Que Shen
- Hao Zhou
affiliations:
- Alibaba Qwen Team
- Tsinghua University
arxiv_id: '2609.04148'
url: https://arxiv.org/abs/2609.04148
pdf_url: https://arxiv.org/pdf/2609.04148
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: Agent 执行环境与训练数据合成
tags:
- Agent Trajectory
- Environment Reconstruction
- Terminal Agent
- SFT Data Synthesis
- Multi-turn Agent
one_liner: 通过Agent轨迹反推重建可复用终端环境，配套多维度任务生成范式，高效优化终端Agent能力
practical_value: '- 针对现有Agent轨迹数据利用率低的问题，可复用「确定重放+Agent补全」的两阶段环境重建方案，把历史交互轨迹转化为可执行训练环境，降低从零构建环境的成本

  - 任务生成的广度+深度扩展思路可迁移到电商Agent训练：广度上做跨场景（如导购+售后）联合任务，深度上做多轮用户交互轨迹生成，提升Agent复杂场景适配能力

  - 验证了基于重建环境重新生成的SFT数据效果远优于直接拟合原始轨迹，做Agent微调时优先选择经过可执行环境验证的高质量轨迹数据，而非直接用历史交互log

  - 可迁移数据预算分配结论：相同训练数据量下，优先扩充不同环境的样本，而非同一环境下多任务/多解样本，性价比更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前终端类代码Agent普及后积累了大量轨迹数据，但可执行、高真实感的训练环境稀缺，人工构建环境成本高、规模有限；直接用原始轨迹做SFT效果差，因为轨迹是静态的，无法验证正确性也无法扩展新任务，亟需低成本大规模构建可执行Agent训练环境的方案。

### 方法关键点
- 环境重建分两阶段：先确定性重放轨迹里的文件读写编辑操作，还原Agent修改前的部分工作区；再用补全Agent自动补充缺失文件和依赖，确保环境可执行且不泄露解决方案
- 任务扩展分两个维度：广度上挖掘不同环境的依赖关系，生成跨工作区复杂任务；深度上用用户模拟器把单轮任务扩展为多轮交互会话，模拟真实迭代需求反馈场景
- 所有生成任务都配套自动生成的可执行验证器，仅保留通过测试的轨迹作为SFT训练数据，严格过滤低质量样本

### 关键实验
基于公开终端Agent轨迹生成37.3k符合要求的可执行环境，配套32k条SFT训练样本；在Qwen3.5-27B上微调后，单轮任务Terminal-Bench 2.1得分提升11.9个百分点，多轮任务EvoCode-Bench v2 MT@4提升13.8个百分点；消融实验验证重建环境后重解任务的效果比直接拟合原始轨迹高15.4分。

### 核心结论
静态的Agent轨迹只是单次演示，反推得到的可执行环境才是可复用、可扩展的高价值训练资源。
