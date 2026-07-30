---
title: 'MindForge: Teaching Small Language Models Whole-Life-Cycle Software Engineering
  via Source-Free Program Synthesis'
title_zh: MindForge：通过无源程序合成赋能小模型全生命周期软件工程能力
authors:
- Yihao Chen
- Shi Chang
- Khaled Chawa
- Feng Lin
- Boyuan Chen
- Shaowei Wang
- Ahmed E. Hassan
affiliations:
- Huawei Canada
- Queen's University
- University of Manitoba
- Concordia University
arxiv_id: '2607.27146'
url: https://arxiv.org/abs/2607.27146
pdf_url: https://arxiv.org/pdf/2607.27146
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: 代码Agent · 小模型轨迹蒸馏
tags:
- CodingAgent
- SFT
- KnowledgeDistillation
- TrajectoryMining
- ProgramSynthesis
one_liner: 提出无源环境构建+全轨迹蒸馏流水线，将27B代码模型的ProgramBench通过率提升11.5个点追平大模型
practical_value: '- 垂直领域Agent训练可复用全任务周期轨迹蒸馏思路：比如电商运营、推荐策略调优类Agent，不要仅训练单点操作，要覆盖从需求理解到落地验证的全链路，提升长任务完成率

  - 轨迹数据清洗可直接复用两个trick：基础设施故障断点续跑、错误推理段重写（不修改真实工具调用记录），大幅降低长轨迹采集的成本浪费，同时保证训练数据质量

  - 小模型优化ROI参考：仅千级高质量全周期SFT轨迹即可让同参数模型性能追平数倍参数的前沿模型，垂直场景无需盲目堆大模型，定制轨迹蒸馏的投入产出比更高'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有代码Agent训练框架均聚焦修改现有代码的单阶段任务（如Bug修复、功能迭代），缺少支撑从0到1构建程序的全生命周期训练环境，导致哪怕前沿大模型在ProgramBench基准上的全任务完成率不足1%，小模型的长链路软件工程能力更是存在明显短板；同时长轨迹采集容易受基础设施故障、老师模型错误等噪声影响，训练数据质量参差不齐，很难直接用于SFT。
### 方法关键点
- 自动化构建无源训练环境：将开源CLI程序转换为仅暴露编译后可执行文件和公开文档的环境，完全隐藏源码，避免数据污染，天然覆盖需求推导、架构设计、编码、调试、验证的全开发流程
- 高质量轨迹采集与清洗：用GLM-5.2作为老师模型批量采集全周期开发轨迹，两层降噪：一是基础设施故障断点续跑，重放健康步骤恢复中断的长轨迹，降低采集成本；二是错误推理重写，仅修改逻辑冲突的推理文本，不碰真实工具调用记录，保证轨迹连贯性和真实性
- 轻量SFT训练：仅用筛选后的973条合格轨迹对Qwen3.6-27B做全参数微调，损失仅计算助手生成的推理、自然语言、工具调用token，屏蔽系统提示和工具返回内容
### 关键结果
- 主基准ProgramBench上，MindForge-27B平均测试通过率从基线37.98%提升至49.51%，绝对涨11.53个点，超过DeepSeek V4 Pro（47.8%），追平参数大得多的GLM-5.1（50.9%）、Claude Opus 4.7（51.38%）
- 泛化性极强，在7个未见过的下游基准全量涨点：RepoZero-C2Rust涨31个点，DeepSWE从1.76%提升至15.92%（相对提升9倍），SWE系列Bug修复基准平均涨5个点以上
### 核心结论
针对垂直复杂长任务，千级高质量全链路轨迹蒸馏对小模型能力的提升效果，远超过盲目堆叠参数带来的收益
