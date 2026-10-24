---
title: 'FilmFlow: Agentic System for 3D Virtual Film Cinematography'
title_zh: FilmFlow：面向3D虚拟电影摄影的多智能体系统
authors:
- Yiming Zhang
- Jiarui Guo
- Haojia Wei
- Yifei Liu
- Yifan Yang
- Hongjie Zhang
- Xue Yang
- Zhihang Zhong
affiliations:
- Cornell University
- Shanghai Jiao Tong University
- University of California, Los Angeles
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2610.30753'
url: https://arxiv.org/abs/2610.30753
pdf_url: https://arxiv.org/pdf/2610.30753
published: '2026-10-21'
collected: '2026-10-24'
category: MultiAgent
direction: 多智能体协作 · 3D虚拟相机轨迹生成
tags:
- MultiAgent
- Agent Collaboration
- 3D Content Generation
- Text-to-Motion
- Benchmark
one_liner: 提出多智能体协作框架，支持文本/参考视频生成3D场景可控相机运动轨迹
practical_value: '- 多智能体分工架构可复用，将复杂任务拆分为意图理解、候选生成、方案规划、评审反馈四类角色，适配电商商品3D展示脚本生成、直播自动运镜等场景

  - 「原子操作组合生成高阶动作」思路可迁移到生成式推荐场景，将推荐话术/展示素材拆分为可控语义单元拼装，降低生成结果的不可控风险

  - 迭代式评审反馈闭环机制可落地到AIGC内容类业务，自动校验生成结果是否符合业务规则，降低人工审核成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
3D虚拟内容创作中，将自然语言描述的摄影意图转化为可控、可执行的相机运动轨迹难度高，现有方案缺乏语义关联能力和迭代优化机制，生成结果往往不符合拍摄需求。
### 方法关键点
1. 采用四智能体协作架构：Interpreter提取和场景绑定的摄影意图，Scout筛选初始视角，Director通过组合平移、旋转、构图等原子操作生成可执行的相机运动计划，Critic评估渲染结果并给出反馈，驱动计划迭代优化
2. 发布CinemaBench评测集，包含150个Blender场景、750条文本驱动任务、60条参考视频驱动任务，覆盖两类相机轨迹生成评测需求
### 关键结果
FilmFlow在所有对比基线中取得最优 benchmark 性能，同时获得最高用户偏好评分，验证了其空间推理、时间协调、视觉构图能力的有效性
