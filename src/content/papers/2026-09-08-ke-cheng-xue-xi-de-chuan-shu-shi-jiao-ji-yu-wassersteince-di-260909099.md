---
title: 'Curriculum Learning as Transport: Understanding Curricula with Wasserstein
  Geodesics'
title_zh: 《课程学习的传输视角：基于Wasserstein测地线的课程机制解析》
authors:
- Changho Shin
- David Alvarez-Melis
affiliations:
- Princeton University
- Microsoft Research
- Harvard University
arxiv_id: '2609.09099'
url: https://arxiv.org/abs/2609.09099
pdf_url: https://arxiv.org/pdf/2609.09099
published: '2026-09-08'
collected: '2026-09-10'
category: Training
direction: 模型训练优化 · 课程学习机制解析
tags:
- CurriculumLearning
- WassersteinDistance
- TrainingOptimization
- SampleScheduling
- ModelTraining
one_liner: 基于Wasserstein传输的课程路径框架，解耦课程学习耦合设计变量，量化各因素的独立作用
practical_value: '- 训练LLM4Rec/搜索语义匹配模型时，可借鉴该框架的解耦思路，分开测试难易样本排序、曝光占比、过渡平滑度等变量的影响，避免调参混淆

  - 针对推荐冷启动/长尾item/低质query等难样本的性能提升需求，优先采用易到难的样本排序策略，相同曝光预算下可比静态采样获得更高的难样本表现

  - 设计训练样本调度策略时，优先关注难易过渡的平滑度和进度速度，根据业务目标（优先提升头部/长尾效果）调整参数，最大化训练预算效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
课程学习效果受难度定义、样本排序、各难度曝光占比、跨难度进度等多个耦合变量共同影响，难以定位核心有效因子，落地调参无明确指导。
### 方法关键点
Wasserstein课程路径框架将课程表示为离散难度级别上训练分布的传输轨迹，完全解耦各设计变量，支持在固定训练预算下孤立测试排序、曝光、平滑度、进度四类变量的独立作用。
### 关键结果
12任务、33个难度轴的合成测试集验证显示：无通用最优课程策略，效果高度依赖任务、难度维度、预算；易到难排序相比曝光匹配的静态采样，难样本级性能提升显著，收益并非仅来自曝光倾斜；端点平滑度、进度速度会显著改变课程在难度谱上的生效区间。
