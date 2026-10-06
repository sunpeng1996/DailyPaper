---
title: 'ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation
  of Verified Experience'
title_zh: ASCENT：基于验证经验自蒸馏的长周期Agent在线测试时训练方法
authors:
- Haodong Lu
- Dong Gong
affiliations:
- University of New South Wales (UNSW Sydney)
arxiv_id: '2610.05303'
url: https://arxiv.org/abs/2610.05303
pdf_url: https://arxiv.org/pdf/2610.05303
published: '2026-10-03'
collected: '2026-10-06'
category: Agent
direction: 长周期Agent在线自进化优化
tags:
- LLM Agent
- Test-Time Training
- Self-Distillation
- LoRA
- Online Learning
one_liner: 以初始冻结LLM为教师自蒸馏验证经验，实现部署阶段Agent的稳定在线权重进化
practical_value: '- 电商导购、多轮搜索推荐类会话Agent可直接复用ASCENT在线进化框架：以用户有效点击、下单、搜索意图命中为验证信号，基于初始冻结基座自蒸馏成功轨迹更新LoRA权重，避免直接模仿/RL导致的策略漂移，无需额外离线训练阶段

  - 长路径交互任务可复用经验过滤trick：仅保留成功轨迹中的有效动作轮次作为教师特权信息，推理内容比纯动作蒸馏效果提升更显著，小模型优先用短的过滤后特权信息，大模型可加入观测信息进一步提效

  - 在线Agent迭代可替代纯上下文记忆方案：同域任务下将经验内化到LoRA权重，避免RAG检索错误、模型不遵循检索内容的问题，算力充足时可结合RAG和LoRA参数进化实现协同提效'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有部署的长周期LLM Agent要么依赖上下文记忆存储经验，受限于检索准确率和冻结基座的执行能力；要么直接基于交互轨迹做模仿/RL在线更新，容易出现策略漂移、有效动作率下降，无法在单次任务尝试、单轮任务流的部署场景下实现跨任务权重积累。

### 方法关键点
- 定义Online Agentic Test-Time Training（OaTTT）范式：部署阶段Agent仅对每个任务做一次尝试，用轨迹验证结果作为唯一学习信号，更新的LoRA权重跨任务保留
- ASCENT核心设计：用初始冻结的LLM副本作为稳定教师，将验证通过的轨迹作为特权信息输入教师，得到带后验知识的next-token分布，蒸馏给带LoRA的学生模型，仅成功轨迹触发权重更新
- 轨迹过滤优化：移除成功轨迹中的无效动作轮次，仅保留有效轮次的推理+动作内容作为教师的特权输入，进一步提升蒸馏效率

### 关键实验
在ALFWorld、WebShop（模拟电商购物场景）基准测试，用Qwen3.5-4B/9B作为基座，对比10+离线/在线自进化基线：WebShop场景4B基座下严格成功率比基座提升24.1pp，比最强在线基线提升5.1pp，平均交互轮次从39.5降到17.8；ALFWorld场景9B基座下整体成功率比基座提升22.4pp，跨未知场景迁移时成功率达90%。

### 核心结论
在线部署的Agent无需外部教师或离线训练，即可将自身验证成功的交互经验内化到参数中，实现稳定持续进化
