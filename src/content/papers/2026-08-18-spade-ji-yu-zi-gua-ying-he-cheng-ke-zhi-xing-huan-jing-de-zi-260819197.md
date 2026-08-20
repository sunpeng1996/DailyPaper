---
title: 'SPADE: Self-Play in Adaptive Synthetic Executable Environments'
title_zh: SPADE：基于自适应合成可执行环境的自训练Agent框架
authors:
- Bo Liu
- Simon Yu
- Yiding Jiang
- Ao Qu
- Andrew Zhao
- Zichen Liu
- Junsu Kim
- Zijian Zhou
- Seungone Kim
- Tongzheng Ren
affiliations:
- University of Washington
- Stanford University
- Northeastern University
- Carnegie Mellon University
- Massachusetts Institute of Technology
arxiv_id: '2608.19197'
url: https://arxiv.org/abs/2608.19197
pdf_url: https://arxiv.org/pdf/2608.19197
published: '2026-08-18'
collected: '2026-08-20'
category: Agent
direction: Agent自训练 · 自适应环境生成
tags:
- Self-Play
- Reinforcement Learning
- LLM Agent
- Environment Generation
- GRPO
one_liner: 单LLM同时扮演环境设计者与推理Agent，通过hint-based regret信号实现能力共进化
practical_value: '- 可复用hint-based regret信号设计业务Agent训练难度函数：训练电商导购、客服Agent时，用「带提示任务完成率
  - 不带提示完成率」作为任务生成器的奖励，自动生成刚好在Agent能力边界的训练任务，大幅降低人工标注与课程设计成本

  - 可复用Gym式代码化环境的统一范式：将电商搜索、推荐、导购的多轮交互场景抽象为带reset()/step()接口的可执行环境，支持单/多轮任务统一训练，同时自动验证环境可执行性过滤无效训练数据

  - 可借鉴corpus grounding + 环境记忆设计避免任务模式坍塌：生成业务训练任务时锚定真实业务语料保证任务多样性，同时缓存历史任务的难度评分，自动避开已掌握/过难的任务，实现动态课程学习'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent训练依赖固定的人工/合成环境池，无法随Agent能力提升动态适配，容易出现性能饱和，且高质量训练环境的人工构建成本极高，已经成为Agent能力迭代的核心瓶颈。

### 方法关键点
- 单LLM共享权重同时扮演双角色：`Environment Designer`生成符合OpenAI Gym接口的可执行Python环境（内置状态转移、奖励函数、验证逻辑），同时输出对应任务的特权hint；`Reasoning Agent`分别在带hint和不带hint的条件下执行环境任务
- 环境设计者奖励采用hint-based regret：即Agent带hint的平均回报减去不带hint的平均回报，引导生成刚好在Agent能力边界、可解且有学习价值的环境
- 新增corpus grounding和环境记忆模块：前者基于外部预训练语料生成环境保证多样性，避免模式坍塌；后者缓存历史环境的难度评分，动态调整生成任务难度

### 关键结果
在30B参数量Qwen3模型上验证，对比固定环境训练基线：数学、科学、代码、推理8个跨域基准平均提升+5.3；工具使用场景下BFCL v4多轮任务提升+5.7，ACEBench-Agent提升+13.9；增益随模型规模扩大进一步提升，且可迁移到完全未见过的OOD任务。

**最值得记住的一句话**：把环境设计本身变成可学习的组件，是实现Agent开放式持续自我提升的核心可行路径。
